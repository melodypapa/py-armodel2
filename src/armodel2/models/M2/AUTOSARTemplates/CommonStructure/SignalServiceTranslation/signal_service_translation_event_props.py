"""SignalServiceTranslationEventProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 731)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_SignalServiceTranslation.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SignalServiceTranslationEventProps(Identifiable):
    """AUTOSAR SignalServiceTranslationEventProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SIGNAL-SERVICE-TRANSLATION-EVENT-PROPS"


    element_propses: list[Any]
    safe_translation: Optional[Boolean]
    secure: Optional[Boolean]
    translation_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "ELEMENT-PROPSS": lambda obj, elem: obj.element_propses.append(SerializationHelper.deserialize_by_tag(elem, "any (SignalService)")),
        "SAFE-TRANSLATION": lambda obj, elem: setattr(obj, "safe_translation", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "SECURE": lambda obj, elem: setattr(obj, "secure", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "TRANSLATION-REF": lambda obj, elem: setattr(obj, "translation_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize SignalServiceTranslationEventProps."""
        super().__init__()
        self.element_propses: list[Any] = []
        self.safe_translation: Optional[Boolean] = None
        self.secure: Optional[Boolean] = None
        self.translation_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize SignalServiceTranslationEventProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SignalServiceTranslationEventProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize element_propses (list to container "ELEMENT-PROPSS")
        if self.element_propses:
            wrapper = ET.Element("ELEMENT-PROPSS")
            for item in self.element_propses:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize safe_translation
        if self.safe_translation is not None:
            serialized = SerializationHelper.serialize_item(self.safe_translation, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SAFE-TRANSLATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize secure
        if self.secure is not None:
            serialized = SerializationHelper.serialize_item(self.secure, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SECURE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize translation_ref
        if self.translation_ref is not None:
            serialized = SerializationHelper.serialize_item(self.translation_ref, "VariableDataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TRANSLATION-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SignalServiceTranslationEventProps":
        """Deserialize XML element to SignalServiceTranslationEventProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SignalServiceTranslationEventProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SignalServiceTranslationEventProps, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ELEMENT-PROPSS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.element_propses.append(SerializationHelper.deserialize_by_tag(item_elem, "any (SignalService)"))
            elif tag == "SAFE-TRANSLATION":
                setattr(obj, "safe_translation", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "SECURE":
                setattr(obj, "secure", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "TRANSLATION-REF":
                setattr(obj, "translation_ref", ARRef.deserialize(child))

        return obj



class SignalServiceTranslationEventPropsBuilder(IdentifiableBuilder):
    """Builder for SignalServiceTranslationEventProps with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SignalServiceTranslationEventProps = SignalServiceTranslationEventProps()


    def with_element_propses(self, items: list[any (SignalService)]) -> "SignalServiceTranslationEventPropsBuilder":
        """Set element_propses list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.element_propses = list(items) if items else []
        return self

    def with_safe_translation(self, value: Optional[Boolean]) -> "SignalServiceTranslationEventPropsBuilder":
        """Set safe_translation attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.safe_translation = value
        return self

    def with_secure(self, value: Optional[Boolean]) -> "SignalServiceTranslationEventPropsBuilder":
        """Set secure attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.secure = value
        return self

    def with_translation(self, value: Optional[VariableDataPrototype]) -> "SignalServiceTranslationEventPropsBuilder":
        """Set translation attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.translation = value
        return self


    def add_element_props(self, item: any (SignalService)) -> "SignalServiceTranslationEventPropsBuilder":
        """Add a single item to element_propses list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.element_propses.append(item)
        return self

    def clear_element_propses(self) -> "SignalServiceTranslationEventPropsBuilder":
        """Clear all items from element_propses list.

        Returns:
            self for method chaining
        """
        self._obj.element_propses = []
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


    def build(self) -> SignalServiceTranslationEventProps:
        """Build and return the SignalServiceTranslationEventProps instance with validation."""
        self._validate_instance()
        pass
        return self._obj