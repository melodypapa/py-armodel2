"""CryptoServiceKey AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 377)
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 58)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    String,
)

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
        ValueSpecification,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class CryptoServiceKey(ARElement):
    """AUTOSAR CryptoServiceKey."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "CRYPTO-SERVICE-KEY"


    algorithm_family: Optional[String]
    development: Optional[ValueSpecification]
    key_generation: Optional[CryptoServiceKey]
    key_storage_type: Optional[String]
    length: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "ALGORITHM-FAMILY": lambda obj, elem: setattr(obj, "algorithm_family", SerializationHelper.deserialize_by_tag(elem, "String")),
        "DEVELOPMENT": ("_POLYMORPHIC", "development", ["AbstractRuleBasedValueSpecification", "ApplicationValueSpecification", "CompositeValueSpecification", "ConstantReference", "NotAvailableValueSpecification", "NumericalValueSpecification", "ReferenceValueSpecification", "TextValueSpecification"]),
        "KEY-GENERATION": lambda obj, elem: setattr(obj, "key_generation", SerializationHelper.deserialize_by_tag(elem, "CryptoServiceKey")),
        "KEY-STORAGE-TYPE": lambda obj, elem: setattr(obj, "key_storage_type", SerializationHelper.deserialize_by_tag(elem, "String")),
        "LENGTH": lambda obj, elem: setattr(obj, "length", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize CryptoServiceKey."""
        super().__init__()
        self.algorithm_family: Optional[String] = None
        self.development: Optional[ValueSpecification] = None
        self.key_generation: Optional[CryptoServiceKey] = None
        self.key_storage_type: Optional[String] = None
        self.length: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize CryptoServiceKey to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CryptoServiceKey, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize algorithm_family
        if self.algorithm_family is not None:
            serialized = SerializationHelper.serialize_item(self.algorithm_family, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ALGORITHM-FAMILY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize development
        if self.development is not None:
            serialized = SerializationHelper.serialize_item(self.development, "ValueSpecification")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DEVELOPMENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize key_generation
        if self.key_generation is not None:
            serialized = SerializationHelper.serialize_item(self.key_generation, "CryptoServiceKey")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("KEY-GENERATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize key_storage_type
        if self.key_storage_type is not None:
            serialized = SerializationHelper.serialize_item(self.key_storage_type, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("KEY-STORAGE-TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize length
        if self.length is not None:
            serialized = SerializationHelper.serialize_item(self.length, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LENGTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CryptoServiceKey":
        """Deserialize XML element to CryptoServiceKey object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CryptoServiceKey object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CryptoServiceKey, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "ALGORITHM-FAMILY":
                setattr(obj, "algorithm_family", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "DEVELOPMENT":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "ABSTRACT-RULE-BASED-VALUE-SPECIFICATION":
                        setattr(obj, "development", SerializationHelper.deserialize_by_tag(child[0], "AbstractRuleBasedValueSpecification"))
                    elif concrete_tag == "APPLICATION-VALUE-SPECIFICATION":
                        setattr(obj, "development", SerializationHelper.deserialize_by_tag(child[0], "ApplicationValueSpecification"))
                    elif concrete_tag == "COMPOSITE-VALUE-SPECIFICATION":
                        setattr(obj, "development", SerializationHelper.deserialize_by_tag(child[0], "CompositeValueSpecification"))
                    elif concrete_tag == "CONSTANT-REFERENCE":
                        setattr(obj, "development", SerializationHelper.deserialize_by_tag(child[0], "ConstantReference"))
                    elif concrete_tag == "NOT-AVAILABLE-VALUE-SPECIFICATION":
                        setattr(obj, "development", SerializationHelper.deserialize_by_tag(child[0], "NotAvailableValueSpecification"))
                    elif concrete_tag == "NUMERICAL-VALUE-SPECIFICATION":
                        setattr(obj, "development", SerializationHelper.deserialize_by_tag(child[0], "NumericalValueSpecification"))
                    elif concrete_tag == "REFERENCE-VALUE-SPECIFICATION":
                        setattr(obj, "development", SerializationHelper.deserialize_by_tag(child[0], "ReferenceValueSpecification"))
                    elif concrete_tag == "TEXT-VALUE-SPECIFICATION":
                        setattr(obj, "development", SerializationHelper.deserialize_by_tag(child[0], "TextValueSpecification"))
            elif tag == "KEY-GENERATION":
                setattr(obj, "key_generation", SerializationHelper.deserialize_by_tag(child, "CryptoServiceKey"))
            elif tag == "KEY-STORAGE-TYPE":
                setattr(obj, "key_storage_type", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "LENGTH":
                setattr(obj, "length", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class CryptoServiceKeyBuilder(ARElementBuilder):
    """Builder for CryptoServiceKey with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: CryptoServiceKey = CryptoServiceKey()


    def with_algorithm_family(self, value: Optional[String]) -> "CryptoServiceKeyBuilder":
        """Set algorithm_family attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.algorithm_family = value
        return self

    def with_development(self, value: Optional[ValueSpecification]) -> "CryptoServiceKeyBuilder":
        """Set development attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.development = value
        return self

    def with_key_generation(self, value: Optional[CryptoServiceKey]) -> "CryptoServiceKeyBuilder":
        """Set key_generation attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.key_generation = value
        return self

    def with_key_storage_type(self, value: Optional[String]) -> "CryptoServiceKeyBuilder":
        """Set key_storage_type attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.key_storage_type = value
        return self

    def with_length(self, value: Optional[PositiveInteger]) -> "CryptoServiceKeyBuilder":
        """Set length attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.length = value
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


    def build(self) -> CryptoServiceKey:
        """Build and return the CryptoServiceKey instance with validation."""
        self._validate_instance()
        pass
        return self._obj