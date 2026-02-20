"""DiagnosticSecureCodingMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 312)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import (
    DiagnosticMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_start_routine import (
    DiagnosticStartRoutine,
)


class DiagnosticSecureCodingMapping(DiagnosticMapping):
    """AUTOSAR DiagnosticSecureCodingMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_identifier_refs: list[Any]
    validation_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize DiagnosticSecureCodingMapping."""
        super().__init__()
        self.data_identifier_refs: list[Any] = []
        self.validation_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticSecureCodingMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticSecureCodingMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize data_identifier_refs (list to container "DATA-IDENTIFIER-REFS")
        if self.data_identifier_refs:
            wrapper = ET.Element("DATA-IDENTIFIER-REFS")
            for item in self.data_identifier_refs:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    child_elem = ET.Element("DATA-IDENTIFIER-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize validation_ref
        if self.validation_ref is not None:
            serialized = ARObject._serialize_item(self.validation_ref, "DiagnosticStartRoutine")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VALIDATION-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticSecureCodingMapping":
        """Deserialize XML element to DiagnosticSecureCodingMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticSecureCodingMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticSecureCodingMapping, cls).deserialize(element)

        # Parse data_identifier_refs (list from container "DATA-IDENTIFIER-REFS")
        obj.data_identifier_refs = []
        container = ARObject._find_child_element(element, "DATA-IDENTIFIER-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.data_identifier_refs.append(child_value)

        # Parse validation_ref
        child = ARObject._find_child_element(element, "VALIDATION-REF")
        if child is not None:
            validation_ref_value = ARRef.deserialize(child)
            obj.validation_ref = validation_ref_value

        return obj



class DiagnosticSecureCodingMappingBuilder:
    """Builder for DiagnosticSecureCodingMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticSecureCodingMapping = DiagnosticSecureCodingMapping()

    def build(self) -> DiagnosticSecureCodingMapping:
        """Build and return DiagnosticSecureCodingMapping object.

        Returns:
            DiagnosticSecureCodingMapping instance
        """
        # TODO: Add validation
        return self._obj
