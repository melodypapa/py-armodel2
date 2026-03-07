"""DiagEventDebounceTimeBased AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 260)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 198)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 758)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diag_event_debounce_algorithm import (
    DiagEventDebounceAlgorithm,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diag_event_debounce_algorithm import DiagEventDebounceAlgorithmBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagEventDebounceTimeBased(DiagEventDebounceAlgorithm):
    """AUTOSAR DiagEventDebounceTimeBased."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAG-EVENT-DEBOUNCE-TIME-BASED"


    time_based_fdc: Optional[TimeValue]
    time_failed: Optional[TimeValue]
    time_passed: Optional[TimeValue]
    _DESERIALIZE_DISPATCH = {
        "TIME-BASED-FDC": lambda obj, elem: setattr(obj, "time_based_fdc", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "TIME-FAILED": lambda obj, elem: setattr(obj, "time_failed", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "TIME-PASSED": lambda obj, elem: setattr(obj, "time_passed", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
    }


    def __init__(self) -> None:
        """Initialize DiagEventDebounceTimeBased."""
        super().__init__()
        self.time_based_fdc: Optional[TimeValue] = None
        self.time_failed: Optional[TimeValue] = None
        self.time_passed: Optional[TimeValue] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagEventDebounceTimeBased to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagEventDebounceTimeBased, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize time_based_fdc
        if self.time_based_fdc is not None:
            serialized = SerializationHelper.serialize_item(self.time_based_fdc, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIME-BASED-FDC")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize time_failed
        if self.time_failed is not None:
            serialized = SerializationHelper.serialize_item(self.time_failed, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIME-FAILED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize time_passed
        if self.time_passed is not None:
            serialized = SerializationHelper.serialize_item(self.time_passed, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIME-PASSED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagEventDebounceTimeBased":
        """Deserialize XML element to DiagEventDebounceTimeBased object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagEventDebounceTimeBased object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagEventDebounceTimeBased, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "TIME-BASED-FDC":
                setattr(obj, "time_based_fdc", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "TIME-FAILED":
                setattr(obj, "time_failed", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "TIME-PASSED":
                setattr(obj, "time_passed", SerializationHelper.deserialize_by_tag(child, "TimeValue"))

        return obj



class DiagEventDebounceTimeBasedBuilder(DiagEventDebounceAlgorithmBuilder):
    """Builder for DiagEventDebounceTimeBased with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagEventDebounceTimeBased = DiagEventDebounceTimeBased()


    def with_time_based_fdc(self, value: Optional[TimeValue]) -> "DiagEventDebounceTimeBasedBuilder":
        """Set time_based_fdc attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'time_based_fdc' is required and cannot be None")
        self._obj.time_based_fdc = value
        return self

    def with_time_failed(self, value: Optional[TimeValue]) -> "DiagEventDebounceTimeBasedBuilder":
        """Set time_failed attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'time_failed' is required and cannot be None")
        self._obj.time_failed = value
        return self

    def with_time_passed(self, value: Optional[TimeValue]) -> "DiagEventDebounceTimeBasedBuilder":
        """Set time_passed attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'time_passed' is required and cannot be None")
        self._obj.time_passed = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "timeBasedFdc",
        "timeFailed",
        "timePassed",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DiagEventDebounceTimeBased:
        """Build and return the DiagEventDebounceTimeBased instance with validation."""
        self._validate_instance()
        return self._obj