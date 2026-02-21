"""DiagnosticEventToDebounceAlgorithmMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 246)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import (
    DiagnosticMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_event import (
    DiagnosticEvent,
)


class DiagnosticEventToDebounceAlgorithmMapping(DiagnosticMapping):
    """AUTOSAR DiagnosticEventToDebounceAlgorithmMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    debounce_ref: Optional[Any]
    diagnostic_event_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize DiagnosticEventToDebounceAlgorithmMapping."""
        super().__init__()
        self.debounce_ref: Optional[Any] = None
        self.diagnostic_event_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticEventToDebounceAlgorithmMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticEventToDebounceAlgorithmMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize debounce_ref
        if self.debounce_ref is not None:
            serialized = ARObject._serialize_item(self.debounce_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DEBOUNCE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize diagnostic_event_ref
        if self.diagnostic_event_ref is not None:
            serialized = ARObject._serialize_item(self.diagnostic_event_ref, "DiagnosticEvent")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DIAGNOSTIC-EVENT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticEventToDebounceAlgorithmMapping":
        """Deserialize XML element to DiagnosticEventToDebounceAlgorithmMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticEventToDebounceAlgorithmMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticEventToDebounceAlgorithmMapping, cls).deserialize(element)

        # Parse debounce_ref
        child = ARObject._find_child_element(element, "DEBOUNCE-REF")
        if child is not None:
            debounce_ref_value = ARRef.deserialize(child)
            obj.debounce_ref = debounce_ref_value

        # Parse diagnostic_event_ref
        child = ARObject._find_child_element(element, "DIAGNOSTIC-EVENT-REF")
        if child is not None:
            diagnostic_event_ref_value = ARRef.deserialize(child)
            obj.diagnostic_event_ref = diagnostic_event_ref_value

        return obj



class DiagnosticEventToDebounceAlgorithmMappingBuilder:
    """Builder for DiagnosticEventToDebounceAlgorithmMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEventToDebounceAlgorithmMapping = DiagnosticEventToDebounceAlgorithmMapping()

    def build(self) -> DiagnosticEventToDebounceAlgorithmMapping:
        """Build and return DiagnosticEventToDebounceAlgorithmMapping object.

        Returns:
            DiagnosticEventToDebounceAlgorithmMapping instance
        """
        # TODO: Add validation
        return self._obj
