"""DltLogChannel AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 722)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Dlt.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Dlt import (
    DltDefaultTraceStateEnum,
    LogTraceDefaultLogLevelEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    String,
)
from armodel2.models.M2.AUTOSARTemplates.LogAndTraceExtract.dlt_context import (
    DltContext,
)
from armodel2.models.M2.AUTOSARTemplates.LogAndTraceExtract.dlt_message import (
    DltMessage,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DltLogChannel(Identifiable):
    """AUTOSAR DltLogChannel."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DLT-LOG-CHANNEL"


    application_refs: list[ARRef]
    default_trace: Optional[DltDefaultTraceStateEnum]
    dlt_message_refs: list[ARRef]
    log_channel_id: Optional[String]
    log_trace_default_log: Optional[LogTraceDefaultLogLevelEnum]
    non_verbose: Optional[Boolean]
    rx_pdu_triggering_channel_ref: Optional[ARRef]
    segmentation: Optional[Boolean]
    tx_pdu_triggering_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "APPLICATION-REFS": lambda obj, elem: obj.application_refs.append(ARRef.deserialize(elem)),
        "DEFAULT-TRACE": lambda obj, elem: setattr(obj, "default_trace", DltDefaultTraceStateEnum.deserialize(elem)),
        "DLT-MESSAGE-REFS": lambda obj, elem: obj.dlt_message_refs.append(ARRef.deserialize(elem)),
        "LOG-CHANNEL-ID": lambda obj, elem: setattr(obj, "log_channel_id", SerializationHelper.deserialize_by_tag(elem, "String")),
        "LOG-TRACE-DEFAULT-LOG": lambda obj, elem: setattr(obj, "log_trace_default_log", LogTraceDefaultLogLevelEnum.deserialize(elem)),
        "NON-VERBOSE": lambda obj, elem: setattr(obj, "non_verbose", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "RX-PDU-TRIGGERING-CHANNEL-REF": lambda obj, elem: setattr(obj, "rx_pdu_triggering_channel_ref", ARRef.deserialize(elem)),
        "SEGMENTATION": lambda obj, elem: setattr(obj, "segmentation", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "TX-PDU-TRIGGERING-REF": lambda obj, elem: setattr(obj, "tx_pdu_triggering_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize DltLogChannel."""
        super().__init__()
        self.application_refs: list[ARRef] = []
        self.default_trace: Optional[DltDefaultTraceStateEnum] = None
        self.dlt_message_refs: list[ARRef] = []
        self.log_channel_id: Optional[String] = None
        self.log_trace_default_log: Optional[LogTraceDefaultLogLevelEnum] = None
        self.non_verbose: Optional[Boolean] = None
        self.rx_pdu_triggering_channel_ref: Optional[ARRef] = None
        self.segmentation: Optional[Boolean] = None
        self.tx_pdu_triggering_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize DltLogChannel to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DltLogChannel, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize application_refs (list to container "APPLICATION-REFS")
        if self.application_refs:
            wrapper = ET.Element("APPLICATION-REFS")
            for item in self.application_refs:
                serialized = SerializationHelper.serialize_item(item, "DltContext")
                if serialized is not None:
                    child_elem = ET.Element("APPLICATION-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize default_trace
        if self.default_trace is not None:
            serialized = SerializationHelper.serialize_item(self.default_trace, "DltDefaultTraceStateEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DEFAULT-TRACE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize dlt_message_refs (list to container "DLT-MESSAGE-REFS")
        if self.dlt_message_refs:
            wrapper = ET.Element("DLT-MESSAGE-REFS")
            for item in self.dlt_message_refs:
                serialized = SerializationHelper.serialize_item(item, "DltMessage")
                if serialized is not None:
                    child_elem = ET.Element("DLT-MESSAGE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize log_channel_id
        if self.log_channel_id is not None:
            serialized = SerializationHelper.serialize_item(self.log_channel_id, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LOG-CHANNEL-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize log_trace_default_log
        if self.log_trace_default_log is not None:
            serialized = SerializationHelper.serialize_item(self.log_trace_default_log, "LogTraceDefaultLogLevelEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LOG-TRACE-DEFAULT-LOG")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize non_verbose
        if self.non_verbose is not None:
            serialized = SerializationHelper.serialize_item(self.non_verbose, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NON-VERBOSE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rx_pdu_triggering_channel_ref
        if self.rx_pdu_triggering_channel_ref is not None:
            serialized = SerializationHelper.serialize_item(self.rx_pdu_triggering_channel_ref, "PduTriggering")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RX-PDU-TRIGGERING-CHANNEL-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize segmentation
        if self.segmentation is not None:
            serialized = SerializationHelper.serialize_item(self.segmentation, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SEGMENTATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tx_pdu_triggering_ref
        if self.tx_pdu_triggering_ref is not None:
            serialized = SerializationHelper.serialize_item(self.tx_pdu_triggering_ref, "PduTriggering")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TX-PDU-TRIGGERING-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DltLogChannel":
        """Deserialize XML element to DltLogChannel object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DltLogChannel object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DltLogChannel, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "APPLICATION-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.application_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "DltContext"))
            elif tag == "DEFAULT-TRACE":
                setattr(obj, "default_trace", DltDefaultTraceStateEnum.deserialize(child))
            elif tag == "DLT-MESSAGE-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.dlt_message_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "DltMessage"))
            elif tag == "LOG-CHANNEL-ID":
                setattr(obj, "log_channel_id", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "LOG-TRACE-DEFAULT-LOG":
                setattr(obj, "log_trace_default_log", LogTraceDefaultLogLevelEnum.deserialize(child))
            elif tag == "NON-VERBOSE":
                setattr(obj, "non_verbose", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "RX-PDU-TRIGGERING-CHANNEL-REF":
                setattr(obj, "rx_pdu_triggering_channel_ref", ARRef.deserialize(child))
            elif tag == "SEGMENTATION":
                setattr(obj, "segmentation", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "TX-PDU-TRIGGERING-REF":
                setattr(obj, "tx_pdu_triggering_ref", ARRef.deserialize(child))

        return obj



class DltLogChannelBuilder(IdentifiableBuilder):
    """Builder for DltLogChannel with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DltLogChannel = DltLogChannel()


    def with_applications(self, items: list[DltContext]) -> "DltLogChannelBuilder":
        """Set applications list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.applications = list(items) if items else []
        return self

    def with_default_trace(self, value: Optional[DltDefaultTraceStateEnum]) -> "DltLogChannelBuilder":
        """Set default_trace attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.default_trace = value
        return self

    def with_dlt_messages(self, items: list[DltMessage]) -> "DltLogChannelBuilder":
        """Set dlt_messages list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.dlt_messages = list(items) if items else []
        return self

    def with_log_channel_id(self, value: Optional[String]) -> "DltLogChannelBuilder":
        """Set log_channel_id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.log_channel_id = value
        return self

    def with_log_trace_default_log(self, value: Optional[LogTraceDefaultLogLevelEnum]) -> "DltLogChannelBuilder":
        """Set log_trace_default_log attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.log_trace_default_log = value
        return self

    def with_non_verbose(self, value: Optional[Boolean]) -> "DltLogChannelBuilder":
        """Set non_verbose attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.non_verbose = value
        return self

    def with_rx_pdu_triggering_channel(self, value: Optional[PduTriggering]) -> "DltLogChannelBuilder":
        """Set rx_pdu_triggering_channel attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.rx_pdu_triggering_channel = value
        return self

    def with_segmentation(self, value: Optional[Boolean]) -> "DltLogChannelBuilder":
        """Set segmentation attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.segmentation = value
        return self

    def with_tx_pdu_triggering(self, value: Optional[PduTriggering]) -> "DltLogChannelBuilder":
        """Set tx_pdu_triggering attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tx_pdu_triggering = value
        return self


    def add_application(self, item: DltContext) -> "DltLogChannelBuilder":
        """Add a single item to applications list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.applications.append(item)
        return self

    def clear_applications(self) -> "DltLogChannelBuilder":
        """Clear all items from applications list.

        Returns:
            self for method chaining
        """
        self._obj.applications = []
        return self

    def add_dlt_message(self, item: DltMessage) -> "DltLogChannelBuilder":
        """Add a single item to dlt_messages list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.dlt_messages.append(item)
        return self

    def clear_dlt_messages(self) -> "DltLogChannelBuilder":
        """Clear all items from dlt_messages list.

        Returns:
            self for method chaining
        """
        self._obj.dlt_messages = []
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


    def build(self) -> DltLogChannel:
        """Build and return the DltLogChannel instance with validation."""
        self._validate_instance()
        pass
        return self._obj