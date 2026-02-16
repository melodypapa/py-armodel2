"""Base AUTOSAR object classes."""

from typing import TYPE_CHECKING, Optional, Union
import xml.etree.ElementTree as ET

if TYPE_CHECKING:
    from armodel.serialization.metadata import XMLMember


class ARObject:
    """Base class for all AUTOSAR objects.

    All generated AUTOSAR classes inherit from this base class.

    The serialize/deserialize pattern uses a member-to-XML mapping where each
    class defines _xml_members for its own attributes. The base class automatically
    collects all _xml_members from the entire class hierarchy (parent to child order).

    This class supports both legacy tuple-based _xml_members and the new
    XMLMember-based dict format for backward compatibility.
    """

    # XML member definitions for this class only (not inherited)
    # Legacy tuple format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    # New dict format: {member_name: XMLMember(...)}
    _xml_members: Union[
        list[tuple[str, Optional[str], bool, bool, Optional[type]]],
        dict[str, "XMLMember"],
    ] = [
        ("checksum", None, True, False, None),  # XML attribute
        ("timestamp", None, True, False, None),  # XML attribute
    ]

    def __init__(self) -> None:
        """Initialize ARObject."""
        self.checksum: Optional[str] = None  # String is a primitive (str) - multiplicity "1"
        self.timestamp: Optional[str] = None  # DateTime is a primitive (str) - multiplicity "1"

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Serialize this object's members to XML element.

        Collects and serializes all members from the class hierarchy.
        Uses the new serialization registry with strategies.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element with this object's members serialized
        """
        # Import here to avoid circular dependency
        from armodel.serialization import get_global_registry
        from armodel.serialization.base import SerializationContext

        registry = get_global_registry()
        strategy = registry.get_strategy(self)

        if strategy is not None:
            # Use registry-based serialization
            context = SerializationContext(namespace=namespace)
            return strategy.serialize(self, context, element)

        # Fall back to legacy implementation
        return self._legacy_serialize(namespace, element)

    def _legacy_serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Legacy serialization implementation for backward compatibility.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to

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
        Uses the new serialization registry with strategies.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized object instance
        """
        # Import here to avoid circular dependency
        from armodel.serialization import get_global_registry
        from armodel.serialization.base import DeserializationContext

        registry = get_global_registry()
        strategy = registry.get_strategy(cls)

        if strategy is not None:
            # Use registry-based deserialization
            context = DeserializationContext(namespace="")
            return strategy.deserialize(cls, element, context)

        # Fall back to legacy implementation
        return cls._legacy_deserialize(element)

    @classmethod
    def _legacy_deserialize(cls, element: ET.Element) -> "ARObject":
        """Legacy deserialization implementation for backward compatibility.

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

    @classmethod
    def _get_all_xml_members(cls) -> list[tuple[str, Optional[str], bool, bool, Optional[type]]]:
        """Collect all _xml_members from the class hierarchy.

        Returns members in parent-to-child order (base classes first).
        Handles both tuple and dict formats for backward compatibility.

        Returns:
            List of (member_name, xml_tag, is_attribute, is_list, element_class) tuples
        """
        all_members = []
        # Iterate through MRO in reverse to get parent-to-child order
        # (we reverse to go from base to derived)
        for base_class in reversed(cls.__mro__):
            if not hasattr(base_class, '_xml_members'):
                continue

            xml_members = base_class._xml_members

            # Handle new dict format
            if isinstance(xml_members, dict):
                # Convert dict to tuple format for compatibility
                for member_name, member_obj in xml_members.items():
                    if hasattr(member_obj, 'xml_tag'):
                        # XMLMember object
                        is_list = member_obj.is_list()
                        all_members.append((
                            member_name,
                            member_obj.xml_tag,
                            member_obj.is_attribute,
                            is_list,
                            member_obj.element_class,
                        ))
            # Handle legacy tuple format
            elif isinstance(xml_members, list):
                all_members.extend(xml_members)

        return all_members

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
