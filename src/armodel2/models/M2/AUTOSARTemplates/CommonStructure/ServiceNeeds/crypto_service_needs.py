"""CryptoServiceNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 235)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 733)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_needs import (
    ServiceNeeds,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_needs import ServiceNeedsBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    String,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class CryptoServiceNeeds(ServiceNeeds):
    """AUTOSAR CryptoServiceNeeds."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "CRYPTO-SERVICE-NEEDS"


    algorithm_family: Optional[String]
    algorithm_mode: Optional[String]
    crypto_key: Optional[String]
    maximum_key: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "ALGORITHM-FAMILY": lambda obj, elem: setattr(obj, "algorithm_family", SerializationHelper.deserialize_by_tag(elem, "String")),
        "ALGORITHM-MODE": lambda obj, elem: setattr(obj, "algorithm_mode", SerializationHelper.deserialize_by_tag(elem, "String")),
        "CRYPTO-KEY": lambda obj, elem: setattr(obj, "crypto_key", SerializationHelper.deserialize_by_tag(elem, "String")),
        "MAXIMUM-KEY": lambda obj, elem: setattr(obj, "maximum_key", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize CryptoServiceNeeds."""
        super().__init__()
        self.algorithm_family: Optional[String] = None
        self.algorithm_mode: Optional[String] = None
        self.crypto_key: Optional[String] = None
        self.maximum_key: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize CryptoServiceNeeds to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CryptoServiceNeeds, self).serialize()

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

        # Serialize algorithm_mode
        if self.algorithm_mode is not None:
            serialized = SerializationHelper.serialize_item(self.algorithm_mode, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ALGORITHM-MODE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize crypto_key
        if self.crypto_key is not None:
            serialized = SerializationHelper.serialize_item(self.crypto_key, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CRYPTO-KEY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize maximum_key
        if self.maximum_key is not None:
            serialized = SerializationHelper.serialize_item(self.maximum_key, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAXIMUM-KEY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CryptoServiceNeeds":
        """Deserialize XML element to CryptoServiceNeeds object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CryptoServiceNeeds object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CryptoServiceNeeds, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ALGORITHM-FAMILY":
                setattr(obj, "algorithm_family", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "ALGORITHM-MODE":
                setattr(obj, "algorithm_mode", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "CRYPTO-KEY":
                setattr(obj, "crypto_key", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "MAXIMUM-KEY":
                setattr(obj, "maximum_key", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class CryptoServiceNeedsBuilder(ServiceNeedsBuilder):
    """Builder for CryptoServiceNeeds with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: CryptoServiceNeeds = CryptoServiceNeeds()


    def with_algorithm_family(self, value: Optional[String]) -> "CryptoServiceNeedsBuilder":
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

    def with_algorithm_mode(self, value: Optional[String]) -> "CryptoServiceNeedsBuilder":
        """Set algorithm_mode attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.algorithm_mode = value
        return self

    def with_crypto_key(self, value: Optional[String]) -> "CryptoServiceNeedsBuilder":
        """Set crypto_key attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.crypto_key = value
        return self

    def with_maximum_key(self, value: Optional[PositiveInteger]) -> "CryptoServiceNeedsBuilder":
        """Set maximum_key attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.maximum_key = value
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


    def build(self) -> CryptoServiceNeeds:
        """Build and return the CryptoServiceNeeds instance with validation."""
        self._validate_instance()
        pass
        return self._obj