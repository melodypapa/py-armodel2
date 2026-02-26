"""TransmissionModeDeclaration AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 392)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication_Timing.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.Timing.mode_driven_transmission_mode_condition import (
    ModeDrivenTransmissionModeCondition,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.Timing.transmission_mode_condition import (
    TransmissionModeCondition,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.Timing.transmission_mode_timing import (
    TransmissionModeTiming,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class TransmissionModeDeclaration(ARObject):
    """AUTOSAR TransmissionModeDeclaration."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    mode_driven_false_conditions: list[ModeDrivenTransmissionModeCondition]
    mode_driven_true_conditions: list[ModeDrivenTransmissionModeCondition]
    transmission_mode_condition: Optional[TransmissionModeCondition]
    transmission_mode_false_timing: Optional[TransmissionModeTiming]
    transmission_mode_true_timing: Optional[TransmissionModeTiming]
    def __init__(self) -> None:
        """Initialize TransmissionModeDeclaration."""
        super().__init__()
        self.mode_driven_false_conditions: list[ModeDrivenTransmissionModeCondition] = []
        self.mode_driven_true_conditions: list[ModeDrivenTransmissionModeCondition] = []
        self.transmission_mode_condition: Optional[TransmissionModeCondition] = None
        self.transmission_mode_false_timing: Optional[TransmissionModeTiming] = None
        self.transmission_mode_true_timing: Optional[TransmissionModeTiming] = None

    def serialize(self) -> ET.Element:
        """Serialize TransmissionModeDeclaration to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TransmissionModeDeclaration, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize mode_driven_false_conditions (list to container "MODE-DRIVEN-FALSE-CONDITIONS")
        if self.mode_driven_false_conditions:
            wrapper = ET.Element("MODE-DRIVEN-FALSE-CONDITIONS")
            for item in self.mode_driven_false_conditions:
                serialized = SerializationHelper.serialize_item(item, "ModeDrivenTransmissionModeCondition")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize mode_driven_true_conditions (list to container "MODE-DRIVEN-TRUE-CONDITIONS")
        if self.mode_driven_true_conditions:
            wrapper = ET.Element("MODE-DRIVEN-TRUE-CONDITIONS")
            for item in self.mode_driven_true_conditions:
                serialized = SerializationHelper.serialize_item(item, "ModeDrivenTransmissionModeCondition")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize transmission_mode_condition
        if self.transmission_mode_condition is not None:
            serialized = SerializationHelper.serialize_item(self.transmission_mode_condition, "TransmissionModeCondition")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TRANSMISSION-MODE-CONDITION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize transmission_mode_false_timing
        if self.transmission_mode_false_timing is not None:
            serialized = SerializationHelper.serialize_item(self.transmission_mode_false_timing, "TransmissionModeTiming")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TRANSMISSION-MODE-FALSE-TIMING")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize transmission_mode_true_timing
        if self.transmission_mode_true_timing is not None:
            serialized = SerializationHelper.serialize_item(self.transmission_mode_true_timing, "TransmissionModeTiming")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TRANSMISSION-MODE-TRUE-TIMING")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TransmissionModeDeclaration":
        """Deserialize XML element to TransmissionModeDeclaration object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TransmissionModeDeclaration object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TransmissionModeDeclaration, cls).deserialize(element)

        # Parse mode_driven_false_conditions (list from container "MODE-DRIVEN-FALSE-CONDITIONS")
        obj.mode_driven_false_conditions = []
        container = SerializationHelper.find_child_element(element, "MODE-DRIVEN-FALSE-CONDITIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.mode_driven_false_conditions.append(child_value)

        # Parse mode_driven_true_conditions (list from container "MODE-DRIVEN-TRUE-CONDITIONS")
        obj.mode_driven_true_conditions = []
        container = SerializationHelper.find_child_element(element, "MODE-DRIVEN-TRUE-CONDITIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.mode_driven_true_conditions.append(child_value)

        # Parse transmission_mode_condition
        child = SerializationHelper.find_child_element(element, "TRANSMISSION-MODE-CONDITION")
        if child is not None:
            transmission_mode_condition_value = SerializationHelper.deserialize_by_tag(child, "TransmissionModeCondition")
            obj.transmission_mode_condition = transmission_mode_condition_value

        # Parse transmission_mode_false_timing
        child = SerializationHelper.find_child_element(element, "TRANSMISSION-MODE-FALSE-TIMING")
        if child is not None:
            transmission_mode_false_timing_value = SerializationHelper.deserialize_by_tag(child, "TransmissionModeTiming")
            obj.transmission_mode_false_timing = transmission_mode_false_timing_value

        # Parse transmission_mode_true_timing
        child = SerializationHelper.find_child_element(element, "TRANSMISSION-MODE-TRUE-TIMING")
        if child is not None:
            transmission_mode_true_timing_value = SerializationHelper.deserialize_by_tag(child, "TransmissionModeTiming")
            obj.transmission_mode_true_timing = transmission_mode_true_timing_value

        return obj



class TransmissionModeDeclarationBuilder(BuilderBase):
    """Builder for TransmissionModeDeclaration with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TransmissionModeDeclaration = TransmissionModeDeclaration()


    def with_mode_driven_false_conditions(self, items: list[ModeDrivenTransmissionModeCondition]) -> "TransmissionModeDeclarationBuilder":
        """Set mode_driven_false_conditions list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.mode_driven_false_conditions = list(items) if items else []
        return self

    def with_mode_driven_true_conditions(self, items: list[ModeDrivenTransmissionModeCondition]) -> "TransmissionModeDeclarationBuilder":
        """Set mode_driven_true_conditions list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.mode_driven_true_conditions = list(items) if items else []
        return self

    def with_transmission_mode_condition(self, value: Optional[TransmissionModeCondition]) -> "TransmissionModeDeclarationBuilder":
        """Set transmission_mode_condition attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.transmission_mode_condition = value
        return self

    def with_transmission_mode_false_timing(self, value: Optional[TransmissionModeTiming]) -> "TransmissionModeDeclarationBuilder":
        """Set transmission_mode_false_timing attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.transmission_mode_false_timing = value
        return self

    def with_transmission_mode_true_timing(self, value: Optional[TransmissionModeTiming]) -> "TransmissionModeDeclarationBuilder":
        """Set transmission_mode_true_timing attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.transmission_mode_true_timing = value
        return self


    def add_mode_driven_false_condition(self, item: ModeDrivenTransmissionModeCondition) -> "TransmissionModeDeclarationBuilder":
        """Add a single item to mode_driven_false_conditions list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.mode_driven_false_conditions.append(item)
        return self

    def clear_mode_driven_false_conditions(self) -> "TransmissionModeDeclarationBuilder":
        """Clear all items from mode_driven_false_conditions list.

        Returns:
            self for method chaining
        """
        self._obj.mode_driven_false_conditions = []
        return self

    def add_mode_driven_true_condition(self, item: ModeDrivenTransmissionModeCondition) -> "TransmissionModeDeclarationBuilder":
        """Add a single item to mode_driven_true_conditions list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.mode_driven_true_conditions.append(item)
        return self

    def clear_mode_driven_true_conditions(self) -> "TransmissionModeDeclarationBuilder":
        """Clear all items from mode_driven_true_conditions list.

        Returns:
            self for method chaining
        """
        self._obj.mode_driven_true_conditions = []
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


    def build(self) -> TransmissionModeDeclaration:
        """Build and return the TransmissionModeDeclaration instance with validation."""
        self._validate_instance()
        pass
        return self._obj