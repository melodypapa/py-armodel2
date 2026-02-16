"""InterpolationRoutineMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
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
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("interpolation_routines", None, False, True, InterpolationRoutine),  # interpolationRoutines
        ("sw_record", None, False, False, SwRecordLayout),  # swRecord
    ]

    def __init__(self) -> None:
        """Initialize InterpolationRoutineMapping."""
        super().__init__()
        self.interpolation_routines: list[InterpolationRoutine] = []
        self.sw_record: Optional[SwRecordLayout] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert InterpolationRoutineMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "InterpolationRoutineMapping":
        """Create InterpolationRoutineMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            InterpolationRoutineMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to InterpolationRoutineMapping since parent returns ARObject
        return cast("InterpolationRoutineMapping", obj)


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
