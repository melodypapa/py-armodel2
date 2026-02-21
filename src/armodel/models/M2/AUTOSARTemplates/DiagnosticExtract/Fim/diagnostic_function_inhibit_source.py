"""DiagnosticFunctionInhibitSource AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 216)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Fim.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef


class DiagnosticFunctionInhibitSource(Identifiable):
    """AUTOSAR DiagnosticFunctionInhibitSource."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    event_ref: Optional[Any]
    event_group_ref: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticFunctionInhibitSource."""
        super().__init__()
        self.event_ref: Optional[Any] = None
        self.event_group_ref: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticFunctionInhibitSource to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticFunctionInhibitSource, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize event_ref
        if self.event_ref is not None:
            serialized = ARObject._serialize_item(self.event_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EVENT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize event_group_ref
        if self.event_group_ref is not None:
            serialized = ARObject._serialize_item(self.event_group_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EVENT-GROUP-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticFunctionInhibitSource":
        """Deserialize XML element to DiagnosticFunctionInhibitSource object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticFunctionInhibitSource object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticFunctionInhibitSource, cls).deserialize(element)

        # Parse event_ref
        child = ARObject._find_child_element(element, "EVENT-REF")
        if child is not None:
            event_ref_value = ARRef.deserialize(child)
            obj.event_ref = event_ref_value

        # Parse event_group_ref
        child = ARObject._find_child_element(element, "EVENT-GROUP-REF")
        if child is not None:
            event_group_ref_value = ARRef.deserialize(child)
            obj.event_group_ref = event_group_ref_value

        return obj



class DiagnosticFunctionInhibitSourceBuilder:
    """Builder for DiagnosticFunctionInhibitSource."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticFunctionInhibitSource = DiagnosticFunctionInhibitSource()

    def build(self) -> DiagnosticFunctionInhibitSource:
        """Build and return DiagnosticFunctionInhibitSource object.

        Returns:
            DiagnosticFunctionInhibitSource instance
        """
        # TODO: Add validation
        return self._obj
