"""NumericalRuleBasedValueSpecification AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 467)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Constants.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Constants.abstract_rule_based_value_specification import (
    AbstractRuleBasedValueSpecification,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Constants.abstract_rule_based_value_specification import AbstractRuleBasedValueSpecificationBuilder
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Constants.rule_based_value_specification import (
    RuleBasedValueSpecification,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class NumericalRuleBasedValueSpecification(AbstractRuleBasedValueSpecification):
    """AUTOSAR NumericalRuleBasedValueSpecification."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "NUMERICAL-RULE-BASED-VALUE-SPECIFICATION"


    rule_based_values: Optional[RuleBasedValueSpecification]
    _DESERIALIZE_DISPATCH = {
        "RULE-BASED-VALUES": lambda obj, elem: setattr(obj, "rule_based_values", SerializationHelper.deserialize_by_tag(elem, "RuleBasedValueSpecification")),
    }


    def __init__(self) -> None:
        """Initialize NumericalRuleBasedValueSpecification."""
        super().__init__()
        self.rule_based_values: Optional[RuleBasedValueSpecification] = None

    def serialize(self) -> ET.Element:
        """Serialize NumericalRuleBasedValueSpecification to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(NumericalRuleBasedValueSpecification, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize rule_based_values
        if self.rule_based_values is not None:
            serialized = SerializationHelper.serialize_item(self.rule_based_values, "RuleBasedValueSpecification")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RULE-BASED-VALUES")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "NumericalRuleBasedValueSpecification":
        """Deserialize XML element to NumericalRuleBasedValueSpecification object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized NumericalRuleBasedValueSpecification object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(NumericalRuleBasedValueSpecification, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "RULE-BASED-VALUES":
                setattr(obj, "rule_based_values", SerializationHelper.deserialize_by_tag(child, "RuleBasedValueSpecification"))

        return obj



class NumericalRuleBasedValueSpecificationBuilder(AbstractRuleBasedValueSpecificationBuilder):
    """Builder for NumericalRuleBasedValueSpecification with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: NumericalRuleBasedValueSpecification = NumericalRuleBasedValueSpecification()


    def with_rule_based_values(self, value: Optional[RuleBasedValueSpecification]) -> "NumericalRuleBasedValueSpecificationBuilder":
        """Set rule_based_values attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'rule_based_values' is required and cannot be None")
        self._obj.rule_based_values = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "ruleBasedValues",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> NumericalRuleBasedValueSpecification:
        """Build and return the NumericalRuleBasedValueSpecification instance with validation."""
        self._validate_instance()
        return self._obj