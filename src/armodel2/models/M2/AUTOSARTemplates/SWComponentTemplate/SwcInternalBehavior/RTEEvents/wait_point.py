"""WaitPoint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 550)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_RTEEvents.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.rte_event import (
        RTEEvent,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class WaitPoint(Identifiable):
    """AUTOSAR WaitPoint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "WAIT-POINT"


    timeout: Optional[TimeValue]
    trigger_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "TIMEOUT": lambda obj, elem: setattr(obj, "timeout", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "TRIGGER-REF": ("_POLYMORPHIC", "trigger_ref", ["AsynchronousServerCallReturnsEvent", "BackgroundEvent", "DataReceiveErrorEvent", "DataReceivedEvent", "DataSendCompletedEvent", "DataWriteCompletedEvent", "ExternalTriggerOccurredEvent", "InitEvent", "InternalTriggerOccurredEvent", "ModeSwitchedAckEvent", "OperationInvokedEvent", "OsTaskExecutionEvent", "SwcModeManagerErrorEvent", "SwcModeSwitchEvent", "TimingEvent", "TransformerHardErrorEvent"]),
    }


    def __init__(self) -> None:
        """Initialize WaitPoint."""
        super().__init__()
        self.timeout: Optional[TimeValue] = None
        self.trigger_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize WaitPoint to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(WaitPoint, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize timeout
        if self.timeout is not None:
            serialized = SerializationHelper.serialize_item(self.timeout, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIMEOUT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize trigger_ref
        if self.trigger_ref is not None:
            serialized = SerializationHelper.serialize_item(self.trigger_ref, "RTEEvent")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TRIGGER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "WaitPoint":
        """Deserialize XML element to WaitPoint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized WaitPoint object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(WaitPoint, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "TIMEOUT":
                setattr(obj, "timeout", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "TRIGGER-REF":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "ASYNCHRONOUS-SERVER-CALL-RETURNS-EVENT":
                        setattr(obj, "trigger_ref", SerializationHelper.deserialize_by_tag(child[0], "AsynchronousServerCallReturnsEvent"))
                    elif concrete_tag == "BACKGROUND-EVENT":
                        setattr(obj, "trigger_ref", SerializationHelper.deserialize_by_tag(child[0], "BackgroundEvent"))
                    elif concrete_tag == "DATA-RECEIVE-ERROR-EVENT":
                        setattr(obj, "trigger_ref", SerializationHelper.deserialize_by_tag(child[0], "DataReceiveErrorEvent"))
                    elif concrete_tag == "DATA-RECEIVED-EVENT":
                        setattr(obj, "trigger_ref", SerializationHelper.deserialize_by_tag(child[0], "DataReceivedEvent"))
                    elif concrete_tag == "DATA-SEND-COMPLETED-EVENT":
                        setattr(obj, "trigger_ref", SerializationHelper.deserialize_by_tag(child[0], "DataSendCompletedEvent"))
                    elif concrete_tag == "DATA-WRITE-COMPLETED-EVENT":
                        setattr(obj, "trigger_ref", SerializationHelper.deserialize_by_tag(child[0], "DataWriteCompletedEvent"))
                    elif concrete_tag == "EXTERNAL-TRIGGER-OCCURRED-EVENT":
                        setattr(obj, "trigger_ref", SerializationHelper.deserialize_by_tag(child[0], "ExternalTriggerOccurredEvent"))
                    elif concrete_tag == "INIT-EVENT":
                        setattr(obj, "trigger_ref", SerializationHelper.deserialize_by_tag(child[0], "InitEvent"))
                    elif concrete_tag == "INTERNAL-TRIGGER-OCCURRED-EVENT":
                        setattr(obj, "trigger_ref", SerializationHelper.deserialize_by_tag(child[0], "InternalTriggerOccurredEvent"))
                    elif concrete_tag == "MODE-SWITCHED-ACK-EVENT":
                        setattr(obj, "trigger_ref", SerializationHelper.deserialize_by_tag(child[0], "ModeSwitchedAckEvent"))
                    elif concrete_tag == "OPERATION-INVOKED-EVENT":
                        setattr(obj, "trigger_ref", SerializationHelper.deserialize_by_tag(child[0], "OperationInvokedEvent"))
                    elif concrete_tag == "OS-TASK-EXECUTION-EVENT":
                        setattr(obj, "trigger_ref", SerializationHelper.deserialize_by_tag(child[0], "OsTaskExecutionEvent"))
                    elif concrete_tag == "SWC-MODE-MANAGER-ERROR-EVENT":
                        setattr(obj, "trigger_ref", SerializationHelper.deserialize_by_tag(child[0], "SwcModeManagerErrorEvent"))
                    elif concrete_tag == "SWC-MODE-SWITCH-EVENT":
                        setattr(obj, "trigger_ref", SerializationHelper.deserialize_by_tag(child[0], "SwcModeSwitchEvent"))
                    elif concrete_tag == "TIMING-EVENT":
                        setattr(obj, "trigger_ref", SerializationHelper.deserialize_by_tag(child[0], "TimingEvent"))
                    elif concrete_tag == "TRANSFORMER-HARD-ERROR-EVENT":
                        setattr(obj, "trigger_ref", SerializationHelper.deserialize_by_tag(child[0], "TransformerHardErrorEvent"))

        return obj



class WaitPointBuilder(IdentifiableBuilder):
    """Builder for WaitPoint with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: WaitPoint = WaitPoint()


    def with_timeout(self, value: Optional[TimeValue]) -> "WaitPointBuilder":
        """Set timeout attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.timeout = value
        return self

    def with_trigger(self, value: Optional[RTEEvent]) -> "WaitPointBuilder":
        """Set trigger attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.trigger = value
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


    def build(self) -> WaitPoint:
        """Build and return the WaitPoint instance with validation."""
        self._validate_instance()
        pass
        return self._obj