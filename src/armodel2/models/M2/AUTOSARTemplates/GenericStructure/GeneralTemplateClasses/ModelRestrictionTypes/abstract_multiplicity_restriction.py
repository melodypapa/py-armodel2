"""AbstractMultiplicityRestriction AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 422)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 88)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_ModelRestrictionTypes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class AbstractMultiplicityRestriction(ARObject, ABC):
    """AUTOSAR AbstractMultiplicityRestriction."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    lower_multiplicity: Optional[PositiveInteger]
    upper_multiplicity: Optional[Boolean]
    _DESERIALIZE_DISPATCH = {
        "LOWER-MULTIPLICITY": lambda obj, elem: setattr(obj, "lower_multiplicity", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "UPPER-MULTIPLICITY": lambda obj, elem: setattr(obj, "upper_multiplicity", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
    }


    def __init__(self) -> None:
        """Initialize AbstractMultiplicityRestriction."""
        super().__init__()
        self.lower_multiplicity: Optional[PositiveInteger] = None
        self.upper_multiplicity: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize AbstractMultiplicityRestriction to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AbstractMultiplicityRestriction, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize lower_multiplicity
        if self.lower_multiplicity is not None:
            serialized = SerializationHelper.serialize_item(self.lower_multiplicity, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LOWER-MULTIPLICITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize upper_multiplicity
        if self.upper_multiplicity is not None:
            serialized = SerializationHelper.serialize_item(self.upper_multiplicity, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("UPPER-MULTIPLICITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AbstractMultiplicityRestriction":
        """Deserialize XML element to AbstractMultiplicityRestriction object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AbstractMultiplicityRestriction object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AbstractMultiplicityRestriction, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "LOWER-MULTIPLICITY":
                setattr(obj, "lower_multiplicity", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "UPPER-MULTIPLICITY":
                setattr(obj, "upper_multiplicity", SerializationHelper.deserialize_by_tag(child, "Boolean"))

        return obj



class AbstractMultiplicityRestrictionBuilder(BuilderBase, ABC):
    """Builder for AbstractMultiplicityRestriction with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: AbstractMultiplicityRestriction = AbstractMultiplicityRestriction()


    def with_lower_multiplicity(self, value: Optional[PositiveInteger]) -> "AbstractMultiplicityRestrictionBuilder":
        """Set lower_multiplicity attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'lower_multiplicity' is required and cannot be None")
        self._obj.lower_multiplicity = value
        return self

    def with_upper_multiplicity(self, value: Optional[Boolean]) -> "AbstractMultiplicityRestrictionBuilder":
        """Set upper_multiplicity attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'upper_multiplicity' is required and cannot be None")
        self._obj.upper_multiplicity = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "lowerMultiplicity",
        "upperMultiplicity",
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
    def build(self) -> AbstractMultiplicityRestriction:
        """Build and return the AbstractMultiplicityRestriction instance (abstract)."""
        raise NotImplementedError