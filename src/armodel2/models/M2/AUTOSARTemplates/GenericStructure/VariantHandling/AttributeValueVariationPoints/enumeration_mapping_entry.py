"""EnumerationMappingEntry AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 443)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_VariantHandling_AttributeValueVariationPoints.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class EnumerationMappingEntry(ARObject):
    """AUTOSAR EnumerationMappingEntry."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "ENUMERATION-MAPPING-ENTRY"


    enumerator: NameToken
    numerical_value: PositiveInteger
    _DESERIALIZE_DISPATCH = {
        "ENUMERATOR": lambda obj, elem: setattr(obj, "enumerator", elem.text),
        "NUMERICAL-VALUE": lambda obj, elem: setattr(obj, "numerical_value", elem.text),
    }


    def __init__(self) -> None:
        """Initialize EnumerationMappingEntry."""
        super().__init__()
        self.enumerator: NameToken = None
        self.numerical_value: PositiveInteger = None

    def serialize(self) -> ET.Element:
        """Serialize EnumerationMappingEntry to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EnumerationMappingEntry, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize enumerator
        if self.enumerator is not None:
            serialized = SerializationHelper.serialize_item(self.enumerator, "NameToken")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ENUMERATOR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize numerical_value
        if self.numerical_value is not None:
            serialized = SerializationHelper.serialize_item(self.numerical_value, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NUMERICAL-VALUE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EnumerationMappingEntry":
        """Deserialize XML element to EnumerationMappingEntry object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EnumerationMappingEntry object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EnumerationMappingEntry, cls).deserialize(element)

        # Parse enumerator
        child = SerializationHelper.find_child_element(element, "ENUMERATOR")
        if child is not None:
            enumerator_value = child.text
            obj.enumerator = enumerator_value

        # Parse numerical_value
        child = SerializationHelper.find_child_element(element, "NUMERICAL-VALUE")
        if child is not None:
            numerical_value_value = child.text
            obj.numerical_value = numerical_value_value

        return obj



class EnumerationMappingEntryBuilder(BuilderBase):
    """Builder for EnumerationMappingEntry with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EnumerationMappingEntry = EnumerationMappingEntry()


    def with_enumerator(self, value: NameToken) -> "EnumerationMappingEntryBuilder":
        """Set enumerator attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.enumerator = value
        return self

    def with_numerical_value(self, value: PositiveInteger) -> "EnumerationMappingEntryBuilder":
        """Set numerical_value attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.numerical_value = value
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


    def build(self) -> EnumerationMappingEntry:
        """Build and return the EnumerationMappingEntry instance with validation."""
        self._validate_instance()
        pass
        return self._obj