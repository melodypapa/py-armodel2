"""DiagnosticEventToEnableConditionGroupMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 247)

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


class DiagnosticEventToEnableConditionGroupMapping(DiagnosticMapping):
    """AUTOSAR DiagnosticEventToEnableConditionGroupMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    diagnostic_event: Optional[DiagnosticEvent]
    enable_condition: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticEventToEnableConditionGroupMapping."""
        super().__init__()
        self.diagnostic_event: Optional[DiagnosticEvent] = None
        self.enable_condition: Optional[Any] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticEventToEnableConditionGroupMapping":
        """Deserialize XML element to DiagnosticEventToEnableConditionGroupMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticEventToEnableConditionGroupMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticEventToEnableConditionGroupMapping, cls).deserialize(element)

        # Parse diagnostic_event
        child = ARObject._find_child_element(element, "DIAGNOSTIC-EVENT")
        if child is not None:
            diagnostic_event_value = ARObject._deserialize_by_tag(child, "DiagnosticEvent")
            obj.diagnostic_event = diagnostic_event_value

        # Parse enable_condition
        child = ARObject._find_child_element(element, "ENABLE-CONDITION")
        if child is not None:
            enable_condition_value = child.text
            obj.enable_condition = enable_condition_value

        return obj



class DiagnosticEventToEnableConditionGroupMappingBuilder:
    """Builder for DiagnosticEventToEnableConditionGroupMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEventToEnableConditionGroupMapping = DiagnosticEventToEnableConditionGroupMapping()

    def build(self) -> DiagnosticEventToEnableConditionGroupMapping:
        """Build and return DiagnosticEventToEnableConditionGroupMapping object.

        Returns:
            DiagnosticEventToEnableConditionGroupMapping instance
        """
        # TODO: Add validation
        return self._obj
