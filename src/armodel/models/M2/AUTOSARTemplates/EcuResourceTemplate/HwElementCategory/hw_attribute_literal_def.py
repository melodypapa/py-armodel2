"""HwAttributeLiteralDef AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)


class HwAttributeLiteralDef(Identifiable):
    """AUTOSAR HwAttributeLiteralDef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize HwAttributeLiteralDef."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert HwAttributeLiteralDef to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "HwAttributeLiteralDef":
        """Create HwAttributeLiteralDef from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            HwAttributeLiteralDef instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to HwAttributeLiteralDef since parent returns ARObject
        return cast("HwAttributeLiteralDef", obj)


class HwAttributeLiteralDefBuilder:
    """Builder for HwAttributeLiteralDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: HwAttributeLiteralDef = HwAttributeLiteralDef()

    def build(self) -> HwAttributeLiteralDef:
        """Build and return HwAttributeLiteralDef object.

        Returns:
            HwAttributeLiteralDef instance
        """
        # TODO: Add validation
        return self._obj
