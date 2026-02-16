"""HwPinGroupConnector AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.describable import (
    Describable,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_pin_connector import (
    HwPinConnector,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_pin_group import (
    HwPinGroup,
)


class HwPinGroupConnector(Describable):
    """AUTOSAR HwPinGroupConnector."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("hw_pins", None, False, True, HwPinConnector),  # hwPins
        ("hw_pin_groups", None, False, True, HwPinGroup),  # hwPinGroups
    ]

    def __init__(self) -> None:
        """Initialize HwPinGroupConnector."""
        super().__init__()
        self.hw_pins: list[HwPinConnector] = []
        self.hw_pin_groups: list[HwPinGroup] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert HwPinGroupConnector to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "HwPinGroupConnector":
        """Create HwPinGroupConnector from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            HwPinGroupConnector instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to HwPinGroupConnector since parent returns ARObject
        return cast("HwPinGroupConnector", obj)


class HwPinGroupConnectorBuilder:
    """Builder for HwPinGroupConnector."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: HwPinGroupConnector = HwPinGroupConnector()

    def build(self) -> HwPinGroupConnector:
        """Build and return HwPinGroupConnector object.

        Returns:
            HwPinGroupConnector instance
        """
        # TODO: Add validation
        return self._obj
