"""ValueList AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Numerical,
)


class ValueList(ARObject):
    """AUTOSAR ValueList."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("v", None, True, False, None),  # v
    ]

    def __init__(self) -> None:
        """Initialize ValueList."""
        super().__init__()
        self.v: Optional[Numerical] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ValueList to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ValueList":
        """Create ValueList from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ValueList instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ValueList since parent returns ARObject
        return cast("ValueList", obj)


class ValueListBuilder:
    """Builder for ValueList."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ValueList = ValueList()

    def build(self) -> ValueList:
        """Build and return ValueList object.

        Returns:
            ValueList instance
        """
        # TODO: Add validation
        return self._obj
