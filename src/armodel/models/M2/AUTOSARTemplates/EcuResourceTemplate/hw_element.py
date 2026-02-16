"""HwElement AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_description_entity import (
    HwDescriptionEntity,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_element import (
    HwElement,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_element_connector import (
    HwElementConnector,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_pin_group import (
    HwPinGroup,
)


class HwElement(HwDescriptionEntity):
    """AUTOSAR HwElement."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("hw_elements", None, False, True, HwElementConnector),  # hwElements
        ("hw_pin_groups", None, False, True, HwPinGroup),  # hwPinGroups
        ("nested_elements", None, False, True, HwElement),  # nestedElements
    ]

    def __init__(self) -> None:
        """Initialize HwElement."""
        super().__init__()
        self.hw_elements: list[HwElementConnector] = []
        self.hw_pin_groups: list[HwPinGroup] = []
        self.nested_elements: list[HwElement] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert HwElement to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "HwElement":
        """Create HwElement from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            HwElement instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to HwElement since parent returns ARObject
        return cast("HwElement", obj)


class HwElementBuilder:
    """Builder for HwElement."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: HwElement = HwElement()

    def build(self) -> HwElement:
        """Build and return HwElement object.

        Returns:
            HwElement instance
        """
        # TODO: Add validation
        return self._obj
