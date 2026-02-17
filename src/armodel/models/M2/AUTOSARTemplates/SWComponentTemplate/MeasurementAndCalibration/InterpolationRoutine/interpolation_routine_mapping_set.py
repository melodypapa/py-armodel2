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
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.MeasurementAndCalibration.InterpolationRoutine.interpolation_routine import (
    InterpolationRoutine,
)


class InterpolationRoutineMappingSet(ARElement):
    """AUTOSAR InterpolationRoutineMappingSet."""

    interpolation_routines: list[InterpolationRoutine]
    def __init__(self) -> None:
        """Initialize InterpolationRoutineMappingSet."""
        super().__init__()
        self.interpolation_routines: list[InterpolationRoutine] = []


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
