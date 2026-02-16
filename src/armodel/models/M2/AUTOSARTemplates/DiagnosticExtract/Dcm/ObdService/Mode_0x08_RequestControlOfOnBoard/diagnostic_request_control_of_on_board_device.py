"""DiagnosticRequestControlOfOnBoardDevice AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.ObdService.Mode_0x08_RequestControlOfOnBoard.diagnostic_test_routine_identifier import (
    DiagnosticTestRoutineIdentifier,
)


class DiagnosticRequestControlOfOnBoardDevice(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticRequestControlOfOnBoardDevice."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("request_control", None, False, False, any (DiagnosticRequest)),  # requestControl
        ("test_id_identifier", None, False, False, DiagnosticTestRoutineIdentifier),  # testIdIdentifier
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticRequestControlOfOnBoardDevice."""
        super().__init__()
        self.request_control: Optional[Any] = None
        self.test_id_identifier: Optional[DiagnosticTestRoutineIdentifier] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticRequestControlOfOnBoardDevice to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticRequestControlOfOnBoardDevice":
        """Create DiagnosticRequestControlOfOnBoardDevice from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticRequestControlOfOnBoardDevice instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticRequestControlOfOnBoardDevice since parent returns ARObject
        return cast("DiagnosticRequestControlOfOnBoardDevice", obj)


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
