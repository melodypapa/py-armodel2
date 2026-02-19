"""
XSD Parser Module for extracting AUTOSAR schema metadata.

Parses XSD files and extracts:
- ComplexTypes with base types and inheritance
- Elements with types and multiplicities
- Attributes with types and constraints
- SimpleTypes with patterns and enums
"""

from dataclasses import dataclass, field
from typing import Optional, Dict, List, Any
from pathlib import Path
import xml.etree.ElementTree as ET
import re


@dataclass
class XSDElementInfo:
    """Information about an XSD element."""

    name: str
    type: str
    min_occurs: int = 1
    max_occurs: int = 1  # Use -1 for unbounded
    required: bool = True
    pattern: Optional[str] = None
    max_length: Optional[int] = None
    min_length: Optional[int] = None


@dataclass
class XSDAttributeInfo:
    """Information about an XSD attribute."""

    name: str
    type: str
    required: bool = False
    default: Optional[str] = None


@dataclass
class XSDComplexTypeInfo:
    """Information about an XSD complexType."""

    name: str
    base_type: Optional[str] = None
    elements: List[XSDElementInfo] = field(default_factory=list)
    attributes: List[XSDAttributeInfo] = field(default_factory=list)
    abstract: bool = False


@dataclass
class XSDSimpleTypeInfo:
    """Information about an XSD simpleType."""

    name: str
    base_type: Optional[str] = None
    enum_values: Optional[List[str]] = None
    pattern: Optional[str] = None
    max_length: Optional[int] = None
    min_length: Optional[int] = None


class XSDParser:
    """Parser for AUTOSAR XSD schemas."""

    # AUTOSAR namespace
    AUTOSAR_NS = "http://autosar.org/schema/r4.0"
    XSD_NS = "http://www.w3.org/2001/XMLSchema"

    def __init__(self, xsd_path: Path):
        """
        Initialize XSD parser.

        Args:
            xsd_path: Path to the main AUTOSAR_*.xsd file
        """
        self.xsd_path = xsd_path
        self._tree: Optional[ET.ElementTree] = None
        self._root: Optional[ET.Element] = None

        # Storage for parsed types
        self.complex_types: Dict[str, XSDComplexTypeInfo] = {}
        self.simple_types: Dict[str, XSDSimpleTypeInfo] = {}
        self.inheritance_map: Dict[str, str] = {}  # type -> base_type

        # Schema metadata
        self.schema_version: Optional[str] = None

    def parse(self) -> None:
        """
        Parse the XSD file and extract all metadata.

        Raises:
            FileNotFoundError: If XSD file doesn't exist
            ValueError: If XSD parsing fails
        """
        if not self.xsd_path.exists():
            raise FileNotFoundError(f"XSD file not found: {self.xsd_path}")

        # Parse the XSD
        self._tree = ET.parse(self.xsd_path)  # type: ignore[assignment]
        self._root = self._tree.getroot()  # type: ignore[union-attr]

        # Extract schema version from filename
        self.schema_version = self._extract_version()

        # Parse all types
        self._parse_complex_types()
        self._parse_simple_types()

        # Build inheritance map
        self._build_inheritance_map()

    def _extract_version(self) -> str:
        """Extract schema version from XSD path."""
        # Path: .../demos/xsd/AUTOSAR_00046/AUTOSAR_00046.xsd
        match = re.search(r"AUTOSAR_(\d{5})", str(self.xsd_path))
        if match:
            return match.group(1)
        return "unknown"

    def _parse_complex_types(self) -> None:
        """Parse all complexType definitions."""
        # Find all complexType elements
        for complex_type in self._root.findall(  # type: ignore[union-attr]
            f".//{{{self.XSD_NS}}}complexType"
        ):
            name = complex_type.get("name")
            if not name:
                continue

            # Create complex type info
            type_info = XSDComplexTypeInfo(name=name)

            # Check if abstract
            type_info.abstract = complex_type.get("abstract", "false").lower() == "true"

            # Parse base type (from complexContent/extension)
            complex_content = complex_type.find(f"./{{{self.XSD_NS}}}complexContent")
            if complex_content is not None:
                extension = complex_content.find(f"./{{{self.XSD_NS}}}extension")
                if extension is not None:
                    type_info.base_type = extension.get("base")

            # Parse elements
            self._parse_elements(complex_type, type_info)

            # Parse attributes
            self._parse_attributes(complex_type, type_info)

            self.complex_types[name] = type_info

    def _parse_elements(self, parent: ET.Element, type_info: XSDComplexTypeInfo) -> None:
        """Parse element definitions within a complexType."""
        # Look for elements in sequence, choice, or all
        for container_name in ["sequence", "choice", "all"]:
            container = parent.find(f"./{{{self.XSD_NS}}}{container_name}")
            if container is not None:
                for elem in container.findall(f"./{{{self.XSD_NS}}}element"):
                    elem_name = elem.get("name")
                    elem_type = elem.get("type")

                    if not elem_name or not elem_type:
                        continue

                    # Parse multiplicities
                    min_occurs = int(elem.get("minOccurs", "1") or "1")
                    max_occurs_str = elem.get("maxOccurs", "1")
                    max_occurs = (
                        int(max_occurs_str) if max_occurs_str != "unbounded" else -1
                    )

                    elem_info = XSDElementInfo(
                        name=elem_name,
                        type=elem_type,
                        min_occurs=min_occurs,
                        max_occurs=max_occurs,
                        required=(min_occurs > 0),
                    )

                    type_info.elements.append(elem_info)

    def _parse_attributes(self, parent: ET.Element, type_info: XSDComplexTypeInfo) -> None:
        """Parse attribute definitions within a complexType."""
        for attr in parent.findall(f".//{{{self.XSD_NS}}}attribute"):
            attr_name = attr.get("name")
            attr_type = attr.get("type")

            if not attr_name or not attr_type:
                continue

            required = attr.get("use", "optional") == "required"
            default = attr.get("default")

            attr_info = XSDAttributeInfo(
                name=attr_name, type=attr_type, required=required, default=default
            )

            type_info.attributes.append(attr_info)

    def _parse_simple_types(self) -> None:
        """Parse all simpleType definitions (enums, patterns)."""
        for simple_type in self._root.findall(  # type: ignore[union-attr]
            f".//{{{self.XSD_NS}}}simpleType"
        ):
            name = simple_type.get("name")
            if not name:
                continue

            type_info = XSDSimpleTypeInfo(name=name)

            # Check for restriction
            restriction = simple_type.find(f"./{{{self.XSD_NS}}}restriction")
            if restriction is not None:
                type_info.base_type = restriction.get("base")  # type: ignore[assignment]

                # Parse enum values
                enum_values = []
                for enum_elem in restriction.findall(f"./{{{self.XSD_NS}}}enumeration"):
                    value = enum_elem.get("value")
                    if value:
                        enum_values.append(value)

                if enum_values:
                    type_info.enum_values = enum_values

                # Parse pattern
                pattern_elem = restriction.find(f"./{{{self.XSD_NS}}}pattern")
                if pattern_elem is not None:
                    type_info.pattern = pattern_elem.get("value")

                # Parse length constraints
                min_length_elem = restriction.find(f"./{{{self.XSD_NS}}}minLength")
                if min_length_elem is not None:
                    type_info.min_length = int(min_length_elem.get("value"))

                max_length_elem = restriction.find(f"./{{{self.XSD_NS}}}maxLength")
                if max_length_elem is not None:
                    type_info.max_length = int(max_length_elem.get("value") or "0")  # type: ignore[assignment]

            self.simple_types[name] = type_info

    def _build_inheritance_map(self) -> None:
        """Build inheritance hierarchy from complexTypes."""
        for name, type_info in self.complex_types.items():
            if type_info.base_type:
                self.inheritance_map[name] = type_info.base_type

    def get_complex_type(self, name: str) -> Optional[XSDComplexTypeInfo]:
        """Get complex type info by name."""
        return self.complex_types.get(name)

    def get_simple_type(self, name: str) -> Optional[XSDSimpleTypeInfo]:
        """Get simple type info by name."""
        return self.simple_types.get(name)

    def get_all_elements_for_type(self, type_name: str) -> List[XSDElementInfo]:
        """
        Get all elements for a type, including inherited elements.

        Args:
            type_name: The complex type name

        Returns:
            List of all elements (including inherited)
        """
        elements = []
        current_type = type_name

        while current_type:
            type_info = self.complex_types.get(current_type)
            if not type_info:
                break

            # Add elements from this type
            elements.extend(type_info.elements)

            # Move to base type
            current_type = type_info.base_type

        return elements

    def get_all_attributes_for_type(self, type_name: str) -> List[XSDAttributeInfo]:
        """
        Get all attributes for a type, including inherited attributes.

        Args:
            type_name: The complex type name

        Returns:
            List of all attributes (including inherited)
        """
        attributes = []
        current_type = type_name

        while current_type:
            type_info = self.complex_types.get(current_type)
            if not type_info:
                break

            # Add attributes from this type
            attributes.extend(type_info.attributes)

            # Move to base type
            current_type = type_info.base_type

        return attributes

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert parsed metadata to dictionary for YAML serialization.

        Returns:
            Dictionary representation of all metadata
        """
        result = {
            "version": self.schema_version,
            "complex_types": {},
            "simple_types": {},
            "inheritance": self.inheritance_map,
        }

        # Convert complex types
        for name, type_info in self.complex_types.items():
            result["complex_types"][name] = {
                "base_type": type_info.base_type,
                "abstract": type_info.abstract,
                "elements": [
                    {
                        "name": elem.name,
                        "type": elem.type,
                        "min_occurs": elem.min_occurs,
                        "max_occurs": elem.max_occurs,
                        "required": elem.required,
                    }
                    for elem in type_info.elements
                ],
                "attributes": [
                    {
                        "name": attr.name,
                        "type": attr.type,
                        "required": attr.required,
                        "default": attr.default,
                    }
                    for attr in type_info.attributes
                ],
            }

        # Convert simple types
        for name, type_info in self.simple_types.items():
            result["simple_types"][name] = {
                "base_type": type_info.base_type,
                "enum_values": type_info.enum_values,
                "pattern": type_info.pattern,
                "max_length": type_info.max_length,
                "min_length": type_info.min_length,
            }

        return result
