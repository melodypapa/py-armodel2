"""SecOcCryptoServiceMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 375)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.crypto_service_mapping import (
    CryptoServiceMapping,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.crypto_service_mapping import CryptoServiceMappingBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.crypto_service_key import (
    CryptoServiceKey,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.crypto_service_primitive import (
    CryptoServicePrimitive,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.crypto_service_queue import (
    CryptoServiceQueue,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SecOcCryptoServiceMapping(CryptoServiceMapping):
    """AUTOSAR SecOcCryptoServiceMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    authentication_ref: Optional[ARRef]
    crypto_service_key_ref: Optional[ARRef]
    crypto_service_queue_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize SecOcCryptoServiceMapping."""
        super().__init__()
        self.authentication_ref: Optional[ARRef] = None
        self.crypto_service_key_ref: Optional[ARRef] = None
        self.crypto_service_queue_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize SecOcCryptoServiceMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SecOcCryptoServiceMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize authentication_ref
        if self.authentication_ref is not None:
            serialized = SerializationHelper.serialize_item(self.authentication_ref, "CryptoServicePrimitive")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("AUTHENTICATION-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize crypto_service_key_ref
        if self.crypto_service_key_ref is not None:
            serialized = SerializationHelper.serialize_item(self.crypto_service_key_ref, "CryptoServiceKey")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CRYPTO-SERVICE-KEY-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize crypto_service_queue_ref
        if self.crypto_service_queue_ref is not None:
            serialized = SerializationHelper.serialize_item(self.crypto_service_queue_ref, "CryptoServiceQueue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CRYPTO-SERVICE-QUEUE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SecOcCryptoServiceMapping":
        """Deserialize XML element to SecOcCryptoServiceMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SecOcCryptoServiceMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SecOcCryptoServiceMapping, cls).deserialize(element)

        # Parse authentication_ref
        child = SerializationHelper.find_child_element(element, "AUTHENTICATION-REF")
        if child is not None:
            authentication_ref_value = ARRef.deserialize(child)
            obj.authentication_ref = authentication_ref_value

        # Parse crypto_service_key_ref
        child = SerializationHelper.find_child_element(element, "CRYPTO-SERVICE-KEY-REF")
        if child is not None:
            crypto_service_key_ref_value = ARRef.deserialize(child)
            obj.crypto_service_key_ref = crypto_service_key_ref_value

        # Parse crypto_service_queue_ref
        child = SerializationHelper.find_child_element(element, "CRYPTO-SERVICE-QUEUE-REF")
        if child is not None:
            crypto_service_queue_ref_value = ARRef.deserialize(child)
            obj.crypto_service_queue_ref = crypto_service_queue_ref_value

        return obj



class SecOcCryptoServiceMappingBuilder(CryptoServiceMappingBuilder):
    """Builder for SecOcCryptoServiceMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SecOcCryptoServiceMapping = SecOcCryptoServiceMapping()


    def with_authentication(self, value: Optional[CryptoServicePrimitive]) -> "SecOcCryptoServiceMappingBuilder":
        """Set authentication attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.authentication = value
        return self

    def with_crypto_service_key(self, value: Optional[CryptoServiceKey]) -> "SecOcCryptoServiceMappingBuilder":
        """Set crypto_service_key attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.crypto_service_key = value
        return self

    def with_crypto_service_queue(self, value: Optional[CryptoServiceQueue]) -> "SecOcCryptoServiceMappingBuilder":
        """Set crypto_service_queue attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.crypto_service_queue = value
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


    def build(self) -> SecOcCryptoServiceMapping:
        """Build and return the SecOcCryptoServiceMapping instance with validation."""
        self._validate_instance()
        pass
        return self._obj