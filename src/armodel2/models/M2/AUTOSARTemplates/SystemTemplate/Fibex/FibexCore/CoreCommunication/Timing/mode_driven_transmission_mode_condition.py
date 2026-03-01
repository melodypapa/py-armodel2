"""ModeDrivenTransmissionModeCondition AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 393)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication_Timing.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ModeDrivenTransmissionModeCondition(ARObject):
    """AUTOSAR ModeDrivenTransmissionModeCondition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "MODE-DRIVEN-TRANSMISSION-MODE-CONDITION"


    mode_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "MODE-REFS": lambda obj, elem: obj.mode_refs.append(ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize ModeDrivenTransmissionModeCondition."""
        super().__init__()
        self.mode_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize ModeDrivenTransmissionModeCondition to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ModeDrivenTransmissionModeCondition, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize mode_refs (list to container "MODE-REFS")
        if self.mode_refs:
            wrapper = ET.Element("MODE-REFS")
            for item in self.mode_refs:
                serialized = SerializationHelper.serialize_item(item, "ModeDeclaration")
                if serialized is not None:
                    child_elem = ET.Element("MODE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ModeDrivenTransmissionModeCondition":
        """Deserialize XML element to ModeDrivenTransmissionModeCondition object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ModeDrivenTransmissionModeCondition object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ModeDrivenTransmissionModeCondition, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "MODE-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.mode_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "ModeDeclaration"))

        return obj



class ModeDrivenTransmissionModeConditionBuilder(BuilderBase):
    """Builder for ModeDrivenTransmissionModeCondition with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ModeDrivenTransmissionModeCondition = ModeDrivenTransmissionModeCondition()


    def with_modes(self, items: list[ModeDeclaration]) -> "ModeDrivenTransmissionModeConditionBuilder":
        """Set modes list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.modes = list(items) if items else []
        return self


    def add_mode(self, item: ModeDeclaration) -> "ModeDrivenTransmissionModeConditionBuilder":
        """Add a single item to modes list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.modes.append(item)
        return self

    def clear_modes(self) -> "ModeDrivenTransmissionModeConditionBuilder":
        """Clear all items from modes list.

        Returns:
            self for method chaining
        """
        self._obj.modes = []
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


    def build(self) -> ModeDrivenTransmissionModeCondition:
        """Build and return the ModeDrivenTransmissionModeCondition instance with validation."""
        self._validate_instance()
        pass
        return self._obj