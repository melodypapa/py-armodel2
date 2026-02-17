"""DiagnosticRequestVehicleInfoClass AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 160)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_ObdService_Mode_0x09_RequestVehicleInformation.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)


class DiagnosticRequestVehicleInfoClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticRequestVehicleInfoClass."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
    }

    def __init__(self) -> None:
        """Initialize DiagnosticRequestVehicleInfoClass."""
        super().__init__()


class DiagnosticRequestVehicleInfoClassBuilder:
    """Builder for DiagnosticRequestVehicleInfoClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticRequestVehicleInfoClass = DiagnosticRequestVehicleInfoClass()

    def build(self) -> DiagnosticRequestVehicleInfoClass:
        """Build and return DiagnosticRequestVehicleInfoClass object.

        Returns:
            DiagnosticRequestVehicleInfoClass instance
        """
        # TODO: Add validation
        return self._obj
