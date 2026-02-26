"""Field AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 45)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_AdaptivePlatform_ApplicationDesign_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.autosar_data_prototype import (
    AutosarDataPrototype,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.autosar_data_prototype import AutosarDataPrototypeBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class Field(AutosarDataPrototype):
    """AUTOSAR Field."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    has_getter: Optional[Boolean]
    has_notifier: Optional[Boolean]
    has_setter: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize Field."""
        super().__init__()
        self.has_getter: Optional[Boolean] = None
        self.has_notifier: Optional[Boolean] = None
        self.has_setter: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize Field to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Field, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize has_getter
        if self.has_getter is not None:
            serialized = SerializationHelper.serialize_item(self.has_getter, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HAS-GETTER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize has_notifier
        if self.has_notifier is not None:
            serialized = SerializationHelper.serialize_item(self.has_notifier, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HAS-NOTIFIER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize has_setter
        if self.has_setter is not None:
            serialized = SerializationHelper.serialize_item(self.has_setter, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HAS-SETTER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Field":
        """Deserialize XML element to Field object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Field object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Field, cls).deserialize(element)

        # Parse has_getter
        child = SerializationHelper.find_child_element(element, "HAS-GETTER")
        if child is not None:
            has_getter_value = child.text
            obj.has_getter = has_getter_value

        # Parse has_notifier
        child = SerializationHelper.find_child_element(element, "HAS-NOTIFIER")
        if child is not None:
            has_notifier_value = child.text
            obj.has_notifier = has_notifier_value

        # Parse has_setter
        child = SerializationHelper.find_child_element(element, "HAS-SETTER")
        if child is not None:
            has_setter_value = child.text
            obj.has_setter = has_setter_value

        return obj



class FieldBuilder(AutosarDataPrototypeBuilder):
    """Builder for Field with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: Field = Field()


    def with_has_getter(self, value: Optional[Boolean]) -> "FieldBuilder":
        """Set has_getter attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.has_getter = value
        return self

    def with_has_notifier(self, value: Optional[Boolean]) -> "FieldBuilder":
        """Set has_notifier attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.has_notifier = value
        return self

    def with_has_setter(self, value: Optional[Boolean]) -> "FieldBuilder":
        """Set has_setter attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.has_setter = value
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


    def build(self) -> Field:
        """Build and return the Field instance with validation."""
        self._validate_instance()
        pass
        return self._obj