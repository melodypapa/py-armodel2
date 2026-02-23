"""LatencyTimingConstraint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 95)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingConstraint_LatencyTimingConstraint.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.timing_constraint import (
    TimingConstraint,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.timing_constraint import TimingConstraintBuilder
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.LatencyTimingConstraint import (
    LatencyConstraintTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description_event import (
    TimingDescriptionEvent,
)


class LatencyTimingConstraint(TimingConstraint):
    """AUTOSAR LatencyTimingConstraint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    latency: Optional[LatencyConstraintTypeEnum]
    maximum: Optional[MultidimensionalTime]
    minimum: Optional[MultidimensionalTime]
    nominal: Optional[MultidimensionalTime]
    scope_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize LatencyTimingConstraint."""
        super().__init__()
        self.latency: Optional[LatencyConstraintTypeEnum] = None
        self.maximum: Optional[MultidimensionalTime] = None
        self.minimum: Optional[MultidimensionalTime] = None
        self.nominal: Optional[MultidimensionalTime] = None
        self.scope_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize LatencyTimingConstraint to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(LatencyTimingConstraint, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize latency
        if self.latency is not None:
            serialized = SerializationHelper.serialize_item(self.latency, "LatencyConstraintTypeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LATENCY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize maximum
        if self.maximum is not None:
            serialized = SerializationHelper.serialize_item(self.maximum, "MultidimensionalTime")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAXIMUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize minimum
        if self.minimum is not None:
            serialized = SerializationHelper.serialize_item(self.minimum, "MultidimensionalTime")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MINIMUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nominal
        if self.nominal is not None:
            serialized = SerializationHelper.serialize_item(self.nominal, "MultidimensionalTime")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NOMINAL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize scope_ref
        if self.scope_ref is not None:
            serialized = SerializationHelper.serialize_item(self.scope_ref, "TimingDescriptionEvent")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SCOPE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LatencyTimingConstraint":
        """Deserialize XML element to LatencyTimingConstraint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LatencyTimingConstraint object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(LatencyTimingConstraint, cls).deserialize(element)

        # Parse latency
        child = SerializationHelper.find_child_element(element, "LATENCY")
        if child is not None:
            latency_value = LatencyConstraintTypeEnum.deserialize(child)
            obj.latency = latency_value

        # Parse maximum
        child = SerializationHelper.find_child_element(element, "MAXIMUM")
        if child is not None:
            maximum_value = SerializationHelper.deserialize_by_tag(child, "MultidimensionalTime")
            obj.maximum = maximum_value

        # Parse minimum
        child = SerializationHelper.find_child_element(element, "MINIMUM")
        if child is not None:
            minimum_value = SerializationHelper.deserialize_by_tag(child, "MultidimensionalTime")
            obj.minimum = minimum_value

        # Parse nominal
        child = SerializationHelper.find_child_element(element, "NOMINAL")
        if child is not None:
            nominal_value = SerializationHelper.deserialize_by_tag(child, "MultidimensionalTime")
            obj.nominal = nominal_value

        # Parse scope_ref
        child = SerializationHelper.find_child_element(element, "SCOPE-REF")
        if child is not None:
            scope_ref_value = ARRef.deserialize(child)
            obj.scope_ref = scope_ref_value

        return obj



class LatencyTimingConstraintBuilder(TimingConstraintBuilder):
    """Builder for LatencyTimingConstraint with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: LatencyTimingConstraint = LatencyTimingConstraint()


    def with_latency(self, value: Optional[LatencyConstraintTypeEnum]) -> "LatencyTimingConstraintBuilder":
        """Set latency attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.latency = value
        return self

    def with_maximum(self, value: Optional[MultidimensionalTime]) -> "LatencyTimingConstraintBuilder":
        """Set maximum attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.maximum = value
        return self

    def with_minimum(self, value: Optional[MultidimensionalTime]) -> "LatencyTimingConstraintBuilder":
        """Set minimum attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.minimum = value
        return self

    def with_nominal(self, value: Optional[MultidimensionalTime]) -> "LatencyTimingConstraintBuilder":
        """Set nominal attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.nominal = value
        return self

    def with_scope(self, value: Optional[TimingDescriptionEvent]) -> "LatencyTimingConstraintBuilder":
        """Set scope attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.scope = value
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


    def build(self) -> LatencyTimingConstraint:
        """Build and return the LatencyTimingConstraint instance with validation."""
        self._validate_instance()
        pass
        return self._obj