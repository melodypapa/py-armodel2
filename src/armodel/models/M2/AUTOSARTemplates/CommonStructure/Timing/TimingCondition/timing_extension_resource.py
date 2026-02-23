"""TimingExtensionResource AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 35)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingCondition.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.autosar_operation_argument_instance import (
    AutosarOperationArgumentInstance,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition.timing_mode_instance import (
    TimingModeInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class TimingExtensionResource(Identifiable):
    """AUTOSAR TimingExtensionResource."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    timing_arguments: list[AutosarOperationArgumentInstance]
    timing_modes: list[TimingModeInstance]
    timing_variables: list[Any]
    def __init__(self) -> None:
        """Initialize TimingExtensionResource."""
        super().__init__()
        self.timing_arguments: list[AutosarOperationArgumentInstance] = []
        self.timing_modes: list[TimingModeInstance] = []
        self.timing_variables: list[Any] = []

    def serialize(self) -> ET.Element:
        """Serialize TimingExtensionResource to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TimingExtensionResource, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize timing_arguments (list to container "TIMING-ARGUMENTS")
        if self.timing_arguments:
            wrapper = ET.Element("TIMING-ARGUMENTS")
            for item in self.timing_arguments:
                serialized = SerializationHelper.serialize_item(item, "AutosarOperationArgumentInstance")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize timing_modes (list to container "TIMING-MODES")
        if self.timing_modes:
            wrapper = ET.Element("TIMING-MODES")
            for item in self.timing_modes:
                serialized = SerializationHelper.serialize_item(item, "TimingModeInstance")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize timing_variables (list to container "TIMING-VARIABLES")
        if self.timing_variables:
            wrapper = ET.Element("TIMING-VARIABLES")
            for item in self.timing_variables:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TimingExtensionResource":
        """Deserialize XML element to TimingExtensionResource object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TimingExtensionResource object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TimingExtensionResource, cls).deserialize(element)

        # Parse timing_arguments (list from container "TIMING-ARGUMENTS")
        obj.timing_arguments = []
        container = SerializationHelper.find_child_element(element, "TIMING-ARGUMENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.timing_arguments.append(child_value)

        # Parse timing_modes (list from container "TIMING-MODES")
        obj.timing_modes = []
        container = SerializationHelper.find_child_element(element, "TIMING-MODES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.timing_modes.append(child_value)

        # Parse timing_variables (list from container "TIMING-VARIABLES")
        obj.timing_variables = []
        container = SerializationHelper.find_child_element(element, "TIMING-VARIABLES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.timing_variables.append(child_value)

        return obj



class TimingExtensionResourceBuilder(IdentifiableBuilder):
    """Builder for TimingExtensionResource with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TimingExtensionResource = TimingExtensionResource()


    def with_timing_arguments(self, items: list[AutosarOperationArgumentInstance]) -> "TimingExtensionResourceBuilder":
        """Set timing_arguments list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.timing_arguments = list(items) if items else []
        return self

    def with_timing_modes(self, items: list[TimingModeInstance]) -> "TimingExtensionResourceBuilder":
        """Set timing_modes list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.timing_modes = list(items) if items else []
        return self

    def with_timing_variables(self, items: list[any (AutosarVariable)]) -> "TimingExtensionResourceBuilder":
        """Set timing_variables list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.timing_variables = list(items) if items else []
        return self


    def add_timing_argument(self, item: AutosarOperationArgumentInstance) -> "TimingExtensionResourceBuilder":
        """Add a single item to timing_arguments list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.timing_arguments.append(item)
        return self

    def clear_timing_arguments(self) -> "TimingExtensionResourceBuilder":
        """Clear all items from timing_arguments list.

        Returns:
            self for method chaining
        """
        self._obj.timing_arguments = []
        return self

    def add_timing_mode(self, item: TimingModeInstance) -> "TimingExtensionResourceBuilder":
        """Add a single item to timing_modes list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.timing_modes.append(item)
        return self

    def clear_timing_modes(self) -> "TimingExtensionResourceBuilder":
        """Clear all items from timing_modes list.

        Returns:
            self for method chaining
        """
        self._obj.timing_modes = []
        return self

    def add_timing_variable(self, item: any (AutosarVariable)) -> "TimingExtensionResourceBuilder":
        """Add a single item to timing_variables list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.timing_variables.append(item)
        return self

    def clear_timing_variables(self) -> "TimingExtensionResourceBuilder":
        """Clear all items from timing_variables list.

        Returns:
            self for method chaining
        """
        self._obj.timing_variables = []
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


    def build(self) -> TimingExtensionResource:
        """Build and return the TimingExtensionResource instance with validation."""
        self._validate_instance()
        pass
        return self._obj