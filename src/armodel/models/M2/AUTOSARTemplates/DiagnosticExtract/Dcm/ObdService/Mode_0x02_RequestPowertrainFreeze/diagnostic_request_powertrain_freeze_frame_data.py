"""DiagnosticRequestPowertrainFreezeFrameData AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.ObdService.Mode_0x02_RequestPowertrainFreeze.diagnostic_powertrain_freeze_frame import (
    DiagnosticPowertrainFreezeFrame,
)


class DiagnosticRequestPowertrainFreezeFrameData(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticRequestPowertrainFreezeFrameData."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("freeze_frame_freeze_frame", None, False, False, DiagnosticPowertrainFreezeFrame),  # freezeFrameFreezeFrame
        ("request", None, False, False, any (DiagnosticRequest)),  # request
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticRequestPowertrainFreezeFrameData."""
        super().__init__()
        self.freeze_frame_freeze_frame: Optional[DiagnosticPowertrainFreezeFrame] = None
        self.request: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticRequestPowertrainFreezeFrameData to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticRequestPowertrainFreezeFrameData":
        """Create DiagnosticRequestPowertrainFreezeFrameData from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticRequestPowertrainFreezeFrameData instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticRequestPowertrainFreezeFrameData since parent returns ARObject
        return cast("DiagnosticRequestPowertrainFreezeFrameData", obj)


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
