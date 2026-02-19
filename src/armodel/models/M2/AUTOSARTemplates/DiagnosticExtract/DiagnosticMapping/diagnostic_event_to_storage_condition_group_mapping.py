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
    def serialize(self) -> ET.Element:
        """Serialize DiagnosticEventToStorageConditionGroupMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticEventToStorageConditionGroupMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize diagnostic_event
        if self.diagnostic_event is not None:
            serialized = ARObject._serialize_item(self.diagnostic_event, "DiagnosticEvent")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DIAGNOSTIC-EVENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize storage
        if self.storage is not None:
            serialized = ARObject._serialize_item(self.storage, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("STORAGE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

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
