"""DiagnosticDynamicallyDefineDataIdentifier AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 127)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_DynamicallyDefineDataIdentifier.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_dynamic_data_identifier import (
    DiagnosticDynamicDataIdentifier,
)


class DiagnosticDynamicallyDefineDataIdentifier(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticDynamicallyDefineDataIdentifier."""

    def __init__(self) -> None:
        """Initialize DiagnosticDynamicallyDefineDataIdentifier."""
        super().__init__()
        self.data_identifier: Optional[DiagnosticDynamicDataIdentifier] = None
        self.dynamically: Optional[Any] = None
        self.max_source: Optional[PositiveInteger] = None


class DiagnosticDynamicallyDefineDataIdentifierBuilder:
    """Builder for DiagnosticDynamicallyDefineDataIdentifier."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticDynamicallyDefineDataIdentifier = DiagnosticDynamicallyDefineDataIdentifier()

    def build(self) -> DiagnosticDynamicallyDefineDataIdentifier:
        """Build and return DiagnosticDynamicallyDefineDataIdentifier object.

        Returns:
            DiagnosticDynamicallyDefineDataIdentifier instance
        """
        # TODO: Add validation
        return self._obj
