"""DiagnosticJ1939SpnMapping AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "sending_nodes": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=DiagnosticJ1939Node,
        ),  # sendingNodes
        "spn": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DiagnosticJ1939Spn,
        ),  # spn
        "system_signal": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SystemSignal,
        ),  # systemSignal
    }

    def __init__(self) -> None:
        """Initialize DiagnosticJ1939SpnMapping."""
        super().__init__()
        self.sending_nodes: list[DiagnosticJ1939Node] = []
        self.spn: Optional[DiagnosticJ1939Spn] = None
        self.system_signal: Optional[SystemSignal] = None


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
