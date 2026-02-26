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

    interpolation_routines: list[InterpolationRoutine]
    sw_record_ref: Optional[ARRef]
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
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

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

        # Parse interpolation_routines (list from container "INTERPOLATION-ROUTINES")
        obj.interpolation_routines = []
        container = SerializationHelper.find_child_element(element, "INTERPOLATION-ROUTINES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.interpolation_routines.append(child_value)

        # Parse sw_record_ref
        child = SerializationHelper.find_child_element(element, "SW-RECORD-REF")
        if child is not None:
            sw_record_ref_value = ARRef.deserialize(child)
            obj.sw_record_ref = sw_record_ref_value

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
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
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



    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Get type hints for the class
        try:
            type_hints_dict = get_type_hints(type(self._obj))
        except Exception:
            # Cannot resolve type hints (e.g., forward references), skip validation
            return

        for attr_name, attr_type in type_hints_dict.items():
            if attr_name.startswith("_"):
                continue

            value = getattr(self._obj, attr_name)

            # Check required fields (not Optional)
            if value is None and not self._is_optional_type(attr_type):
                if mode == BuilderValidationMode.STRICT:
                    raise ValueError(
                        f"Required attribute '{attr_name}' is None"
                    )
                elif mode == BuilderValidationMode.LENIENT:
                    import warnings
                    warnings.warn(
                        f"Required attribute '{attr_name}' is None",
                        UserWarning
                    )

    @staticmethod
    def _is_optional_type(type_hint: Any) -> bool:
        """Check if a type hint is Optional.

        Args:
            type_hint: Type hint to check

        Returns:
            True if type is Optional, False otherwise
        """
        origin = getattr(type_hint, "__origin__", None)
        return origin is Union

    @staticmethod
    def _get_expected_type(type_hint: Any) -> type:
        """Extract expected type from type hint.

        Args:
            type_hint: Type hint to extract from

        Returns:
            Expected type
        """
        if isinstance(type_hint, str):
            return object
        origin = getattr(type_hint, "__origin__", None)
        if origin is Union:
            args = getattr(type_hint, "__args__", [])
            for arg in args:
                if arg is not type(None):
                    return arg
        elif origin is list:
            args = getattr(type_hint, "__args__", [object])
            return args[0] if args else object
        return type_hint if isinstance(type_hint, type) else object


    def build(self) -> InterpolationRoutineMapping:
        """Build and return the InterpolationRoutineMapping instance with validation."""
        self._validate_instance()
        pass
        return self._obj