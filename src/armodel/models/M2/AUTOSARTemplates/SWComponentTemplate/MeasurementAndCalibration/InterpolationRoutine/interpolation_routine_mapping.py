"""InterpolationRoutineMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 430)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 46)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_MeasurementAndCalibration_InterpolationRoutine.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.MeasurementAndCalibration.InterpolationRoutine.interpolation_routine import (
    InterpolationRoutine,
)
from armodel.models.M2.MSR.DataDictionary.RecordLayout.sw_record_layout import (
    SwRecordLayout,
)


class InterpolationRoutineMapping(ARObject):
    """AUTOSAR InterpolationRoutineMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    interpolation_routines: list[InterpolationRoutine]
    sw_record: Optional[SwRecordLayout]
    def __init__(self) -> None:
        """Initialize InterpolationRoutineMapping."""
        super().__init__()
        self.interpolation_routines: list[InterpolationRoutine] = []
        self.sw_record: Optional[SwRecordLayout] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "InterpolationRoutineMapping":
        """Deserialize XML element to InterpolationRoutineMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized InterpolationRoutineMapping object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse interpolation_routines (list)
        obj.interpolation_routines = []
        for child in ARObject._find_all_child_elements(element, "INTERPOLATION-ROUTINES"):
            interpolation_routines_value = ARObject._deserialize_by_tag(child, "InterpolationRoutine")
            obj.interpolation_routines.append(interpolation_routines_value)

        # Parse sw_record
        child = ARObject._find_child_element(element, "SW-RECORD")
        if child is not None:
            sw_record_value = ARObject._deserialize_by_tag(child, "SwRecordLayout")
            obj.sw_record = sw_record_value

        return obj



class InterpolationRoutineMappingBuilder:
    """Builder for InterpolationRoutineMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: InterpolationRoutineMapping = InterpolationRoutineMapping()

    def build(self) -> InterpolationRoutineMapping:
        """Build and return InterpolationRoutineMapping object.

        Returns:
            InterpolationRoutineMapping instance
        """
        # TODO: Add validation
        return self._obj
