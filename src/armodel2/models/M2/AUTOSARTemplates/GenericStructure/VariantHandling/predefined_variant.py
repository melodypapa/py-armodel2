"""PredefinedVariant AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 305)
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 77)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 257)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_VariantHandling.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling.sw_systemconstant_value_set import (
    SwSystemconstantValueSet,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class PredefinedVariant(ARElement):
    """AUTOSAR PredefinedVariant."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "PREDEFINED-VARIANT"


    included_variant_refs: list[ARRef]
    post_build_variant_refs: list[Any]
    sw_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "INCLUDED-VARIANT-REFS": lambda obj, elem: [obj.included_variant_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
        "POST-BUILD-VARIANT-REFS": lambda obj, elem: [obj.post_build_variant_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
        "SW-REFS": lambda obj, elem: [obj.sw_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
    }


    def __init__(self) -> None:
        """Initialize PredefinedVariant."""
        super().__init__()
        self.included_variant_refs: list[ARRef] = []
        self.post_build_variant_refs: list[Any] = []
        self.sw_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize PredefinedVariant to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(PredefinedVariant, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize included_variant_refs (list to container "INCLUDED-VARIANT-REFS")
        if self.included_variant_refs:
            wrapper = ET.Element("INCLUDED-VARIANT-REFS")
            for item in self.included_variant_refs:
                serialized = SerializationHelper.serialize_item(item, "PredefinedVariant")
                if serialized is not None:
                    child_elem = ET.Element("INCLUDED-VARIANT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize post_build_variant_refs (list to container "POST-BUILD-VARIANT-REFS")
        if self.post_build_variant_refs:
            wrapper = ET.Element("POST-BUILD-VARIANT-REFS")
            for item in self.post_build_variant_refs:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    child_elem = ET.Element("POST-BUILD-VARIANT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize sw_refs (list to container "SW-REFS")
        if self.sw_refs:
            wrapper = ET.Element("SW-REFS")
            for item in self.sw_refs:
                serialized = SerializationHelper.serialize_item(item, "SwSystemconstantValueSet")
                if serialized is not None:
                    child_elem = ET.Element("SW-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PredefinedVariant":
        """Deserialize XML element to PredefinedVariant object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PredefinedVariant object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PredefinedVariant, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "INCLUDED-VARIANT-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.included_variant_refs.append(ARRef.deserialize(item_elem))
            elif tag == "POST-BUILD-VARIANT-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.post_build_variant_refs.append(ARRef.deserialize(item_elem))
            elif tag == "SW-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.sw_refs.append(ARRef.deserialize(item_elem))

        return obj



class PredefinedVariantBuilder(ARElementBuilder):
    """Builder for PredefinedVariant with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: PredefinedVariant = PredefinedVariant()


    def with_included_variants(self, items: list[PredefinedVariant]) -> "PredefinedVariantBuilder":
        """Set included_variants list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.included_variants = list(items) if items else []
        return self

    def with_post_build_variants(self, items: list[any (PostBuildVariant)]) -> "PredefinedVariantBuilder":
        """Set post_build_variants list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.post_build_variants = list(items) if items else []
        return self

    def with_sws(self, items: list[SwSystemconstantValueSet]) -> "PredefinedVariantBuilder":
        """Set sws list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.sws = list(items) if items else []
        return self


    def add_included_variant(self, item: PredefinedVariant) -> "PredefinedVariantBuilder":
        """Add a single item to included_variants list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.included_variants.append(item)
        return self

    def clear_included_variants(self) -> "PredefinedVariantBuilder":
        """Clear all items from included_variants list.

        Returns:
            self for method chaining
        """
        self._obj.included_variants = []
        return self

    def add_post_build_variant(self, item: any (PostBuildVariant)) -> "PredefinedVariantBuilder":
        """Add a single item to post_build_variants list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.post_build_variants.append(item)
        return self

    def clear_post_build_variants(self) -> "PredefinedVariantBuilder":
        """Clear all items from post_build_variants list.

        Returns:
            self for method chaining
        """
        self._obj.post_build_variants = []
        return self

    def add_sw(self, item: SwSystemconstantValueSet) -> "PredefinedVariantBuilder":
        """Add a single item to sws list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.sws.append(item)
        return self

    def clear_sws(self) -> "PredefinedVariantBuilder":
        """Clear all items from sws list.

        Returns:
            self for method chaining
        """
        self._obj.sws = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "includedVariant",
        "postBuildVariant",
        "sw",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> PredefinedVariant:
        """Build and return the PredefinedVariant instance with validation."""
        self._validate_instance()
        return self._obj