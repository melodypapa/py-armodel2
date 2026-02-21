"""XSD parser using lxml.iterparse() for memory-efficient parsing of large XSD files."""

import re
from pathlib import Path
from typing import Dict, List, Optional

from lxml import etree

from tools.validation.models import XSDComplexType, XSDMember


class XSDParser:
    """Parser for AUTOSAR XSD schema files."""

    # XSD namespace
    XSD_NS = "http://www.w3.org/2001/XMLSchema"
    AUTOSAR_NS = "http://autosar.org/schema/r5.0"

    def __init__(self, xsd_path: str):
        """Initialize XSD parser.

        Args:
            xsd_path: Path to XSD file
        """
        self.xsd_path = Path(xsd_path)
        self.complex_types: Dict[str, XSDComplexType] = {}
        self.groups: Dict[str, List[XSDMember]] = {}
        self.attribute_groups: Dict[str, List[XSDMember]] = {}

    def parse(self) -> Dict[str, XSDComplexType]:
        """Parse XSD file and extract complexTypes.

        Returns:
            Dictionary mapping class names to XSDComplexType objects
        """
        if not self.xsd_path.exists():
            raise FileNotFoundError(f"XSD file not found: {self.xsd_path}")

        # Use iterparse for memory-efficient streaming
        context = etree.iterparse(
            str(self.xsd_path),
            events=("end",),
            tag=f"{{{self.XSD_NS}}}complexType",
        )

        for event, elem in context:
            self._parse_complex_type(elem)
            # Clear element to free memory
            elem.clear()

        # Now parse groups (need to be available for inheritance resolution)
        context = etree.iterparse(
            str(self.xsd_path),
            events=("end",),
            tag=f"{{{self.XSD_NS}}}group",
        )

        for event, elem in context:
            self._parse_group(elem)
            elem.clear()

        # Parse attribute groups
        context = etree.iterparse(
            str(self.xsd_path),
            events=("end",),
            tag=f"{{{self.XSD_NS}}}attributeGroup",
        )

        for event, elem in context:
            self._parse_attribute_group(elem)
            elem.clear()

        # Resolve inheritance (expand group references)
        self._resolve_inheritance()

        return self.complex_types

    def _parse_complex_type(self, elem: etree._Element) -> None:
        """Parse a complexType element.

        Args:
            elem: complexType XML element
        """
        name = elem.get("name", "")
        if not name:
            return

        # Extract qualified name from appinfo
        qualified_name = self._extract_qualified_name(elem)
        if not qualified_name:
            return

        # Create complex type
        complex_type = XSDComplexType(
            xsd_name=name,
            qualified_name=qualified_name,
        )

        # Store base types from group references
        sequence = elem.find(f"{{{self.XSD_NS}}}sequence")
        if sequence is not None:
            for group_ref in sequence.findall(f"{{{self.XSD_NS}}}group"):
                ref = group_ref.get("ref", "")
                if ref.startswith("AR:"):
                    base_type = ref[3:]  # Remove "AR:" prefix
                    complex_type.base_types.append(base_type)

        self.complex_types[qualified_name] = complex_type

    def _parse_group(self, elem: etree._Element) -> None:
        """Parse a group element (contains class members).

        Args:
            elem: group XML element
        """
        name = elem.get("name", "")
        if not name:
            return

        members: List[XSDMember] = []

        # Parse elements in the group
        sequence = elem.find(f"{{{self.XSD_NS}}}sequence")
        if sequence is not None:
            for element in sequence.findall(f"{{{self.XSD_NS}}}element"):
                member = self._parse_element(element)
                if member:
                    members.append(member)

        self.groups[name] = members

    def _parse_attribute_group(self, elem: etree._Element) -> None:
        """Parse an attributeGroup element (contains XML attributes).

        Args:
            elem: attributeGroup XML element
        """
        name = elem.get("name", "")
        if not name:
            return

        members: List[XSDMember] = []

        # Parse attributes in the group
        for attribute in elem.findall(f"{{{self.XSD_NS}}}attribute"):
            member = self._parse_attribute(attribute)
            if member:
                members.append(member)

        self.attribute_groups[name] = members

    def _parse_element(self, elem: etree._Element) -> Optional[XSDMember]:
        """Parse an element (class member).

        Args:
            elem: element XML element

        Returns:
            XSDMember or None if parsing fails
        """
        name = elem.get("name", "")
        if not name:
            return None

        # Extract qualified name from appinfo
        qualified_name = self._extract_qualified_name(elem)
        if not qualified_name:
            return None

        # Extract JSON name from qualified name (e.g., "Collection.autoCollect" -> "autoCollect")
        json_name = qualified_name.split(".", 1)[1] if "." in qualified_name else qualified_name.lower()

        # Extract type
        type_name = elem.get("type", "")

        # Extract cardinality
        min_occurs = int(elem.get("minOccurs", "1"))
        max_occurs = elem.get("maxOccurs", "1")

        # Convert to multiplicity
        multiplicity = self._xsd_to_multiplicity(min_occurs, max_occurs)

        # Detect reference type
        is_reference, reference_kind = self._detect_reference_type(name, elem)

        return XSDMember(
            xsd_name=name,
            qualified_name=qualified_name,
            json_name=json_name,
            type_name=type_name,
            min_occurs=min_occurs,
            max_occurs=max_occurs,
            multiplicity=multiplicity,
            is_reference=is_reference,
            reference_kind=reference_kind,
            is_attribute=False,
        )

    def _parse_attribute(self, elem: etree._Element) -> Optional[XSDMember]:
        """Parse an attribute (XML attribute, not element).

        Args:
            elem: attribute XML element

        Returns:
            XSDMember or None if parsing fails
        """
        name = elem.get("name", "")
        if not name:
            return None

        # Extract qualified name from appinfo
        qualified_name = self._extract_qualified_name(elem)
        if not qualified_name:
            return None

        # Extract JSON name from qualified name
        json_name = qualified_name.split(".", 1)[1] if "." in qualified_name else qualified_name.lower()

        # Extract type
        type_name = elem.get("type", "")

        # Attributes are typically single cardinality
        use = elem.get("use", "optional")
        min_occurs = 0 if use == "optional" else 1
        max_occurs = "1"
        multiplicity = "0..1" if use == "optional" else "1"

        return XSDMember(
            xsd_name=name,
            qualified_name=qualified_name,
            json_name=json_name,
            type_name=type_name,
            min_occurs=min_occurs,
            max_occurs=max_occurs,
            multiplicity=multiplicity,
            is_reference=False,
            reference_kind="attribute",
            is_attribute=True,
        )

    def _extract_qualified_name(self, elem: etree._Element) -> Optional[str]:
        """Extract mmt.qualifiedName from appinfo.

        Args:
            elem: XML element with appinfo annotation

        Returns:
            Qualified name string or None
        """
        annotation = elem.find(f"{{{self.XSD_NS}}}annotation")
        if annotation is None:
            return None

        # Check all appinfo tags
        for appinfo in annotation.findall(f"{{{self.XSD_NS}}}appinfo"):
            source = appinfo.get("source", "")
            if source == "tags":
                # Parse mmt.qualifiedName from content
                content = appinfo.text or ""
                match = re.search(r'mmt\.qualifiedName="([^"]+)"', content)
                if match:
                    return match.group(1)

        return None

    def _xsd_to_multiplicity(self, min_occurs: int, max_occurs: str) -> str:
        """Convert XSD cardinality to JSON multiplicity.

        Args:
            min_occurs: minOccurs value
            max_occurs: maxOccurs value ("1", "unbounded", "-1")

        Returns:
            Multiplicity string ("0..1", "1", "*")
        """
        if max_occurs == "unbounded" or max_occurs == "-1":
            return "*"
        max_val = int(max_occurs)
        if min_occurs == 0 and max_val == 1:
            return "0..1"
        if min_occurs == 1 and max_val == 1:
            return "1"
        return "*"

    def _detect_reference_type(self, name: str, elem: etree._Element) -> tuple[bool, Optional[str]]:
        """Detect if element is a reference and determine reference kind.

        Args:
            name: Element name
            elem: XML element

        Returns:
            Tuple of (is_reference, reference_kind)
        """
        # Check element name patterns
        if name.endswith("-REFS"):
            return True, "ref"
        elif name.endswith("-IREFS"):
            return True, "iref"
        elif name.endswith("-TREFS"):
            return True, "tref"

        # Check appinfo for xml.attribute
        annotation = elem.find(f"{{{self.XSD_NS}}}annotation")
        if annotation is not None:
            for appinfo in annotation.findall(f"{{{self.XSD_NS}}}appinfo"):
                source = appinfo.get("source", "")
                if source == "tags":
                    content = appinfo.text or ""
                    if 'xml.attribute="true"' in content:
                        return False, "attribute"

        return False, None

    def _resolve_inheritance(self) -> None:
        """Resolve inheritance by expanding group references for each complex type."""
        for complex_type in self.complex_types.values():
            # Get the group name matching the class name (own members)
            group_name = complex_type.xsd_name.upper().replace("-", "-")  # Keep original format

            # Collect own members from this type's group
            own_members: Dict[str, XSDMember] = {}

            if group_name in self.groups:
                for member in self.groups[group_name]:
                    own_members[member.json_name] = member

            # Collect all members (own + inherited)
            all_members: Dict[str, XSDMember] = {}

            # Start with own members
            all_members.update(own_members)

            # Recursively add members from base types
            for base_type in complex_type.base_types:
                self._add_inherited_members(base_type, all_members)

            # Add attributes from attribute groups
            for base_type in complex_type.base_types:
                self._add_inherited_attributes(base_type, all_members)

            complex_type.members = own_members  # Only own members
            complex_type.all_members = all_members  # All members

    def _add_inherited_members(self, group_name: str, members_dict: Dict[str, XSDMember]) -> None:
        """Recursively add members from group references.

        Args:
            group_name: Group name to resolve
            members_dict: Dictionary to populate with members
        """
        if group_name in self.groups:
            for member in self.groups[group_name]:
                # Don't override existing members (child takes precedence)
                if member.json_name not in members_dict:
                    members_dict[member.json_name] = member

            # Recursively resolve nested group references if any
            # (This is handled by XSD structure, not by us)

    def _add_inherited_attributes(self, group_name: str, members_dict: Dict[str, XSDMember]) -> None:
        """Add XML attributes from attribute groups.

        Args:
            group_name: Attribute group name to resolve
            members_dict: Dictionary to populate with attributes
        """
        if group_name in self.attribute_groups:
            for member in self.attribute_groups[group_name]:
                if member.json_name not in members_dict:
                    members_dict[member.json_name] = member