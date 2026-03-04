"""SwSystemconstantValueSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 313)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 1007)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2069)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 246)
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 56)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 258)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_VariantHandling.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling.sw_systemconst_value import (
    SwSystemconstValue,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SwSystemconstantValueSet(ARElement):
    """AUTOSAR SwSystemconstantValueSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SW-SYSTEMCONSTANT-VALUE-SET"


    sws: list[SwSystemconstValue]
    _DESERIALIZE_DISPATCH = {
        "SWS": lambda obj, elem: obj.sws.append(SerializationHelper.deserialize_by_tag(elem, "SwSystemconstValue")),
    }


    def __init__(self) -> None:
        """Initialize SwSystemconstantValueSet."""
        super().__init__()
        self.sws: list[SwSystemconstValue] = []

    def serialize(self) -> ET.Element:
        """Serialize SwSystemconstantValueSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwSystemconstantValueSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize sws (list to container "SWS")
        if self.sws:
            wrapper = ET.Element("SWS")
            for item in self.sws:
                serialized = SerializationHelper.serialize_item(item, "SwSystemconstValue")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwSystemconstantValueSet":
        """Deserialize XML element to SwSystemconstantValueSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwSystemconstantValueSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwSystemconstantValueSet, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "SWS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.sws.append(SerializationHelper.deserialize_by_tag(item_elem, "SwSystemconstValue"))

        return obj



class SwSystemconstantValueSetBuilder(ARElementBuilder):
    """Builder for SwSystemconstantValueSet with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SwSystemconstantValueSet = SwSystemconstantValueSet()


    def with_sws(self, items: list[SwSystemconstValue]) -> "SwSystemconstantValueSetBuilder":
        """Set sws list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.sws = list(items) if items else []
        return self


    def add_sw(self, item: SwSystemconstValue) -> "SwSystemconstantValueSetBuilder":
        """Add a single item to sws list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.sws.append(item)
        return self

    def clear_sws(self) -> "SwSystemconstantValueSetBuilder":
        """Clear all items from sws list.

        Returns:
            self for method chaining
        """
        self._obj.sws = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
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


    def build(self) -> SwSystemconstantValueSet:
        """Build and return the SwSystemconstantValueSet instance with validation."""
        self._validate_instance()
        return self._obj