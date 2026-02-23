"""IoHwAbstractionServerAnnotation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 156)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_ApplicationAttributes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.GeneralAnnotation.general_annotation import (
    GeneralAnnotation,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.GeneralAnnotation.general_annotation import GeneralAnnotationBuilder
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes import (
    FilterDebouncingEnum,
    PulseTestEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Float,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.argument_data_prototype import (
    ArgumentDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger import (
    Trigger,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
        PortPrototype,
    )



class IoHwAbstractionServerAnnotation(GeneralAnnotation):
    """AUTOSAR IoHwAbstractionServerAnnotation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    age: Optional[MultidimensionalTime]
    argument_ref: Optional[ARRef]
    bsw_resolution: Optional[Float]
    data_element_ref: Optional[ARRef]
    failure_ref: Optional[ARRef]
    filtering: Optional[FilterDebouncingEnum]
    pulse_test: Optional[PulseTestEnum]
    trigger_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize IoHwAbstractionServerAnnotation."""
        super().__init__()
        self.age: Optional[MultidimensionalTime] = None
        self.argument_ref: Optional[ARRef] = None
        self.bsw_resolution: Optional[Float] = None
        self.data_element_ref: Optional[ARRef] = None
        self.failure_ref: Optional[ARRef] = None
        self.filtering: Optional[FilterDebouncingEnum] = None
        self.pulse_test: Optional[PulseTestEnum] = None
        self.trigger_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize IoHwAbstractionServerAnnotation to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(IoHwAbstractionServerAnnotation, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize age
        if self.age is not None:
            serialized = SerializationHelper.serialize_item(self.age, "MultidimensionalTime")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("AGE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize argument_ref
        if self.argument_ref is not None:
            serialized = SerializationHelper.serialize_item(self.argument_ref, "ArgumentDataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ARGUMENT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize bsw_resolution
        if self.bsw_resolution is not None:
            serialized = SerializationHelper.serialize_item(self.bsw_resolution, "Float")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BSW-RESOLUTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize data_element_ref
        if self.data_element_ref is not None:
            serialized = SerializationHelper.serialize_item(self.data_element_ref, "VariableDataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-ELEMENT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize failure_ref
        if self.failure_ref is not None:
            serialized = SerializationHelper.serialize_item(self.failure_ref, "PortPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FAILURE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize filtering
        if self.filtering is not None:
            serialized = SerializationHelper.serialize_item(self.filtering, "FilterDebouncingEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FILTERING")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize pulse_test
        if self.pulse_test is not None:
            serialized = SerializationHelper.serialize_item(self.pulse_test, "PulseTestEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PULSE-TEST")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize trigger_ref
        if self.trigger_ref is not None:
            serialized = SerializationHelper.serialize_item(self.trigger_ref, "Trigger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TRIGGER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IoHwAbstractionServerAnnotation":
        """Deserialize XML element to IoHwAbstractionServerAnnotation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IoHwAbstractionServerAnnotation object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(IoHwAbstractionServerAnnotation, cls).deserialize(element)

        # Parse age
        child = SerializationHelper.find_child_element(element, "AGE")
        if child is not None:
            age_value = SerializationHelper.deserialize_by_tag(child, "MultidimensionalTime")
            obj.age = age_value

        # Parse argument_ref
        child = SerializationHelper.find_child_element(element, "ARGUMENT-REF")
        if child is not None:
            argument_ref_value = ARRef.deserialize(child)
            obj.argument_ref = argument_ref_value

        # Parse bsw_resolution
        child = SerializationHelper.find_child_element(element, "BSW-RESOLUTION")
        if child is not None:
            bsw_resolution_value = child.text
            obj.bsw_resolution = bsw_resolution_value

        # Parse data_element_ref
        child = SerializationHelper.find_child_element(element, "DATA-ELEMENT-REF")
        if child is not None:
            data_element_ref_value = ARRef.deserialize(child)
            obj.data_element_ref = data_element_ref_value

        # Parse failure_ref
        child = SerializationHelper.find_child_element(element, "FAILURE-REF")
        if child is not None:
            failure_ref_value = ARRef.deserialize(child)
            obj.failure_ref = failure_ref_value

        # Parse filtering
        child = SerializationHelper.find_child_element(element, "FILTERING")
        if child is not None:
            filtering_value = FilterDebouncingEnum.deserialize(child)
            obj.filtering = filtering_value

        # Parse pulse_test
        child = SerializationHelper.find_child_element(element, "PULSE-TEST")
        if child is not None:
            pulse_test_value = PulseTestEnum.deserialize(child)
            obj.pulse_test = pulse_test_value

        # Parse trigger_ref
        child = SerializationHelper.find_child_element(element, "TRIGGER-REF")
        if child is not None:
            trigger_ref_value = ARRef.deserialize(child)
            obj.trigger_ref = trigger_ref_value

        return obj



class IoHwAbstractionServerAnnotationBuilder(GeneralAnnotationBuilder):
    """Builder for IoHwAbstractionServerAnnotation with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: IoHwAbstractionServerAnnotation = IoHwAbstractionServerAnnotation()


    def with_age(self, value: Optional[MultidimensionalTime]) -> "IoHwAbstractionServerAnnotationBuilder":
        """Set age attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.age = value
        return self

    def with_argument(self, value: Optional[ArgumentDataPrototype]) -> "IoHwAbstractionServerAnnotationBuilder":
        """Set argument attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.argument = value
        return self

    def with_bsw_resolution(self, value: Optional[Float]) -> "IoHwAbstractionServerAnnotationBuilder":
        """Set bsw_resolution attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.bsw_resolution = value
        return self

    def with_data_element(self, value: Optional[VariableDataPrototype]) -> "IoHwAbstractionServerAnnotationBuilder":
        """Set data_element attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.data_element = value
        return self

    def with_failure(self, value: Optional[PortPrototype]) -> "IoHwAbstractionServerAnnotationBuilder":
        """Set failure attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.failure = value
        return self

    def with_filtering(self, value: Optional[FilterDebouncingEnum]) -> "IoHwAbstractionServerAnnotationBuilder":
        """Set filtering attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.filtering = value
        return self

    def with_pulse_test(self, value: Optional[PulseTestEnum]) -> "IoHwAbstractionServerAnnotationBuilder":
        """Set pulse_test attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.pulse_test = value
        return self

    def with_trigger(self, value: Optional[Trigger]) -> "IoHwAbstractionServerAnnotationBuilder":
        """Set trigger attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.trigger = value
        return self




    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel.core import GlobalSettingsManager, BuilderValidationMode

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


    def build(self) -> IoHwAbstractionServerAnnotation:
        """Build and return the IoHwAbstractionServerAnnotation instance with validation."""
        self._validate_instance()
        pass
        return self._obj