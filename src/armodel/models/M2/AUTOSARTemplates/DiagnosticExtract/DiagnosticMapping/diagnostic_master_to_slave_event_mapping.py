"""DiagnosticMasterToSlaveEventMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import (
    DiagnosticMapping,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_event import (
    DiagnosticEvent,
)


class DiagnosticMasterToSlaveEventMapping(DiagnosticMapping):
    """AUTOSAR DiagnosticMasterToSlaveEventMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("master_event", None, False, False, DiagnosticEvent),  # masterEvent
        ("slave_event", None, False, False, DiagnosticEvent),  # slaveEvent
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticMasterToSlaveEventMapping."""
        super().__init__()
        self.master_event: Optional[DiagnosticEvent] = None
        self.slave_event: Optional[DiagnosticEvent] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticMasterToSlaveEventMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticMasterToSlaveEventMapping":
        """Create DiagnosticMasterToSlaveEventMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticMasterToSlaveEventMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticMasterToSlaveEventMapping since parent returns ARObject
        return cast("DiagnosticMasterToSlaveEventMapping", obj)


class DiagnosticMasterToSlaveEventMappingBuilder:
    """Builder for DiagnosticMasterToSlaveEventMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticMasterToSlaveEventMapping = DiagnosticMasterToSlaveEventMapping()

    def build(self) -> DiagnosticMasterToSlaveEventMapping:
        """Build and return DiagnosticMasterToSlaveEventMapping object.

        Returns:
            DiagnosticMasterToSlaveEventMapping instance
        """
        # TODO: Add validation
        return self._obj
