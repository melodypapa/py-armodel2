"""ExclusiveAreaNestingOrder AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 84)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 554)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_InternalBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import ReferrableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.exclusive_area import (
    ExclusiveArea,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ExclusiveAreaNestingOrder(Referrable):
    """AUTOSAR ExclusiveAreaNestingOrder."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "EXCLUSIVE-AREA-NESTING-ORDER"


    exclusive_area_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "EXCLUSIVE-AREA-REFS": lambda obj, elem: [obj.exclusive_area_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
    }


    def __init__(self) -> None:
        """Initialize ExclusiveAreaNestingOrder."""
        super().__init__()
        self.exclusive_area_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize ExclusiveAreaNestingOrder to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ExclusiveAreaNestingOrder, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize exclusive_area_refs (list to container "EXCLUSIVE-AREA-REFS")
        if self.exclusive_area_refs:
            wrapper = ET.Element("EXCLUSIVE-AREA-REFS")
            for item in self.exclusive_area_refs:
                serialized = SerializationHelper.serialize_item(item, "ExclusiveArea")
                if serialized is not None:
                    child_elem = ET.Element("EXCLUSIVE-AREA-REF")
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
    def deserialize(cls, element: ET.Element) -> "ExclusiveAreaNestingOrder":
        """Deserialize XML element to ExclusiveAreaNestingOrder object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ExclusiveAreaNestingOrder object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ExclusiveAreaNestingOrder, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "EXCLUSIVE-AREA-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.exclusive_area_refs.append(ARRef.deserialize(item_elem))

        return obj



class ExclusiveAreaNestingOrderBuilder(ReferrableBuilder):
    """Builder for ExclusiveAreaNestingOrder with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ExclusiveAreaNestingOrder = ExclusiveAreaNestingOrder()


    def with_exclusive_areas(self, items: list[ExclusiveArea]) -> "ExclusiveAreaNestingOrderBuilder":
        """Set exclusive_areas list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.exclusive_areas = list(items) if items else []
        return self


    def add_exclusive_area(self, item: ExclusiveArea) -> "ExclusiveAreaNestingOrderBuilder":
        """Add a single item to exclusive_areas list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.exclusive_areas.append(item)
        return self

    def clear_exclusive_areas(self) -> "ExclusiveAreaNestingOrderBuilder":
        """Clear all items from exclusive_areas list.

        Returns:
            self for method chaining
        """
        self._obj.exclusive_areas = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "exclusiveArea",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> ExclusiveAreaNestingOrder:
        """Build and return the ExclusiveAreaNestingOrder instance with validation."""
        self._validate_instance()
        return self._obj