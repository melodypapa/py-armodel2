"""DiagnosticRequestFileTransfer AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 146)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_RequestFileTransfer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class DiagnosticRequestFileTransfer(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticRequestFileTransfer."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    request_file: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticRequestFileTransfer."""
        super().__init__()
        self.request_file: Optional[Any] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticRequestFileTransfer":
        """Deserialize XML element to DiagnosticRequestFileTransfer object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticRequestFileTransfer object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse request_file
        child = ARObject._find_child_element(element, "REQUEST-FILE")
        if child is not None:
            request_file_value = child.text
            obj.request_file = request_file_value

        return obj



class DiagnosticRequestFileTransferBuilder:
    """Builder for DiagnosticRequestFileTransfer."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticRequestFileTransfer = DiagnosticRequestFileTransfer()

    def build(self) -> DiagnosticRequestFileTransfer:
        """Build and return DiagnosticRequestFileTransfer object.

        Returns:
            DiagnosticRequestFileTransfer instance
        """
        # TODO: Add validation
        return self._obj
