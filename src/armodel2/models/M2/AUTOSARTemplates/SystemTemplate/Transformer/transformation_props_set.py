"""TransformationPropsSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 782)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.transformation_props import (
    TransformationProps,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class TransformationPropsSet(ARElement):
    """AUTOSAR TransformationPropsSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "TRANSFORMATION-PROPS-SET"


    transformation_props_propses: list[TransformationProps]
    _DESERIALIZE_DISPATCH = {
        "TRANSFORMATION-PROPS-PROPSS": ("_POLYMORPHIC_LIST", "transformation_props_propses", ["SOMEIPTransformationProps", "UserDefinedTransformationProps"]),
    }


    def __init__(self) -> None:
        """Initialize TransformationPropsSet."""
        super().__init__()
        self.transformation_props_propses: list[TransformationProps] = []

    def serialize(self) -> ET.Element:
        """Serialize TransformationPropsSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TransformationPropsSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize transformation_props_propses (list to container "TRANSFORMATION-PROPS-PROPSS")
        if self.transformation_props_propses:
            wrapper = ET.Element("TRANSFORMATION-PROPS-PROPSS")
            for item in self.transformation_props_propses:
                serialized = SerializationHelper.serialize_item(item, "TransformationProps")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TransformationPropsSet":
        """Deserialize XML element to TransformationPropsSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TransformationPropsSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TransformationPropsSet, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "TRANSFORMATION-PROPS-PROPSS":
                # Iterate through all child elements and deserialize each based on its concrete type
                for item_elem in child:
                    concrete_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    if concrete_tag == "S-O-M-E-I-P-TRANSFORMATION-PROPS":
                        obj.transformation_props_propses.append(SerializationHelper.deserialize_by_tag(item_elem, "SOMEIPTransformationProps"))
                    elif concrete_tag == "USER-DEFINED-TRANSFORMATION-PROPS":
                        obj.transformation_props_propses.append(SerializationHelper.deserialize_by_tag(item_elem, "UserDefinedTransformationProps"))

        return obj



class TransformationPropsSetBuilder(ARElementBuilder):
    """Builder for TransformationPropsSet with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TransformationPropsSet = TransformationPropsSet()


    def with_transformation_props_propses(self, items: list[TransformationProps]) -> "TransformationPropsSetBuilder":
        """Set transformation_props_propses list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.transformation_props_propses = list(items) if items else []
        return self


    def add_transformation_props_props(self, item: TransformationProps) -> "TransformationPropsSetBuilder":
        """Add a single item to transformation_props_propses list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.transformation_props_propses.append(item)
        return self

    def clear_transformation_props_propses(self) -> "TransformationPropsSetBuilder":
        """Clear all items from transformation_props_propses list.

        Returns:
            self for method chaining
        """
        self._obj.transformation_props_propses = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "transformationPropsProps",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> TransformationPropsSet:
        """Build and return the TransformationPropsSet instance with validation."""
        self._validate_instance()
        return self._obj