"""EcucParameterValue AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 124)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 442)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 189)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCDescriptionTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.ecuc_indexable_value import (
    EcucIndexableValue,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.ecuc_indexable_value import EcucIndexableValueBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel2.models.M2.MSR.Documentation.Annotation.annotation import (
    Annotation,
)
from armodel2.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_parameter_def import (
    EcucParameterDef,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class EcucParameterValue(EcucIndexableValue, ABC):
    """AUTOSAR EcucParameterValue."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    annotations: list[Annotation]
    definition_ref: Optional[ARRef]
    is_auto_value: Optional[Boolean]
    _DESERIALIZE_DISPATCH = {
        "ANNOTATIONS": lambda obj, elem: obj.annotations.append(SerializationHelper.deserialize_by_tag(elem, "Annotation")),
        "DEFINITION-REF": ("_POLYMORPHIC", "definition_ref", ["EcucAbstractStringParamDef", "EcucAddInfoParamDef", "EcucBooleanParamDef", "EcucEnumerationParamDef", "EcucFloatParamDef", "EcucIntegerParamDef"]),
        "IS-AUTO-VALUE": lambda obj, elem: setattr(obj, "is_auto_value", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
    }


    def __init__(self) -> None:
        """Initialize EcucParameterValue."""
        super().__init__()
        self.annotations: list[Annotation] = []
        self.definition_ref: Optional[ARRef] = None
        self.is_auto_value: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize EcucParameterValue to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcucParameterValue, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize annotations (list to container "ANNOTATIONS")
        if self.annotations:
            wrapper = ET.Element("ANNOTATIONS")
            for item in self.annotations:
                serialized = SerializationHelper.serialize_item(item, "Annotation")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize definition_ref
        if self.definition_ref is not None:
            serialized = SerializationHelper.serialize_item(self.definition_ref, "EcucParameterDef")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DEFINITION-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize is_auto_value
        if self.is_auto_value is not None:
            serialized = SerializationHelper.serialize_item(self.is_auto_value, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IS-AUTO-VALUE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucParameterValue":
        """Deserialize XML element to EcucParameterValue object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucParameterValue object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcucParameterValue, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "ANNOTATIONS":
                obj.annotations.append(SerializationHelper.deserialize_by_tag(child, "Annotation"))
            elif tag == "DEFINITION-REF":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "ECUC-ABSTRACT-STRING-PARAM-DEF":
                        setattr(obj, "definition_ref", SerializationHelper.deserialize_by_tag(child[0], "EcucAbstractStringParamDef"))
                    elif concrete_tag == "ECUC-ADD-INFO-PARAM-DEF":
                        setattr(obj, "definition_ref", SerializationHelper.deserialize_by_tag(child[0], "EcucAddInfoParamDef"))
                    elif concrete_tag == "ECUC-BOOLEAN-PARAM-DEF":
                        setattr(obj, "definition_ref", SerializationHelper.deserialize_by_tag(child[0], "EcucBooleanParamDef"))
                    elif concrete_tag == "ECUC-ENUMERATION-PARAM-DEF":
                        setattr(obj, "definition_ref", SerializationHelper.deserialize_by_tag(child[0], "EcucEnumerationParamDef"))
                    elif concrete_tag == "ECUC-FLOAT-PARAM-DEF":
                        setattr(obj, "definition_ref", SerializationHelper.deserialize_by_tag(child[0], "EcucFloatParamDef"))
                    elif concrete_tag == "ECUC-INTEGER-PARAM-DEF":
                        setattr(obj, "definition_ref", SerializationHelper.deserialize_by_tag(child[0], "EcucIntegerParamDef"))
            elif tag == "IS-AUTO-VALUE":
                setattr(obj, "is_auto_value", SerializationHelper.deserialize_by_tag(child, "Boolean"))

        return obj



class EcucParameterValueBuilder(EcucIndexableValueBuilder):
    """Builder for EcucParameterValue with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EcucParameterValue = EcucParameterValue()


    def with_annotations(self, items: list[Annotation]) -> "EcucParameterValueBuilder":
        """Set annotations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.annotations = list(items) if items else []
        return self

    def with_definition(self, value: Optional[EcucParameterDef]) -> "EcucParameterValueBuilder":
        """Set definition attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.definition = value
        return self

    def with_is_auto_value(self, value: Optional[Boolean]) -> "EcucParameterValueBuilder":
        """Set is_auto_value attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.is_auto_value = value
        return self


    def add_annotation(self, item: Annotation) -> "EcucParameterValueBuilder":
        """Add a single item to annotations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.annotations.append(item)
        return self

    def clear_annotations(self) -> "EcucParameterValueBuilder":
        """Clear all items from annotations list.

        Returns:
            self for method chaining
        """
        self._obj.annotations = []
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
    def build(self) -> EcucParameterValue:
        """Build and return the EcucParameterValue instance (abstract)."""
        raise NotImplementedError