"""CompositeRuleBasedValueSpecification AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 471)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Constants.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
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
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Constants.composite_rule_based_value_argument import (
    CompositeRuleBasedValueArgument,
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

    _XML_TAG = "COMPOSITE-RULE-BASED-VALUE-SPECIFICATION"


    arguments: list[CompositeValueSpecification]
    compound_primitive_arguments: list[CompositeRuleBasedValueArgument]
    max_size_to_fill: Optional[PositiveInteger]
    rule: Optional[Identifier]
    _DESERIALIZE_DISPATCH = {
        "ARGUMENTS": ("_POLYMORPHIC_LIST", "arguments", ["ArrayValueSpecification", "RecordValueSpecification"]),
        "COMPOUND-PRIMITIVE-ARGUMENTS": ("_POLYMORPHIC_LIST", "compound_primitive_arguments", ["ApplicationRuleBasedValueSpecification", "ApplicationValueSpecification"]),
        "MAX-SIZE-TO-FILL": lambda obj, elem: setattr(obj, "max_size_to_fill", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "RULE": lambda obj, elem: setattr(obj, "rule", SerializationHelper.deserialize_by_tag(elem, "Identifier")),
    }


    def __init__(self) -> None:
        """Initialize CompositeRuleBasedValueSpecification."""
        super().__init__()
        self.arguments: list[CompositeValueSpecification] = []
        self.compound_primitive_arguments: list[CompositeRuleBasedValueArgument] = []
        self.max_size_to_fill: Optional[PositiveInteger] = None
        self.rule: Optional[Identifier] = None

    def serialize(self) -> ET.Element:
        """Serialize CompositeRuleBasedValueSpecification to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

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

        # Serialize compound_primitive_arguments (list to container "COMPOUND-PRIMITIVE-ARGUMENTS")
        if self.compound_primitive_arguments:
            wrapper = ET.Element("COMPOUND-PRIMITIVE-ARGUMENTS")
            for item in self.compound_primitive_arguments:
                serialized = SerializationHelper.serialize_item(item, "CompositeRuleBasedValueArgument")
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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ARGUMENTS":
                # Iterate through all child elements and deserialize each based on its concrete type
                for item_elem in child:
                    concrete_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    if concrete_tag == "ARRAY-VALUE-SPECIFICATION":
                        obj.arguments.append(SerializationHelper.deserialize_by_tag(item_elem, "ArrayValueSpecification"))
                    elif concrete_tag == "RECORD-VALUE-SPECIFICATION":
                        obj.arguments.append(SerializationHelper.deserialize_by_tag(item_elem, "RecordValueSpecification"))
            elif tag == "COMPOUND-PRIMITIVE-ARGUMENTS":
                # Iterate through all child elements and deserialize each based on its concrete type
                for item_elem in child:
                    concrete_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    if concrete_tag == "APPLICATION-RULE-BASED-VALUE-SPECIFICATION":
                        obj.compound_primitive_arguments.append(SerializationHelper.deserialize_by_tag(item_elem, "ApplicationRuleBasedValueSpecification"))
                    elif concrete_tag == "APPLICATION-VALUE-SPECIFICATION":
                        obj.compound_primitive_arguments.append(SerializationHelper.deserialize_by_tag(item_elem, "ApplicationValueSpecification"))
            elif tag == "MAX-SIZE-TO-FILL":
                setattr(obj, "max_size_to_fill", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "RULE":
                setattr(obj, "rule", SerializationHelper.deserialize_by_tag(child, "Identifier"))

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

    def with_compound_primitive_arguments(self, items: list[CompositeRuleBasedValueArgument]) -> "CompositeRuleBasedValueSpecificationBuilder":
        """Set compound_primitive_arguments list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.compound_primitive_arguments = list(items) if items else []
        return self

    def with_max_size_to_fill(self, value: Optional[PositiveInteger]) -> "CompositeRuleBasedValueSpecificationBuilder":
        """Set max_size_to_fill attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'max_size_to_fill' is required and cannot be None")
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
            raise ValueError("Attribute 'rule' is required and cannot be None")
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

    def add_compound_primitive_argument(self, item: CompositeRuleBasedValueArgument) -> "CompositeRuleBasedValueSpecificationBuilder":
        """Add a single item to compound_primitive_arguments list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.compound_primitive_arguments.append(item)
        return self

    def clear_compound_primitive_arguments(self) -> "CompositeRuleBasedValueSpecificationBuilder":
        """Clear all items from compound_primitive_arguments list.

        Returns:
            self for method chaining
        """
        self._obj.compound_primitive_arguments = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "argument",
        "compoundPrimitiveArgument",
        "maxSizeToFill",
        "rule",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> CompositeRuleBasedValueSpecification:
        """Build and return the CompositeRuleBasedValueSpecification instance with validation."""
        self._validate_instance()
        return self._obj