"""InitialSdDelayConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 514)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ServiceInstances.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class InitialSdDelayConfig(ARObject):
    """AUTOSAR InitialSdDelayConfig."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    initial_delay_max: Optional[TimeValue]
    initial_delay_min: Optional[TimeValue]
    initial: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize InitialSdDelayConfig."""
        super().__init__()
        self.initial_delay_max: Optional[TimeValue] = None
        self.initial_delay_min: Optional[TimeValue] = None
        self.initial: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize InitialSdDelayConfig to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(InitialSdDelayConfig, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize initial_delay_max
        if self.initial_delay_max is not None:
            serialized = SerializationHelper.serialize_item(self.initial_delay_max, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INITIAL-DELAY-MAX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize initial_delay_min
        if self.initial_delay_min is not None:
            serialized = SerializationHelper.serialize_item(self.initial_delay_min, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INITIAL-DELAY-MIN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize initial
        if self.initial is not None:
            serialized = SerializationHelper.serialize_item(self.initial, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INITIAL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "InitialSdDelayConfig":
        """Deserialize XML element to InitialSdDelayConfig object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized InitialSdDelayConfig object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(InitialSdDelayConfig, cls).deserialize(element)

        # Parse initial_delay_max
        child = SerializationHelper.find_child_element(element, "INITIAL-DELAY-MAX")
        if child is not None:
            initial_delay_max_value = child.text
            obj.initial_delay_max = initial_delay_max_value

        # Parse initial_delay_min
        child = SerializationHelper.find_child_element(element, "INITIAL-DELAY-MIN")
        if child is not None:
            initial_delay_min_value = child.text
            obj.initial_delay_min = initial_delay_min_value

        # Parse initial
        child = SerializationHelper.find_child_element(element, "INITIAL")
        if child is not None:
            initial_value = child.text
            obj.initial = initial_value

        return obj



class InitialSdDelayConfigBuilder(BuilderBase):
    """Builder for InitialSdDelayConfig with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: InitialSdDelayConfig = InitialSdDelayConfig()


    def with_initial_delay_max(self, value: Optional[TimeValue]) -> "InitialSdDelayConfigBuilder":
        """Set initial_delay_max attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.initial_delay_max = value
        return self

    def with_initial_delay_min(self, value: Optional[TimeValue]) -> "InitialSdDelayConfigBuilder":
        """Set initial_delay_min attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.initial_delay_min = value
        return self

    def with_initial(self, value: Optional[PositiveInteger]) -> "InitialSdDelayConfigBuilder":
        """Set initial attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.initial = value
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


    def build(self) -> InitialSdDelayConfig:
        """Build and return the InitialSdDelayConfig instance with validation."""
        self._validate_instance()
        pass
        return self._obj