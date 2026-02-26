"""DltConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 722)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Dlt.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel2.models.M2.AUTOSARTemplates.LogAndTraceExtract.dlt_ecu import (
    DltEcu,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Dlt.dlt_log_channel import (
    DltLogChannel,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DltConfig(ARObject):
    """AUTOSAR DltConfig."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    dlt_ecu_ref: Optional[ARRef]
    dlt_log_channels: list[DltLogChannel]
    session_id: Optional[Boolean]
    timestamp: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize DltConfig."""
        super().__init__()
        self.dlt_ecu_ref: Optional[ARRef] = None
        self.dlt_log_channels: list[DltLogChannel] = []
        self.session_id: Optional[Boolean] = None
        self.timestamp: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize DltConfig to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DltConfig, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize dlt_ecu_ref
        if self.dlt_ecu_ref is not None:
            serialized = SerializationHelper.serialize_item(self.dlt_ecu_ref, "DltEcu")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DLT-ECU-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize dlt_log_channels (list to container "DLT-LOG-CHANNELS")
        if self.dlt_log_channels:
            wrapper = ET.Element("DLT-LOG-CHANNELS")
            for item in self.dlt_log_channels:
                serialized = SerializationHelper.serialize_item(item, "DltLogChannel")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize session_id
        if self.session_id is not None:
            serialized = SerializationHelper.serialize_item(self.session_id, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SESSION-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize timestamp
        if self.timestamp is not None:
            serialized = SerializationHelper.serialize_item(self.timestamp, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIMESTAMP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DltConfig":
        """Deserialize XML element to DltConfig object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DltConfig object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DltConfig, cls).deserialize(element)

        # Parse dlt_ecu_ref
        child = SerializationHelper.find_child_element(element, "DLT-ECU-REF")
        if child is not None:
            dlt_ecu_ref_value = ARRef.deserialize(child)
            obj.dlt_ecu_ref = dlt_ecu_ref_value

        # Parse dlt_log_channels (list from container "DLT-LOG-CHANNELS")
        obj.dlt_log_channels = []
        container = SerializationHelper.find_child_element(element, "DLT-LOG-CHANNELS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.dlt_log_channels.append(child_value)

        # Parse session_id
        child = SerializationHelper.find_child_element(element, "SESSION-ID")
        if child is not None:
            session_id_value = child.text
            obj.session_id = session_id_value

        # Parse timestamp
        child = SerializationHelper.find_child_element(element, "TIMESTAMP")
        if child is not None:
            timestamp_value = child.text
            obj.timestamp = timestamp_value

        return obj



class DltConfigBuilder(BuilderBase):
    """Builder for DltConfig with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DltConfig = DltConfig()


    def with_dlt_ecu(self, value: Optional[DltEcu]) -> "DltConfigBuilder":
        """Set dlt_ecu attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.dlt_ecu = value
        return self

    def with_dlt_log_channels(self, items: list[DltLogChannel]) -> "DltConfigBuilder":
        """Set dlt_log_channels list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.dlt_log_channels = list(items) if items else []
        return self

    def with_session_id(self, value: Optional[Boolean]) -> "DltConfigBuilder":
        """Set session_id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.session_id = value
        return self

    def with_timestamp(self, value: Optional[Boolean]) -> "DltConfigBuilder":
        """Set timestamp attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.timestamp = value
        return self


    def add_dlt_log_channel(self, item: DltLogChannel) -> "DltConfigBuilder":
        """Add a single item to dlt_log_channels list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.dlt_log_channels.append(item)
        return self

    def clear_dlt_log_channels(self) -> "DltConfigBuilder":
        """Clear all items from dlt_log_channels list.

        Returns:
            self for method chaining
        """
        self._obj.dlt_log_channels = []
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


    def build(self) -> DltConfig:
        """Build and return the DltConfig instance with validation."""
        self._validate_instance()
        pass
        return self._obj