"""AggregationCondition AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 102)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint_Data.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.attribute_condition import (
    AttributeCondition,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.attribute_condition import AttributeConditionBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.aggregation_tailoring import (
    AggregationTailoring,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class AggregationCondition(AttributeCondition):
    """AUTOSAR AggregationCondition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "AGGREGATION-CONDITION"


    aggregation_ref: ARRef
    _DESERIALIZE_DISPATCH = {
        "AGGREGATION-REF": lambda obj, elem: setattr(obj, "aggregation_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize AggregationCondition."""
        super().__init__()
        self.aggregation_ref: ARRef = None

    def serialize(self) -> ET.Element:
        """Serialize AggregationCondition to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AggregationCondition, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize aggregation_ref
        if self.aggregation_ref is not None:
            serialized = SerializationHelper.serialize_item(self.aggregation_ref, "AggregationTailoring")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("AGGREGATION-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AggregationCondition":
        """Deserialize XML element to AggregationCondition object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AggregationCondition object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AggregationCondition, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "AGGREGATION-REF":
                setattr(obj, "aggregation_ref", ARRef.deserialize(child))

        return obj



class AggregationConditionBuilder(AttributeConditionBuilder):
    """Builder for AggregationCondition with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: AggregationCondition = AggregationCondition()


    def with_aggregation(self, value: AggregationTailoring) -> "AggregationConditionBuilder":
        """Set aggregation attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute 'aggregation' is required and cannot be None")
        self._obj.aggregation = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _REQUIRED_ATTRIBUTES = {
        "aggregation",
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
        if getattr(self._obj, "aggregation", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError("Required attribute 'aggregation' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn("Required attribute 'aggregation' is None", UserWarning)


    def build(self) -> AggregationCondition:
        """Build and return the AggregationCondition instance with validation."""
        self._validate_instance()
        return self._obj