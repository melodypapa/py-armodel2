"""HwPin AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
    String,
)


class HwPin(Identifiable):
    """AUTOSAR HwPin."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("function_names", None, False, True, None),  # functionNames
        ("packaging_pin", None, True, False, None),  # packagingPin
        ("pin_number", None, True, False, None),  # pinNumber
    ]

    def __init__(self) -> None:
        """Initialize HwPin."""
        super().__init__()
        self.function_names: list[String] = []
        self.packaging_pin: Optional[String] = None
        self.pin_number: Optional[Integer] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert HwPin to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "HwPin":
        """Create HwPin from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            HwPin instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to HwPin since parent returns ARObject
        return cast("HwPin", obj)


class HwPinBuilder:
    """Builder for HwPin."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: HwPin = HwPin()

    def build(self) -> HwPin:
        """Build and return HwPin object.

        Returns:
            HwPin instance
        """
        # TODO: Add validation
        return self._obj
