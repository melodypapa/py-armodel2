"""DltLogChannel AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 722)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Dlt.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Dlt import (
    DltDefaultTraceStateEnum,
    LogTraceDefaultLogLevelEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    String,
)
from armodel.models.M2.AUTOSARTemplates.LogAndTraceExtract.dlt_context import (
    DltContext,
)
from armodel.models.M2.AUTOSARTemplates.LogAndTraceExtract.dlt_message import (
    DltMessage,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)


class DltLogChannel(Identifiable):
    """AUTOSAR DltLogChannel."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    application_refs: list[ARRef]
    default_trace: Optional[DltDefaultTraceStateEnum]
    dlt_message_refs: list[ARRef]
    log_channel_id: Optional[String]
    log_trace_default_log: Optional[LogTraceDefaultLogLevelEnum]
    non_verbose: Optional[Boolean]
    rx_pdu_triggering_channel_ref: Optional[ARRef]
    segmentation: Optional[Boolean]
    tx_pdu_triggering_ref: Optional[ARRef]
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
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

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

        # Parse application_refs (list from container "APPLICATION-REFS")
        obj.application_refs = []
        container = SerializationHelper.find_child_element(element, "APPLICATION-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.application_refs.append(child_value)

        # Parse default_trace
        child = SerializationHelper.find_child_element(element, "DEFAULT-TRACE")
        if child is not None:
            default_trace_value = DltDefaultTraceStateEnum.deserialize(child)
            obj.default_trace = default_trace_value

        # Parse dlt_message_refs (list from container "DLT-MESSAGE-REFS")
        obj.dlt_message_refs = []
        container = SerializationHelper.find_child_element(element, "DLT-MESSAGE-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.dlt_message_refs.append(child_value)

        # Parse log_channel_id
        child = SerializationHelper.find_child_element(element, "LOG-CHANNEL-ID")
        if child is not None:
            log_channel_id_value = child.text
            obj.log_channel_id = log_channel_id_value

        # Parse log_trace_default_log
        child = SerializationHelper.find_child_element(element, "LOG-TRACE-DEFAULT-LOG")
        if child is not None:
            log_trace_default_log_value = LogTraceDefaultLogLevelEnum.deserialize(child)
            obj.log_trace_default_log = log_trace_default_log_value

        # Parse non_verbose
        child = SerializationHelper.find_child_element(element, "NON-VERBOSE")
        if child is not None:
            non_verbose_value = child.text
            obj.non_verbose = non_verbose_value

        # Parse rx_pdu_triggering_channel_ref
        child = SerializationHelper.find_child_element(element, "RX-PDU-TRIGGERING-CHANNEL-REF")
        if child is not None:
            rx_pdu_triggering_channel_ref_value = ARRef.deserialize(child)
            obj.rx_pdu_triggering_channel_ref = rx_pdu_triggering_channel_ref_value

        # Parse segmentation
        child = SerializationHelper.find_child_element(element, "SEGMENTATION")
        if child is not None:
            segmentation_value = child.text
            obj.segmentation = segmentation_value

        # Parse tx_pdu_triggering_ref
        child = SerializationHelper.find_child_element(element, "TX-PDU-TRIGGERING-REF")
        if child is not None:
            tx_pdu_triggering_ref_value = ARRef.deserialize(child)
            obj.tx_pdu_triggering_ref = tx_pdu_triggering_ref_value

        return obj



class DltLogChannelBuilder:
    """Builder for DltLogChannel with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: DltLogChannel = DltLogChannel()


    def with_short_name(self, value: Identifier) -> "DltLogChannelBuilder":
        """Set short_name attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.short_name = value
        return self

    def with_short_name_fragments(self, items: list[ShortNameFragment]) -> "DltLogChannelBuilder":
        """Set short_name_fragments list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = list(items) if items else []
        return self

    def with_long_name(self, value: Optional[MultilanguageLongName]) -> "DltLogChannelBuilder":
        """Set long_name attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.long_name = value
        return self

    def with_admin_data(self, value: Optional[AdminData]) -> "DltLogChannelBuilder":
        """Set admin_data attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.admin_data = value
        return self

    def with_annotations(self, items: list[Annotation]) -> "DltLogChannelBuilder":
        """Set annotations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.annotations = list(items) if items else []
        return self

    def with_desc(self, value: Optional[MultiLanguageOverviewParagraph]) -> "DltLogChannelBuilder":
        """Set desc attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.desc = value
        return self

    def with_category(self, value: Optional[CategoryString]) -> "DltLogChannelBuilder":
        """Set category attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.category = value
        return self

    def with_introduction(self, value: Optional[DocumentationBlock]) -> "DltLogChannelBuilder":
        """Set introduction attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.introduction = value
        return self

    def with_uuid(self, value: Optional[String]) -> "DltLogChannelBuilder":
        """Set uuid attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.uuid = value
        return self

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


    def add_short_name_fragment(self, item: ShortNameFragment) -> "DltLogChannelBuilder":
        """Add a single item to short_name_fragments list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments.append(item)
        return self

    def clear_short_name_fragments(self) -> "DltLogChannelBuilder":
        """Clear all items from short_name_fragments list.

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = []
        return self

    def add_annotation(self, item: Annotation) -> "DltLogChannelBuilder":
        """Add a single item to annotations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.annotations.append(item)
        return self

    def clear_annotations(self) -> "DltLogChannelBuilder":
        """Clear all items from annotations list.

        Returns:
            self for method chaining
        """
        self._obj.annotations = []
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


    @staticmethod
    def _coerce_to_int(value: Any) -> int:
        """Coerce value to int.

        Args:
            value: Value to coerce

        Returns:
            Integer value

        Raises:
            ValueError: If value cannot be coerced to int
        """
        if isinstance(value, int):
            return value
        if isinstance(value, str) and value.isdigit():
            return int(value)
        if isinstance(value, float):
            return int(value)
        if isinstance(value, bool):
            return int(value)
        raise ValueError(f"Cannot coerce {type(value).__name__} to int: {value}")

    @staticmethod
    def _coerce_to_float(value: Any) -> float:
        """Coerce value to float.

        Args:
            value: Value to coerce

        Returns:
            Float value

        Raises:
            ValueError: If value cannot be coerced to float
        """
        if isinstance(value, float):
            return value
        if isinstance(value, int):
            return float(value)
        if isinstance(value, str):
            try:
                return float(value)
            except ValueError:
                pass
        raise ValueError(f"Cannot coerce {type(value).__name__} to float: {value}")

    @staticmethod
    def _coerce_to_bool(value: Any) -> bool:
        """Coerce value to bool.

        Args:
            value: Value to coerce

        Returns:
            Boolean value

        Raises:
            ValueError: If value cannot be coerced to bool
        """
        if isinstance(value, bool):
            return value
        if isinstance(value, int):
            return bool(value)
        if isinstance(value, str):
            if value.lower() in ("true", "1", "yes"):
                return True
            if value.lower() in ("false", "0", "no"):
                return False
        raise ValueError(f"Cannot coerce {type(value).__name__} to bool: {value}")

    @staticmethod
    def _coerce_to_str(value: Any) -> str:
        """Coerce value to str.

        Args:
            value: Value to coerce

        Returns:
            String value
        """
        return str(value)


    @staticmethod
    def _coerce_to_list(value: Any, item_type: str) -> list:
        """Coerce value to list.

        Args:
            value: Value to coerce
            item_type: Expected item type (for error messages)

        Returns:
            List value

        Raises:
            ValueError: If value cannot be coerced to list
        """
        if isinstance(value, list):
            return value
        if isinstance(value, tuple):
            return list(value)
        raise ValueError(f"Cannot coerce {type(value).__name__} to list[{item_type}]: {value}")


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel.core import GlobalSettingsManager, BuilderValidationMode

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