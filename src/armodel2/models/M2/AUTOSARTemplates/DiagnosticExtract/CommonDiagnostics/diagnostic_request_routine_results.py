"""DiagnosticRequestRoutineResults AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 125)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_CommonDiagnostics.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_routine_subfunction import (
    DiagnosticRoutineSubfunction,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_routine_subfunction import DiagnosticRoutineSubfunctionBuilder
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_parameter import (
    DiagnosticParameter,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticRequestRoutineResults(DiagnosticRoutineSubfunction):
    """AUTOSAR DiagnosticRequestRoutineResults."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-REQUEST-ROUTINE-RESULTS"


    requests: list[DiagnosticParameter]
    responses: list[DiagnosticParameter]
    _DESERIALIZE_DISPATCH = {
        "REQUESTS": lambda obj, elem: obj.requests.append(SerializationHelper.deserialize_by_tag(elem, "DiagnosticParameter")),
        "RESPONSS": lambda obj, elem: obj.responses.append(SerializationHelper.deserialize_by_tag(elem, "DiagnosticParameter")),
    }


    def __init__(self) -> None:
        """Initialize DiagnosticRequestRoutineResults."""
        super().__init__()
        self.requests: list[DiagnosticParameter] = []
        self.responses: list[DiagnosticParameter] = []

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticRequestRoutineResults to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticRequestRoutineResults, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize requests (list to container "REQUESTS")
        if self.requests:
            wrapper = ET.Element("REQUESTS")
            for item in self.requests:
                serialized = SerializationHelper.serialize_item(item, "DiagnosticParameter")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize responses (list to container "RESPONSS")
        if self.responses:
            wrapper = ET.Element("RESPONSS")
            for item in self.responses:
                serialized = SerializationHelper.serialize_item(item, "DiagnosticParameter")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticRequestRoutineResults":
        """Deserialize XML element to DiagnosticRequestRoutineResults object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticRequestRoutineResults object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticRequestRoutineResults, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "REQUESTS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.requests.append(SerializationHelper.deserialize_by_tag(item_elem, "DiagnosticParameter"))
            elif tag == "RESPONSS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.responses.append(SerializationHelper.deserialize_by_tag(item_elem, "DiagnosticParameter"))

        return obj



class DiagnosticRequestRoutineResultsBuilder(DiagnosticRoutineSubfunctionBuilder):
    """Builder for DiagnosticRequestRoutineResults with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticRequestRoutineResults = DiagnosticRequestRoutineResults()


    def with_requests(self, items: list[DiagnosticParameter]) -> "DiagnosticRequestRoutineResultsBuilder":
        """Set requests list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.requests = list(items) if items else []
        return self

    def with_responses(self, items: list[DiagnosticParameter]) -> "DiagnosticRequestRoutineResultsBuilder":
        """Set responses list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.responses = list(items) if items else []
        return self


    def add_request(self, item: DiagnosticParameter) -> "DiagnosticRequestRoutineResultsBuilder":
        """Add a single item to requests list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.requests.append(item)
        return self

    def clear_requests(self) -> "DiagnosticRequestRoutineResultsBuilder":
        """Clear all items from requests list.

        Returns:
            self for method chaining
        """
        self._obj.requests = []
        return self

    def add_respons(self, item: DiagnosticParameter) -> "DiagnosticRequestRoutineResultsBuilder":
        """Add a single item to responses list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.responses.append(item)
        return self

    def clear_responses(self) -> "DiagnosticRequestRoutineResultsBuilder":
        """Clear all items from responses list.

        Returns:
            self for method chaining
        """
        self._obj.responses = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "request",
        "respons",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DiagnosticRequestRoutineResults:
        """Build and return the DiagnosticRequestRoutineResults instance with validation."""
        self._validate_instance()
        return self._obj