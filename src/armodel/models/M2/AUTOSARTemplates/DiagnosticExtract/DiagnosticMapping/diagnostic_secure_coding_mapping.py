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

    data_identifiers: list[Any]
    validation: Optional[DiagnosticStartRoutine]
    def __init__(self) -> None:
        """Initialize DiagnosticSecureCodingMapping."""
        super().__init__()
        self.data_identifiers: list[Any] = []
        self.validation: Optional[DiagnosticStartRoutine] = None
    def serialize(self) -> ET.Element:
        """Serialize DiagnosticSecureCodingMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticSecureCodingMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize data_identifiers (list to container "DATA-IDENTIFIERS")
        if self.data_identifiers:
            wrapper = ET.Element("DATA-IDENTIFIERS")
            for item in self.data_identifiers:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize validation
        if self.validation is not None:
            serialized = ARObject._serialize_item(self.validation, "DiagnosticStartRoutine")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VALIDATION")
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

        # Parse data_identifiers (list from container "DATA-IDENTIFIERS")
        obj.data_identifiers = []
        container = ARObject._find_child_element(element, "DATA-IDENTIFIERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.data_identifiers.append(child_value)

        # Parse validation
        child = ARObject._find_child_element(element, "VALIDATION")
        if child is not None:
            validation_value = ARObject._deserialize_by_tag(child, "DiagnosticStartRoutine")
            obj.validation = validation_value

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
