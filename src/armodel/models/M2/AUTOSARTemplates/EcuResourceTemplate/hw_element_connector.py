"""HwElementConnector AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.describable import (
    Describable,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_element import (
    HwElement,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_pin_connector import (
    HwPinConnector,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_pin_group_connector import (
    HwPinGroupConnector,
)


class HwElementConnector(Describable):
    """AUTOSAR HwElementConnector."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("hw_elements", None, False, True, HwElement),  # hwElements
        ("hw_pins", None, False, True, HwPinConnector),  # hwPins
        ("hw_pin_groups", None, False, True, HwPinGroupConnector),  # hwPinGroups
    ]

    def __init__(self) -> None:
        """Initialize HwElementConnector."""
        super().__init__()
        self.hw_elements: list[HwElement] = []
        self.hw_pins: list[HwPinConnector] = []
        self.hw_pin_groups: list[HwPinGroupConnector] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert HwElementConnector to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "HwElementConnector":
        """Create HwElementConnector from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            HwElementConnector instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to HwElementConnector since parent returns ARObject
        return cast("HwElementConnector", obj)


class HwElementConnectorBuilder:
    """Builder for HwElementConnector."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: HwElementConnector = HwElementConnector()

    def build(self) -> HwElementConnector:
        """Build and return HwElementConnector object.

        Returns:
            HwElementConnector instance
        """
        # TODO: Add validation
        return self._obj
