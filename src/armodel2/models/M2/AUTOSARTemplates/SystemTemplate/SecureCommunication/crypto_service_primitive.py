"""CryptoServicePrimitive AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 376)
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 59)

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
    String,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class CryptoServicePrimitive(ARElement):
    """AUTOSAR CryptoServicePrimitive."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "CRYPTO-SERVICE-PRIMITIVE"


    algorithm_family: Optional[String]
    algorithm_mode: Optional[String]
    algorithm: Optional[String]
    _DESERIALIZE_DISPATCH = {
        "ALGORITHM-FAMILY": lambda obj, elem: setattr(obj, "algorithm_family", elem.text),
        "ALGORITHM-MODE": lambda obj, elem: setattr(obj, "algorithm_mode", elem.text),
        "ALGORITHM": lambda obj, elem: setattr(obj, "algorithm", elem.text),
    }


    def __init__(self) -> None:
        """Initialize CryptoServicePrimitive."""
        super().__init__()
        self.algorithm_family: Optional[String] = None
        self.algorithm_mode: Optional[String] = None
        self.algorithm: Optional[String] = None

    def serialize(self) -> ET.Element:
        """Serialize CryptoServicePrimitive to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CryptoServicePrimitive, self).serialize()

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

        # Serialize algorithm
        if self.algorithm is not None:
            serialized = SerializationHelper.serialize_item(self.algorithm, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ALGORITHM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CryptoServicePrimitive":
        """Deserialize XML element to CryptoServicePrimitive object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CryptoServicePrimitive object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CryptoServicePrimitive, cls).deserialize(element)

        # Parse algorithm_family
        child = SerializationHelper.find_child_element(element, "ALGORITHM-FAMILY")
        if child is not None:
            algorithm_family_value = child.text
            obj.algorithm_family = algorithm_family_value

        # Parse algorithm_mode
        child = SerializationHelper.find_child_element(element, "ALGORITHM-MODE")
        if child is not None:
            algorithm_mode_value = child.text
            obj.algorithm_mode = algorithm_mode_value

        # Parse algorithm
        child = SerializationHelper.find_child_element(element, "ALGORITHM")
        if child is not None:
            algorithm_value = child.text
            obj.algorithm = algorithm_value

        return obj



class CryptoServicePrimitiveBuilder(ARElementBuilder):
    """Builder for CryptoServicePrimitive with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: CryptoServicePrimitive = CryptoServicePrimitive()


    def with_algorithm_family(self, value: Optional[String]) -> "CryptoServicePrimitiveBuilder":
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

    def with_algorithm_mode(self, value: Optional[String]) -> "CryptoServicePrimitiveBuilder":
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

    def with_algorithm(self, value: Optional[String]) -> "CryptoServicePrimitiveBuilder":
        """Set algorithm attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.algorithm = value
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


    def build(self) -> CryptoServicePrimitive:
        """Build and return the CryptoServicePrimitive instance with validation."""
        self._validate_instance()
        pass
        return self._obj