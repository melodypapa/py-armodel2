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
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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

    diagnostic_event_ref: Optional[ARRef]
    storage_ref: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticEventToStorageConditionGroupMapping."""
        super().__init__()
        self.diagnostic_event_ref: Optional[ARRef] = None
        self.storage_ref: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticEventToStorageConditionGroupMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticEventToStorageConditionGroupMapping, self).serialize()

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
            serialized = SerializationHelper.serialize_item(self.diagnostic_event_ref, "DiagnosticEvent")
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

        # Serialize storage_ref
        if self.storage_ref is not None:
            serialized = SerializationHelper.serialize_item(self.storage_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("STORAGE-REF")
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

        # Parse diagnostic_event_ref
        child = SerializationHelper.find_child_element(element, "DIAGNOSTIC-EVENT-REF")
        if child is not None:
            diagnostic_event_ref_value = ARRef.deserialize(child)
            obj.diagnostic_event_ref = diagnostic_event_ref_value

        # Parse storage_ref
        child = SerializationHelper.find_child_element(element, "STORAGE-REF")
        if child is not None:
            storage_ref_value = ARRef.deserialize(child)
            obj.storage_ref = storage_ref_value

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
