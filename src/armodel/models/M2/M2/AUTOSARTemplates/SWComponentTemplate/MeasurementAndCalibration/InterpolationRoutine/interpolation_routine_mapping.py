"""InterpolationRoutineMapping AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.MeasurementAndCalibration.InterpolationRoutine.interpolation_routine import (
    InterpolationRoutine,
)
from armodel.models.M2.MSR.DataDictionary.RecordLayout.sw_record_layout import (
    SwRecordLayout,
)


class InterpolationRoutineMapping(ARObject):
    """AUTOSAR InterpolationRoutineMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "interpolation_routines": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=InterpolationRoutine,
        ),  # interpolationRoutines
        "sw_record": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SwRecordLayout,
        ),  # swRecord
    }

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
