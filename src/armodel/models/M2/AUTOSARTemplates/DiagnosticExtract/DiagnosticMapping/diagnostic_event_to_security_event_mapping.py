"""DiagnosticEventToSecurityEventMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 257)

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


class DiagnosticEventToSecurityEventMapping(DiagnosticMapping):
    """AUTOSAR DiagnosticEventToSecurityEventMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    diagnostic_event_ref: Optional[ARRef]
    security_event_context_ref: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticEventToSecurityEventMapping."""
        super().__init__()
        self.diagnostic_event_ref: Optional[ARRef] = None
        self.security_event_context_ref: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticEventToSecurityEventMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticEventToSecurityEventMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

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

        # Serialize security_event_context_ref
        if self.security_event_context_ref is not None:
            serialized = ARObject._serialize_item(self.security_event_context_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SECURITY-EVENT-CONTEXT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticEventToSecurityEventMapping":
        """Deserialize XML element to DiagnosticEventToSecurityEventMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticEventToSecurityEventMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticEventToSecurityEventMapping, cls).deserialize(element)

        # Parse diagnostic_event_ref
        child = ARObject._find_child_element(element, "DIAGNOSTIC-EVENT-REF")
        if child is not None:
            diagnostic_event_ref_value = ARRef.deserialize(child)
            obj.diagnostic_event_ref = diagnostic_event_ref_value

        # Parse security_event_context_ref
        child = ARObject._find_child_element(element, "SECURITY-EVENT-CONTEXT-REF")
        if child is not None:
            security_event_context_ref_value = ARRef.deserialize(child)
            obj.security_event_context_ref = security_event_context_ref_value

        return obj



class DiagnosticEventToSecurityEventMappingBuilder:
    """Builder for DiagnosticEventToSecurityEventMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEventToSecurityEventMapping = DiagnosticEventToSecurityEventMapping()

    def build(self) -> DiagnosticEventToSecurityEventMapping:
        """Build and return DiagnosticEventToSecurityEventMapping object.

        Returns:
            DiagnosticEventToSecurityEventMapping instance
        """
        # TODO: Add validation
        return self._obj
