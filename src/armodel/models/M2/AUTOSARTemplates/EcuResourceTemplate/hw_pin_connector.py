"""HwPinConnector AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.describable import (
    Describable,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_pin import (
    HwPin,
)


class HwPinConnector(Describable):
    """AUTOSAR HwPinConnector."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("hw_pins", None, False, True, HwPin),  # hwPins
    ]

    def __init__(self) -> None:
        """Initialize HwPinConnector."""
        super().__init__()
        self.hw_pins: list[HwPin] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert HwPinConnector to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "HwPinConnector":
        """Create HwPinConnector from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            HwPinConnector instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to HwPinConnector since parent returns ARObject
        return cast("HwPinConnector", obj)


class HwPinConnectorBuilder:
    """Builder for HwPinConnector."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: HwPinConnector = HwPinConnector()

    def build(self) -> HwPinConnector:
        """Build and return HwPinConnector object.

        Returns:
            HwPinConnector instance
        """
        # TODO: Add validation
        return self._obj
