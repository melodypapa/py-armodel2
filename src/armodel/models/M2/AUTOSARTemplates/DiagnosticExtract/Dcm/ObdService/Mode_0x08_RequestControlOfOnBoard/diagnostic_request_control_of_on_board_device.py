"""DiagnosticRequestControlOfOnBoardDevice AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.ObdService.Mode_0x08_RequestControlOfOnBoard.diagnostic_test_routine_identifier import (
    DiagnosticTestRoutineIdentifier,
)


class DiagnosticRequestControlOfOnBoardDevice(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticRequestControlOfOnBoardDevice."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "request_control": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (DiagnosticRequest),
        ),  # requestControl
        "test_id_identifier": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DiagnosticTestRoutineIdentifier,
        ),  # testIdIdentifier
    }

    def __init__(self) -> None:
        """Initialize DiagnosticRequestControlOfOnBoardDevice."""
        super().__init__()
        self.request_control: Optional[Any] = None
        self.test_id_identifier: Optional[DiagnosticTestRoutineIdentifier] = None


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
