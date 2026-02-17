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

    interpolation_routines: list[InterpolationRoutine]
    sw_record: Optional[SwRecordLayout]
    def __init__(self) -> None:
        """Initialize InterpolationRoutineMapping."""
        super().__init__()
        self.interpolation_routines: list[InterpolationRoutine] = []
        self.sw_record: Optional[SwRecordLayout] = None


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
