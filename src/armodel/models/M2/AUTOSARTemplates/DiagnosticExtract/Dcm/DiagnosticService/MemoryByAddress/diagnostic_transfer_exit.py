"""DiagnosticTransferExit AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 142)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_MemoryByAddress.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.MemoryByAddress.diagnostic_memory_by_address import (
    DiagnosticMemoryByAddress,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class DiagnosticTransferExit(DiagnosticMemoryByAddress):
    """AUTOSAR DiagnosticTransferExit."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    transfer_exit: Optional[DiagnosticTransferExit]
    def __init__(self) -> None:
        """Initialize DiagnosticTransferExit."""
        super().__init__()
        self.transfer_exit: Optional[DiagnosticTransferExit] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticTransferExit":
        """Deserialize XML element to DiagnosticTransferExit object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticTransferExit object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticTransferExit, cls).deserialize(element)

        # Parse transfer_exit
        child = ARObject._find_child_element(element, "TRANSFER-EXIT")
        if child is not None:
            transfer_exit_value = ARObject._deserialize_by_tag(child, "DiagnosticTransferExit")
            obj.transfer_exit = transfer_exit_value

        return obj



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
