"""SecurityEventFilterChain AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 20)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SecurityExtractTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SecurityExtractTemplate.ids_common_element import (
    IdsCommonElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SecurityExtractTemplate.ids_common_element import IdsCommonElementBuilder
from armodel2.models.M2.AUTOSARTemplates.SecurityExtractTemplate.security_event_one_every_n_filter import (
    SecurityEventOneEveryNFilter,
)
from armodel2.models.M2.AUTOSARTemplates.SecurityExtractTemplate.security_event_state_filter import (
    SecurityEventStateFilter,
)
from armodel2.models.M2.AUTOSARTemplates.SecurityExtractTemplate.security_event_threshold_filter import (
    SecurityEventThresholdFilter,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SecurityEventFilterChain(IdsCommonElement):
    """AUTOSAR SecurityEventFilterChain."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SECURITY-EVENT-FILTER-CHAIN"


    aggregation: Optional[Any]
    one_every_n: Optional[SecurityEventOneEveryNFilter]
    state: Optional[SecurityEventStateFilter]
    threshold: Optional[SecurityEventThresholdFilter]
    _DESERIALIZE_DISPATCH = {
        "AGGREGATION": lambda obj, elem: setattr(obj, "aggregation", SerializationHelper.deserialize_by_tag(elem, "any (SecurityEvent)")),
        "ONE-EVERY-N": lambda obj, elem: setattr(obj, "one_every_n", SerializationHelper.deserialize_by_tag(elem, "SecurityEventOneEveryNFilter")),
        "STATE": lambda obj, elem: setattr(obj, "state", SerializationHelper.deserialize_by_tag(elem, "SecurityEventStateFilter")),
        "THRESHOLD": lambda obj, elem: setattr(obj, "threshold", SerializationHelper.deserialize_by_tag(elem, "SecurityEventThresholdFilter")),
    }


    def __init__(self) -> None:
        """Initialize SecurityEventFilterChain."""
        super().__init__()
        self.aggregation: Optional[Any] = None
        self.one_every_n: Optional[SecurityEventOneEveryNFilter] = None
        self.state: Optional[SecurityEventStateFilter] = None
        self.threshold: Optional[SecurityEventThresholdFilter] = None

    def serialize(self) -> ET.Element:
        """Serialize SecurityEventFilterChain to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SecurityEventFilterChain, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize aggregation
        if self.aggregation is not None:
            serialized = SerializationHelper.serialize_item(self.aggregation, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("AGGREGATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize one_every_n
        if self.one_every_n is not None:
            serialized = SerializationHelper.serialize_item(self.one_every_n, "SecurityEventOneEveryNFilter")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ONE-EVERY-N")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize state
        if self.state is not None:
            serialized = SerializationHelper.serialize_item(self.state, "SecurityEventStateFilter")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("STATE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize threshold
        if self.threshold is not None:
            serialized = SerializationHelper.serialize_item(self.threshold, "SecurityEventThresholdFilter")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("THRESHOLD")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SecurityEventFilterChain":
        """Deserialize XML element to SecurityEventFilterChain object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SecurityEventFilterChain object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SecurityEventFilterChain, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "AGGREGATION":
                setattr(obj, "aggregation", SerializationHelper.deserialize_by_tag(child, "any (SecurityEvent)"))
            elif tag == "ONE-EVERY-N":
                setattr(obj, "one_every_n", SerializationHelper.deserialize_by_tag(child, "SecurityEventOneEveryNFilter"))
            elif tag == "STATE":
                setattr(obj, "state", SerializationHelper.deserialize_by_tag(child, "SecurityEventStateFilter"))
            elif tag == "THRESHOLD":
                setattr(obj, "threshold", SerializationHelper.deserialize_by_tag(child, "SecurityEventThresholdFilter"))

        return obj



class SecurityEventFilterChainBuilder(IdsCommonElementBuilder):
    """Builder for SecurityEventFilterChain with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SecurityEventFilterChain = SecurityEventFilterChain()


    def with_aggregation(self, value: Optional[any (SecurityEvent)]) -> "SecurityEventFilterChainBuilder":
        """Set aggregation attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.aggregation = value
        return self

    def with_one_every_n(self, value: Optional[SecurityEventOneEveryNFilter]) -> "SecurityEventFilterChainBuilder":
        """Set one_every_n attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.one_every_n = value
        return self

    def with_state(self, value: Optional[SecurityEventStateFilter]) -> "SecurityEventFilterChainBuilder":
        """Set state attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.state = value
        return self

    def with_threshold(self, value: Optional[SecurityEventThresholdFilter]) -> "SecurityEventFilterChainBuilder":
        """Set threshold attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.threshold = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "aggregation",
        "oneEveryN",
        "state",
        "threshold",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> SecurityEventFilterChain:
        """Build and return the SecurityEventFilterChain instance with validation."""
        self._validate_instance()
        return self._obj