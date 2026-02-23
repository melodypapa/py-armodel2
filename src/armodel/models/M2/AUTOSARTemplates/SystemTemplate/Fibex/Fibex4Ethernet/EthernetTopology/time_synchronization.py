"""TimeSynchronization AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 469)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.time_sync_client_configuration import (
    TimeSyncClientConfiguration,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.time_sync_server_configuration import (
    TimeSyncServerConfiguration,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class TimeSynchronization(ARObject):
    """AUTOSAR TimeSynchronization."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    time_sync_client_configuration: Optional[TimeSyncClientConfiguration]
    time_sync_server_configuration: Optional[TimeSyncServerConfiguration]
    def __init__(self) -> None:
        """Initialize TimeSynchronization."""
        super().__init__()
        self.time_sync_client_configuration: Optional[TimeSyncClientConfiguration] = None
        self.time_sync_server_configuration: Optional[TimeSyncServerConfiguration] = None

    def serialize(self) -> ET.Element:
        """Serialize TimeSynchronization to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TimeSynchronization, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize time_sync_client_configuration
        if self.time_sync_client_configuration is not None:
            serialized = SerializationHelper.serialize_item(self.time_sync_client_configuration, "TimeSyncClientConfiguration")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIME-SYNC-CLIENT-CONFIGURATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize time_sync_server_configuration
        if self.time_sync_server_configuration is not None:
            serialized = SerializationHelper.serialize_item(self.time_sync_server_configuration, "TimeSyncServerConfiguration")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIME-SYNC-SERVER-CONFIGURATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TimeSynchronization":
        """Deserialize XML element to TimeSynchronization object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TimeSynchronization object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TimeSynchronization, cls).deserialize(element)

        # Parse time_sync_client_configuration
        child = SerializationHelper.find_child_element(element, "TIME-SYNC-CLIENT-CONFIGURATION")
        if child is not None:
            time_sync_client_configuration_value = SerializationHelper.deserialize_by_tag(child, "TimeSyncClientConfiguration")
            obj.time_sync_client_configuration = time_sync_client_configuration_value

        # Parse time_sync_server_configuration
        child = SerializationHelper.find_child_element(element, "TIME-SYNC-SERVER-CONFIGURATION")
        if child is not None:
            time_sync_server_configuration_value = SerializationHelper.deserialize_by_tag(child, "TimeSyncServerConfiguration")
            obj.time_sync_server_configuration = time_sync_server_configuration_value

        return obj



class TimeSynchronizationBuilder(BuilderBase):
    """Builder for TimeSynchronization with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TimeSynchronization = TimeSynchronization()


    def with_time_sync_client_configuration(self, value: Optional[TimeSyncClientConfiguration]) -> "TimeSynchronizationBuilder":
        """Set time_sync_client_configuration attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.time_sync_client_configuration = value
        return self

    def with_time_sync_server_configuration(self, value: Optional[TimeSyncServerConfiguration]) -> "TimeSynchronizationBuilder":
        """Set time_sync_server_configuration attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.time_sync_server_configuration = value
        return self




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


    def build(self) -> TimeSynchronization:
        """Build and return the TimeSynchronization instance with validation."""
        self._validate_instance()
        pass
        return self._obj