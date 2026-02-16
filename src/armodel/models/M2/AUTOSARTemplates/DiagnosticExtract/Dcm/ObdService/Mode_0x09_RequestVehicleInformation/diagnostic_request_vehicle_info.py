"""DiagnosticRequestVehicleInfo AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_info_type import (
    DiagnosticInfoType,
)


class DiagnosticRequestVehicleInfo(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticRequestVehicleInfo."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("info_type", None, False, False, DiagnosticInfoType),  # infoType
        ("request_vehicle", None, False, False, any (DiagnosticRequest)),  # requestVehicle
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticRequestVehicleInfo."""
        super().__init__()
        self.info_type: Optional[DiagnosticInfoType] = None
        self.request_vehicle: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticRequestVehicleInfo to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticRequestVehicleInfo":
        """Create DiagnosticRequestVehicleInfo from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticRequestVehicleInfo instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticRequestVehicleInfo since parent returns ARObject
        return cast("DiagnosticRequestVehicleInfo", obj)


class DiagnosticRequestVehicleInfoBuilder:
    """Builder for DiagnosticRequestVehicleInfo."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticRequestVehicleInfo = DiagnosticRequestVehicleInfo()

    def build(self) -> DiagnosticRequestVehicleInfo:
        """Build and return DiagnosticRequestVehicleInfo object.

        Returns:
            DiagnosticRequestVehicleInfo instance
        """
        # TODO: Add validation
        return self._obj
