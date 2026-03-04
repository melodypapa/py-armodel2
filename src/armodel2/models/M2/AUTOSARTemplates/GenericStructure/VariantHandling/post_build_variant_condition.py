"""PostBuildVariantCondition AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 614)
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 76)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 232)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_VariantHandling.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class PostBuildVariantCondition(ARObject):
    """AUTOSAR PostBuildVariantCondition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "POST-BUILD-VARIANT-CONDITION"


    matching_ref: Any
    value: Integer
    _DESERIALIZE_DISPATCH = {
        "MATCHING-REF": lambda obj, elem: setattr(obj, "matching_ref", ARRef.deserialize(elem)),
        "VALUE": lambda obj, elem: setattr(obj, "value", SerializationHelper.deserialize_by_tag(elem, "Integer")),
    }


    def __init__(self) -> None:
        """Initialize PostBuildVariantCondition."""
        super().__init__()
        self.matching_ref: Any = None
        self.value: Integer = None

    def serialize(self) -> ET.Element:
        """Serialize PostBuildVariantCondition to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(PostBuildVariantCondition, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize matching_ref
        if self.matching_ref is not None:
            serialized = SerializationHelper.serialize_item(self.matching_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MATCHING-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize value
        if self.value is not None:
            serialized = SerializationHelper.serialize_item(self.value, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VALUE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PostBuildVariantCondition":
        """Deserialize XML element to PostBuildVariantCondition object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PostBuildVariantCondition object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PostBuildVariantCondition, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "MATCHING-REF":
                setattr(obj, "matching_ref", ARRef.deserialize(child))
            elif tag == "VALUE":
                setattr(obj, "value", SerializationHelper.deserialize_by_tag(child, "Integer"))

        return obj



class PostBuildVariantConditionBuilder(BuilderBase):
    """Builder for PostBuildVariantCondition with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: PostBuildVariantCondition = PostBuildVariantCondition()


    def with_matching(self, value: any (PostBuildVariant)) -> "PostBuildVariantConditionBuilder":
        """Set matching attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.matching = value
        return self

    def with_value(self, value: Integer) -> "PostBuildVariantConditionBuilder":
        """Set value attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.value = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _REQUIRED_ATTRIBUTES = {
        "matching",
        "value",
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
        if getattr(self._obj, "matching", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError("Required attribute 'matching' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn("Required attribute 'matching' is None", UserWarning)
        if getattr(self._obj, "value", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError("Required attribute 'value' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn("Required attribute 'value' is None", UserWarning)


    def build(self) -> PostBuildVariantCondition:
        """Build and return the PostBuildVariantCondition instance with validation."""
        self._validate_instance()
        return self._obj