"""ModeErrorBehavior AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 44)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 637)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ModeDeclaration.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration import (
    ModeErrorReactionPolicyEnum,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ModeErrorBehavior(ARObject):
    """AUTOSAR ModeErrorBehavior."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    default_mode_ref: Optional[ARRef]
    error_reaction: Optional[ModeErrorReactionPolicyEnum]
    def __init__(self) -> None:
        """Initialize ModeErrorBehavior."""
        super().__init__()
        self.default_mode_ref: Optional[ARRef] = None
        self.error_reaction: Optional[ModeErrorReactionPolicyEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize ModeErrorBehavior to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ModeErrorBehavior, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize default_mode_ref
        if self.default_mode_ref is not None:
            serialized = SerializationHelper.serialize_item(self.default_mode_ref, "ModeDeclaration")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DEFAULT-MODE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize error_reaction
        if self.error_reaction is not None:
            serialized = SerializationHelper.serialize_item(self.error_reaction, "ModeErrorReactionPolicyEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ERROR-REACTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ModeErrorBehavior":
        """Deserialize XML element to ModeErrorBehavior object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ModeErrorBehavior object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ModeErrorBehavior, cls).deserialize(element)

        # Parse default_mode_ref
        child = SerializationHelper.find_child_element(element, "DEFAULT-MODE-REF")
        if child is not None:
            default_mode_ref_value = ARRef.deserialize(child)
            obj.default_mode_ref = default_mode_ref_value

        # Parse error_reaction
        child = SerializationHelper.find_child_element(element, "ERROR-REACTION")
        if child is not None:
            error_reaction_value = ModeErrorReactionPolicyEnum.deserialize(child)
            obj.error_reaction = error_reaction_value

        return obj



class ModeErrorBehaviorBuilder(BuilderBase):
    """Builder for ModeErrorBehavior with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ModeErrorBehavior = ModeErrorBehavior()


    def with_default_mode(self, value: Optional[ModeDeclaration]) -> "ModeErrorBehaviorBuilder":
        """Set default_mode attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.default_mode = value
        return self

    def with_error_reaction(self, value: Optional[ModeErrorReactionPolicyEnum]) -> "ModeErrorBehaviorBuilder":
        """Set error_reaction attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.error_reaction = value
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


    def build(self) -> ModeErrorBehavior:
        """Build and return the ModeErrorBehavior instance with validation."""
        self._validate_instance()
        pass
        return self._obj