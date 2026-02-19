"""DiagnosticRequestVehicleInfo AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 160)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_ObdService_Mode_0x09_RequestVehicleInformation.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_info_type import (
    DiagnosticInfoType,
)


class DiagnosticRequestVehicleInfo(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticRequestVehicleInfo."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    info_type: Optional[DiagnosticInfoType]
    request_vehicle: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticRequestVehicleInfo."""
        super().__init__()
        self.info_type: Optional[DiagnosticInfoType] = None
        self.request_vehicle: Optional[Any] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticRequestVehicleInfo":
        """Deserialize XML element to DiagnosticRequestVehicleInfo object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticRequestVehicleInfo object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticRequestVehicleInfo, cls).deserialize(element)

        # Parse info_type
        child = ARObject._find_child_element(element, "INFO-TYPE")
        if child is not None:
            info_type_value = ARObject._deserialize_by_tag(child, "DiagnosticInfoType")
            obj.info_type = info_type_value

        # Parse request_vehicle
        child = ARObject._find_child_element(element, "REQUEST-VEHICLE")
        if child is not None:
            request_vehicle_value = child.text
            obj.request_vehicle = request_vehicle_value

        return obj



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
