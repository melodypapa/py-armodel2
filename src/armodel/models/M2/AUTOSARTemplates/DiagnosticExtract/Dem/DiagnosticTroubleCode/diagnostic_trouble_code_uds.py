"""DiagnosticTroubleCodeUds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 173)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticTroubleCode.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTroubleCode.diagnostic_trouble_code import (
    DiagnosticTroubleCode,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTroubleCode import (
    DiagnosticUdsSeverityEnum,
    DiagnosticWwhObdDtcClassEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTroubleCode.event_obd_readiness_group import (
    EventObdReadinessGroup,
)


class DiagnosticTroubleCodeUds(DiagnosticTroubleCode):
    """AUTOSAR DiagnosticTroubleCodeUds."""

    def __init__(self) -> None:
        """Initialize DiagnosticTroubleCodeUds."""
        super().__init__()
        self.consider_pto: Optional[Boolean] = None
        self.dtc_props_props: Optional[DiagnosticTroubleCode] = None
        self.event_readiness: Optional[EventObdReadinessGroup] = None
        self.functional_unit: Optional[PositiveInteger] = None
        self.obd_dtc: Optional[PositiveInteger] = None
        self.severity: Optional[DiagnosticUdsSeverityEnum] = None
        self.uds_dtc_value: Optional[PositiveInteger] = None
        self.wwh_obd_dtc: Optional[DiagnosticWwhObdDtcClassEnum] = None


class DiagnosticTroubleCodeUdsBuilder:
    """Builder for DiagnosticTroubleCodeUds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticTroubleCodeUds = DiagnosticTroubleCodeUds()

    def build(self) -> DiagnosticTroubleCodeUds:
        """Build and return DiagnosticTroubleCodeUds object.

        Returns:
            DiagnosticTroubleCodeUds instance
        """
        # TODO: Add validation
        return self._obj
