"""AsynchronousServerCallReturnsEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 541)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_RTEEvents.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.rte_event import (
    RTEEvent,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.rte_event import RTEEventBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServerCall.asynchronous_server_call_result_point import (
    AsynchronousServerCallResultPoint,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class AsynchronousServerCallReturnsEvent(RTEEvent):
    """AUTOSAR AsynchronousServerCallReturnsEvent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "ASYNCHRONOUS-SERVER-CALL-RETURNS-EVENT"


    event_source_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "EVENT-SOURCE-REF": lambda obj, elem: setattr(obj, "event_source_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize AsynchronousServerCallReturnsEvent."""
        super().__init__()
        self.event_source_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize AsynchronousServerCallReturnsEvent to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AsynchronousServerCallReturnsEvent, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize event_source_ref
        if self.event_source_ref is not None:
            serialized = SerializationHelper.serialize_item(self.event_source_ref, "AsynchronousServerCallResultPoint")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EVENT-SOURCE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AsynchronousServerCallReturnsEvent":
        """Deserialize XML element to AsynchronousServerCallReturnsEvent object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AsynchronousServerCallReturnsEvent object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AsynchronousServerCallReturnsEvent, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "EVENT-SOURCE-REF":
                setattr(obj, "event_source_ref", ARRef.deserialize(child))

        return obj



class AsynchronousServerCallReturnsEventBuilder(RTEEventBuilder):
    """Builder for AsynchronousServerCallReturnsEvent with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: AsynchronousServerCallReturnsEvent = AsynchronousServerCallReturnsEvent()


    def with_event_source(self, value: Optional[AsynchronousServerCallResultPoint]) -> "AsynchronousServerCallReturnsEventBuilder":
        """Set event_source attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'event_source' is required and cannot be None")
        self._obj.event_source = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "eventSource",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> AsynchronousServerCallReturnsEvent:
        """Build and return the AsynchronousServerCallReturnsEvent instance with validation."""
        self._validate_instance()
        return self._obj