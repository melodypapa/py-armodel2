"""DiagnosticTransferExit AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.MemoryByAddress.diagnostic_memory_by_address import (
    DiagnosticMemoryByAddress,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.MemoryByAddress.diagnostic_transfer_exit import (
    DiagnosticTransferExit,
)


class DiagnosticTransferExit(DiagnosticMemoryByAddress):
    """AUTOSAR DiagnosticTransferExit."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "transfer_exit": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DiagnosticTransferExit,
        ),  # transferExit
    }

    def __init__(self) -> None:
        """Initialize DiagnosticTransferExit."""
        super().__init__()
        self.transfer_exit: Optional[DiagnosticTransferExit] = None


class DiagnosticTransferExitBuilder:
    """Builder for DiagnosticTransferExit."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticTransferExit = DiagnosticTransferExit()

    def build(self) -> DiagnosticTransferExit:
        """Build and return DiagnosticTransferExit object.

        Returns:
            DiagnosticTransferExit instance
        """
        # TODO: Add validation
        return self._obj
