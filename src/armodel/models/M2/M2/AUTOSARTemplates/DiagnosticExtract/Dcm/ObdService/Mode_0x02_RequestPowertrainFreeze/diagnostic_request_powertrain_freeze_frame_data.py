"""DiagnosticRequestPowertrainFreezeFrameData AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.ObdService.Mode_0x02_RequestPowertrainFreeze.diagnostic_powertrain_freeze_frame import (
    DiagnosticPowertrainFreezeFrame,
)


class DiagnosticRequestPowertrainFreezeFrameData(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticRequestPowertrainFreezeFrameData."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "freeze_frame_freeze_frame": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DiagnosticPowertrainFreezeFrame,
        ),  # freezeFrameFreezeFrame
        "request": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (DiagnosticRequest),
        ),  # request
    }

    def __init__(self) -> None:
        """Initialize DiagnosticRequestPowertrainFreezeFrameData."""
        super().__init__()
        self.freeze_frame_freeze_frame: Optional[DiagnosticPowertrainFreezeFrame] = None
        self.request: Optional[Any] = None


class DiagnosticRequestPowertrainFreezeFrameDataBuilder:
    """Builder for DiagnosticRequestPowertrainFreezeFrameData."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticRequestPowertrainFreezeFrameData = DiagnosticRequestPowertrainFreezeFrameData()

    def build(self) -> DiagnosticRequestPowertrainFreezeFrameData:
        """Build and return DiagnosticRequestPowertrainFreezeFrameData object.

        Returns:
            DiagnosticRequestPowertrainFreezeFrameData instance
        """
        # TODO: Add validation
        return self._obj
