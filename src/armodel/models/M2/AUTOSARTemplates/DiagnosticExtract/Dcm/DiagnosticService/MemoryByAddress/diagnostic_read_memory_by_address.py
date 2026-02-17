"""DiagnosticReadMemoryByAddress AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 141)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_MemoryByAddress.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.MemoryByAddress.diagnostic_memory_addressable_range_access import (
    DiagnosticMemoryAddressableRangeAccess,
)


class DiagnosticReadMemoryByAddress(DiagnosticMemoryAddressableRangeAccess):
    """AUTOSAR DiagnosticReadMemoryByAddress."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "read_class": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (DiagnosticReadMemory),
        ),  # readClass
    }

    def __init__(self) -> None:
        """Initialize DiagnosticReadMemoryByAddress."""
        super().__init__()
        self.read_class: Optional[Any] = None


class DiagnosticReadMemoryByAddressBuilder:
    """Builder for DiagnosticReadMemoryByAddress."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticReadMemoryByAddress = DiagnosticReadMemoryByAddress()

    def build(self) -> DiagnosticReadMemoryByAddress:
        """Build and return DiagnosticReadMemoryByAddress object.

        Returns:
            DiagnosticReadMemoryByAddress instance
        """
        # TODO: Add validation
        return self._obj
