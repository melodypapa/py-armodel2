"""PhysicalDimensionMappingSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 399)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_Units.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.MSR.AsamHdo.Units.physical_dimension import (
    PhysicalDimension,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class PhysicalDimensionMappingSet(ARElement):
    """AUTOSAR PhysicalDimensionMappingSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "PHYSICAL-DIMENSION-MAPPING-SET"


    physicals: list[PhysicalDimension]
    _DESERIALIZE_DISPATCH = {
        "PHYSICALS": lambda obj, elem: obj.physicals.append(SerializationHelper.deserialize_by_tag(elem, "PhysicalDimension")),
    }


    def __init__(self) -> None:
        """Initialize PhysicalDimensionMappingSet."""
        super().__init__()
        self.physicals: list[PhysicalDimension] = []

    def serialize(self) -> ET.Element:
        """Serialize PhysicalDimensionMappingSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(PhysicalDimensionMappingSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize physicals (list to container "PHYSICALS")
        if self.physicals:
            wrapper = ET.Element("PHYSICALS")
            for item in self.physicals:
                serialized = SerializationHelper.serialize_item(item, "PhysicalDimension")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PhysicalDimensionMappingSet":
        """Deserialize XML element to PhysicalDimensionMappingSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PhysicalDimensionMappingSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PhysicalDimensionMappingSet, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "PHYSICALS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.physicals.append(SerializationHelper.deserialize_by_tag(item_elem, "PhysicalDimension"))

        return obj



class PhysicalDimensionMappingSetBuilder(ARElementBuilder):
    """Builder for PhysicalDimensionMappingSet with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: PhysicalDimensionMappingSet = PhysicalDimensionMappingSet()


    def with_physicals(self, items: list[PhysicalDimension]) -> "PhysicalDimensionMappingSetBuilder":
        """Set physicals list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.physicals = list(items) if items else []
        return self


    def add_physical(self, item: PhysicalDimension) -> "PhysicalDimensionMappingSetBuilder":
        """Add a single item to physicals list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.physicals.append(item)
        return self

    def clear_physicals(self) -> "PhysicalDimensionMappingSetBuilder":
        """Clear all items from physicals list.

        Returns:
            self for method chaining
        """
        self._obj.physicals = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "physical",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> PhysicalDimensionMappingSet:
        """Build and return the PhysicalDimensionMappingSet instance with validation."""
        self._validate_instance()
        return self._obj