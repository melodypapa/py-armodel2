"""CompositeRuleBasedValueSpecification AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 471)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Constants.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Constants.abstract_rule_based_value_specification import (
    AbstractRuleBasedValueSpecification,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Constants.abstract_rule_based_value_specification import AbstractRuleBasedValueSpecificationBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Constants.composite_value_specification import (
    CompositeValueSpecification,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class CompositeRuleBasedValueSpecification(AbstractRuleBasedValueSpecification):
    """AUTOSAR CompositeRuleBasedValueSpecification."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    arguments: list[CompositeValueSpecification]
    compounds: list[Any]
    max_size_to_fill: Optional[PositiveInteger]
    rule: Optional[Identifier]
    def __init__(self) -> None:
        """Initialize CompositeRuleBasedValueSpecification."""
        super().__init__()
        self.arguments: list[CompositeValueSpecification] = []
        self.compounds: list[Any] = []
        self.max_size_to_fill: Optional[PositiveInteger] = None
        self.rule: Optional[Identifier] = None

    def serialize(self) -> ET.Element:
        """Serialize CompositeRuleBasedValueSpecification to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CompositeRuleBasedValueSpecification, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize arguments (list to container "ARGUMENTS")
        if self.arguments:
            wrapper = ET.Element("ARGUMENTS")
            for item in self.arguments:
                serialized = SerializationHelper.serialize_item(item, "CompositeValueSpecification")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize compounds (list to container "COMPOUNDS")
        if self.compounds:
            wrapper = ET.Element("COMPOUNDS")
            for item in self.compounds:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize max_size_to_fill
        if self.max_size_to_fill is not None:
            serialized = SerializationHelper.serialize_item(self.max_size_to_fill, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-SIZE-TO-FILL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rule
        if self.rule is not None:
            serialized = SerializationHelper.serialize_item(self.rule, "Identifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RULE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CompositeRuleBasedValueSpecification":
        """Deserialize XML element to CompositeRuleBasedValueSpecification object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CompositeRuleBasedValueSpecification object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CompositeRuleBasedValueSpecification, cls).deserialize(element)

        # Parse arguments (list from container "ARGUMENTS")
        obj.arguments = []
        container = SerializationHelper.find_child_element(element, "ARGUMENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.arguments.append(child_value)

        # Parse compounds (list from container "COMPOUNDS")
        obj.compounds = []
        container = SerializationHelper.find_child_element(element, "COMPOUNDS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.compounds.append(child_value)

        # Parse max_size_to_fill
        child = SerializationHelper.find_child_element(element, "MAX-SIZE-TO-FILL")
        if child is not None:
            max_size_to_fill_value = child.text
            obj.max_size_to_fill = max_size_to_fill_value

        # Parse rule
        child = SerializationHelper.find_child_element(element, "RULE")
        if child is not None:
            rule_value = SerializationHelper.deserialize_by_tag(child, "Identifier")
            obj.rule = rule_value

        return obj



class CompositeRuleBasedValueSpecificationBuilder(AbstractRuleBasedValueSpecificationBuilder):
    """Builder for CompositeRuleBasedValueSpecification with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: CompositeRuleBasedValueSpecification = CompositeRuleBasedValueSpecification()


    def with_arguments(self, items: list[CompositeValueSpecification]) -> "CompositeRuleBasedValueSpecificationBuilder":
        """Set arguments list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.arguments = list(items) if items else []
        return self

    def with_compounds(self, items: list[any (CompositeRuleBased)]) -> "CompositeRuleBasedValueSpecificationBuilder":
        """Set compounds list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.compounds = list(items) if items else []
        return self

    def with_max_size_to_fill(self, value: Optional[PositiveInteger]) -> "CompositeRuleBasedValueSpecificationBuilder":
        """Set max_size_to_fill attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.max_size_to_fill = value
        return self

    def with_rule(self, value: Optional[Identifier]) -> "CompositeRuleBasedValueSpecificationBuilder":
        """Set rule attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.rule = value
        return self


    def add_argument(self, item: CompositeValueSpecification) -> "CompositeRuleBasedValueSpecificationBuilder":
        """Add a single item to arguments list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.arguments.append(item)
        return self

    def clear_arguments(self) -> "CompositeRuleBasedValueSpecificationBuilder":
        """Clear all items from arguments list.

        Returns:
            self for method chaining
        """
        self._obj.arguments = []
        return self

    def add_compound(self, item: any (CompositeRuleBased)) -> "CompositeRuleBasedValueSpecificationBuilder":
        """Add a single item to compounds list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.compounds.append(item)
        return self

    def clear_compounds(self) -> "CompositeRuleBasedValueSpecificationBuilder":
        """Clear all items from compounds list.

        Returns:
            self for method chaining
        """
        self._obj.compounds = []
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


    def build(self) -> CompositeRuleBasedValueSpecification:
        """Build and return the CompositeRuleBasedValueSpecification instance with validation."""
        self._validate_instance()
        pass
        return self._obj