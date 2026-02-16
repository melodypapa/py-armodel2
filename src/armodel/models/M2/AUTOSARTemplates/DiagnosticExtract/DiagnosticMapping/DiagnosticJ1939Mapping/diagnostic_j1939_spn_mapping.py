"""DiagnosticJ1939SpnMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import (
    DiagnosticMapping,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.J1939.diagnostic_j1939_node import (
    DiagnosticJ1939Node,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.J1939.diagnostic_j1939_spn import (
    DiagnosticJ1939Spn,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.system_signal import (
    SystemSignal,
)


class DiagnosticJ1939SpnMapping(DiagnosticMapping):
    """AUTOSAR DiagnosticJ1939SpnMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("sending_nodes", None, False, True, DiagnosticJ1939Node),  # sendingNodes
        ("spn", None, False, False, DiagnosticJ1939Spn),  # spn
        ("system_signal", None, False, False, SystemSignal),  # systemSignal
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticJ1939SpnMapping."""
        super().__init__()
        self.sending_nodes: list[DiagnosticJ1939Node] = []
        self.spn: Optional[DiagnosticJ1939Spn] = None
        self.system_signal: Optional[SystemSignal] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticJ1939SpnMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticJ1939SpnMapping":
        """Create DiagnosticJ1939SpnMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticJ1939SpnMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticJ1939SpnMapping since parent returns ARObject
        return cast("DiagnosticJ1939SpnMapping", obj)


class DiagnosticJ1939SpnMappingBuilder:
    """Builder for DiagnosticJ1939SpnMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticJ1939SpnMapping = DiagnosticJ1939SpnMapping()

    def build(self) -> DiagnosticJ1939SpnMapping:
        """Build and return DiagnosticJ1939SpnMapping object.

        Returns:
            DiagnosticJ1939SpnMapping instance
        """
        # TODO: Add validation
        return self._obj
