"""EcucCommonAttributes AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 48)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_definition_element import (
    EcucDefinitionElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_definition_element import EcucDefinitionElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    String,
)
from armodel2.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_multiplicity_configuration_class import (
    EcucMultiplicityConfigurationClass,
)
from armodel2.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_value_configuration_class import (
    EcucValueConfigurationClass,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class EcucCommonAttributes(EcucDefinitionElement, ABC):
    """AUTOSAR EcucCommonAttributes."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    multiplicities: list[EcucMultiplicityConfigurationClass]
    origin: Optional[String]
    post_build_variant: Optional[Boolean]
    requires_index: Optional[Boolean]
    value_configs: list[EcucValueConfigurationClass]
    _DESERIALIZE_DISPATCH = {
        "MULTIPLICITIES": lambda obj, elem: obj.multiplicities.append(SerializationHelper.deserialize_by_tag(elem, "EcucMultiplicityConfigurationClass")),
        "ORIGIN": lambda obj, elem: setattr(obj, "origin", SerializationHelper.deserialize_by_tag(elem, "String")),
        "POST-BUILD-VARIANT": lambda obj, elem: setattr(obj, "post_build_variant", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "REQUIRES-INDEX": lambda obj, elem: setattr(obj, "requires_index", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "VALUE-CONFIGS": lambda obj, elem: obj.value_configs.append(SerializationHelper.deserialize_by_tag(elem, "EcucValueConfigurationClass")),
    }


    def __init__(self) -> None:
        """Initialize EcucCommonAttributes."""
        super().__init__()
        self.multiplicities: list[EcucMultiplicityConfigurationClass] = []
        self.origin: Optional[String] = None
        self.post_build_variant: Optional[Boolean] = None
        self.requires_index: Optional[Boolean] = None
        self.value_configs: list[EcucValueConfigurationClass] = []

    def serialize(self) -> ET.Element:
        """Serialize EcucCommonAttributes to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcucCommonAttributes, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize multiplicities (list to container "MULTIPLICITIES")
        if self.multiplicities:
            wrapper = ET.Element("MULTIPLICITIES")
            for item in self.multiplicities:
                serialized = SerializationHelper.serialize_item(item, "EcucMultiplicityConfigurationClass")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize origin
        if self.origin is not None:
            serialized = SerializationHelper.serialize_item(self.origin, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ORIGIN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize post_build_variant
        if self.post_build_variant is not None:
            serialized = SerializationHelper.serialize_item(self.post_build_variant, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("POST-BUILD-VARIANT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize requires_index
        if self.requires_index is not None:
            serialized = SerializationHelper.serialize_item(self.requires_index, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REQUIRES-INDEX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize value_configs (list to container "VALUE-CONFIGS")
        if self.value_configs:
            wrapper = ET.Element("VALUE-CONFIGS")
            for item in self.value_configs:
                serialized = SerializationHelper.serialize_item(item, "EcucValueConfigurationClass")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucCommonAttributes":
        """Deserialize XML element to EcucCommonAttributes object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucCommonAttributes object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcucCommonAttributes, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "MULTIPLICITIES":
                # Iterate through wrapper children
                for item_elem in child:
                    item_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    obj.multiplicities.append(SerializationHelper.deserialize_by_tag(item_elem, "EcucMultiplicityConfigurationClass"))
            elif tag == "ORIGIN":
                setattr(obj, "origin", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "POST-BUILD-VARIANT":
                setattr(obj, "post_build_variant", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "REQUIRES-INDEX":
                setattr(obj, "requires_index", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "VALUE-CONFIGS":
                # Iterate through wrapper children
                for item_elem in child:
                    item_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    obj.value_configs.append(SerializationHelper.deserialize_by_tag(item_elem, "EcucValueConfigurationClass"))

        return obj



class EcucCommonAttributesBuilder(EcucDefinitionElementBuilder):
    """Builder for EcucCommonAttributes with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EcucCommonAttributes = EcucCommonAttributes()


    def with_multiplicities(self, items: list[EcucMultiplicityConfigurationClass]) -> "EcucCommonAttributesBuilder":
        """Set multiplicities list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.multiplicities = list(items) if items else []
        return self

    def with_origin(self, value: Optional[String]) -> "EcucCommonAttributesBuilder":
        """Set origin attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.origin = value
        return self

    def with_post_build_variant(self, value: Optional[Boolean]) -> "EcucCommonAttributesBuilder":
        """Set post_build_variant attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.post_build_variant = value
        return self

    def with_requires_index(self, value: Optional[Boolean]) -> "EcucCommonAttributesBuilder":
        """Set requires_index attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.requires_index = value
        return self

    def with_value_configs(self, items: list[EcucValueConfigurationClass]) -> "EcucCommonAttributesBuilder":
        """Set value_configs list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.value_configs = list(items) if items else []
        return self


    def add_multiplicity(self, item: EcucMultiplicityConfigurationClass) -> "EcucCommonAttributesBuilder":
        """Add a single item to multiplicities list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.multiplicities.append(item)
        return self

    def clear_multiplicities(self) -> "EcucCommonAttributesBuilder":
        """Clear all items from multiplicities list.

        Returns:
            self for method chaining
        """
        self._obj.multiplicities = []
        return self

    def add_value_config(self, item: EcucValueConfigurationClass) -> "EcucCommonAttributesBuilder":
        """Add a single item to value_configs list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.value_configs.append(item)
        return self

    def clear_value_configs(self) -> "EcucCommonAttributesBuilder":
        """Clear all items from value_configs list.

        Returns:
            self for method chaining
        """
        self._obj.value_configs = []
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
    def build(self) -> EcucCommonAttributes:
        """Build and return the EcucCommonAttributes instance (abstract)."""
        raise NotImplementedError