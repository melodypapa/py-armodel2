"""DiagnosticFimAliasEventGroupMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 263)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping_FimMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import (
    DiagnosticMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Fim.diagnostic_fim_event_group import (
    DiagnosticFimEventGroup,
)


class DiagnosticFimAliasEventGroupMapping(DiagnosticMapping):
    """AUTOSAR DiagnosticFimAliasEventGroupMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    actual_event_ref: Optional[ARRef]
    alias_event_ref: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticFimAliasEventGroupMapping."""
        super().__init__()
        self.actual_event_ref: Optional[ARRef] = None
        self.alias_event_ref: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticFimAliasEventGroupMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticFimAliasEventGroupMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize actual_event_ref
        if self.actual_event_ref is not None:
            serialized = ARObject._serialize_item(self.actual_event_ref, "DiagnosticFimEventGroup")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ACTUAL-EVENT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize alias_event_ref
        if self.alias_event_ref is not None:
            serialized = ARObject._serialize_item(self.alias_event_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ALIAS-EVENT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticFimAliasEventGroupMapping":
        """Deserialize XML element to DiagnosticFimAliasEventGroupMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticFimAliasEventGroupMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticFimAliasEventGroupMapping, cls).deserialize(element)

        # Parse actual_event_ref
        child = ARObject._find_child_element(element, "ACTUAL-EVENT-REF")
        if child is not None:
            actual_event_ref_value = ARRef.deserialize(child)
            obj.actual_event_ref = actual_event_ref_value

        # Parse alias_event_ref
        child = ARObject._find_child_element(element, "ALIAS-EVENT-REF")
        if child is not None:
            alias_event_ref_value = ARRef.deserialize(child)
            obj.alias_event_ref = alias_event_ref_value

        return obj



class DiagnosticFimAliasEventGroupMappingBuilder:
    """Builder for DiagnosticFimAliasEventGroupMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticFimAliasEventGroupMapping = DiagnosticFimAliasEventGroupMapping()

    def build(self) -> DiagnosticFimAliasEventGroupMapping:
        """Build and return DiagnosticFimAliasEventGroupMapping object.

        Returns:
            DiagnosticFimAliasEventGroupMapping instance
        """
        # TODO: Add validation
        return self._obj
