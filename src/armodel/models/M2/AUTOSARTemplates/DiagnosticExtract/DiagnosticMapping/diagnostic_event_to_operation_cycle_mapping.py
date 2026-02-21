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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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

    diagnostic_event_ref: Optional[ARRef]
    operation_cycle_ref: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticEventToOperationCycleMapping."""
        super().__init__()
        self.diagnostic_event_ref: Optional[ARRef] = None
        self.operation_cycle_ref: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticEventToOperationCycleMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticEventToOperationCycleMapping, self).serialize()

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

        # Serialize operation_cycle_ref
        if self.operation_cycle_ref is not None:
            serialized = ARObject._serialize_item(self.operation_cycle_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("OPERATION-CYCLE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

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

        # Parse diagnostic_event_ref
        child = ARObject._find_child_element(element, "DIAGNOSTIC-EVENT-REF")
        if child is not None:
            diagnostic_event_ref_value = ARRef.deserialize(child)
            obj.diagnostic_event_ref = diagnostic_event_ref_value

        # Parse operation_cycle_ref
        child = ARObject._find_child_element(element, "OPERATION-CYCLE-REF")
        if child is not None:
            operation_cycle_ref_value = ARRef.deserialize(child)
            obj.operation_cycle_ref = operation_cycle_ref_value

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
