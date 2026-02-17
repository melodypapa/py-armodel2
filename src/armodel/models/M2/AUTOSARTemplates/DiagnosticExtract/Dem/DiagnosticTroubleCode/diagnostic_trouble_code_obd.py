"""DiagnosticTroubleCodeObd AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 174)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticTroubleCode.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTroubleCode.diagnostic_trouble_code import (
    DiagnosticTroubleCode,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTroubleCode.event_obd_readiness_group import (
    EventObdReadinessGroup,
)


class DiagnosticTroubleCodeObd(DiagnosticTroubleCode):
    """AUTOSAR DiagnosticTroubleCodeObd."""

    consider_pto: Optional[Boolean]
    dtc_props_props: Optional[DiagnosticTroubleCode]
    event_readiness: Optional[EventObdReadinessGroup]
    obd_dtc_value: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize DiagnosticTroubleCodeObd."""
        super().__init__()
        self.consider_pto: Optional[Boolean] = None
        self.dtc_props_props: Optional[DiagnosticTroubleCode] = None
        self.event_readiness: Optional[EventObdReadinessGroup] = None
        self.obd_dtc_value: Optional[PositiveInteger] = None


class DiagnosticTroubleCodeObdBuilder:
    """Builder for DiagnosticTroubleCodeObd."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticTroubleCodeObd = DiagnosticTroubleCodeObd()

    def build(self) -> DiagnosticTroubleCodeObd:
        """Build and return DiagnosticTroubleCodeObd object.

        Returns:
            DiagnosticTroubleCodeObd instance
        """
        # TODO: Add validation
        return self._obj
