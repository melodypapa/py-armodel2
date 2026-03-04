"""Traceable AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 312)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 221)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_RequirementsTracing.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.multilanguage_referrable import (
    MultilanguageReferrable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.multilanguage_referrable import MultilanguageReferrableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class Traceable(MultilanguageReferrable, ABC):
    """AUTOSAR Traceable."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    trace_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "TRACE-REFS": ("_POLYMORPHIC_LIST", "trace_refs", ["AgeConstraint", "ArbitraryEventTriggering", "BurstPatternEventTriggering", "ConcretePatternEventTriggering", "ExecutionOrderConstraint", "ExecutionTimeConstraint", "LatencyTimingConstraint", "OffsetTimingConstraint", "PeriodicEventTriggering", "SporadicEventTriggering", "StructuredReq", "SynchronizationPointConstraint", "TimingConstraint", "TraceableTable", "TraceableText"]),
    }


    def __init__(self) -> None:
        """Initialize Traceable."""
        super().__init__()
        self.trace_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize Traceable to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Traceable, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize trace_refs (list to container "TRACE-REFS")
        if self.trace_refs:
            wrapper = ET.Element("TRACE-REFS")
            for item in self.trace_refs:
                serialized = SerializationHelper.serialize_item(item, "Traceable")
                if serialized is not None:
                    child_elem = ET.Element("TRACE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Traceable":
        """Deserialize XML element to Traceable object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Traceable object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Traceable, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "TRACE-REFS":
                for item_elem in child:
                    obj.trace_refs.append(ARRef.deserialize(item_elem))

        return obj



class TraceableBuilder(MultilanguageReferrableBuilder):
    """Builder for Traceable with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: Traceable = Traceable()


    def with_traces(self, items: list[Traceable]) -> "TraceableBuilder":
        """Set traces list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.traces = list(items) if items else []
        return self


    def add_trace(self, item: Traceable) -> "TraceableBuilder":
        """Add a single item to traces list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.traces.append(item)
        return self

    def clear_traces(self) -> "TraceableBuilder":
        """Clear all items from traces list.

        Returns:
            self for method chaining
        """
        self._obj.traces = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "trace",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    @abstractmethod
    def build(self) -> Traceable:
        """Build and return the Traceable instance (abstract)."""
        raise NotImplementedError