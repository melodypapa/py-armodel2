"""RuleBasedValueSpecification AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 331)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 469)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Constants.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    Integer,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.rule_arguments import (
    RuleArguments,
)


class RuleBasedValueSpecification(ARObject):
    """AUTOSAR RuleBasedValueSpecification."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    arguments: Optional[RuleArguments]
    max_size_to_fill: Optional[Integer]
    rule: Optional[Identifier]
    def __init__(self) -> None:
        """Initialize RuleBasedValueSpecification."""
        super().__init__()
        self.arguments: Optional[RuleArguments] = None
        self.max_size_to_fill: Optional[Integer] = None
        self.rule: Optional[Identifier] = None

    def serialize(self) -> ET.Element:
        """Serialize RuleBasedValueSpecification to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(RuleBasedValueSpecification, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize arguments
        if self.arguments is not None:
            serialized = SerializationHelper.serialize_item(self.arguments, "RuleArguments")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ARGUMENTS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_size_to_fill
        if self.max_size_to_fill is not None:
            serialized = SerializationHelper.serialize_item(self.max_size_to_fill, "Integer")
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
    def deserialize(cls, element: ET.Element) -> "RuleBasedValueSpecification":
        """Deserialize XML element to RuleBasedValueSpecification object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RuleBasedValueSpecification object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(RuleBasedValueSpecification, cls).deserialize(element)

        # Parse arguments
        child = SerializationHelper.find_child_element(element, "ARGUMENTS")
        if child is not None:
            arguments_value = SerializationHelper.deserialize_by_tag(child, "RuleArguments")
            obj.arguments = arguments_value

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



class RuleBasedValueSpecificationBuilder(BuilderBase):
    """Builder for RuleBasedValueSpecification with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: RuleBasedValueSpecification = RuleBasedValueSpecification()


    def with_arguments(self, value: Optional[RuleArguments]) -> "RuleBasedValueSpecificationBuilder":
        """Set arguments attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.arguments = value
        return self

    def with_max_size_to_fill(self, value: Optional[Integer]) -> "RuleBasedValueSpecificationBuilder":
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

    def with_rule(self, value: Optional[Identifier]) -> "RuleBasedValueSpecificationBuilder":
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


    def build(self) -> RuleBasedValueSpecification:
        """Build and return the RuleBasedValueSpecification instance with validation."""
        self._validate_instance()
        pass
        return self._obj