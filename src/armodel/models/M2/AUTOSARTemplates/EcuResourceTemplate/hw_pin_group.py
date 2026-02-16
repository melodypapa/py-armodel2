"""HwPinGroup AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_pin_group_content import (
    HwPinGroupContent,
)


class HwPinGroup(Identifiable):
    """AUTOSAR HwPinGroup."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("hw_pin_group_content", None, False, False, HwPinGroupContent),  # hwPinGroupContent
    ]

    def __init__(self) -> None:
        """Initialize HwPinGroup."""
        super().__init__()
        self.hw_pin_group_content: Optional[HwPinGroupContent] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert HwPinGroup to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "HwPinGroup":
        """Create HwPinGroup from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            HwPinGroup instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to HwPinGroup since parent returns ARObject
        return cast("HwPinGroup", obj)


class HwPinGroupBuilder:
    """Builder for HwPinGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: HwPinGroup = HwPinGroup()

    def build(self) -> HwPinGroup:
        """Build and return HwPinGroup object.

        Returns:
            HwPinGroup instance
        """
        # TODO: Add validation
        return self._obj
