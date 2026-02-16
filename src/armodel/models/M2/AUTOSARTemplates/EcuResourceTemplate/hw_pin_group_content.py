"""HwPinGroupContent AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_pin import (
    HwPin,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_pin_group import (
    HwPinGroup,
)


class HwPinGroupContent(ARObject):
    """AUTOSAR HwPinGroupContent."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("hw_pin", None, False, False, HwPin),  # hwPin
        ("hw_pin_group", None, False, False, HwPinGroup),  # hwPinGroup
    ]

    def __init__(self) -> None:
        """Initialize HwPinGroupContent."""
        super().__init__()
        self.hw_pin: Optional[HwPin] = None
        self.hw_pin_group: Optional[HwPinGroup] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert HwPinGroupContent to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "HwPinGroupContent":
        """Create HwPinGroupContent from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            HwPinGroupContent instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to HwPinGroupContent since parent returns ARObject
        return cast("HwPinGroupContent", obj)


class HwPinGroupContentBuilder:
    """Builder for HwPinGroupContent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: HwPinGroupContent = HwPinGroupContent()

    def build(self) -> HwPinGroupContent:
        """Build and return HwPinGroupContent object.

        Returns:
            HwPinGroupContent instance
        """
        # TODO: Add validation
        return self._obj
