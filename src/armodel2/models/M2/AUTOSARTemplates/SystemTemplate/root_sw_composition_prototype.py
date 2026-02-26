"""RootSwCompositionPrototype AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 1003)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 186)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 240)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 18)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.MeasurementAndCalibration.CalibrationParameter.calibration_parameter_value_set import (
    CalibrationParameterValueSet,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.composition_sw_component_type import (
    CompositionSwComponentType,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.FlatMap.flat_map import (
    FlatMap,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class RootSwCompositionPrototype(Identifiable):
    """AUTOSAR RootSwCompositionPrototype."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    calibration_parameter_value_set_refs: list[ARRef]
    flat_map_ref: Optional[ARRef]
    software_composition_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize RootSwCompositionPrototype."""
        super().__init__()
        self.calibration_parameter_value_set_refs: list[ARRef] = []
        self.flat_map_ref: Optional[ARRef] = None
        self.software_composition_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize RootSwCompositionPrototype to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(RootSwCompositionPrototype, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize calibration_parameter_value_set_refs (list to container "CALIBRATION-PARAMETER-VALUE-SET-REFS")
        if self.calibration_parameter_value_set_refs:
            wrapper = ET.Element("CALIBRATION-PARAMETER-VALUE-SET-REFS")
            for item in self.calibration_parameter_value_set_refs:
                serialized = SerializationHelper.serialize_item(item, "CalibrationParameterValueSet")
                if serialized is not None:
                    child_elem = ET.Element("CALIBRATION-PARAMETER-VALUE-SET-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize flat_map_ref
        if self.flat_map_ref is not None:
            serialized = SerializationHelper.serialize_item(self.flat_map_ref, "FlatMap")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FLAT-MAP-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize software_composition_ref
        if self.software_composition_ref is not None:
            serialized = SerializationHelper.serialize_item(self.software_composition_ref, "CompositionSwComponentType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SOFTWARE-COMPOSITION-TREF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RootSwCompositionPrototype":
        """Deserialize XML element to RootSwCompositionPrototype object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RootSwCompositionPrototype object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(RootSwCompositionPrototype, cls).deserialize(element)

        # Parse calibration_parameter_value_set_refs (list from container "CALIBRATION-PARAMETER-VALUE-SET-REFS")
        obj.calibration_parameter_value_set_refs = []
        container = SerializationHelper.find_child_element(element, "CALIBRATION-PARAMETER-VALUE-SET-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.calibration_parameter_value_set_refs.append(child_value)

        # Parse flat_map_ref
        child = SerializationHelper.find_child_element(element, "FLAT-MAP-REF")
        if child is not None:
            flat_map_ref_value = ARRef.deserialize(child)
            obj.flat_map_ref = flat_map_ref_value

        # Parse software_composition_ref
        child = SerializationHelper.find_child_element(element, "SOFTWARE-COMPOSITION-TREF")
        if child is not None:
            software_composition_ref_value = ARRef.deserialize(child)
            obj.software_composition_ref = software_composition_ref_value

        return obj



class RootSwCompositionPrototypeBuilder(IdentifiableBuilder):
    """Builder for RootSwCompositionPrototype with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: RootSwCompositionPrototype = RootSwCompositionPrototype()


    def with_calibration_parameter_value_sets(self, items: list[CalibrationParameterValueSet]) -> "RootSwCompositionPrototypeBuilder":
        """Set calibration_parameter_value_sets list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.calibration_parameter_value_sets = list(items) if items else []
        return self

    def with_flat_map(self, value: Optional[FlatMap]) -> "RootSwCompositionPrototypeBuilder":
        """Set flat_map attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.flat_map = value
        return self

    def with_software_composition(self, value: Optional[CompositionSwComponentType]) -> "RootSwCompositionPrototypeBuilder":
        """Set software_composition attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.software_composition = value
        return self


    def add_calibration_parameter_value_set(self, item: CalibrationParameterValueSet) -> "RootSwCompositionPrototypeBuilder":
        """Add a single item to calibration_parameter_value_sets list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.calibration_parameter_value_sets.append(item)
        return self

    def clear_calibration_parameter_value_sets(self) -> "RootSwCompositionPrototypeBuilder":
        """Clear all items from calibration_parameter_value_sets list.

        Returns:
            self for method chaining
        """
        self._obj.calibration_parameter_value_sets = []
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


    def build(self) -> RootSwCompositionPrototype:
        """Build and return the RootSwCompositionPrototype instance with validation."""
        self._validate_instance()
        pass
        return self._obj