"""DiagnosticDataTransfer AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 143)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_MemoryByAddress.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.MemoryByAddress.diagnostic_memory_by_address import (
    DiagnosticMemoryByAddress,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class DiagnosticDataTransfer(DiagnosticMemoryByAddress):
    """AUTOSAR DiagnosticDataTransfer."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_transfer: Optional[DiagnosticDataTransfer]
    def __init__(self) -> None:
        """Initialize DiagnosticDataTransfer."""
        super().__init__()
        self.data_transfer: Optional[DiagnosticDataTransfer] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticDataTransfer":
        """Deserialize XML element to DiagnosticDataTransfer object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticDataTransfer object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticDataTransfer, cls).deserialize(element)

        # Parse data_transfer
        child = ARObject._find_child_element(element, "DATA-TRANSFER")
        if child is not None:
            data_transfer_value = ARObject._deserialize_by_tag(child, "DiagnosticDataTransfer")
            obj.data_transfer = data_transfer_value

        return obj



class DiagnosticDataTransferBuilder:
    """Builder for DiagnosticDataTransfer."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticDataTransfer = DiagnosticDataTransfer()

    def build(self) -> DiagnosticDataTransfer:
        """Build and return DiagnosticDataTransfer object.

        Returns:
            DiagnosticDataTransfer instance
        """
        # TODO: Add validation
        return self._obj
