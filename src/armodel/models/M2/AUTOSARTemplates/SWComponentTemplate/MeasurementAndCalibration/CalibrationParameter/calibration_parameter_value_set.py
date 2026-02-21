"""CalibrationParameterValueSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 477)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_MeasurementAndCalibration_CalibrationParameter.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class CalibrationParameterValueSet(ARElement):
    """AUTOSAR CalibrationParameterValueSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    calibrations: list[Any]
    def __init__(self) -> None:
        """Initialize CalibrationParameterValueSet."""
        super().__init__()
        self.calibrations: list[Any] = []

    def serialize(self) -> ET.Element:
        """Serialize CalibrationParameterValueSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

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
                serialized = ARObject._serialize_item(item, "Any")
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

        # Parse calibrations (list from container "CALIBRATIONS")
        obj.calibrations = []
        container = ARObject._find_child_element(element, "CALIBRATIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.calibrations.append(child_value)

        return obj



class CalibrationParameterValueSetBuilder:
    """Builder for CalibrationParameterValueSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CalibrationParameterValueSet = CalibrationParameterValueSet()

    def build(self) -> CalibrationParameterValueSet:
        """Build and return CalibrationParameterValueSet object.

        Returns:
            CalibrationParameterValueSet instance
        """
        # TODO: Add validation
        return self._obj
