"""DiagnosticComControl AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 108)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_CommunicationControl.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class DiagnosticComControl(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticComControl."""

    com_control: Optional[DiagnosticComControl]
    custom_sub: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize DiagnosticComControl."""
        super().__init__()
        self.com_control: Optional[DiagnosticComControl] = None
        self.custom_sub: Optional[PositiveInteger] = None


class DiagnosticComControlBuilder:
    """Builder for DiagnosticComControl."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticComControl = DiagnosticComControl()

    def build(self) -> DiagnosticComControl:
        """Build and return DiagnosticComControl object.

        Returns:
            DiagnosticComControl instance
        """
        # TODO: Add validation
        return self._obj
