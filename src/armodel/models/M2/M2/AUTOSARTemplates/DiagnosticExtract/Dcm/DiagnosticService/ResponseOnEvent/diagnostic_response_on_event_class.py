"""DiagnosticResponseOnEventClass AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 132)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_ResponseOnEvent.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    TimeValue,
)


class DiagnosticResponseOnEventClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticResponseOnEventClass."""

    def __init__(self) -> None:
        """Initialize DiagnosticResponseOnEventClass."""
        super().__init__()
        self.max_number_of: Optional[PositiveInteger] = None
        self.max_num: Optional[PositiveInteger] = None
        self.max_supported: Optional[PositiveInteger] = None
        self.response_on: Optional[TimeValue] = None
        self.store_event: Optional[Boolean] = None


class DiagnosticResponseOnEventClassBuilder:
    """Builder for DiagnosticResponseOnEventClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticResponseOnEventClass = DiagnosticResponseOnEventClass()

    def build(self) -> DiagnosticResponseOnEventClass:
        """Build and return DiagnosticResponseOnEventClass object.

        Returns:
            DiagnosticResponseOnEventClass instance
        """
        # TODO: Add validation
        return self._obj
