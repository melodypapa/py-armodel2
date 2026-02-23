"""RteEventInCompositionSeparation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 212)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_RteEventToOsTaskMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.rte_event import (
    RTEEvent,
)


class RteEventInCompositionSeparation(Identifiable):
    """AUTOSAR RteEventInCompositionSeparation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    rte_event_instance_refs: list[RTEEvent]
    def __init__(self) -> None:
        """Initialize RteEventInCompositionSeparation."""
        super().__init__()
        self.rte_event_instance_refs: list[RTEEvent] = []

    def serialize(self) -> ET.Element:
        """Serialize RteEventInCompositionSeparation to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(RteEventInCompositionSeparation, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize rte_event_instance_refs (list to container "RTE-EVENT-INSTANCE-REFS")
        if self.rte_event_instance_refs:
            wrapper = ET.Element("RTE-EVENT-INSTANCE-REFS")
            for item in self.rte_event_instance_refs:
                serialized = SerializationHelper.serialize_item(item, "RTEEvent")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RteEventInCompositionSeparation":
        """Deserialize XML element to RteEventInCompositionSeparation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RteEventInCompositionSeparation object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(RteEventInCompositionSeparation, cls).deserialize(element)

        # Parse rte_event_instance_refs (list from container "RTE-EVENT-INSTANCE-REFS")
        obj.rte_event_instance_refs = []
        container = SerializationHelper.find_child_element(element, "RTE-EVENT-INSTANCE-REFS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.rte_event_instance_refs.append(child_value)

        return obj



class RteEventInCompositionSeparationBuilder(IdentifiableBuilder):
    """Builder for RteEventInCompositionSeparation with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: RteEventInCompositionSeparation = RteEventInCompositionSeparation()


    def with_rte_event_instance_refs(self, items: list[RTEEvent]) -> "RteEventInCompositionSeparationBuilder":
        """Set rte_event_instance_refs list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.rte_event_instance_refs = list(items) if items else []
        return self


    def add_rte_event_instance_ref(self, item: RTEEvent) -> "RteEventInCompositionSeparationBuilder":
        """Add a single item to rte_event_instance_refs list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.rte_event_instance_refs.append(item)
        return self

    def clear_rte_event_instance_refs(self) -> "RteEventInCompositionSeparationBuilder":
        """Clear all items from rte_event_instance_refs list.

        Returns:
            self for method chaining
        """
        self._obj.rte_event_instance_refs = []
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


    def build(self) -> RteEventInCompositionSeparation:
        """Build and return the RteEventInCompositionSeparation instance with validation."""
        self._validate_instance()
        pass
        return self._obj