"""EcucChoiceContainerDef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 41)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_container_def import (
    EcucContainerDef,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_container_def import EcucContainerDefBuilder
from armodel2.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_param_conf_container_def import (
    EcucParamConfContainerDef,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class EcucChoiceContainerDef(EcucContainerDef):
    """AUTOSAR EcucChoiceContainerDef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "ECUC-CHOICE-CONTAINER-DEF"


    choices: list[EcucParamConfContainerDef]
    _DESERIALIZE_DISPATCH = {
        "CHOICES": lambda obj, elem: obj.choices.append(EcucParamConfContainerDef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize EcucChoiceContainerDef."""
        super().__init__()
        self.choices: list[EcucParamConfContainerDef] = []

    def serialize(self) -> ET.Element:
        """Serialize EcucChoiceContainerDef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcucChoiceContainerDef, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize choices (list to container "CHOICES")
        if self.choices:
            wrapper = ET.Element("CHOICES")
            for item in self.choices:
                serialized = SerializationHelper.serialize_item(item, "EcucParamConfContainerDef")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucChoiceContainerDef":
        """Deserialize XML element to EcucChoiceContainerDef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucChoiceContainerDef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcucChoiceContainerDef, cls).deserialize(element)

        # Parse choices (list from container "CHOICES")
        obj.choices = []
        container = SerializationHelper.find_child_element(element, "CHOICES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.choices.append(child_value)

        return obj



class EcucChoiceContainerDefBuilder(EcucContainerDefBuilder):
    """Builder for EcucChoiceContainerDef with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EcucChoiceContainerDef = EcucChoiceContainerDef()


    def with_choices(self, items: list[EcucParamConfContainerDef]) -> "EcucChoiceContainerDefBuilder":
        """Set choices list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.choices = list(items) if items else []
        return self


    def add_choice(self, item: EcucParamConfContainerDef) -> "EcucChoiceContainerDefBuilder":
        """Add a single item to choices list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.choices.append(item)
        return self

    def clear_choices(self) -> "EcucChoiceContainerDefBuilder":
        """Clear all items from choices list.

        Returns:
            self for method chaining
        """
        self._obj.choices = []
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


    def build(self) -> EcucChoiceContainerDef:
        """Build and return the EcucChoiceContainerDef instance with validation."""
        self._validate_instance()
        pass
        return self._obj