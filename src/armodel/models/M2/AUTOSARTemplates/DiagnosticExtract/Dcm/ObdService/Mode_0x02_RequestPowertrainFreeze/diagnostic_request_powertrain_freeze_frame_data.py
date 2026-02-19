"""DiagnosticRequestPowertrainFreezeFrameData AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 152)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_ObdService_Mode_0x02_RequestPowertrainFreeze.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.ObdService.Mode_0x02_RequestPowertrainFreeze.diagnostic_powertrain_freeze_frame import (
    DiagnosticPowertrainFreezeFrame,
)


class DiagnosticRequestPowertrainFreezeFrameData(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticRequestPowertrainFreezeFrameData."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    freeze_frame_freeze_frame: Optional[DiagnosticPowertrainFreezeFrame]
    request: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticRequestPowertrainFreezeFrameData."""
        super().__init__()
        self.freeze_frame_freeze_frame: Optional[DiagnosticPowertrainFreezeFrame] = None
        self.request: Optional[Any] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticRequestPowertrainFreezeFrameData":
        """Deserialize XML element to DiagnosticRequestPowertrainFreezeFrameData object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticRequestPowertrainFreezeFrameData object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse freeze_frame_freeze_frame
        child = ARObject._find_child_element(element, "FREEZE-FRAME-FREEZE-FRAME")
        if child is not None:
            freeze_frame_freeze_frame_value = ARObject._deserialize_by_tag(child, "DiagnosticPowertrainFreezeFrame")
            obj.freeze_frame_freeze_frame = freeze_frame_freeze_frame_value

        # Parse request
        child = ARObject._find_child_element(element, "REQUEST")
        if child is not None:
            request_value = child.text
            obj.request = request_value

        return obj



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
