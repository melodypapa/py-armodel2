"""McDataAccessDetails AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 195)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_MeasurementCalibrationSupport.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.builder_base import BuilderBase

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.rte_event import (
        RTEEvent,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.variable_access import (
        VariableAccess,
    )



from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
class McDataAccessDetails(ARObject):
    """AUTOSAR McDataAccessDetails."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    rte_event_reves: list[RTEEvent]
    variable_accesses: list[VariableAccess]
    def __init__(self) -> None:
        """Initialize McDataAccessDetails."""
        super().__init__()
        self.rte_event_reves: list[RTEEvent] = []
        self.variable_accesses: list[VariableAccess] = []

    def serialize(self) -> ET.Element:
        """Serialize McDataAccessDetails to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(McDataAccessDetails, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize rte_event_reves (list to container "RTE-EVENT-REVES")
        if self.rte_event_reves:
            wrapper = ET.Element("RTE-EVENT-REVES")
            for item in self.rte_event_reves:
                serialized = SerializationHelper.serialize_item(item, "RTEEvent")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize variable_accesses (list to container "VARIABLE-ACCESSES")
        if self.variable_accesses:
            wrapper = ET.Element("VARIABLE-ACCESSES")
            for item in self.variable_accesses:
                serialized = SerializationHelper.serialize_item(item, "VariableAccess")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "McDataAccessDetails":
        """Deserialize XML element to McDataAccessDetails object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized McDataAccessDetails object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(McDataAccessDetails, cls).deserialize(element)

        # Parse rte_event_reves (list from container "RTE-EVENT-REVES")
        obj.rte_event_reves = []
        container = SerializationHelper.find_child_element(element, "RTE-EVENT-REVES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.rte_event_reves.append(child_value)

        # Parse variable_accesses (list from container "VARIABLE-ACCESSES")
        obj.variable_accesses = []
        container = SerializationHelper.find_child_element(element, "VARIABLE-ACCESSES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.variable_accesses.append(child_value)

        return obj



class McDataAccessDetailsBuilder(BuilderBase):
    """Builder for McDataAccessDetails with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: McDataAccessDetails = McDataAccessDetails()


    def with_rte_event_reves(self, items: list[RTEEvent]) -> "McDataAccessDetailsBuilder":
        """Set rte_event_reves list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.rte_event_reves = list(items) if items else []
        return self

    def with_variable_accesses(self, items: list[VariableAccess]) -> "McDataAccessDetailsBuilder":
        """Set variable_accesses list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.variable_accesses = list(items) if items else []
        return self


    def add_rte_event_ref(self, item: RTEEvent) -> "McDataAccessDetailsBuilder":
        """Add a single item to rte_event_reves list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.rte_event_reves.append(item)
        return self

    def clear_rte_event_reves(self) -> "McDataAccessDetailsBuilder":
        """Clear all items from rte_event_reves list.

        Returns:
            self for method chaining
        """
        self._obj.rte_event_reves = []
        return self

    def add_variable_access(self, item: VariableAccess) -> "McDataAccessDetailsBuilder":
        """Add a single item to variable_accesses list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.variable_accesses.append(item)
        return self

    def clear_variable_accesses(self) -> "McDataAccessDetailsBuilder":
        """Clear all items from variable_accesses list.

        Returns:
            self for method chaining
        """
        self._obj.variable_accesses = []
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


    def build(self) -> McDataAccessDetails:
        """Build and return the McDataAccessDetails instance with validation."""
        self._validate_instance()
        pass
        return self._obj