"""DiagnosticEventToOperationCycleMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 245)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import (
    DiagnosticMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_event import (
    DiagnosticEvent,
)


class DiagnosticEventToOperationCycleMapping(DiagnosticMapping):
    """AUTOSAR DiagnosticEventToOperationCycleMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    diagnostic_event: Optional[DiagnosticEvent]
    operation_cycle: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticEventToOperationCycleMapping."""
        super().__init__()
        self.diagnostic_event: Optional[DiagnosticEvent] = None
        self.operation_cycle: Optional[Any] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticEventToOperationCycleMapping":
        """Deserialize XML element to DiagnosticEventToOperationCycleMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticEventToOperationCycleMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticEventToOperationCycleMapping, cls).deserialize(element)

        # Parse diagnostic_event
        child = ARObject._find_child_element(element, "DIAGNOSTIC-EVENT")
        if child is not None:
            diagnostic_event_value = ARObject._deserialize_by_tag(child, "DiagnosticEvent")
            obj.diagnostic_event = diagnostic_event_value

        # Parse operation_cycle
        child = ARObject._find_child_element(element, "OPERATION-CYCLE")
        if child is not None:
            operation_cycle_value = child.text
            obj.operation_cycle = operation_cycle_value

        return obj



class DiagnosticEventToOperationCycleMappingBuilder:
    """Builder for DiagnosticEventToOperationCycleMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEventToOperationCycleMapping = DiagnosticEventToOperationCycleMapping()

    def build(self) -> DiagnosticEventToOperationCycleMapping:
        """Build and return DiagnosticEventToOperationCycleMapping object.

        Returns:
            DiagnosticEventToOperationCycleMapping instance
        """
        # TODO: Add validation
        return self._obj
