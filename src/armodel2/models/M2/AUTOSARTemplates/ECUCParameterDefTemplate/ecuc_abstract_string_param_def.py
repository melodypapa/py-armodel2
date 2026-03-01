"""EcucAbstractStringParamDef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 63)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 183)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    RegularExpression,
    VerbatimString,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class EcucAbstractStringParamDef(ARObject, ABC):
    """AUTOSAR EcucAbstractStringParamDef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    default_value: Optional[VerbatimString]
    max_length: Optional[PositiveInteger]
    min_length: Optional[PositiveInteger]
    regular: Optional[RegularExpression]
    _DESERIALIZE_DISPATCH = {
        "DEFAULT-VALUE": lambda obj, elem: setattr(obj, "default_value", SerializationHelper.deserialize_by_tag(elem, "VerbatimString")),
        "MAX-LENGTH": lambda obj, elem: setattr(obj, "max_length", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "MIN-LENGTH": lambda obj, elem: setattr(obj, "min_length", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "REGULAR": lambda obj, elem: setattr(obj, "regular", SerializationHelper.deserialize_by_tag(elem, "RegularExpression")),
    }


    def __init__(self) -> None:
        """Initialize EcucAbstractStringParamDef."""
        super().__init__()
        self.default_value: Optional[VerbatimString] = None
        self.max_length: Optional[PositiveInteger] = None
        self.min_length: Optional[PositiveInteger] = None
        self.regular: Optional[RegularExpression] = None

    def serialize(self) -> ET.Element:
        """Serialize EcucAbstractStringParamDef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcucAbstractStringParamDef, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize default_value
        if self.default_value is not None:
            serialized = SerializationHelper.serialize_item(self.default_value, "VerbatimString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DEFAULT-VALUE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_length
        if self.max_length is not None:
            serialized = SerializationHelper.serialize_item(self.max_length, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-LENGTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize min_length
        if self.min_length is not None:
            serialized = SerializationHelper.serialize_item(self.min_length, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MIN-LENGTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize regular
        if self.regular is not None:
            serialized = SerializationHelper.serialize_item(self.regular, "RegularExpression")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REGULAR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucAbstractStringParamDef":
        """Deserialize XML element to EcucAbstractStringParamDef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucAbstractStringParamDef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcucAbstractStringParamDef, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "DEFAULT-VALUE":
                setattr(obj, "default_value", SerializationHelper.deserialize_by_tag(child, "VerbatimString"))
            elif tag == "MAX-LENGTH":
                setattr(obj, "max_length", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "MIN-LENGTH":
                setattr(obj, "min_length", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "REGULAR":
                setattr(obj, "regular", SerializationHelper.deserialize_by_tag(child, "RegularExpression"))

        return obj



class EcucAbstractStringParamDefBuilder(BuilderBase, ABC):
    """Builder for EcucAbstractStringParamDef with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EcucAbstractStringParamDef = EcucAbstractStringParamDef()


    def with_default_value(self, value: Optional[VerbatimString]) -> "EcucAbstractStringParamDefBuilder":
        """Set default_value attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.default_value = value
        return self

    def with_max_length(self, value: Optional[PositiveInteger]) -> "EcucAbstractStringParamDefBuilder":
        """Set max_length attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.max_length = value
        return self

    def with_min_length(self, value: Optional[PositiveInteger]) -> "EcucAbstractStringParamDefBuilder":
        """Set min_length attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.min_length = value
        return self

    def with_regular(self, value: Optional[RegularExpression]) -> "EcucAbstractStringParamDefBuilder":
        """Set regular attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.regular = value
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


    @abstractmethod
    def build(self) -> EcucAbstractStringParamDef:
        """Build and return the EcucAbstractStringParamDef instance (abstract)."""
        raise NotImplementedError