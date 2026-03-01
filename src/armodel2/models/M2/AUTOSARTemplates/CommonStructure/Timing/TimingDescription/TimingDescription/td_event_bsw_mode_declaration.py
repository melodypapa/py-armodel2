"""TDEventBswModeDeclaration AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 76)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_bsw import (
    TDEventBsw,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_bsw import TDEventBswBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class TDEventBswModeDeclaration(TDEventBsw):
    """AUTOSAR TDEventBswModeDeclaration."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "T-D-EVENT-BSW-MODE-DECLARATION"


    entry_mode_ref: Optional[ARRef]
    exit_mode_ref: Optional[ARRef]
    mode_ref: Optional[ARRef]
    td_event_bsw_declaration_type: Optional[Any]
    _DESERIALIZE_DISPATCH = {
        "ENTRY-MODE-REF": lambda obj, elem: setattr(obj, "entry_mode_ref", ARRef.deserialize(elem)),
        "EXIT-MODE-REF": lambda obj, elem: setattr(obj, "exit_mode_ref", ARRef.deserialize(elem)),
        "MODE-REF": lambda obj, elem: setattr(obj, "mode_ref", ARRef.deserialize(elem)),
        "TD-EVENT-BSW-DECLARATION-TYPE": lambda obj, elem: setattr(obj, "td_event_bsw_declaration_type", SerializationHelper.deserialize_by_tag(elem, "any (TDEventBswMode)")),
    }


    def __init__(self) -> None:
        """Initialize TDEventBswModeDeclaration."""
        super().__init__()
        self.entry_mode_ref: Optional[ARRef] = None
        self.exit_mode_ref: Optional[ARRef] = None
        self.mode_ref: Optional[ARRef] = None
        self.td_event_bsw_declaration_type: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize TDEventBswModeDeclaration to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TDEventBswModeDeclaration, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize entry_mode_ref
        if self.entry_mode_ref is not None:
            serialized = SerializationHelper.serialize_item(self.entry_mode_ref, "ModeDeclaration")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ENTRY-MODE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize exit_mode_ref
        if self.exit_mode_ref is not None:
            serialized = SerializationHelper.serialize_item(self.exit_mode_ref, "ModeDeclaration")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EXIT-MODE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mode_ref
        if self.mode_ref is not None:
            serialized = SerializationHelper.serialize_item(self.mode_ref, "ModeDeclarationGroup")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MODE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize td_event_bsw_declaration_type
        if self.td_event_bsw_declaration_type is not None:
            serialized = SerializationHelper.serialize_item(self.td_event_bsw_declaration_type, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TD-EVENT-BSW-DECLARATION-TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventBswModeDeclaration":
        """Deserialize XML element to TDEventBswModeDeclaration object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TDEventBswModeDeclaration object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TDEventBswModeDeclaration, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ENTRY-MODE-REF":
                setattr(obj, "entry_mode_ref", ARRef.deserialize(child))
            elif tag == "EXIT-MODE-REF":
                setattr(obj, "exit_mode_ref", ARRef.deserialize(child))
            elif tag == "MODE-REF":
                setattr(obj, "mode_ref", ARRef.deserialize(child))
            elif tag == "TD-EVENT-BSW-DECLARATION-TYPE":
                setattr(obj, "td_event_bsw_declaration_type", SerializationHelper.deserialize_by_tag(child, "any (TDEventBswMode)"))

        return obj



class TDEventBswModeDeclarationBuilder(TDEventBswBuilder):
    """Builder for TDEventBswModeDeclaration with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TDEventBswModeDeclaration = TDEventBswModeDeclaration()


    def with_entry_mode(self, value: Optional[ModeDeclaration]) -> "TDEventBswModeDeclarationBuilder":
        """Set entry_mode attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.entry_mode = value
        return self

    def with_exit_mode(self, value: Optional[ModeDeclaration]) -> "TDEventBswModeDeclarationBuilder":
        """Set exit_mode attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.exit_mode = value
        return self

    def with_mode(self, value: Optional[ModeDeclarationGroup]) -> "TDEventBswModeDeclarationBuilder":
        """Set mode attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.mode = value
        return self

    def with_td_event_bsw_declaration_type(self, value: Optional[any (TDEventBswMode)]) -> "TDEventBswModeDeclarationBuilder":
        """Set td_event_bsw_declaration_type attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.td_event_bsw_declaration_type = value
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


    def build(self) -> TDEventBswModeDeclaration:
        """Build and return the TDEventBswModeDeclaration instance with validation."""
        self._validate_instance()
        pass
        return self._obj