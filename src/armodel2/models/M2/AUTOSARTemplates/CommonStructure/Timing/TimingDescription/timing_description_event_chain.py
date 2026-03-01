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

    _XML_TAG = "TIMING-DESCRIPTION-EVENT-CHAIN"


    is_pipelining: Optional[Boolean]
    response_ref: Optional[ARRef]
    segment_refs: list[ARRef]
    stimulus_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "IS-PIPELINING": lambda obj, elem: setattr(obj, "is_pipelining", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "RESPONSE-REF": ("_POLYMORPHIC", "response_ref", ["TDEventBsw", "TDEventBswInternalBehavior", "TDEventCom", "TDEventComplex", "TDEventSLLET", "TDEventSwc", "TDEventVfb"]),
        "SEGMENTS": ("_POLYMORPHIC_LIST", "segment_refs", ["TDEventBsw", "TDEventBswInternalBehavior", "TDEventCom", "TDEventComplex", "TDEventSLLET", "TDEventSwc", "TDEventVfb"]),
        "STIMULUS-REF": ("_POLYMORPHIC", "stimulus_ref", ["TDEventBsw", "TDEventBswInternalBehavior", "TDEventCom", "TDEventComplex", "TDEventSLLET", "TDEventSwc", "TDEventVfb"]),
    }


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
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

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

        # Serialize segment_refs (list to container "SEGMENT-REFS")
        if self.segment_refs:
            wrapper = ET.Element("SEGMENT-REFS")
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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "IS-PIPELINING":
                setattr(obj, "is_pipelining", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "RESPONSE-REF":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "T-D-EVENT-BSW":
                        setattr(obj, "response_ref", SerializationHelper.deserialize_by_tag(child[0], "TDEventBsw"))
                    elif concrete_tag == "T-D-EVENT-BSW-INTERNAL-BEHAVIOR":
                        setattr(obj, "response_ref", SerializationHelper.deserialize_by_tag(child[0], "TDEventBswInternalBehavior"))
                    elif concrete_tag == "T-D-EVENT-COM":
                        setattr(obj, "response_ref", SerializationHelper.deserialize_by_tag(child[0], "TDEventCom"))
                    elif concrete_tag == "T-D-EVENT-COMPLEX":
                        setattr(obj, "response_ref", SerializationHelper.deserialize_by_tag(child[0], "TDEventComplex"))
                    elif concrete_tag == "T-D-EVENT-S-L-L-E-T":
                        setattr(obj, "response_ref", SerializationHelper.deserialize_by_tag(child[0], "TDEventSLLET"))
                    elif concrete_tag == "T-D-EVENT-SWC":
                        setattr(obj, "response_ref", SerializationHelper.deserialize_by_tag(child[0], "TDEventSwc"))
                    elif concrete_tag == "T-D-EVENT-VFB":
                        setattr(obj, "response_ref", SerializationHelper.deserialize_by_tag(child[0], "TDEventVfb"))
            elif tag == "SEGMENTS":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "T-D-EVENT-BSW":
                        obj.segment_refs.append(SerializationHelper.deserialize_by_tag(child[0], "TDEventBsw"))
                    elif concrete_tag == "T-D-EVENT-BSW-INTERNAL-BEHAVIOR":
                        obj.segment_refs.append(SerializationHelper.deserialize_by_tag(child[0], "TDEventBswInternalBehavior"))
                    elif concrete_tag == "T-D-EVENT-COM":
                        obj.segment_refs.append(SerializationHelper.deserialize_by_tag(child[0], "TDEventCom"))
                    elif concrete_tag == "T-D-EVENT-COMPLEX":
                        obj.segment_refs.append(SerializationHelper.deserialize_by_tag(child[0], "TDEventComplex"))
                    elif concrete_tag == "T-D-EVENT-S-L-L-E-T":
                        obj.segment_refs.append(SerializationHelper.deserialize_by_tag(child[0], "TDEventSLLET"))
                    elif concrete_tag == "T-D-EVENT-SWC":
                        obj.segment_refs.append(SerializationHelper.deserialize_by_tag(child[0], "TDEventSwc"))
                    elif concrete_tag == "T-D-EVENT-VFB":
                        obj.segment_refs.append(SerializationHelper.deserialize_by_tag(child[0], "TDEventVfb"))
            elif tag == "STIMULUS-REF":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "T-D-EVENT-BSW":
                        setattr(obj, "stimulus_ref", SerializationHelper.deserialize_by_tag(child[0], "TDEventBsw"))
                    elif concrete_tag == "T-D-EVENT-BSW-INTERNAL-BEHAVIOR":
                        setattr(obj, "stimulus_ref", SerializationHelper.deserialize_by_tag(child[0], "TDEventBswInternalBehavior"))
                    elif concrete_tag == "T-D-EVENT-COM":
                        setattr(obj, "stimulus_ref", SerializationHelper.deserialize_by_tag(child[0], "TDEventCom"))
                    elif concrete_tag == "T-D-EVENT-COMPLEX":
                        setattr(obj, "stimulus_ref", SerializationHelper.deserialize_by_tag(child[0], "TDEventComplex"))
                    elif concrete_tag == "T-D-EVENT-S-L-L-E-T":
                        setattr(obj, "stimulus_ref", SerializationHelper.deserialize_by_tag(child[0], "TDEventSLLET"))
                    elif concrete_tag == "T-D-EVENT-SWC":
                        setattr(obj, "stimulus_ref", SerializationHelper.deserialize_by_tag(child[0], "TDEventSwc"))
                    elif concrete_tag == "T-D-EVENT-VFB":
                        setattr(obj, "stimulus_ref", SerializationHelper.deserialize_by_tag(child[0], "TDEventVfb"))

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