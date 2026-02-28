"""EcucAbstractConfigurationClass AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 51)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import (
    EcucConfigurationClassEnum,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class EcucAbstractConfigurationClass(ARObject, ABC):
    """AUTOSAR EcucAbstractConfigurationClass."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    config_class: Optional[EcucConfigurationClassEnum]
    config_variant: Optional[Any]
    _DESERIALIZE_DISPATCH = {
        "CONFIG-CLASS": lambda obj, elem: setattr(obj, "config_class", EcucConfigurationClassEnum.deserialize(elem)),
        "CONFIG-VARIANT": lambda obj, elem: setattr(obj, "config_variant", any (EcucConfiguration).deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize EcucAbstractConfigurationClass."""
        super().__init__()
        self.config_class: Optional[EcucConfigurationClassEnum] = None
        self.config_variant: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize EcucAbstractConfigurationClass to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcucAbstractConfigurationClass, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize config_class
        if self.config_class is not None:
            serialized = SerializationHelper.serialize_item(self.config_class, "EcucConfigurationClassEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONFIG-CLASS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize config_variant
        if self.config_variant is not None:
            serialized = SerializationHelper.serialize_item(self.config_variant, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONFIG-VARIANT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucAbstractConfigurationClass":
        """Deserialize XML element to EcucAbstractConfigurationClass object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucAbstractConfigurationClass object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcucAbstractConfigurationClass, cls).deserialize(element)

        # Parse config_class
        child = SerializationHelper.find_child_element(element, "CONFIG-CLASS")
        if child is not None:
            config_class_value = EcucConfigurationClassEnum.deserialize(child)
            obj.config_class = config_class_value

        # Parse config_variant
        child = SerializationHelper.find_child_element(element, "CONFIG-VARIANT")
        if child is not None:
            config_variant_value = child.text
            obj.config_variant = config_variant_value

        return obj



class EcucAbstractConfigurationClassBuilder(BuilderBase, ABC):
    """Builder for EcucAbstractConfigurationClass with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EcucAbstractConfigurationClass = EcucAbstractConfigurationClass()


    def with_config_class(self, value: Optional[EcucConfigurationClassEnum]) -> "EcucAbstractConfigurationClassBuilder":
        """Set config_class attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.config_class = value
        return self

    def with_config_variant(self, value: Optional[any (EcucConfiguration)]) -> "EcucAbstractConfigurationClassBuilder":
        """Set config_variant attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.config_variant = value
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


    @abstractmethod
    def build(self) -> EcucAbstractConfigurationClass:
        """Build and return the EcucAbstractConfigurationClass instance (abstract)."""
        raise NotImplementedError