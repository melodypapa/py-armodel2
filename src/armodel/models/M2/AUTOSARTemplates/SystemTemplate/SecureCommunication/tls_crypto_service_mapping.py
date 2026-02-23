"""TlsCryptoServiceMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 559)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.crypto_service_mapping import (
    CryptoServiceMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.crypto_service_mapping import CryptoServiceMappingBuilder
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.crypto_service_primitive import (
    CryptoServicePrimitive,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.tls_crypto_cipher_suite import (
    TlsCryptoCipherSuite,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class TlsCryptoServiceMapping(CryptoServiceMapping):
    """AUTOSAR TlsCryptoServiceMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    key_exchange_refs: list[ARRef]
    tls_cipher_suites: list[TlsCryptoCipherSuite]
    use_client: Optional[Boolean]
    use_security: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize TlsCryptoServiceMapping."""
        super().__init__()
        self.key_exchange_refs: list[ARRef] = []
        self.tls_cipher_suites: list[TlsCryptoCipherSuite] = []
        self.use_client: Optional[Boolean] = None
        self.use_security: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize TlsCryptoServiceMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TlsCryptoServiceMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize key_exchange_refs (list to container "KEY-EXCHANGE-REFS")
        if self.key_exchange_refs:
            wrapper = ET.Element("KEY-EXCHANGE-REFS")
            for item in self.key_exchange_refs:
                serialized = SerializationHelper.serialize_item(item, "CryptoServicePrimitive")
                if serialized is not None:
                    child_elem = ET.Element("KEY-EXCHANGE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize tls_cipher_suites (list to container "TLS-CIPHER-SUITES")
        if self.tls_cipher_suites:
            wrapper = ET.Element("TLS-CIPHER-SUITES")
            for item in self.tls_cipher_suites:
                serialized = SerializationHelper.serialize_item(item, "TlsCryptoCipherSuite")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize use_client
        if self.use_client is not None:
            serialized = SerializationHelper.serialize_item(self.use_client, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("USE-CLIENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize use_security
        if self.use_security is not None:
            serialized = SerializationHelper.serialize_item(self.use_security, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("USE-SECURITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TlsCryptoServiceMapping":
        """Deserialize XML element to TlsCryptoServiceMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TlsCryptoServiceMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TlsCryptoServiceMapping, cls).deserialize(element)

        # Parse key_exchange_refs (list from container "KEY-EXCHANGE-REFS")
        obj.key_exchange_refs = []
        container = SerializationHelper.find_child_element(element, "KEY-EXCHANGE-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.key_exchange_refs.append(child_value)

        # Parse tls_cipher_suites (list from container "TLS-CIPHER-SUITES")
        obj.tls_cipher_suites = []
        container = SerializationHelper.find_child_element(element, "TLS-CIPHER-SUITES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.tls_cipher_suites.append(child_value)

        # Parse use_client
        child = SerializationHelper.find_child_element(element, "USE-CLIENT")
        if child is not None:
            use_client_value = child.text
            obj.use_client = use_client_value

        # Parse use_security
        child = SerializationHelper.find_child_element(element, "USE-SECURITY")
        if child is not None:
            use_security_value = child.text
            obj.use_security = use_security_value

        return obj



class TlsCryptoServiceMappingBuilder(CryptoServiceMappingBuilder):
    """Builder for TlsCryptoServiceMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TlsCryptoServiceMapping = TlsCryptoServiceMapping()


    def with_key_exchanges(self, items: list[CryptoServicePrimitive]) -> "TlsCryptoServiceMappingBuilder":
        """Set key_exchanges list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.key_exchanges = list(items) if items else []
        return self

    def with_tls_cipher_suites(self, items: list[TlsCryptoCipherSuite]) -> "TlsCryptoServiceMappingBuilder":
        """Set tls_cipher_suites list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.tls_cipher_suites = list(items) if items else []
        return self

    def with_use_client(self, value: Optional[Boolean]) -> "TlsCryptoServiceMappingBuilder":
        """Set use_client attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.use_client = value
        return self

    def with_use_security(self, value: Optional[Boolean]) -> "TlsCryptoServiceMappingBuilder":
        """Set use_security attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.use_security = value
        return self


    def add_key_exchange(self, item: CryptoServicePrimitive) -> "TlsCryptoServiceMappingBuilder":
        """Add a single item to key_exchanges list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.key_exchanges.append(item)
        return self

    def clear_key_exchanges(self) -> "TlsCryptoServiceMappingBuilder":
        """Clear all items from key_exchanges list.

        Returns:
            self for method chaining
        """
        self._obj.key_exchanges = []
        return self

    def add_tls_cipher_suite(self, item: TlsCryptoCipherSuite) -> "TlsCryptoServiceMappingBuilder":
        """Add a single item to tls_cipher_suites list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.tls_cipher_suites.append(item)
        return self

    def clear_tls_cipher_suites(self) -> "TlsCryptoServiceMappingBuilder":
        """Clear all items from tls_cipher_suites list.

        Returns:
            self for method chaining
        """
        self._obj.tls_cipher_suites = []
        return self



    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel.core import GlobalSettingsManager, BuilderValidationMode

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


    def build(self) -> TlsCryptoServiceMapping:
        """Build and return the TlsCryptoServiceMapping instance with validation."""
        self._validate_instance()
        pass
        return self._obj