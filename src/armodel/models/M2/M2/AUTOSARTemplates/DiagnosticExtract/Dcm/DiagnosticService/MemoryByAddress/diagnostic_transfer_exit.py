"""DiagnosticTransferExit AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 142)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_MemoryByAddress.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.MemoryByAddress.diagnostic_memory_by_address import (
    DiagnosticMemoryByAddress,
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
            element_class="DiagnosticTransferExit",
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
