"""DiagnosticRequestUpload AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 145)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_MemoryByAddress.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.MemoryByAddress.diagnostic_memory_addressable_range_access import (
    DiagnosticMemoryAddressableRangeAccess,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class DiagnosticRequestUpload(DiagnosticMemoryAddressableRangeAccess):
    """AUTOSAR DiagnosticRequestUpload."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    request_upload: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticRequestUpload."""
        super().__init__()
        self.request_upload: Optional[Any] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticRequestUpload":
        """Deserialize XML element to DiagnosticRequestUpload object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticRequestUpload object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse request_upload
        child = ARObject._find_child_element(element, "REQUEST-UPLOAD")
        if child is not None:
            request_upload_value = child.text
            obj.request_upload = request_upload_value

        return obj



class DiagnosticRequestUploadBuilder:
    """Builder for DiagnosticRequestUpload."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticRequestUpload = DiagnosticRequestUpload()

    def build(self) -> DiagnosticRequestUpload:
        """Build and return DiagnosticRequestUpload object.

        Returns:
            DiagnosticRequestUpload instance
        """
        # TODO: Add validation
        return self._obj
