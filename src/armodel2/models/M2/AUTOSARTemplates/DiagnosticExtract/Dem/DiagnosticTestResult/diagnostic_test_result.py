"""DiagnosticTestResult AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 204)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 804)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticTestResult.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import DiagnosticCommonElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_event import (
    DiagnosticEvent,
)
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTestResult.diagnostic_test_identifier import (
    DiagnosticTestIdentifier,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticTestResult(DiagnosticCommonElement):
    """AUTOSAR DiagnosticTestResult."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-TEST-RESULT"


    diagnostic_event_ref: Optional[ARRef]
    monitored_ref: Optional[Any]
    test_identifier: Optional[DiagnosticTestIdentifier]
    update_kind: Optional[DiagnosticTestResult]
    _DESERIALIZE_DISPATCH = {
        "DIAGNOSTIC-EVENT-REF": lambda obj, elem: setattr(obj, "diagnostic_event_ref", ARRef.deserialize(elem)),
        "MONITORED-REF": lambda obj, elem: setattr(obj, "monitored_ref", ARRef.deserialize(elem)),
        "TEST-IDENTIFIER": lambda obj, elem: setattr(obj, "test_identifier", SerializationHelper.deserialize_by_tag(elem, "DiagnosticTestIdentifier")),
        "UPDATE-KIND": lambda obj, elem: setattr(obj, "update_kind", SerializationHelper.deserialize_by_tag(elem, "DiagnosticTestResult")),
    }


    def __init__(self) -> None:
        """Initialize DiagnosticTestResult."""
        super().__init__()
        self.diagnostic_event_ref: Optional[ARRef] = None
        self.monitored_ref: Optional[Any] = None
        self.test_identifier: Optional[DiagnosticTestIdentifier] = None
        self.update_kind: Optional[DiagnosticTestResult] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticTestResult to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticTestResult, self).serialize()

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

        # Serialize monitored_ref
        if self.monitored_ref is not None:
            serialized = SerializationHelper.serialize_item(self.monitored_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MONITORED-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize test_identifier
        if self.test_identifier is not None:
            serialized = SerializationHelper.serialize_item(self.test_identifier, "DiagnosticTestIdentifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TEST-IDENTIFIER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize update_kind
        if self.update_kind is not None:
            serialized = SerializationHelper.serialize_item(self.update_kind, "DiagnosticTestResult")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("UPDATE-KIND")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticTestResult":
        """Deserialize XML element to DiagnosticTestResult object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticTestResult object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticTestResult, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DIAGNOSTIC-EVENT-REF":
                setattr(obj, "diagnostic_event_ref", ARRef.deserialize(child))
            elif tag == "MONITORED-REF":
                setattr(obj, "monitored_ref", ARRef.deserialize(child))
            elif tag == "TEST-IDENTIFIER":
                setattr(obj, "test_identifier", SerializationHelper.deserialize_by_tag(child, "DiagnosticTestIdentifier"))
            elif tag == "UPDATE-KIND":
                setattr(obj, "update_kind", SerializationHelper.deserialize_by_tag(child, "DiagnosticTestResult"))

        return obj



class DiagnosticTestResultBuilder(DiagnosticCommonElementBuilder):
    """Builder for DiagnosticTestResult with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticTestResult = DiagnosticTestResult()


    def with_diagnostic_event(self, value: Optional[DiagnosticEvent]) -> "DiagnosticTestResultBuilder":
        """Set diagnostic_event attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.diagnostic_event = value
        return self

    def with_monitored(self, value: Optional[any (Diagnostic)]) -> "DiagnosticTestResultBuilder":
        """Set monitored attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.monitored = value
        return self

    def with_test_identifier(self, value: Optional[DiagnosticTestIdentifier]) -> "DiagnosticTestResultBuilder":
        """Set test_identifier attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.test_identifier = value
        return self

    def with_update_kind(self, value: Optional[DiagnosticTestResult]) -> "DiagnosticTestResultBuilder":
        """Set update_kind attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.update_kind = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "diagnosticEvent",
        "monitored",
        "testIdentifier",
        "updateKind",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DiagnosticTestResult:
        """Build and return the DiagnosticTestResult instance with validation."""
        self._validate_instance()
        return self._obj