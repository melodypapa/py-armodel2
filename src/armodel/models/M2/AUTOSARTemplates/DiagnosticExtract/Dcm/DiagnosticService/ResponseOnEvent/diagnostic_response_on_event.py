"""DiagnosticResponseOnEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 132)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_ResponseOnEvent.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.ResponseOnEvent.diagnostic_event_window import (
    DiagnosticEventWindow,
)


class DiagnosticResponseOnEvent(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticResponseOnEvent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    event_windows: list[DiagnosticEventWindow]
    response_on: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticResponseOnEvent."""
        super().__init__()
        self.event_windows: list[DiagnosticEventWindow] = []
        self.response_on: Optional[Any] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticResponseOnEvent":
        """Deserialize XML element to DiagnosticResponseOnEvent object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticResponseOnEvent object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticResponseOnEvent, cls).deserialize(element)

        # Parse event_windows (list from container "EVENT-WINDOWS")
        obj.event_windows = []
        container = ARObject._find_child_element(element, "EVENT-WINDOWS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.event_windows.append(child_value)

        # Parse response_on
        child = ARObject._find_child_element(element, "RESPONSE-ON")
        if child is not None:
            response_on_value = child.text
            obj.response_on = response_on_value

        return obj



class DiagnosticResponseOnEventBuilder:
    """Builder for DiagnosticResponseOnEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticResponseOnEvent = DiagnosticResponseOnEvent()

    def build(self) -> DiagnosticResponseOnEvent:
        """Build and return DiagnosticResponseOnEvent object.

        Returns:
            DiagnosticResponseOnEvent instance
        """
        # TODO: Add validation
        return self._obj
