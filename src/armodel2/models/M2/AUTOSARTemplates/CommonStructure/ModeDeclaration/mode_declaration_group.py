"""ModeDeclarationGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 42)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 322)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 628)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2038)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 197)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ModeDeclaration.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_error_behavior import (
    ModeErrorBehavior,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_transition import (
    ModeTransition,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ModeDeclarationGroup(ARElement):
    """AUTOSAR ModeDeclarationGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "MODE-DECLARATION-GROUP"


    initial_mode_ref: Optional[ARRef]
    mode_declarations: list[ModeDeclaration]
    mode_manager_error_behavior: Optional[ModeErrorBehavior]
    mode_transitions: list[ModeTransition]
    mode_user_error_behavior: Optional[ModeErrorBehavior]
    on_transition_value: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "INITIAL-MODE-REF": lambda obj, elem: setattr(obj, "initial_mode_ref", ARRef.deserialize(elem)),
        "MODE-DECLARATIONS": lambda obj, elem: obj.mode_declarations.append(SerializationHelper.deserialize_by_tag(elem, "ModeDeclaration")),
        "MODE-MANAGER-ERROR-BEHAVIOR": lambda obj, elem: setattr(obj, "mode_manager_error_behavior", SerializationHelper.deserialize_by_tag(elem, "ModeErrorBehavior")),
        "MODE-TRANSITIONS": lambda obj, elem: obj.mode_transitions.append(SerializationHelper.deserialize_by_tag(elem, "ModeTransition")),
        "MODE-USER-ERROR-BEHAVIOR": lambda obj, elem: setattr(obj, "mode_user_error_behavior", SerializationHelper.deserialize_by_tag(elem, "ModeErrorBehavior")),
        "ON-TRANSITION-VALUE": lambda obj, elem: setattr(obj, "on_transition_value", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize ModeDeclarationGroup."""
        super().__init__()
        self.initial_mode_ref: Optional[ARRef] = None
        self.mode_declarations: list[ModeDeclaration] = []
        self.mode_manager_error_behavior: Optional[ModeErrorBehavior] = None
        self.mode_transitions: list[ModeTransition] = []
        self.mode_user_error_behavior: Optional[ModeErrorBehavior] = None
        self.on_transition_value: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize ModeDeclarationGroup to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ModeDeclarationGroup, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize initial_mode_ref
        if self.initial_mode_ref is not None:
            serialized = SerializationHelper.serialize_item(self.initial_mode_ref, "ModeDeclaration")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INITIAL-MODE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mode_declarations (list to container "MODE-DECLARATIONS")
        if self.mode_declarations:
            wrapper = ET.Element("MODE-DECLARATIONS")
            for item in self.mode_declarations:
                serialized = SerializationHelper.serialize_item(item, "ModeDeclaration")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize mode_manager_error_behavior
        if self.mode_manager_error_behavior is not None:
            serialized = SerializationHelper.serialize_item(self.mode_manager_error_behavior, "ModeErrorBehavior")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MODE-MANAGER-ERROR-BEHAVIOR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mode_transitions (list to container "MODE-TRANSITIONS")
        if self.mode_transitions:
            wrapper = ET.Element("MODE-TRANSITIONS")
            for item in self.mode_transitions:
                serialized = SerializationHelper.serialize_item(item, "ModeTransition")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize mode_user_error_behavior
        if self.mode_user_error_behavior is not None:
            serialized = SerializationHelper.serialize_item(self.mode_user_error_behavior, "ModeErrorBehavior")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MODE-USER-ERROR-BEHAVIOR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize on_transition_value
        if self.on_transition_value is not None:
            serialized = SerializationHelper.serialize_item(self.on_transition_value, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ON-TRANSITION-VALUE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ModeDeclarationGroup":
        """Deserialize XML element to ModeDeclarationGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ModeDeclarationGroup object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ModeDeclarationGroup, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "INITIAL-MODE-REF":
                setattr(obj, "initial_mode_ref", ARRef.deserialize(child))
            elif tag == "MODE-DECLARATIONS":
                obj.mode_declarations.append(SerializationHelper.deserialize_by_tag(child, "ModeDeclaration"))
            elif tag == "MODE-MANAGER-ERROR-BEHAVIOR":
                setattr(obj, "mode_manager_error_behavior", SerializationHelper.deserialize_by_tag(child, "ModeErrorBehavior"))
            elif tag == "MODE-TRANSITIONS":
                obj.mode_transitions.append(SerializationHelper.deserialize_by_tag(child, "ModeTransition"))
            elif tag == "MODE-USER-ERROR-BEHAVIOR":
                setattr(obj, "mode_user_error_behavior", SerializationHelper.deserialize_by_tag(child, "ModeErrorBehavior"))
            elif tag == "ON-TRANSITION-VALUE":
                setattr(obj, "on_transition_value", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class ModeDeclarationGroupBuilder(ARElementBuilder):
    """Builder for ModeDeclarationGroup with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ModeDeclarationGroup = ModeDeclarationGroup()


    def with_initial_mode(self, value: Optional[ModeDeclaration]) -> "ModeDeclarationGroupBuilder":
        """Set initial_mode attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.initial_mode = value
        return self

    def with_mode_declarations(self, items: list[ModeDeclaration]) -> "ModeDeclarationGroupBuilder":
        """Set mode_declarations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.mode_declarations = list(items) if items else []
        return self

    def with_mode_manager_error_behavior(self, value: Optional[ModeErrorBehavior]) -> "ModeDeclarationGroupBuilder":
        """Set mode_manager_error_behavior attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.mode_manager_error_behavior = value
        return self

    def with_mode_transitions(self, items: list[ModeTransition]) -> "ModeDeclarationGroupBuilder":
        """Set mode_transitions list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.mode_transitions = list(items) if items else []
        return self

    def with_mode_user_error_behavior(self, value: Optional[ModeErrorBehavior]) -> "ModeDeclarationGroupBuilder":
        """Set mode_user_error_behavior attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.mode_user_error_behavior = value
        return self

    def with_on_transition_value(self, value: Optional[PositiveInteger]) -> "ModeDeclarationGroupBuilder":
        """Set on_transition_value attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.on_transition_value = value
        return self


    def add_mode_declaration(self, item: ModeDeclaration) -> "ModeDeclarationGroupBuilder":
        """Add a single item to mode_declarations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.mode_declarations.append(item)
        return self

    def clear_mode_declarations(self) -> "ModeDeclarationGroupBuilder":
        """Clear all items from mode_declarations list.

        Returns:
            self for method chaining
        """
        self._obj.mode_declarations = []
        return self

    def add_mode_transition(self, item: ModeTransition) -> "ModeDeclarationGroupBuilder":
        """Add a single item to mode_transitions list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.mode_transitions.append(item)
        return self

    def clear_mode_transitions(self) -> "ModeDeclarationGroupBuilder":
        """Clear all items from mode_transitions list.

        Returns:
            self for method chaining
        """
        self._obj.mode_transitions = []
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


    def build(self) -> ModeDeclarationGroup:
        """Build and return the ModeDeclarationGroup instance with validation."""
        self._validate_instance()
        pass
        return self._obj