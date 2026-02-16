"""DiagnosticRequestCurrentPowertrainData AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_parameter import (
    DiagnosticParameter,
)


class DiagnosticRequestCurrentPowertrainData(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticRequestCurrentPowertrainData."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("pid", None, False, False, DiagnosticParameter),  # pid
        ("request_current", None, False, False, any (DiagnosticRequest)),  # requestCurrent
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticRequestCurrentPowertrainData."""
        super().__init__()
        self.pid: Optional[DiagnosticParameter] = None
        self.request_current: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticRequestCurrentPowertrainData to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticRequestCurrentPowertrainData":
        """Create DiagnosticRequestCurrentPowertrainData from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticRequestCurrentPowertrainData instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticRequestCurrentPowertrainData since parent returns ARObject
        return cast("DiagnosticRequestCurrentPowertrainData", obj)


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
