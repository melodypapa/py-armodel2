"""ARObject AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    DateTime,
    String,
)


class ARObject:
    """AUTOSAR ARObject."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("checksum", None, True, False, None),  # checksum
        ("timestamp", None, True, False, None),  # timestamp
    ]

    def __init__(self) -> None:
        """Initialize ARObject."""
        self.checksum: Optional[String] = None
        self.timestamp: Optional[DateTime] = None

    @classmethod
    def _get_all_xml_members(cls) -> list:
        """Collect all _xml_members from the class hierarchy.

        Returns members in parent-to-child order (base classes first).

        Returns:
            List of (member_name, xml_tag, is_attribute, is_list, element_class) tuples
        """
        all_members = []
        # Iterate through MRO in reverse to get parent-to-child order
        for base_class in reversed(cls.__mro__):
            if hasattr(base_class, '_xml_members') and base_class._xml_members:
                all_members.extend(base_class._xml_members)
        return all_members

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Serialize this object's members to XML element.

        Collects and serializes all members from the class hierarchy.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element with this object's members serialized
        """
        if element is None:
            # Create element if this is the root call
            tag = f"{{{namespace}}}{self.__class__.__name__.upper()}"
            element = ET.Element(tag)

        # Serialize all members from class hierarchy (parent to child order)
        all_members = self._get_all_xml_members()
        for member_name, xml_tag, is_attribute, is_list, _ in all_members:
            value = getattr(self, member_name, None)

            if value is None:
                continue

            # Infer XML tag from member name if not provided
            tag = xml_tag or self._member_to_xml_tag(member_name)

            if is_attribute:
                # Serialize as XML attribute
                element.set(tag, str(value))
            elif is_list:
                # Serialize list of items as child elements
                for item in value:
                    if hasattr(item, 'serialize'):
                        # Item has serialize method
                        child_elem = item.serialize(namespace)
                        element.append(child_elem)
                    else:
                        # Primitive item
                        child_tag = f"{{{namespace}}}{tag}"
                        child_elem = ET.SubElement(element, child_tag)
                        child_elem.text = str(item)
            else:
                # Serialize single item as child element
                if hasattr(value, 'serialize'):
                    # Item has serialize method
                    child_elem = value.serialize(namespace)
                    element.append(child_elem)
                else:
                    # Primitive item
                    child_tag = f"{{{namespace}}}{tag}"
                    child_elem = ET.SubElement(element, child_tag)
                    child_elem.text = str(value)

        return element

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ARObject":
        """Deserialize XML element to object.

        Collects and deserializes all members from the class hierarchy.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized object instance
        """
        obj = cls()

        # Deserialize all members from class hierarchy (parent to child order)
        all_members = cls._get_all_xml_members()
        for member_name, xml_tag, is_attribute, is_list, element_class in all_members:
            tag = xml_tag or cls._member_to_xml_tag(member_name)

            if is_attribute:
                # Deserialize from XML attribute
                if tag in element.attrib:
                    setattr(obj, member_name, element.attrib[tag])
            elif is_list:
                # Deserialize list of items from child elements
                items = []
                for child in element:
                    child_tag = child.tag.split('}')[1] if '}' in child.tag else child.tag
                    if child_tag == tag:
                        if element_class and hasattr(element_class, 'deserialize'):
                            # Deserialize to class instance
                            items.append(element_class.deserialize(child))
                        else:
                            # Primitive value
                            items.append(child.text if child.text else None)
                setattr(obj, member_name, items)
            else:
                # Deserialize single item from child element
                for child in element:
                    child_tag = child.tag.split('}')[1] if '}' in child.tag else child.tag
                    if child_tag == tag:
                        if element_class and hasattr(element_class, 'deserialize'):
                            setattr(obj, member_name, element_class.deserialize(child))
                        else:
                            setattr(obj, member_name, child.text if child.text else None)
                        break

        return obj

    @staticmethod
    def _member_to_xml_tag(member_name: str) -> str:
        """Convert Python member name to XML tag name.

        Args:
            member_name: Python attribute name (snake_case)

        Returns:
            XML tag name (UPPER-CASE with hyphens)

        Examples:
            short_name -> SHORT-NAME
            category -> CATEGORY
        """
        return member_name.replace('_', '-').upper()


class ARObjectBuilder:
    """Builder for ARObject."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ARObject = ARObject

    def build(self) -> ARObject:
        """Build and return ARObject object.

        Returns:
            ARObject instance
        """
        # TODO: Add validation
        return self._obj
