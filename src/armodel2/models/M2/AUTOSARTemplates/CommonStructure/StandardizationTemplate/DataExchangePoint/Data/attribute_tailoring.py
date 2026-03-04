"""AttributeTailoring AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 109)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint_Data.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.data_format_element_scope import (
    DataFormatElementScope,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.data_format_element_scope import DataFormatElementScopeBuilder
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.variation_restriction_with_severity import (
    VariationRestrictionWithSeverity,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class AttributeTailoring(DataFormatElementScope, ABC):
    """AUTOSAR AttributeTailoring."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    multiplicity: Optional[Any]
    variation: Optional[VariationRestrictionWithSeverity]
    _DESERIALIZE_DISPATCH = {
        "MULTIPLICITY": lambda obj, elem: setattr(obj, "multiplicity", SerializationHelper.deserialize_by_tag(elem, "any (MultiplicityRestriction)")),
        "VARIATION": lambda obj, elem: setattr(obj, "variation", SerializationHelper.deserialize_by_tag(elem, "VariationRestrictionWithSeverity")),
    }


    def __init__(self) -> None:
        """Initialize AttributeTailoring."""
        super().__init__()
        self.multiplicity: Optional[Any] = None
        self.variation: Optional[VariationRestrictionWithSeverity] = None

    def serialize(self) -> ET.Element:
        """Serialize AttributeTailoring to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AttributeTailoring, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize multiplicity
        if self.multiplicity is not None:
            serialized = SerializationHelper.serialize_item(self.multiplicity, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MULTIPLICITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize variation
        if self.variation is not None:
            serialized = SerializationHelper.serialize_item(self.variation, "VariationRestrictionWithSeverity")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VARIATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AttributeTailoring":
        """Deserialize XML element to AttributeTailoring object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AttributeTailoring object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AttributeTailoring, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "MULTIPLICITY":
                setattr(obj, "multiplicity", SerializationHelper.deserialize_by_tag(child, "any (MultiplicityRestriction)"))
            elif tag == "VARIATION":
                setattr(obj, "variation", SerializationHelper.deserialize_by_tag(child, "VariationRestrictionWithSeverity"))

        return obj



class AttributeTailoringBuilder(DataFormatElementScopeBuilder):
    """Builder for AttributeTailoring with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: AttributeTailoring = AttributeTailoring()


    def with_multiplicity(self, value: Optional[any (MultiplicityRestriction)]) -> "AttributeTailoringBuilder":
        """Set multiplicity attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.multiplicity = value
        return self

    def with_variation(self, value: Optional[VariationRestrictionWithSeverity]) -> "AttributeTailoringBuilder":
        """Set variation attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.variation = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "multiplicity",
        "variation",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    @abstractmethod
    def build(self) -> AttributeTailoring:
        """Build and return the AttributeTailoring instance (abstract)."""
        raise NotImplementedError