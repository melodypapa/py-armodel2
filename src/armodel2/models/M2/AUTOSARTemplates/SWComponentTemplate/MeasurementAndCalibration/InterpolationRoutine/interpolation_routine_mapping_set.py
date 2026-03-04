"""InterpolationRoutineMappingSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 429)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 46)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_MeasurementAndCalibration_InterpolationRoutine.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.MeasurementAndCalibration.InterpolationRoutine.interpolation_routine import (
    InterpolationRoutine,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class InterpolationRoutineMappingSet(ARElement):
    """AUTOSAR InterpolationRoutineMappingSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "INTERPOLATION-ROUTINE-MAPPING-SET"


    interpolation_routines: list[InterpolationRoutine]
    _DESERIALIZE_DISPATCH = {
        "INTERPOLATION-ROUTINES": lambda obj, elem: obj.interpolation_routines.append(SerializationHelper.deserialize_by_tag(elem, "InterpolationRoutine")),
    }


    def __init__(self) -> None:
        """Initialize InterpolationRoutineMappingSet."""
        super().__init__()
        self.interpolation_routines: list[InterpolationRoutine] = []

    def serialize(self) -> ET.Element:
        """Serialize InterpolationRoutineMappingSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(InterpolationRoutineMappingSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize interpolation_routines (list to container "INTERPOLATION-ROUTINES")
        if self.interpolation_routines:
            wrapper = ET.Element("INTERPOLATION-ROUTINES")
            for item in self.interpolation_routines:
                serialized = SerializationHelper.serialize_item(item, "InterpolationRoutine")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "InterpolationRoutineMappingSet":
        """Deserialize XML element to InterpolationRoutineMappingSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized InterpolationRoutineMappingSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(InterpolationRoutineMappingSet, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "INTERPOLATION-ROUTINES":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.interpolation_routines.append(SerializationHelper.deserialize_by_tag(item_elem, "InterpolationRoutine"))

        return obj



class InterpolationRoutineMappingSetBuilder(ARElementBuilder):
    """Builder for InterpolationRoutineMappingSet with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: InterpolationRoutineMappingSet = InterpolationRoutineMappingSet()


    def with_interpolation_routines(self, items: list[InterpolationRoutine]) -> "InterpolationRoutineMappingSetBuilder":
        """Set interpolation_routines list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.interpolation_routines = list(items) if items else []
        return self


    def add_interpolation_routine(self, item: InterpolationRoutine) -> "InterpolationRoutineMappingSetBuilder":
        """Add a single item to interpolation_routines list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.interpolation_routines.append(item)
        return self

    def clear_interpolation_routines(self) -> "InterpolationRoutineMappingSetBuilder":
        """Clear all items from interpolation_routines list.

        Returns:
            self for method chaining
        """
        self._obj.interpolation_routines = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "interpolationRoutine",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> InterpolationRoutineMappingSet:
        """Build and return the InterpolationRoutineMappingSet instance with validation."""
        self._validate_instance()
        return self._obj