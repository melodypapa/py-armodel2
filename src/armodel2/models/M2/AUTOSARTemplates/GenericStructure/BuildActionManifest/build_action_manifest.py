"""BuildActionManifest AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 134)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 365)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 173)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_BuildActionManifest.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.BuildActionManifest.build_action import (
    BuildAction,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.BuildActionManifest.build_action_environment import (
    BuildActionEnvironment,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class BuildActionManifest(ARElement):
    """AUTOSAR BuildActionManifest."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "BUILD-ACTION-MANIFEST"


    build_actions: list[BuildActionEnvironment]
    dynamic_action_refs: list[ARRef]
    start_action_refs: list[ARRef]
    tear_down_action_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "BUILD-ACTIONS": lambda obj, elem: obj.build_actions.append(SerializationHelper.deserialize_by_tag(elem, "BuildActionEnvironment")),
        "DYNAMIC-ACTIONS": lambda obj, elem: obj.dynamic_action_refs.append(ARRef.deserialize(elem)),
        "START-ACTIONS": lambda obj, elem: obj.start_action_refs.append(ARRef.deserialize(elem)),
        "TEAR-DOWN-ACTIONS": lambda obj, elem: obj.tear_down_action_refs.append(ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize BuildActionManifest."""
        super().__init__()
        self.build_actions: list[BuildActionEnvironment] = []
        self.dynamic_action_refs: list[ARRef] = []
        self.start_action_refs: list[ARRef] = []
        self.tear_down_action_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize BuildActionManifest to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BuildActionManifest, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize build_actions (list to container "BUILD-ACTIONS")
        if self.build_actions:
            wrapper = ET.Element("BUILD-ACTIONS")
            for item in self.build_actions:
                serialized = SerializationHelper.serialize_item(item, "BuildActionEnvironment")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize dynamic_action_refs (list to container "DYNAMIC-ACTION-REFS")
        if self.dynamic_action_refs:
            wrapper = ET.Element("DYNAMIC-ACTION-REFS")
            for item in self.dynamic_action_refs:
                serialized = SerializationHelper.serialize_item(item, "BuildAction")
                if serialized is not None:
                    child_elem = ET.Element("DYNAMIC-ACTION-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize start_action_refs (list to container "START-ACTION-REFS")
        if self.start_action_refs:
            wrapper = ET.Element("START-ACTION-REFS")
            for item in self.start_action_refs:
                serialized = SerializationHelper.serialize_item(item, "BuildAction")
                if serialized is not None:
                    child_elem = ET.Element("START-ACTION-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize tear_down_action_refs (list to container "TEAR-DOWN-ACTION-REFS")
        if self.tear_down_action_refs:
            wrapper = ET.Element("TEAR-DOWN-ACTION-REFS")
            for item in self.tear_down_action_refs:
                serialized = SerializationHelper.serialize_item(item, "BuildAction")
                if serialized is not None:
                    child_elem = ET.Element("TEAR-DOWN-ACTION-REF")
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
    def deserialize(cls, element: ET.Element) -> "BuildActionManifest":
        """Deserialize XML element to BuildActionManifest object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BuildActionManifest object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BuildActionManifest, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "BUILD-ACTIONS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.build_actions.append(SerializationHelper.deserialize_by_tag(item_elem, "BuildActionEnvironment"))
            elif tag == "DYNAMIC-ACTIONS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.dynamic_action_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "BuildAction"))
            elif tag == "START-ACTIONS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.start_action_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "BuildAction"))
            elif tag == "TEAR-DOWN-ACTIONS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.tear_down_action_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "BuildAction"))

        return obj



class BuildActionManifestBuilder(ARElementBuilder):
    """Builder for BuildActionManifest with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: BuildActionManifest = BuildActionManifest()


    def with_build_actions(self, items: list[BuildActionEnvironment]) -> "BuildActionManifestBuilder":
        """Set build_actions list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.build_actions = list(items) if items else []
        return self

    def with_dynamic_actions(self, items: list[BuildAction]) -> "BuildActionManifestBuilder":
        """Set dynamic_actions list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.dynamic_actions = list(items) if items else []
        return self

    def with_start_actions(self, items: list[BuildAction]) -> "BuildActionManifestBuilder":
        """Set start_actions list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.start_actions = list(items) if items else []
        return self

    def with_tear_down_actions(self, items: list[BuildAction]) -> "BuildActionManifestBuilder":
        """Set tear_down_actions list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.tear_down_actions = list(items) if items else []
        return self


    def add_build_action(self, item: BuildActionEnvironment) -> "BuildActionManifestBuilder":
        """Add a single item to build_actions list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.build_actions.append(item)
        return self

    def clear_build_actions(self) -> "BuildActionManifestBuilder":
        """Clear all items from build_actions list.

        Returns:
            self for method chaining
        """
        self._obj.build_actions = []
        return self

    def add_dynamic_action(self, item: BuildAction) -> "BuildActionManifestBuilder":
        """Add a single item to dynamic_actions list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.dynamic_actions.append(item)
        return self

    def clear_dynamic_actions(self) -> "BuildActionManifestBuilder":
        """Clear all items from dynamic_actions list.

        Returns:
            self for method chaining
        """
        self._obj.dynamic_actions = []
        return self

    def add_start_action(self, item: BuildAction) -> "BuildActionManifestBuilder":
        """Add a single item to start_actions list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.start_actions.append(item)
        return self

    def clear_start_actions(self) -> "BuildActionManifestBuilder":
        """Clear all items from start_actions list.

        Returns:
            self for method chaining
        """
        self._obj.start_actions = []
        return self

    def add_tear_down_action(self, item: BuildAction) -> "BuildActionManifestBuilder":
        """Add a single item to tear_down_actions list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.tear_down_actions.append(item)
        return self

    def clear_tear_down_actions(self) -> "BuildActionManifestBuilder":
        """Clear all items from tear_down_actions list.

        Returns:
            self for method chaining
        """
        self._obj.tear_down_actions = []
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


    def build(self) -> BuildActionManifest:
        """Build and return the BuildActionManifest instance with validation."""
        self._validate_instance()
        pass
        return self._obj