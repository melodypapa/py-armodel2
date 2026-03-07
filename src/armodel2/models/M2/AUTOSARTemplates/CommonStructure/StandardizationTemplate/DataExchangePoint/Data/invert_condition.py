"""InvertCondition AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 104)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint_Data.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.abstract_condition import (
    AbstractCondition,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.abstract_condition import AbstractConditionBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class InvertCondition(AbstractCondition):
    """AUTOSAR InvertCondition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "INVERT-CONDITION"


    condition: AbstractCondition
    _DESERIALIZE_DISPATCH = {
        "CONDITION": ("_POLYMORPHIC", "condition", ["AggregationCondition", "AttributeCondition", "InvertCondition", "PrimitiveAttributeCondition", "ReferenceCondition", "TextualCondition"]),
    }


    def __init__(self) -> None:
        """Initialize InvertCondition."""
        super().__init__()
        self.condition: AbstractCondition = None

    def serialize(self) -> ET.Element:
        """Serialize InvertCondition to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(InvertCondition, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize condition
        if self.condition is not None:
            serialized = SerializationHelper.serialize_item(self.condition, "AbstractCondition")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONDITION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "InvertCondition":
        """Deserialize XML element to InvertCondition object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized InvertCondition object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(InvertCondition, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CONDITION":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "AGGREGATION-CONDITION":
                        setattr(obj, "condition", SerializationHelper.deserialize_by_tag(child[0], "AggregationCondition"))
                    elif concrete_tag == "ATTRIBUTE-CONDITION":
                        setattr(obj, "condition", SerializationHelper.deserialize_by_tag(child[0], "AttributeCondition"))
                    elif concrete_tag == "INVERT-CONDITION":
                        setattr(obj, "condition", SerializationHelper.deserialize_by_tag(child[0], "InvertCondition"))
                    elif concrete_tag == "PRIMITIVE-ATTRIBUTE-CONDITION":
                        setattr(obj, "condition", SerializationHelper.deserialize_by_tag(child[0], "PrimitiveAttributeCondition"))
                    elif concrete_tag == "REFERENCE-CONDITION":
                        setattr(obj, "condition", SerializationHelper.deserialize_by_tag(child[0], "ReferenceCondition"))
                    elif concrete_tag == "TEXTUAL-CONDITION":
                        setattr(obj, "condition", SerializationHelper.deserialize_by_tag(child[0], "TextualCondition"))

        return obj



class InvertConditionBuilder(AbstractConditionBuilder):
    """Builder for InvertCondition with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: InvertCondition = InvertCondition()


    def with_condition(self, value: AbstractCondition) -> "InvertConditionBuilder":
        """Set condition attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute 'condition' is required and cannot be None")
        self._obj.condition = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _REQUIRED_ATTRIBUTES = {
        "condition",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Validate required attributes using pre-computed constants (O(1) lookup)
        # This is much faster than calling get_type_hints() at runtime
        if getattr(self._obj, "condition", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError("Required attribute 'condition' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn("Required attribute 'condition' is None", UserWarning)


    def build(self) -> InvertCondition:
        """Build and return the InvertCondition instance with validation."""
        self._validate_instance()
        return self._obj