"""TimingDescriptionEventChain AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 40)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description import (
    TimingDescription,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description import TimingDescriptionBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description_event import (
    TimingDescriptionEvent,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class TimingDescriptionEventChain(TimingDescription):
    """AUTOSAR TimingDescriptionEventChain."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    is_pipelining: Optional[Boolean]
    response_ref: Optional[ARRef]
    segment_refs: list[ARRef]
    stimulus_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize TimingDescriptionEventChain."""
        super().__init__()
        self.is_pipelining: Optional[Boolean] = None
        self.response_ref: Optional[ARRef] = None
        self.segment_refs: list[ARRef] = []
        self.stimulus_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize TimingDescriptionEventChain to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TimingDescriptionEventChain, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize is_pipelining
        if self.is_pipelining is not None:
            serialized = SerializationHelper.serialize_item(self.is_pipelining, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IS-PIPELINING")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize response_ref
        if self.response_ref is not None:
            serialized = SerializationHelper.serialize_item(self.response_ref, "TimingDescriptionEvent")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RESPONSE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize segment_refs (list to container "SEGMENTS")
        if self.segment_refs:
            wrapper = ET.Element("SEGMENTS")
            for item in self.segment_refs:
                serialized = SerializationHelper.serialize_item(item, "TimingDescriptionEvent")
                if serialized is not None:
                    child_elem = ET.Element("SEGMENT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize stimulus_ref
        if self.stimulus_ref is not None:
            serialized = SerializationHelper.serialize_item(self.stimulus_ref, "TimingDescriptionEvent")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("STIMULUS-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TimingDescriptionEventChain":
        """Deserialize XML element to TimingDescriptionEventChain object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TimingDescriptionEventChain object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TimingDescriptionEventChain, cls).deserialize(element)

        # Parse is_pipelining
        child = SerializationHelper.find_child_element(element, "IS-PIPELINING")
        if child is not None:
            is_pipelining_value = child.text
            obj.is_pipelining = is_pipelining_value

        # Parse response_ref
        child = SerializationHelper.find_child_element(element, "RESPONSE-REF")
        if child is not None:
            response_ref_value = ARRef.deserialize(child)
            obj.response_ref = response_ref_value

        # Parse segment_refs (list from container "SEGMENTS")
        obj.segment_refs = []
        container = SerializationHelper.find_child_element(element, "SEGMENTS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.segment_refs.append(child_value)

        # Parse stimulus_ref
        child = SerializationHelper.find_child_element(element, "STIMULUS-REF")
        if child is not None:
            stimulus_ref_value = ARRef.deserialize(child)
            obj.stimulus_ref = stimulus_ref_value

        return obj



class TimingDescriptionEventChainBuilder(TimingDescriptionBuilder):
    """Builder for TimingDescriptionEventChain with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TimingDescriptionEventChain = TimingDescriptionEventChain()


    def with_is_pipelining(self, value: Optional[Boolean]) -> "TimingDescriptionEventChainBuilder":
        """Set is_pipelining attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.is_pipelining = value
        return self

    def with_response(self, value: Optional[TimingDescriptionEvent]) -> "TimingDescriptionEventChainBuilder":
        """Set response attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.response = value
        return self

    def with_segments(self, items: list[TimingDescriptionEvent]) -> "TimingDescriptionEventChainBuilder":
        """Set segments list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.segments = list(items) if items else []
        return self

    def with_stimulus(self, value: Optional[TimingDescriptionEvent]) -> "TimingDescriptionEventChainBuilder":
        """Set stimulus attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.stimulus = value
        return self


    def add_segment(self, item: TimingDescriptionEvent) -> "TimingDescriptionEventChainBuilder":
        """Add a single item to segments list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.segments.append(item)
        return self

    def clear_segments(self) -> "TimingDescriptionEventChainBuilder":
        """Clear all items from segments list.

        Returns:
            self for method chaining
        """
        self._obj.segments = []
        return self



    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Get type hints for the class
        try:
            type_hints_dict = get_type_hints(type(self._obj))
        except Exception:
            # Cannot resolve type hints (e.g., forward references), skip validation
            return

        for attr_name, attr_type in type_hints_dict.items():
            if attr_name.startswith("_"):
                continue

            value = getattr(self._obj, attr_name)

            # Check required fields (not Optional)
            if value is None and not self._is_optional_type(attr_type):
                if mode == BuilderValidationMode.STRICT:
                    raise ValueError(
                        f"Required attribute '{attr_name}' is None"
                    )
                elif mode == BuilderValidationMode.LENIENT:
                    import warnings
                    warnings.warn(
                        f"Required attribute '{attr_name}' is None",
                        UserWarning
                    )

    @staticmethod
    def _is_optional_type(type_hint: Any) -> bool:
        """Check if a type hint is Optional.

        Args:
            type_hint: Type hint to check

        Returns:
            True if type is Optional, False otherwise
        """
        origin = getattr(type_hint, "__origin__", None)
        return origin is Union

    @staticmethod
    def _get_expected_type(type_hint: Any) -> type:
        """Extract expected type from type hint.

        Args:
            type_hint: Type hint to extract from

        Returns:
            Expected type
        """
        if isinstance(type_hint, str):
            return object
        origin = getattr(type_hint, "__origin__", None)
        if origin is Union:
            args = getattr(type_hint, "__args__", [])
            for arg in args:
                if arg is not type(None):
                    return arg
        elif origin is list:
            args = getattr(type_hint, "__args__", [object])
            return args[0] if args else object
        return type_hint if isinstance(type_hint, type) else object


    def build(self) -> TimingDescriptionEventChain:
        """Build and return the TimingDescriptionEventChain instance with validation."""
        self._validate_instance()
        pass
        return self._obj