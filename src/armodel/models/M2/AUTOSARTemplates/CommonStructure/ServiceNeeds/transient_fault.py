"""TransientFault AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 1009)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.traced_failure import (
    TracedFailure,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.traced_failure import TracedFailureBuilder


class TransientFault(TracedFailure):
    """AUTOSAR TransientFault."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    possible_error_reactions: list[Any]
    def __init__(self) -> None:
        """Initialize TransientFault."""
        super().__init__()
        self.possible_error_reactions: list[Any] = []

    def serialize(self) -> ET.Element:
        """Serialize TransientFault to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TransientFault, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize possible_error_reactions (list to container "POSSIBLE-ERROR-REACTIONS")
        if self.possible_error_reactions:
            wrapper = ET.Element("POSSIBLE-ERROR-REACTIONS")
            for item in self.possible_error_reactions:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TransientFault":
        """Deserialize XML element to TransientFault object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TransientFault object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TransientFault, cls).deserialize(element)

        # Parse possible_error_reactions (list from container "POSSIBLE-ERROR-REACTIONS")
        obj.possible_error_reactions = []
        container = SerializationHelper.find_child_element(element, "POSSIBLE-ERROR-REACTIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.possible_error_reactions.append(child_value)

        return obj



class TransientFaultBuilder(TracedFailureBuilder):
    """Builder for TransientFault with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TransientFault = TransientFault()


    def with_possible_error_reactions(self, items: list[any (PossibleErrorReaction)]) -> "TransientFaultBuilder":
        """Set possible_error_reactions list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.possible_error_reactions = list(items) if items else []
        return self


    def add_possible_error_reaction(self, item: any (PossibleErrorReaction)) -> "TransientFaultBuilder":
        """Add a single item to possible_error_reactions list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.possible_error_reactions.append(item)
        return self

    def clear_possible_error_reactions(self) -> "TransientFaultBuilder":
        """Clear all items from possible_error_reactions list.

        Returns:
            self for method chaining
        """
        self._obj.possible_error_reactions = []
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


    def build(self) -> TransientFault:
        """Build and return the TransientFault instance with validation."""
        self._validate_instance()
        pass
        return self._obj