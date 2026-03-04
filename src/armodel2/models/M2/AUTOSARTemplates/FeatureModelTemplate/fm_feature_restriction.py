"""FMFeatureRestriction AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 32)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_FeatureModelTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class FMFeatureRestriction(Identifiable):
    """AUTOSAR FMFeatureRestriction."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "F-M-FEATURE-RESTRICTION"


    restriction_and_attributes: Optional[Any]
    _DESERIALIZE_DISPATCH = {
        "RESTRICTION-AND-ATTRIBUTES": lambda obj, elem: setattr(obj, "restriction_and_attributes", SerializationHelper.deserialize_by_tag(elem, "any (FMConditionByFeatures)")),
    }


    def __init__(self) -> None:
        """Initialize FMFeatureRestriction."""
        super().__init__()
        self.restriction_and_attributes: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize FMFeatureRestriction to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(FMFeatureRestriction, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize restriction_and_attributes
        if self.restriction_and_attributes is not None:
            serialized = SerializationHelper.serialize_item(self.restriction_and_attributes, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RESTRICTION-AND-ATTRIBUTES")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FMFeatureRestriction":
        """Deserialize XML element to FMFeatureRestriction object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FMFeatureRestriction object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(FMFeatureRestriction, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "RESTRICTION-AND-ATTRIBUTES":
                setattr(obj, "restriction_and_attributes", SerializationHelper.deserialize_by_tag(child, "any (FMConditionByFeatures)"))

        return obj



class FMFeatureRestrictionBuilder(IdentifiableBuilder):
    """Builder for FMFeatureRestriction with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: FMFeatureRestriction = FMFeatureRestriction()


    def with_restriction_and_attributes(self, value: Optional[any (FMConditionByFeatures)]) -> "FMFeatureRestrictionBuilder":
        """Set restriction_and_attributes attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.restriction_and_attributes = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "restrictionAndAttributes",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> FMFeatureRestriction:
        """Build and return the FMFeatureRestriction instance with validation."""
        self._validate_instance()
        return self._obj