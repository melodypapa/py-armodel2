"""DiagnosticClearResetEmissionRelatedInfo AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 154)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_ObdService_Mode_0x04_ClearResetEmission.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class DiagnosticClearResetEmissionRelatedInfo(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticClearResetEmissionRelatedInfo."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    clear_reset: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticClearResetEmissionRelatedInfo."""
        super().__init__()
        self.clear_reset: Optional[Any] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticClearResetEmissionRelatedInfo":
        """Deserialize XML element to DiagnosticClearResetEmissionRelatedInfo object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticClearResetEmissionRelatedInfo object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse clear_reset
        child = ARObject._find_child_element(element, "CLEAR-RESET")
        if child is not None:
            clear_reset_value = child.text
            obj.clear_reset = clear_reset_value

        return obj



class DiagnosticClearResetEmissionRelatedInfoBuilder:
    """Builder for DiagnosticClearResetEmissionRelatedInfo."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticClearResetEmissionRelatedInfo = DiagnosticClearResetEmissionRelatedInfo()

    def build(self) -> DiagnosticClearResetEmissionRelatedInfo:
        """Build and return DiagnosticClearResetEmissionRelatedInfo object.

        Returns:
            DiagnosticClearResetEmissionRelatedInfo instance
        """
        # TODO: Add validation
        return self._obj
