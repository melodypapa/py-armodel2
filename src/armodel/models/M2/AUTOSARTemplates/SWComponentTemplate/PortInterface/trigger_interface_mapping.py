"""TriggerInterfaceMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface_mapping import (
    PortInterfaceMapping,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger_mapping import (
    TriggerMapping,
)


class TriggerInterfaceMapping(PortInterfaceMapping):
    """AUTOSAR TriggerInterfaceMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("trigger_mappings", None, False, True, TriggerMapping),  # triggerMappings
    ]

    def __init__(self) -> None:
        """Initialize TriggerInterfaceMapping."""
        super().__init__()
        self.trigger_mappings: list[TriggerMapping] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TriggerInterfaceMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TriggerInterfaceMapping":
        """Create TriggerInterfaceMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TriggerInterfaceMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TriggerInterfaceMapping since parent returns ARObject
        return cast("TriggerInterfaceMapping", obj)


class TriggerInterfaceMappingBuilder:
    """Builder for TriggerInterfaceMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TriggerInterfaceMapping = TriggerInterfaceMapping()

    def build(self) -> TriggerInterfaceMapping:
        """Build and return TriggerInterfaceMapping object.

        Returns:
            TriggerInterfaceMapping instance
        """
        # TODO: Add validation
        return self._obj
