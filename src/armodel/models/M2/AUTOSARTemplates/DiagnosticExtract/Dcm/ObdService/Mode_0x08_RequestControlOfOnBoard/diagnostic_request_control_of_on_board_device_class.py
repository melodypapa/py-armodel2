"""DiagnosticRequestControlOfOnBoardDeviceClass AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 158)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_ObdService_Mode_0x08_RequestControlOfOnBoard.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)


class DiagnosticRequestControlOfOnBoardDeviceClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticRequestControlOfOnBoardDeviceClass."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
    }

    def __init__(self) -> None:
        """Initialize DiagnosticRequestControlOfOnBoardDeviceClass."""
        super().__init__()


class DiagnosticRequestControlOfOnBoardDeviceClassBuilder:
    """Builder for DiagnosticRequestControlOfOnBoardDeviceClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticRequestControlOfOnBoardDeviceClass = DiagnosticRequestControlOfOnBoardDeviceClass()

    def build(self) -> DiagnosticRequestControlOfOnBoardDeviceClass:
        """Build and return DiagnosticRequestControlOfOnBoardDeviceClass object.

        Returns:
            DiagnosticRequestControlOfOnBoardDeviceClass instance
        """
        # TODO: Add validation
        return self._obj
