"""UnitGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 314)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 402)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_Units.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.MSR.AsamHdo.Units.unit import (
    Unit,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class UnitGroup(ARElement):
    """AUTOSAR UnitGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "UNIT-GROUP"


    unit_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "UNIT-REFS": lambda obj, elem: [obj.unit_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
    }


    def __init__(self) -> None:
        """Initialize UnitGroup."""
        super().__init__()
        self.unit_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize UnitGroup to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(UnitGroup, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize unit_refs (list to container "UNIT-REFS")
        if self.unit_refs:
            wrapper = ET.Element("UNIT-REFS")
            for item in self.unit_refs:
                serialized = SerializationHelper.serialize_item(item, "Unit")
                if serialized is not None:
                    child_elem = ET.Element("UNIT-REF")
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
    def deserialize(cls, element: ET.Element) -> "UnitGroup":
        """Deserialize XML element to UnitGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized UnitGroup object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(UnitGroup, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "UNIT-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.unit_refs.append(ARRef.deserialize(item_elem))

        return obj



class UnitGroupBuilder(ARElementBuilder):
    """Builder for UnitGroup with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: UnitGroup = UnitGroup()


    def with_units(self, items: list[Unit]) -> "UnitGroupBuilder":
        """Set units list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.units = list(items) if items else []
        return self


    def add_unit(self, item: Unit) -> "UnitGroupBuilder":
        """Add a single item to units list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.units.append(item)
        return self

    def clear_units(self) -> "UnitGroupBuilder":
        """Clear all items from units list.

        Returns:
            self for method chaining
        """
        self._obj.units = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "unit",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> UnitGroup:
        """Build and return the UnitGroup instance with validation."""
        self._validate_instance()
        return self._obj