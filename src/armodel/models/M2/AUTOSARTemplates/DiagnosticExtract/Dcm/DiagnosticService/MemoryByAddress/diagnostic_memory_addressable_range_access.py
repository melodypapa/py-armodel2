"""DiagnosticMemoryAddressableRangeAccess AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 140)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_MemoryByAddress.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.MemoryByAddress.diagnostic_memory_by_address import (
    DiagnosticMemoryByAddress,
)


class DiagnosticMemoryAddressableRangeAccess(DiagnosticMemoryByAddress):
    """AUTOSAR DiagnosticMemoryAddressableRangeAccess."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "memory_ranges": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=any (DiagnosticMemory),
        ),  # memoryRanges
    }

    def __init__(self) -> None:
        """Initialize DiagnosticMemoryAddressableRangeAccess."""
        super().__init__()
        self.memory_ranges: list[Any] = []


class DiagnosticMemoryAddressableRangeAccessBuilder:
    """Builder for DiagnosticMemoryAddressableRangeAccess."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticMemoryAddressableRangeAccess = DiagnosticMemoryAddressableRangeAccess()

    def build(self) -> DiagnosticMemoryAddressableRangeAccess:
        """Build and return DiagnosticMemoryAddressableRangeAccess object.

        Returns:
            DiagnosticMemoryAddressableRangeAccess instance
        """
        # TODO: Add validation
        return self._obj
