"""SignalServiceTranslationElementProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 735)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_SignalServiceTranslation.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
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
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Filter.data_filter import (
    DataFilter,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SignalServiceTranslationElementProps(Identifiable):
    """AUTOSAR SignalServiceTranslationElementProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SIGNAL-SERVICE-TRANSLATION-ELEMENT-PROPS"


    element_ref: Optional[ARRef]
    filter: Optional[DataFilter]
    transmission: Optional[Boolean]
    _DESERIALIZE_DISPATCH = {
        "ELEMENT-REF": ("_POLYMORPHIC", "element_ref", ["ApplicationCompositeElementDataPrototype", "AutosarDataPrototype"]),
        "FILTER": lambda obj, elem: setattr(obj, "filter", SerializationHelper.deserialize_by_tag(elem, "DataFilter")),
        "TRANSMISSION": lambda obj, elem: setattr(obj, "transmission", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
    }


    def __init__(self) -> None:
        """Initialize SignalServiceTranslationElementProps."""
        super().__init__()
        self.element_ref: Optional[ARRef] = None
        self.filter: Optional[DataFilter] = None
        self.transmission: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize SignalServiceTranslationElementProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SignalServiceTranslationElementProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize element_ref
        if self.element_ref is not None:
            serialized = SerializationHelper.serialize_item(self.element_ref, "DataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ELEMENT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize filter
        if self.filter is not None:
            serialized = SerializationHelper.serialize_item(self.filter, "DataFilter")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FILTER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize transmission
        if self.transmission is not None:
            serialized = SerializationHelper.serialize_item(self.transmission, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TRANSMISSION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SignalServiceTranslationElementProps":
        """Deserialize XML element to SignalServiceTranslationElementProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SignalServiceTranslationElementProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SignalServiceTranslationElementProps, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ELEMENT-REF":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "APPLICATION-COMPOSITE-ELEMENT-DATA-PROTOTYPE":
                        setattr(obj, "element_ref", SerializationHelper.deserialize_by_tag(child[0], "ApplicationCompositeElementDataPrototype"))
                    elif concrete_tag == "AUTOSAR-DATA-PROTOTYPE":
                        setattr(obj, "element_ref", SerializationHelper.deserialize_by_tag(child[0], "AutosarDataPrototype"))
            elif tag == "FILTER":
                setattr(obj, "filter", SerializationHelper.deserialize_by_tag(child, "DataFilter"))
            elif tag == "TRANSMISSION":
                setattr(obj, "transmission", SerializationHelper.deserialize_by_tag(child, "Boolean"))

        return obj



class SignalServiceTranslationElementPropsBuilder(IdentifiableBuilder):
    """Builder for SignalServiceTranslationElementProps with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SignalServiceTranslationElementProps = SignalServiceTranslationElementProps()


    def with_element(self, value: Optional[DataPrototype]) -> "SignalServiceTranslationElementPropsBuilder":
        """Set element attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.element = value
        return self

    def with_filter(self, value: Optional[DataFilter]) -> "SignalServiceTranslationElementPropsBuilder":
        """Set filter attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.filter = value
        return self

    def with_transmission(self, value: Optional[Boolean]) -> "SignalServiceTranslationElementPropsBuilder":
        """Set transmission attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.transmission = value
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


    def build(self) -> SignalServiceTranslationElementProps:
        """Build and return the SignalServiceTranslationElementProps instance with validation."""
        self._validate_instance()
        pass
        return self._obj