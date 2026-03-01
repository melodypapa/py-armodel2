"""DiagnosticResponseOnEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 132)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_ResponseOnEvent.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import DiagnosticServiceInstanceBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.ResponseOnEvent.diagnostic_event_window import (
    DiagnosticEventWindow,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticResponseOnEvent(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticResponseOnEvent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-RESPONSE-ON-EVENT"


    event_windows: list[DiagnosticEventWindow]
    response_on_ref: Optional[Any]
    _DESERIALIZE_DISPATCH = {
        "EVENT-WINDOWS": lambda obj, elem: obj.event_windows.append(SerializationHelper.deserialize_by_tag(elem, "DiagnosticEventWindow")),
        "RESPONSE-ON-REF": lambda obj, elem: setattr(obj, "response_on_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize DiagnosticResponseOnEvent."""
        super().__init__()
        self.event_windows: list[DiagnosticEventWindow] = []
        self.response_on_ref: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticResponseOnEvent to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticResponseOnEvent, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize event_windows (list to container "EVENT-WINDOWS")
        if self.event_windows:
            wrapper = ET.Element("EVENT-WINDOWS")
            for item in self.event_windows:
                serialized = SerializationHelper.serialize_item(item, "DiagnosticEventWindow")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize response_on_ref
        if self.response_on_ref is not None:
            serialized = SerializationHelper.serialize_item(self.response_on_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RESPONSE-ON-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticResponseOnEvent":
        """Deserialize XML element to DiagnosticResponseOnEvent object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticResponseOnEvent object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticResponseOnEvent, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "EVENT-WINDOWS":
                obj.event_windows.append(SerializationHelper.deserialize_by_tag(child, "DiagnosticEventWindow"))
            elif tag == "RESPONSE-ON-REF":
                setattr(obj, "response_on_ref", ARRef.deserialize(child))

        return obj



class DiagnosticResponseOnEventBuilder(DiagnosticServiceInstanceBuilder):
    """Builder for DiagnosticResponseOnEvent with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticResponseOnEvent = DiagnosticResponseOnEvent()


    def with_event_windows(self, items: list[DiagnosticEventWindow]) -> "DiagnosticResponseOnEventBuilder":
        """Set event_windows list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.event_windows = list(items) if items else []
        return self

    def with_response_on(self, value: Optional[any (DiagnosticResponseOn)]) -> "DiagnosticResponseOnEventBuilder":
        """Set response_on attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.response_on = value
        return self


    def add_event_window(self, item: DiagnosticEventWindow) -> "DiagnosticResponseOnEventBuilder":
        """Add a single item to event_windows list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.event_windows.append(item)
        return self

    def clear_event_windows(self) -> "DiagnosticResponseOnEventBuilder":
        """Clear all items from event_windows list.

        Returns:
            self for method chaining
        """
        self._obj.event_windows = []
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


    def build(self) -> DiagnosticResponseOnEvent:
        """Build and return the DiagnosticResponseOnEvent instance with validation."""
        self._validate_instance()
        pass
        return self._obj