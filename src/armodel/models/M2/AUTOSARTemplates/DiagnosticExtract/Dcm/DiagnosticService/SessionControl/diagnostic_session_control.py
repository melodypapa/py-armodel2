"""DiagnosticSessionControl AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 93)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_SessionControl.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.diagnostic_session import (
    DiagnosticSession,
)


class DiagnosticSessionControl(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticSessionControl."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    diagnostic_session_session: Optional[DiagnosticSession]
    session_control: Optional[DiagnosticSession]
    def __init__(self) -> None:
        """Initialize DiagnosticSessionControl."""
        super().__init__()
        self.diagnostic_session_session: Optional[DiagnosticSession] = None
        self.session_control: Optional[DiagnosticSession] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticSessionControl":
        """Deserialize XML element to DiagnosticSessionControl object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticSessionControl object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse diagnostic_session_session
        child = ARObject._find_child_element(element, "DIAGNOSTIC-SESSION-SESSION")
        if child is not None:
            diagnostic_session_session_value = ARObject._deserialize_by_tag(child, "DiagnosticSession")
            obj.diagnostic_session_session = diagnostic_session_session_value

        # Parse session_control
        child = ARObject._find_child_element(element, "SESSION-CONTROL")
        if child is not None:
            session_control_value = ARObject._deserialize_by_tag(child, "DiagnosticSession")
            obj.session_control = session_control_value

        return obj



class DiagnosticSessionControlBuilder:
    """Builder for DiagnosticSessionControl."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticSessionControl = DiagnosticSessionControl()

    def build(self) -> DiagnosticSessionControl:
        """Build and return DiagnosticSessionControl object.

        Returns:
            DiagnosticSessionControl instance
        """
        # TODO: Add validation
        return self._obj
