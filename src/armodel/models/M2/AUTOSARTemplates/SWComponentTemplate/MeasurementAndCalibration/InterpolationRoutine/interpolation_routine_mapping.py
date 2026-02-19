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
    def serialize(self) -> ET.Element:
        """Serialize InterpolationRoutineMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize interpolation_routines (list to container "INTERPOLATION-ROUTINES")
        if self.interpolation_routines:
            wrapper = ET.Element("INTERPOLATION-ROUTINES")
            for item in self.interpolation_routines:
                serialized = ARObject._serialize_item(item, "InterpolationRoutine")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize sw_record
        if self.sw_record is not None:
            serialized = ARObject._serialize_item(self.sw_record, "SwRecordLayout")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-RECORD")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

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

        # Parse interpolation_routines (list from container "INTERPOLATION-ROUTINES")
        obj.interpolation_routines = []
        container = ARObject._find_child_element(element, "INTERPOLATION-ROUTINES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.interpolation_routines.append(child_value)

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
