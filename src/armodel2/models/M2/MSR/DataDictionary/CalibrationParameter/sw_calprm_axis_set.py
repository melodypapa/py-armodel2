"""SwCalprmAxisSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 351)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_CalibrationParameter.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.MSR.DataDictionary.CalibrationParameter.sw_calprm_axis import (
    SwCalprmAxis,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SwCalprmAxisSet(ARObject):
    """AUTOSAR SwCalprmAxisSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SW-CALPRM-AXIS-SET"


    sw_calprm_axises: list[SwCalprmAxis]
    _DESERIALIZE_DISPATCH = {
        "SW-CALPRM-AXISS": lambda obj, elem: obj.sw_calprm_axises.append(SerializationHelper.deserialize_by_tag(elem, "SwCalprmAxis")),
    }


    def __init__(self) -> None:
        """Initialize SwCalprmAxisSet."""
        super().__init__()
        self.sw_calprm_axises: list[SwCalprmAxis] = []

    def serialize(self) -> ET.Element:
        """Serialize SwCalprmAxisSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwCalprmAxisSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize sw_calprm_axises (list to container "SW-CALPRM-AXISS")
        if self.sw_calprm_axises:
            wrapper = ET.Element("SW-CALPRM-AXISS")
            for item in self.sw_calprm_axises:
                serialized = SerializationHelper.serialize_item(item, "SwCalprmAxis")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwCalprmAxisSet":
        """Deserialize XML element to SwCalprmAxisSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwCalprmAxisSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwCalprmAxisSet, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "SW-CALPRM-AXISS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.sw_calprm_axises.append(SerializationHelper.deserialize_by_tag(item_elem, "SwCalprmAxis"))

        return obj



class SwCalprmAxisSetBuilder(BuilderBase):
    """Builder for SwCalprmAxisSet with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SwCalprmAxisSet = SwCalprmAxisSet()


    def with_sw_calprm_axises(self, items: list[SwCalprmAxis]) -> "SwCalprmAxisSetBuilder":
        """Set sw_calprm_axises list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.sw_calprm_axises = list(items) if items else []
        return self


    def add_sw_calprm_axis(self, item: SwCalprmAxis) -> "SwCalprmAxisSetBuilder":
        """Add a single item to sw_calprm_axises list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.sw_calprm_axises.append(item)
        return self

    def clear_sw_calprm_axises(self) -> "SwCalprmAxisSetBuilder":
        """Clear all items from sw_calprm_axises list.

        Returns:
            self for method chaining
        """
        self._obj.sw_calprm_axises = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "swCalprmAxis",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> SwCalprmAxisSet:
        """Build and return the SwCalprmAxisSet instance with validation."""
        self._validate_instance()
        return self._obj