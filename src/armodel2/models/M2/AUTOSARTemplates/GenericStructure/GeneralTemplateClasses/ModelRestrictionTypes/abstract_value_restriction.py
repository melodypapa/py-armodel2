"""AbstractValueRestriction AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 103)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 87)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_ModelRestrictionTypes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Limit,
    PositiveInteger,
    RegularExpression,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class AbstractValueRestriction(ARObject, ABC):
    """AUTOSAR AbstractValueRestriction."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    max: Optional[Limit]
    max_length: Optional[PositiveInteger]
    min: Optional[Limit]
    min_length: Optional[PositiveInteger]
    pattern: Optional[RegularExpression]
    _DESERIALIZE_DISPATCH = {
        "MAX": lambda obj, elem: setattr(obj, "max", SerializationHelper.deserialize_by_tag(elem, "Limit")),
        "MAX-LENGTH": lambda obj, elem: setattr(obj, "max_length", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "MIN": lambda obj, elem: setattr(obj, "min", SerializationHelper.deserialize_by_tag(elem, "Limit")),
        "MIN-LENGTH": lambda obj, elem: setattr(obj, "min_length", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "PATTERN": lambda obj, elem: setattr(obj, "pattern", SerializationHelper.deserialize_by_tag(elem, "RegularExpression")),
    }


    def __init__(self) -> None:
        """Initialize AbstractValueRestriction."""
        super().__init__()
        self.max: Optional[Limit] = None
        self.max_length: Optional[PositiveInteger] = None
        self.min: Optional[Limit] = None
        self.min_length: Optional[PositiveInteger] = None
        self.pattern: Optional[RegularExpression] = None

    def serialize(self) -> ET.Element:
        """Serialize AbstractValueRestriction to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AbstractValueRestriction, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize max
        if self.max is not None:
            serialized = SerializationHelper.serialize_item(self.max, "Limit")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_length
        if self.max_length is not None:
            serialized = SerializationHelper.serialize_item(self.max_length, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-LENGTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize min
        if self.min is not None:
            serialized = SerializationHelper.serialize_item(self.min, "Limit")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MIN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize min_length
        if self.min_length is not None:
            serialized = SerializationHelper.serialize_item(self.min_length, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MIN-LENGTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize pattern
        if self.pattern is not None:
            serialized = SerializationHelper.serialize_item(self.pattern, "RegularExpression")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PATTERN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AbstractValueRestriction":
        """Deserialize XML element to AbstractValueRestriction object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AbstractValueRestriction object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AbstractValueRestriction, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "MAX":
                setattr(obj, "max", SerializationHelper.deserialize_by_tag(child, "Limit"))
            elif tag == "MAX-LENGTH":
                setattr(obj, "max_length", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "MIN":
                setattr(obj, "min", SerializationHelper.deserialize_by_tag(child, "Limit"))
            elif tag == "MIN-LENGTH":
                setattr(obj, "min_length", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "PATTERN":
                setattr(obj, "pattern", SerializationHelper.deserialize_by_tag(child, "RegularExpression"))

        return obj



class AbstractValueRestrictionBuilder(BuilderBase, ABC):
    """Builder for AbstractValueRestriction with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: AbstractValueRestriction = AbstractValueRestriction()


    def with_max(self, value: Optional[Limit]) -> "AbstractValueRestrictionBuilder":
        """Set max attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.max = value
        return self

    def with_max_length(self, value: Optional[PositiveInteger]) -> "AbstractValueRestrictionBuilder":
        """Set max_length attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.max_length = value
        return self

    def with_min(self, value: Optional[Limit]) -> "AbstractValueRestrictionBuilder":
        """Set min attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.min = value
        return self

    def with_min_length(self, value: Optional[PositiveInteger]) -> "AbstractValueRestrictionBuilder":
        """Set min_length attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.min_length = value
        return self

    def with_pattern(self, value: Optional[RegularExpression]) -> "AbstractValueRestrictionBuilder":
        """Set pattern attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.pattern = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "max",
        "maxLength",
        "min",
        "minLength",
        "pattern",
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
    def build(self) -> AbstractValueRestriction:
        """Build and return the AbstractValueRestriction instance (abstract)."""
        raise NotImplementedError