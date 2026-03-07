"""PrimitiveAttributeCondition AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 104)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint_Data.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.attribute_condition import (
    AttributeCondition,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.attribute_condition import AttributeConditionBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class PrimitiveAttributeCondition(AttributeCondition):
    """AUTOSAR PrimitiveAttributeCondition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "PRIMITIVE-ATTRIBUTE-CONDITION"


    attribute_ref: Any
    _DESERIALIZE_DISPATCH = {
        "ATTRIBUTE-REF": lambda obj, elem: setattr(obj, "attribute_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize PrimitiveAttributeCondition."""
        super().__init__()
        self.attribute_ref: Any = None

    def serialize(self) -> ET.Element:
        """Serialize PrimitiveAttributeCondition to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(PrimitiveAttributeCondition, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize attribute_ref
        if self.attribute_ref is not None:
            serialized = SerializationHelper.serialize_item(self.attribute_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ATTRIBUTE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PrimitiveAttributeCondition":
        """Deserialize XML element to PrimitiveAttributeCondition object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PrimitiveAttributeCondition object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PrimitiveAttributeCondition, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ATTRIBUTE-REF":
                setattr(obj, "attribute_ref", ARRef.deserialize(child))

        return obj



class PrimitiveAttributeConditionBuilder(AttributeConditionBuilder):
    """Builder for PrimitiveAttributeCondition with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: PrimitiveAttributeCondition = PrimitiveAttributeCondition()


    def with_attribute(self, value: Any) -> "PrimitiveAttributeConditionBuilder":
        """Set attribute attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute 'attribute' is required and cannot be None")
        self._obj.attribute = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _REQUIRED_ATTRIBUTES = {
        "attribute",
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
        if getattr(self._obj, "attribute", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError("Required attribute 'attribute' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn("Required attribute 'attribute' is None", UserWarning)


    def build(self) -> PrimitiveAttributeCondition:
        """Build and return the PrimitiveAttributeCondition instance with validation."""
        self._validate_instance()
        return self._obj