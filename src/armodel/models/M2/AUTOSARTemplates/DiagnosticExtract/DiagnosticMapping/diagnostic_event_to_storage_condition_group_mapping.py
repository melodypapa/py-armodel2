"""DiagnosticEventToStorageConditionGroupMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 248)

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


class DiagnosticEventToStorageConditionGroupMapping(DiagnosticMapping):
    """AUTOSAR DiagnosticEventToStorageConditionGroupMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    diagnostic_event: Optional[DiagnosticEvent]
    storage: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticEventToStorageConditionGroupMapping."""
        super().__init__()
        self.diagnostic_event: Optional[DiagnosticEvent] = None
        self.storage: Optional[Any] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticEventToStorageConditionGroupMapping":
        """Deserialize XML element to DiagnosticEventToStorageConditionGroupMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticEventToStorageConditionGroupMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticEventToStorageConditionGroupMapping, cls).deserialize(element)

        # Parse diagnostic_event
        child = ARObject._find_child_element(element, "DIAGNOSTIC-EVENT")
        if child is not None:
            diagnostic_event_value = ARObject._deserialize_by_tag(child, "DiagnosticEvent")
            obj.diagnostic_event = diagnostic_event_value

        # Parse storage
        child = ARObject._find_child_element(element, "STORAGE")
        if child is not None:
            storage_value = child.text
            obj.storage = storage_value

        return obj



class DiagnosticEventToStorageConditionGroupMappingBuilder:
    """Builder for DiagnosticEventToStorageConditionGroupMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEventToStorageConditionGroupMapping = DiagnosticEventToStorageConditionGroupMapping()

    def build(self) -> DiagnosticEventToStorageConditionGroupMapping:
        """Build and return DiagnosticEventToStorageConditionGroupMapping object.

        Returns:
            DiagnosticEventToStorageConditionGroupMapping instance
        """
        # TODO: Add validation
        return self._obj
