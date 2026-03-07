"""InterpolationRoutineMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 430)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 46)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_MeasurementAndCalibration_InterpolationRoutine.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.MeasurementAndCalibration.InterpolationRoutine.interpolation_routine import (
    InterpolationRoutine,
)
from armodel2.models.M2.MSR.DataDictionary.RecordLayout.sw_record_layout import (
    SwRecordLayout,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class InterpolationRoutineMapping(ARObject):
    """AUTOSAR InterpolationRoutineMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "INTERPOLATION-ROUTINE-MAPPING"


    interpolation_routines: list[InterpolationRoutine]
    sw_record_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "INTERPOLATION-ROUTINES": lambda obj, elem: obj.interpolation_routines.append(SerializationHelper.deserialize_by_tag(elem, "InterpolationRoutine")),
        "SW-RECORD-REF": lambda obj, elem: setattr(obj, "sw_record_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize InterpolationRoutineMapping."""
        super().__init__()
        self.interpolation_routines: list[InterpolationRoutine] = []
        self.sw_record_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize InterpolationRoutineMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(InterpolationRoutineMapping, self).serialize()

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

        # Serialize sw_record_ref
        if self.sw_record_ref is not None:
            serialized = SerializationHelper.serialize_item(self.sw_record_ref, "SwRecordLayout")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-RECORD-REF")
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
        # First, call parent's deserialize to handle inherited attributes
        obj = super(InterpolationRoutineMapping, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "INTERPOLATION-ROUTINES":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.interpolation_routines.append(SerializationHelper.deserialize_by_tag(item_elem, "InterpolationRoutine"))
            elif tag == "SW-RECORD-REF":
                setattr(obj, "sw_record_ref", ARRef.deserialize(child))

        return obj



class InterpolationRoutineMappingBuilder(BuilderBase):
    """Builder for InterpolationRoutineMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: InterpolationRoutineMapping = InterpolationRoutineMapping()


    def with_interpolation_routines(self, items: list[InterpolationRoutine]) -> "InterpolationRoutineMappingBuilder":
        """Set interpolation_routines list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.interpolation_routines = list(items) if items else []
        return self

    def with_sw_record(self, value: Optional[SwRecordLayout]) -> "InterpolationRoutineMappingBuilder":
        """Set sw_record attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'sw_record' is required and cannot be None")
        self._obj.sw_record = value
        return self


    def add_interpolation_routine(self, item: InterpolationRoutine) -> "InterpolationRoutineMappingBuilder":
        """Add a single item to interpolation_routines list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.interpolation_routines.append(item)
        return self

    def clear_interpolation_routines(self) -> "InterpolationRoutineMappingBuilder":
        """Clear all items from interpolation_routines list.

        Returns:
            self for method chaining
        """
        self._obj.interpolation_routines = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "interpolationRoutine",
        "swRecord",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> InterpolationRoutineMapping:
        """Build and return the InterpolationRoutineMapping instance with validation."""
        self._validate_instance()
        return self._obj