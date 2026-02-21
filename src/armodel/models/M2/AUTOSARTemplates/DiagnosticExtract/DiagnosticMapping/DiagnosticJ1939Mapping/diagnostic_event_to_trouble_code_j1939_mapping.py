"""DiagnosticEventToTroubleCodeJ1939Mapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 269)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping_DiagnosticJ1939Mapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import (
    DiagnosticMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_event import (
    DiagnosticEvent,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTroubleCode.diagnostic_trouble_code import (
    DiagnosticTroubleCode,
)


class DiagnosticEventToTroubleCodeJ1939Mapping(DiagnosticMapping):
    """AUTOSAR DiagnosticEventToTroubleCodeJ1939Mapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    diagnostic_event_ref: Optional[ARRef]
    trouble_code_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize DiagnosticEventToTroubleCodeJ1939Mapping."""
        super().__init__()
        self.diagnostic_event_ref: Optional[ARRef] = None
        self.trouble_code_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticEventToTroubleCodeJ1939Mapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticEventToTroubleCodeJ1939Mapping, self).serialize()

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

        # Serialize trouble_code_ref
        if self.trouble_code_ref is not None:
            serialized = ARObject._serialize_item(self.trouble_code_ref, "DiagnosticTroubleCode")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TROUBLE-CODE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticEventToTroubleCodeJ1939Mapping":
        """Deserialize XML element to DiagnosticEventToTroubleCodeJ1939Mapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticEventToTroubleCodeJ1939Mapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticEventToTroubleCodeJ1939Mapping, cls).deserialize(element)

        # Parse diagnostic_event_ref
        child = ARObject._find_child_element(element, "DIAGNOSTIC-EVENT-REF")
        if child is not None:
            diagnostic_event_ref_value = ARRef.deserialize(child)
            obj.diagnostic_event_ref = diagnostic_event_ref_value

        # Parse trouble_code_ref
        child = ARObject._find_child_element(element, "TROUBLE-CODE-REF")
        if child is not None:
            trouble_code_ref_value = ARRef.deserialize(child)
            obj.trouble_code_ref = trouble_code_ref_value

        return obj



class DiagnosticEventToTroubleCodeJ1939MappingBuilder:
    """Builder for DiagnosticEventToTroubleCodeJ1939Mapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEventToTroubleCodeJ1939Mapping = DiagnosticEventToTroubleCodeJ1939Mapping()

    def build(self) -> DiagnosticEventToTroubleCodeJ1939Mapping:
        """Build and return DiagnosticEventToTroubleCodeJ1939Mapping object.

        Returns:
            DiagnosticEventToTroubleCodeJ1939Mapping instance
        """
        # TODO: Add validation
        return self._obj
