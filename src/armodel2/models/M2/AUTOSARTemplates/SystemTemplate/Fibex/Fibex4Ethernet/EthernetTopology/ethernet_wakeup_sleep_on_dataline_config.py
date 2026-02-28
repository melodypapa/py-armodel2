"""EthernetWakeupSleepOnDatalineConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 158)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    TimeValue,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class EthernetWakeupSleepOnDatalineConfig(Identifiable):
    """AUTOSAR EthernetWakeupSleepOnDatalineConfig."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "ETHERNET-WAKEUP-SLEEP-ON-DATALINE-CONFIG"


    sleep_mode: Optional[TimeValue]
    sleep_repetition: Optional[TimeValue]
    sleep: Optional[PositiveInteger]
    wakeup_forward: Optional[Boolean]
    wakeup_local: Optional[Boolean]
    wakeup_remote: Optional[Boolean]
    wakeup: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "SLEEP-MODE": lambda obj, elem: setattr(obj, "sleep_mode", elem.text),
        "SLEEP-REPETITION": lambda obj, elem: setattr(obj, "sleep_repetition", elem.text),
        "SLEEP": lambda obj, elem: setattr(obj, "sleep", elem.text),
        "WAKEUP-FORWARD": lambda obj, elem: setattr(obj, "wakeup_forward", elem.text),
        "WAKEUP-LOCAL": lambda obj, elem: setattr(obj, "wakeup_local", elem.text),
        "WAKEUP-REMOTE": lambda obj, elem: setattr(obj, "wakeup_remote", elem.text),
        "WAKEUP": lambda obj, elem: setattr(obj, "wakeup", elem.text),
    }


    def __init__(self) -> None:
        """Initialize EthernetWakeupSleepOnDatalineConfig."""
        super().__init__()
        self.sleep_mode: Optional[TimeValue] = None
        self.sleep_repetition: Optional[TimeValue] = None
        self.sleep: Optional[PositiveInteger] = None
        self.wakeup_forward: Optional[Boolean] = None
        self.wakeup_local: Optional[Boolean] = None
        self.wakeup_remote: Optional[Boolean] = None
        self.wakeup: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize EthernetWakeupSleepOnDatalineConfig to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EthernetWakeupSleepOnDatalineConfig, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize sleep_mode
        if self.sleep_mode is not None:
            serialized = SerializationHelper.serialize_item(self.sleep_mode, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SLEEP-MODE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sleep_repetition
        if self.sleep_repetition is not None:
            serialized = SerializationHelper.serialize_item(self.sleep_repetition, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SLEEP-REPETITION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sleep
        if self.sleep is not None:
            serialized = SerializationHelper.serialize_item(self.sleep, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SLEEP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize wakeup_forward
        if self.wakeup_forward is not None:
            serialized = SerializationHelper.serialize_item(self.wakeup_forward, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("WAKEUP-FORWARD")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize wakeup_local
        if self.wakeup_local is not None:
            serialized = SerializationHelper.serialize_item(self.wakeup_local, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("WAKEUP-LOCAL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize wakeup_remote
        if self.wakeup_remote is not None:
            serialized = SerializationHelper.serialize_item(self.wakeup_remote, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("WAKEUP-REMOTE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize wakeup
        if self.wakeup is not None:
            serialized = SerializationHelper.serialize_item(self.wakeup, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("WAKEUP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EthernetWakeupSleepOnDatalineConfig":
        """Deserialize XML element to EthernetWakeupSleepOnDatalineConfig object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EthernetWakeupSleepOnDatalineConfig object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EthernetWakeupSleepOnDatalineConfig, cls).deserialize(element)

        # Parse sleep_mode
        child = SerializationHelper.find_child_element(element, "SLEEP-MODE")
        if child is not None:
            sleep_mode_value = child.text
            obj.sleep_mode = sleep_mode_value

        # Parse sleep_repetition
        child = SerializationHelper.find_child_element(element, "SLEEP-REPETITION")
        if child is not None:
            sleep_repetition_value = child.text
            obj.sleep_repetition = sleep_repetition_value

        # Parse sleep
        child = SerializationHelper.find_child_element(element, "SLEEP")
        if child is not None:
            sleep_value = child.text
            obj.sleep = sleep_value

        # Parse wakeup_forward
        child = SerializationHelper.find_child_element(element, "WAKEUP-FORWARD")
        if child is not None:
            wakeup_forward_value = child.text
            obj.wakeup_forward = wakeup_forward_value

        # Parse wakeup_local
        child = SerializationHelper.find_child_element(element, "WAKEUP-LOCAL")
        if child is not None:
            wakeup_local_value = child.text
            obj.wakeup_local = wakeup_local_value

        # Parse wakeup_remote
        child = SerializationHelper.find_child_element(element, "WAKEUP-REMOTE")
        if child is not None:
            wakeup_remote_value = child.text
            obj.wakeup_remote = wakeup_remote_value

        # Parse wakeup
        child = SerializationHelper.find_child_element(element, "WAKEUP")
        if child is not None:
            wakeup_value = child.text
            obj.wakeup = wakeup_value

        return obj



class EthernetWakeupSleepOnDatalineConfigBuilder(IdentifiableBuilder):
    """Builder for EthernetWakeupSleepOnDatalineConfig with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EthernetWakeupSleepOnDatalineConfig = EthernetWakeupSleepOnDatalineConfig()


    def with_sleep_mode(self, value: Optional[TimeValue]) -> "EthernetWakeupSleepOnDatalineConfigBuilder":
        """Set sleep_mode attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sleep_mode = value
        return self

    def with_sleep_repetition(self, value: Optional[TimeValue]) -> "EthernetWakeupSleepOnDatalineConfigBuilder":
        """Set sleep_repetition attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sleep_repetition = value
        return self

    def with_sleep(self, value: Optional[PositiveInteger]) -> "EthernetWakeupSleepOnDatalineConfigBuilder":
        """Set sleep attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sleep = value
        return self

    def with_wakeup_forward(self, value: Optional[Boolean]) -> "EthernetWakeupSleepOnDatalineConfigBuilder":
        """Set wakeup_forward attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.wakeup_forward = value
        return self

    def with_wakeup_local(self, value: Optional[Boolean]) -> "EthernetWakeupSleepOnDatalineConfigBuilder":
        """Set wakeup_local attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.wakeup_local = value
        return self

    def with_wakeup_remote(self, value: Optional[Boolean]) -> "EthernetWakeupSleepOnDatalineConfigBuilder":
        """Set wakeup_remote attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.wakeup_remote = value
        return self

    def with_wakeup(self, value: Optional[PositiveInteger]) -> "EthernetWakeupSleepOnDatalineConfigBuilder":
        """Set wakeup attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.wakeup = value
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


    def build(self) -> EthernetWakeupSleepOnDatalineConfig:
        """Build and return the EthernetWakeupSleepOnDatalineConfig instance with validation."""
        self._validate_instance()
        pass
        return self._obj