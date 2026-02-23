"""TimeSyncServerConfiguration AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 470)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import ReferrableBuilder
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    TimeSyncTechnologyEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    String,
    TimeValue,
)


class TimeSyncServerConfiguration(Referrable):
    """AUTOSAR TimeSyncServerConfiguration."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    priority: Optional[PositiveInteger]
    sync_interval: Optional[TimeValue]
    time_sync_server_identifier: Optional[String]
    time_sync: Optional[TimeSyncTechnologyEnum]
    def __init__(self) -> None:
        """Initialize TimeSyncServerConfiguration."""
        super().__init__()
        self.priority: Optional[PositiveInteger] = None
        self.sync_interval: Optional[TimeValue] = None
        self.time_sync_server_identifier: Optional[String] = None
        self.time_sync: Optional[TimeSyncTechnologyEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize TimeSyncServerConfiguration to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TimeSyncServerConfiguration, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize priority
        if self.priority is not None:
            serialized = SerializationHelper.serialize_item(self.priority, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PRIORITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sync_interval
        if self.sync_interval is not None:
            serialized = SerializationHelper.serialize_item(self.sync_interval, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SYNC-INTERVAL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize time_sync_server_identifier
        if self.time_sync_server_identifier is not None:
            serialized = SerializationHelper.serialize_item(self.time_sync_server_identifier, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIME-SYNC-SERVER-IDENTIFIER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize time_sync
        if self.time_sync is not None:
            serialized = SerializationHelper.serialize_item(self.time_sync, "TimeSyncTechnologyEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIME-SYNC")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TimeSyncServerConfiguration":
        """Deserialize XML element to TimeSyncServerConfiguration object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TimeSyncServerConfiguration object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TimeSyncServerConfiguration, cls).deserialize(element)

        # Parse priority
        child = SerializationHelper.find_child_element(element, "PRIORITY")
        if child is not None:
            priority_value = child.text
            obj.priority = priority_value

        # Parse sync_interval
        child = SerializationHelper.find_child_element(element, "SYNC-INTERVAL")
        if child is not None:
            sync_interval_value = child.text
            obj.sync_interval = sync_interval_value

        # Parse time_sync_server_identifier
        child = SerializationHelper.find_child_element(element, "TIME-SYNC-SERVER-IDENTIFIER")
        if child is not None:
            time_sync_server_identifier_value = child.text
            obj.time_sync_server_identifier = time_sync_server_identifier_value

        # Parse time_sync
        child = SerializationHelper.find_child_element(element, "TIME-SYNC")
        if child is not None:
            time_sync_value = TimeSyncTechnologyEnum.deserialize(child)
            obj.time_sync = time_sync_value

        return obj



class TimeSyncServerConfigurationBuilder(ReferrableBuilder):
    """Builder for TimeSyncServerConfiguration with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TimeSyncServerConfiguration = TimeSyncServerConfiguration()


    def with_priority(self, value: Optional[PositiveInteger]) -> "TimeSyncServerConfigurationBuilder":
        """Set priority attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.priority = value
        return self

    def with_sync_interval(self, value: Optional[TimeValue]) -> "TimeSyncServerConfigurationBuilder":
        """Set sync_interval attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sync_interval = value
        return self

    def with_time_sync_server_identifier(self, value: Optional[String]) -> "TimeSyncServerConfigurationBuilder":
        """Set time_sync_server_identifier attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.time_sync_server_identifier = value
        return self

    def with_time_sync(self, value: Optional[TimeSyncTechnologyEnum]) -> "TimeSyncServerConfigurationBuilder":
        """Set time_sync attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.time_sync = value
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


    def build(self) -> TimeSyncServerConfiguration:
        """Build and return the TimeSyncServerConfiguration instance with validation."""
        self._validate_instance()
        pass
        return self._obj