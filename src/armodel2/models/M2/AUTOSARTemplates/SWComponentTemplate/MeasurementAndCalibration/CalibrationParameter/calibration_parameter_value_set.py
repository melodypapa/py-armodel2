"""CalibrationParameterValueSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 477)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_MeasurementAndCalibration_CalibrationParameter.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class CalibrationParameterValueSet(ARElement):
    """AUTOSAR CalibrationParameterValueSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "CALIBRATION-PARAMETER-VALUE-SET"


    calibrations: list[Any]
    _DESERIALIZE_DISPATCH = {
        "CALIBRATIONS": lambda obj, elem: obj.calibrations.append(SerializationHelper.deserialize_by_tag(elem, "any (CalibrationParameter)")),
    }


    def __init__(self) -> None:
        """Initialize CalibrationParameterValueSet."""
        super().__init__()
        self.calibrations: list[Any] = []

    def serialize(self) -> ET.Element:
        """Serialize CalibrationParameterValueSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CalibrationParameterValueSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize calibrations (list to container "CALIBRATIONS")
        if self.calibrations:
            wrapper = ET.Element("CALIBRATIONS")
            for item in self.calibrations:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CalibrationParameterValueSet":
        """Deserialize XML element to CalibrationParameterValueSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CalibrationParameterValueSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CalibrationParameterValueSet, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CALIBRATIONS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.calibrations.append(SerializationHelper.deserialize_by_tag(item_elem, "any (CalibrationParameter)"))

        return obj



class CalibrationParameterValueSetBuilder(ARElementBuilder):
    """Builder for CalibrationParameterValueSet with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: CalibrationParameterValueSet = CalibrationParameterValueSet()


    def with_calibrations(self, items: list[any (CalibrationParameter)]) -> "CalibrationParameterValueSetBuilder":
        """Set calibrations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.calibrations = list(items) if items else []
        return self


    def add_calibration(self, item: any (CalibrationParameter)) -> "CalibrationParameterValueSetBuilder":
        """Add a single item to calibrations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.calibrations.append(item)
        return self

    def clear_calibrations(self) -> "CalibrationParameterValueSetBuilder":
        """Clear all items from calibrations list.

        Returns:
            self for method chaining
        """
        self._obj.calibrations = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "calibration",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> CalibrationParameterValueSet:
        """Build and return the CalibrationParameterValueSet instance with validation."""
        self._validate_instance()
        return self._obj