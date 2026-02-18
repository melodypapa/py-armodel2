"""DiagnosticControlDTCSetting AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 110)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_ControlDTCSetting.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)


class DiagnosticControlDTCSetting(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticControlDTCSetting."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    dtc_setting_class: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticControlDTCSetting."""
        super().__init__()
        self.dtc_setting_class: Optional[Any] = None


class DiagnosticControlDTCSettingBuilder:
    """Builder for DiagnosticControlDTCSetting."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticControlDTCSetting = DiagnosticControlDTCSetting()

    def build(self) -> DiagnosticControlDTCSetting:
        """Build and return DiagnosticControlDTCSetting object.

        Returns:
            DiagnosticControlDTCSetting instance
        """
        # TODO: Add validation
        return self._obj
