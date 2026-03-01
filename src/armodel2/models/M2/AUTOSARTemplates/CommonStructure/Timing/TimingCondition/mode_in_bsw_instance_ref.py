"""ModeInBswInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 38)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingCondition.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswImplementation.bsw_implementation import (
    BswImplementation,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ModeInBswInstanceRef(ARObject):
    """AUTOSAR ModeInBswInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "MODE-IN-BSW-INSTANCE-REF"


    context_bsw_ref: Optional[ARRef]
    context_mode_ref: Optional[ARRef]
    target_mode_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "CONTEXT-BSW-REF": lambda obj, elem: setattr(obj, "context_bsw_ref", ARRef.deserialize(elem)),
        "CONTEXT-MODE-REF": lambda obj, elem: setattr(obj, "context_mode_ref", ARRef.deserialize(elem)),
        "TARGET-MODE-REF": lambda obj, elem: setattr(obj, "target_mode_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize ModeInBswInstanceRef."""
        super().__init__()
        self.context_bsw_ref: Optional[ARRef] = None
        self.context_mode_ref: Optional[ARRef] = None
        self.target_mode_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize ModeInBswInstanceRef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ModeInBswInstanceRef, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize context_bsw_ref
        if self.context_bsw_ref is not None:
            serialized = SerializationHelper.serialize_item(self.context_bsw_ref, "BswImplementation")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONTEXT-BSW-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize context_mode_ref
        if self.context_mode_ref is not None:
            serialized = SerializationHelper.serialize_item(self.context_mode_ref, "ModeDeclarationGroup")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONTEXT-MODE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize target_mode_ref
        if self.target_mode_ref is not None:
            serialized = SerializationHelper.serialize_item(self.target_mode_ref, "ModeDeclaration")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TARGET-MODE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ModeInBswInstanceRef":
        """Deserialize XML element to ModeInBswInstanceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ModeInBswInstanceRef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ModeInBswInstanceRef, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CONTEXT-BSW-REF":
                setattr(obj, "context_bsw_ref", ARRef.deserialize(child))
            elif tag == "CONTEXT-MODE-REF":
                setattr(obj, "context_mode_ref", ARRef.deserialize(child))
            elif tag == "TARGET-MODE-REF":
                setattr(obj, "target_mode_ref", ARRef.deserialize(child))

        return obj



class ModeInBswInstanceRefBuilder(BuilderBase):
    """Builder for ModeInBswInstanceRef with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ModeInBswInstanceRef = ModeInBswInstanceRef()


    def with_context_bsw(self, value: Optional[BswImplementation]) -> "ModeInBswInstanceRefBuilder":
        """Set context_bsw attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.context_bsw = value
        return self

    def with_context_mode(self, value: Optional[ModeDeclarationGroup]) -> "ModeInBswInstanceRefBuilder":
        """Set context_mode attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.context_mode = value
        return self

    def with_target_mode(self, value: Optional[ModeDeclaration]) -> "ModeInBswInstanceRefBuilder":
        """Set target_mode attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.target_mode = value
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


    def build(self) -> ModeInBswInstanceRef:
        """Build and return the ModeInBswInstanceRef instance with validation."""
        self._validate_instance()
        pass
        return self._obj