"""InterpolationRoutineMappingSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 429)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 46)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_MeasurementAndCalibration_InterpolationRoutine.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.MeasurementAndCalibration.InterpolationRoutine.interpolation_routine import (
    InterpolationRoutine,
)


class InterpolationRoutineMappingSet(ARElement):
    """AUTOSAR InterpolationRoutineMappingSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    interpolation_routines: list[InterpolationRoutine]
    def __init__(self) -> None:
        """Initialize InterpolationRoutineMappingSet."""
        super().__init__()
        self.interpolation_routines: list[InterpolationRoutine] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "InterpolationRoutineMappingSet":
        """Deserialize XML element to InterpolationRoutineMappingSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized InterpolationRoutineMappingSet object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse interpolation_routines (list)
        obj.interpolation_routines = []
        for child in ARObject._find_all_child_elements(element, "INTERPOLATION-ROUTINES"):
            interpolation_routines_value = ARObject._deserialize_by_tag(child, "InterpolationRoutine")
            obj.interpolation_routines.append(interpolation_routines_value)

        return obj



class InterpolationRoutineMappingSetBuilder:
    """Builder for InterpolationRoutineMappingSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: InterpolationRoutineMappingSet = InterpolationRoutineMappingSet()

    def build(self) -> InterpolationRoutineMappingSet:
        """Build and return InterpolationRoutineMappingSet object.

        Returns:
            InterpolationRoutineMappingSet instance
        """
        # TODO: Add validation
        return self._obj
