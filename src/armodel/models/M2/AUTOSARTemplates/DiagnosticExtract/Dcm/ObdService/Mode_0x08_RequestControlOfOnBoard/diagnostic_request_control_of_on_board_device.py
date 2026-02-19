"""DiagnosticRequestControlOfOnBoardDevice AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 157)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_ObdService_Mode_0x08_RequestControlOfOnBoard.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.ObdService.Mode_0x08_RequestControlOfOnBoard.diagnostic_test_routine_identifier import (
    DiagnosticTestRoutineIdentifier,
)


class DiagnosticRequestControlOfOnBoardDevice(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticRequestControlOfOnBoardDevice."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    request_control: Optional[Any]
    test_id_identifier: Optional[DiagnosticTestRoutineIdentifier]
    def __init__(self) -> None:
        """Initialize DiagnosticRequestControlOfOnBoardDevice."""
        super().__init__()
        self.request_control: Optional[Any] = None
        self.test_id_identifier: Optional[DiagnosticTestRoutineIdentifier] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticRequestControlOfOnBoardDevice":
        """Deserialize XML element to DiagnosticRequestControlOfOnBoardDevice object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticRequestControlOfOnBoardDevice object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticRequestControlOfOnBoardDevice, cls).deserialize(element)

        # Parse request_control
        child = ARObject._find_child_element(element, "REQUEST-CONTROL")
        if child is not None:
            request_control_value = child.text
            obj.request_control = request_control_value

        # Parse test_id_identifier
        child = ARObject._find_child_element(element, "TEST-ID-IDENTIFIER")
        if child is not None:
            test_id_identifier_value = ARObject._deserialize_by_tag(child, "DiagnosticTestRoutineIdentifier")
            obj.test_id_identifier = test_id_identifier_value

        return obj



class DiagnosticRequestControlOfOnBoardDeviceBuilder:
    """Builder for DiagnosticRequestControlOfOnBoardDevice."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticRequestControlOfOnBoardDevice = DiagnosticRequestControlOfOnBoardDevice()

    def build(self) -> DiagnosticRequestControlOfOnBoardDevice:
        """Build and return DiagnosticRequestControlOfOnBoardDevice object.

        Returns:
            DiagnosticRequestControlOfOnBoardDevice instance
        """
        # TODO: Add validation
        return self._obj
