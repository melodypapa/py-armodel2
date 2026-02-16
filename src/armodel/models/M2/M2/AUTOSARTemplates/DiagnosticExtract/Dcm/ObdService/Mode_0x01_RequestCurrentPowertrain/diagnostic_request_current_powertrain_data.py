"""DiagnosticRequestCurrentPowertrainData AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_parameter import (
    DiagnosticParameter,
)


class DiagnosticRequestCurrentPowertrainData(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticRequestCurrentPowertrainData."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "pid": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DiagnosticParameter,
        ),  # pid
        "request_current": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (DiagnosticRequest),
        ),  # requestCurrent
    }

    def __init__(self) -> None:
        """Initialize DiagnosticRequestCurrentPowertrainData."""
        super().__init__()
        self.pid: Optional[DiagnosticParameter] = None
        self.request_current: Optional[Any] = None


class DiagnosticRequestCurrentPowertrainDataBuilder:
    """Builder for DiagnosticRequestCurrentPowertrainData."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticRequestCurrentPowertrainData = DiagnosticRequestCurrentPowertrainData()

    def build(self) -> DiagnosticRequestCurrentPowertrainData:
        """Build and return DiagnosticRequestCurrentPowertrainData object.

        Returns:
            DiagnosticRequestCurrentPowertrainData instance
        """
        # TODO: Add validation
        return self._obj
