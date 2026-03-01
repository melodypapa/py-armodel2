"""BuildAction AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 366)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 172)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_BuildActionManifest.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.BuildActionManifest.build_action_entity import (
    BuildActionEntity,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.BuildActionManifest.build_action_entity import BuildActionEntityBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.BuildActionManifest.build_action_environment import (
    BuildActionEnvironment,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.BuildActionManifest.build_action_io_element import (
    BuildActionIoElement,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class BuildAction(BuildActionEntity):
    """AUTOSAR BuildAction."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "BUILD-ACTION"


    created_datas: list[BuildActionIoElement]
    follow_up_action_refs: list[ARRef]
    input_datas: list[BuildActionIoElement]
    modified_datas: list[BuildActionIoElement]
    predecessor_refs: list[ARRef]
    required_ref: ARRef
    _DESERIALIZE_DISPATCH = {
        "CREATED-DATAS": lambda obj, elem: obj.created_datas.append(SerializationHelper.deserialize_by_tag(elem, "BuildActionIoElement")),
        "FOLLOW-UP-ACTIONS": lambda obj, elem: obj.follow_up_action_refs.append(ARRef.deserialize(elem)),
        "INPUT-DATAS": lambda obj, elem: obj.input_datas.append(SerializationHelper.deserialize_by_tag(elem, "BuildActionIoElement")),
        "MODIFIED-DATAS": lambda obj, elem: obj.modified_datas.append(SerializationHelper.deserialize_by_tag(elem, "BuildActionIoElement")),
        "PREDECESSORS": lambda obj, elem: obj.predecessor_refs.append(ARRef.deserialize(elem)),
        "REQUIRED-REF": lambda obj, elem: setattr(obj, "required_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize BuildAction."""
        super().__init__()
        self.created_datas: list[BuildActionIoElement] = []
        self.follow_up_action_refs: list[ARRef] = []
        self.input_datas: list[BuildActionIoElement] = []
        self.modified_datas: list[BuildActionIoElement] = []
        self.predecessor_refs: list[ARRef] = []
        self.required_ref: ARRef = None

    def serialize(self) -> ET.Element:
        """Serialize BuildAction to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BuildAction, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize created_datas (list to container "CREATED-DATAS")
        if self.created_datas:
            wrapper = ET.Element("CREATED-DATAS")
            for item in self.created_datas:
                serialized = SerializationHelper.serialize_item(item, "BuildActionIoElement")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize follow_up_action_refs (list to container "FOLLOW-UP-ACTION-REFS")
        if self.follow_up_action_refs:
            wrapper = ET.Element("FOLLOW-UP-ACTION-REFS")
            for item in self.follow_up_action_refs:
                serialized = SerializationHelper.serialize_item(item, "BuildAction")
                if serialized is not None:
                    child_elem = ET.Element("FOLLOW-UP-ACTION-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize input_datas (list to container "INPUT-DATAS")
        if self.input_datas:
            wrapper = ET.Element("INPUT-DATAS")
            for item in self.input_datas:
                serialized = SerializationHelper.serialize_item(item, "BuildActionIoElement")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize modified_datas (list to container "MODIFIED-DATAS")
        if self.modified_datas:
            wrapper = ET.Element("MODIFIED-DATAS")
            for item in self.modified_datas:
                serialized = SerializationHelper.serialize_item(item, "BuildActionIoElement")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize predecessor_refs (list to container "PREDECESSOR-REFS")
        if self.predecessor_refs:
            wrapper = ET.Element("PREDECESSOR-REFS")
            for item in self.predecessor_refs:
                serialized = SerializationHelper.serialize_item(item, "BuildAction")
                if serialized is not None:
                    child_elem = ET.Element("PREDECESSOR-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize required_ref
        if self.required_ref is not None:
            serialized = SerializationHelper.serialize_item(self.required_ref, "BuildActionEnvironment")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REQUIRED-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BuildAction":
        """Deserialize XML element to BuildAction object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BuildAction object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BuildAction, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "CREATED-DATAS":
                # Iterate through wrapper children
                for item_elem in child:
                    item_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    obj.created_datas.append(SerializationHelper.deserialize_by_tag(item_elem, "BuildActionIoElement"))
            elif tag == "FOLLOW-UP-ACTIONS":
                # Iterate through wrapper children
                for item_elem in child:
                    item_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    obj.follow_up_action_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "BuildAction"))
            elif tag == "INPUT-DATAS":
                # Iterate through wrapper children
                for item_elem in child:
                    item_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    obj.input_datas.append(SerializationHelper.deserialize_by_tag(item_elem, "BuildActionIoElement"))
            elif tag == "MODIFIED-DATAS":
                # Iterate through wrapper children
                for item_elem in child:
                    item_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    obj.modified_datas.append(SerializationHelper.deserialize_by_tag(item_elem, "BuildActionIoElement"))
            elif tag == "PREDECESSORS":
                # Iterate through wrapper children
                for item_elem in child:
                    item_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    obj.predecessor_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "BuildAction"))
            elif tag == "REQUIRED-REF":
                setattr(obj, "required_ref", ARRef.deserialize(child))

        return obj



class BuildActionBuilder(BuildActionEntityBuilder):
    """Builder for BuildAction with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: BuildAction = BuildAction()


    def with_created_datas(self, items: list[BuildActionIoElement]) -> "BuildActionBuilder":
        """Set created_datas list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.created_datas = list(items) if items else []
        return self

    def with_follow_up_actions(self, items: list[BuildAction]) -> "BuildActionBuilder":
        """Set follow_up_actions list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.follow_up_actions = list(items) if items else []
        return self

    def with_input_datas(self, items: list[BuildActionIoElement]) -> "BuildActionBuilder":
        """Set input_datas list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.input_datas = list(items) if items else []
        return self

    def with_modified_datas(self, items: list[BuildActionIoElement]) -> "BuildActionBuilder":
        """Set modified_datas list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.modified_datas = list(items) if items else []
        return self

    def with_predecessors(self, items: list[BuildAction]) -> "BuildActionBuilder":
        """Set predecessors list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.predecessors = list(items) if items else []
        return self

    def with_required(self, value: BuildActionEnvironment) -> "BuildActionBuilder":
        """Set required attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.required = value
        return self


    def add_created_data(self, item: BuildActionIoElement) -> "BuildActionBuilder":
        """Add a single item to created_datas list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.created_datas.append(item)
        return self

    def clear_created_datas(self) -> "BuildActionBuilder":
        """Clear all items from created_datas list.

        Returns:
            self for method chaining
        """
        self._obj.created_datas = []
        return self

    def add_follow_up_action(self, item: BuildAction) -> "BuildActionBuilder":
        """Add a single item to follow_up_actions list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.follow_up_actions.append(item)
        return self

    def clear_follow_up_actions(self) -> "BuildActionBuilder":
        """Clear all items from follow_up_actions list.

        Returns:
            self for method chaining
        """
        self._obj.follow_up_actions = []
        return self

    def add_input_data(self, item: BuildActionIoElement) -> "BuildActionBuilder":
        """Add a single item to input_datas list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.input_datas.append(item)
        return self

    def clear_input_datas(self) -> "BuildActionBuilder":
        """Clear all items from input_datas list.

        Returns:
            self for method chaining
        """
        self._obj.input_datas = []
        return self

    def add_modified_data(self, item: BuildActionIoElement) -> "BuildActionBuilder":
        """Add a single item to modified_datas list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.modified_datas.append(item)
        return self

    def clear_modified_datas(self) -> "BuildActionBuilder":
        """Clear all items from modified_datas list.

        Returns:
            self for method chaining
        """
        self._obj.modified_datas = []
        return self

    def add_predecessor(self, item: BuildAction) -> "BuildActionBuilder":
        """Add a single item to predecessors list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.predecessors.append(item)
        return self

    def clear_predecessors(self) -> "BuildActionBuilder":
        """Clear all items from predecessors list.

        Returns:
            self for method chaining
        """
        self._obj.predecessors = []
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


    def build(self) -> BuildAction:
        """Build and return the BuildAction instance with validation."""
        self._validate_instance()
        pass
        return self._obj