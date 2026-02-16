"""HardwareConfiguration AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class HardwareConfiguration(ARObject):
    """AUTOSAR HardwareConfiguration."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("additional", None, True, False, None),  # additional
        ("processor_mode", None, True, False, None),  # processorMode
        ("processor_speed", None, True, False, None),  # processorSpeed
    ]

    def __init__(self) -> None:
        """Initialize HardwareConfiguration."""
        super().__init__()
        self.additional: Optional[String] = None
        self.processor_mode: Optional[String] = None
        self.processor_speed: Optional[String] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert HardwareConfiguration to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "HardwareConfiguration":
        """Create HardwareConfiguration from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            HardwareConfiguration instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to HardwareConfiguration since parent returns ARObject
        return cast("HardwareConfiguration", obj)


class HardwareConfigurationBuilder:
    """Builder for HardwareConfiguration."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: HardwareConfiguration = HardwareConfiguration()

    def build(self) -> HardwareConfiguration:
        """Build and return HardwareConfiguration object.

        Returns:
            HardwareConfiguration instance
        """
        # TODO: Add validation
        return self._obj
