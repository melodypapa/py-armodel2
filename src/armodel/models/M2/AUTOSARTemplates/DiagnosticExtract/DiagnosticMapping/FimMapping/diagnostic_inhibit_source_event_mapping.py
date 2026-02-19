"""DiagnosticInhibitSourceEventMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 260)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping_FimMapping.classes.json"""

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
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Fim.diagnostic_fim_event_group import (
    DiagnosticFimEventGroup,
)


class DiagnosticInhibitSourceEventMapping(DiagnosticMapping):
    """AUTOSAR DiagnosticInhibitSourceEventMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    diagnostic_event: Optional[DiagnosticEvent]
    event_group_group: Optional[DiagnosticFimEventGroup]
    inhibition_source: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticInhibitSourceEventMapping."""
        super().__init__()
        self.diagnostic_event: Optional[DiagnosticEvent] = None
        self.event_group_group: Optional[DiagnosticFimEventGroup] = None
        self.inhibition_source: Optional[Any] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticInhibitSourceEventMapping":
        """Deserialize XML element to DiagnosticInhibitSourceEventMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticInhibitSourceEventMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticInhibitSourceEventMapping, cls).deserialize(element)

        # Parse diagnostic_event
        child = ARObject._find_child_element(element, "DIAGNOSTIC-EVENT")
        if child is not None:
            diagnostic_event_value = ARObject._deserialize_by_tag(child, "DiagnosticEvent")
            obj.diagnostic_event = diagnostic_event_value

        # Parse event_group_group
        child = ARObject._find_child_element(element, "EVENT-GROUP-GROUP")
        if child is not None:
            event_group_group_value = ARObject._deserialize_by_tag(child, "DiagnosticFimEventGroup")
            obj.event_group_group = event_group_group_value

        # Parse inhibition_source
        child = ARObject._find_child_element(element, "INHIBITION-SOURCE")
        if child is not None:
            inhibition_source_value = child.text
            obj.inhibition_source = inhibition_source_value

        return obj



class DiagnosticInhibitSourceEventMappingBuilder:
    """Builder for DiagnosticInhibitSourceEventMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticInhibitSourceEventMapping = DiagnosticInhibitSourceEventMapping()

    def build(self) -> DiagnosticInhibitSourceEventMapping:
        """Build and return DiagnosticInhibitSourceEventMapping object.

        Returns:
            DiagnosticInhibitSourceEventMapping instance
        """
        # TODO: Add validation
        return self._obj
