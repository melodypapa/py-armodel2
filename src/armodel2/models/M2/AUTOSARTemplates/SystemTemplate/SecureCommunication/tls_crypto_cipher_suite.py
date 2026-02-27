"""TlsCryptoCipherSuite AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 562)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import (
    TlsVersionEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    String,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.crypto_elliptic_curve_props import (
    CryptoEllipticCurveProps,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.crypto_service_primitive import (
    CryptoServicePrimitive,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.crypto_signature_scheme import (
    CryptoSignatureScheme,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.tls_psk_identity import (
    TlsPskIdentity,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class TlsCryptoCipherSuite(Identifiable):
    """AUTOSAR TlsCryptoCipherSuite."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    authentication_ref: Optional[ARRef]
    certificate_ref: Optional[Any]
    cipher_suite_id: Optional[PositiveInteger]
    cipher_suite: Optional[String]
    elliptic_curf_refs: list[ARRef]
    encryption_ref: Optional[ARRef]
    key_exchange_refs: list[ARRef]
    priority: Optional[PositiveInteger]
    props: Optional[TlsCryptoCipherSuite]
    psk_identity: Optional[TlsPskIdentity]
    remote_ref: Optional[Any]
    signature_refs: list[ARRef]
    version: Optional[TlsVersionEnum]
    def __init__(self) -> None:
        """Initialize TlsCryptoCipherSuite."""
        super().__init__()
        self.authentication_ref: Optional[ARRef] = None
        self.certificate_ref: Optional[Any] = None
        self.cipher_suite_id: Optional[PositiveInteger] = None
        self.cipher_suite: Optional[String] = None
        self.elliptic_curf_refs: list[ARRef] = []
        self.encryption_ref: Optional[ARRef] = None
        self.key_exchange_refs: list[ARRef] = []
        self.priority: Optional[PositiveInteger] = None
        self.props: Optional[TlsCryptoCipherSuite] = None
        self.psk_identity: Optional[TlsPskIdentity] = None
        self.remote_ref: Optional[Any] = None
        self.signature_refs: list[ARRef] = []
        self.version: Optional[TlsVersionEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize TlsCryptoCipherSuite to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TlsCryptoCipherSuite, self).serialize()

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

        # Serialize certificate_ref
        if self.certificate_ref is not None:
            serialized = SerializationHelper.serialize_item(self.certificate_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CERTIFICATE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize cipher_suite_id
        if self.cipher_suite_id is not None:
            serialized = SerializationHelper.serialize_item(self.cipher_suite_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CIPHER-SUITE-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize cipher_suite
        if self.cipher_suite is not None:
            serialized = SerializationHelper.serialize_item(self.cipher_suite, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CIPHER-SUITE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize elliptic_curf_refs (list to container "ELLIPTIC-CURFS")
        if self.elliptic_curf_refs:
            wrapper = ET.Element("ELLIPTIC-CURFS")
            for item in self.elliptic_curf_refs:
                serialized = SerializationHelper.serialize_item(item, "CryptoEllipticCurveProps")
                if serialized is not None:
                    child_elem = ET.Element("ELLIPTIC-CURF-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize encryption_ref
        if self.encryption_ref is not None:
            serialized = SerializationHelper.serialize_item(self.encryption_ref, "CryptoServicePrimitive")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ENCRYPTION-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize key_exchange_refs (list to container "KEY-EXCHANGES")
        if self.key_exchange_refs:
            wrapper = ET.Element("KEY-EXCHANGES")
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

        # Serialize priority
        if self.priority is not None:
            serialized = SerializationHelper.serialize_item(self.priority, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PRIORITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize props
        if self.props is not None:
            serialized = SerializationHelper.serialize_item(self.props, "TlsCryptoCipherSuite")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PROPS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize psk_identity
        if self.psk_identity is not None:
            serialized = SerializationHelper.serialize_item(self.psk_identity, "TlsPskIdentity")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PSK-IDENTITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize remote_ref
        if self.remote_ref is not None:
            serialized = SerializationHelper.serialize_item(self.remote_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REMOTE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize signature_refs (list to container "SIGNATURES")
        if self.signature_refs:
            wrapper = ET.Element("SIGNATURES")
            for item in self.signature_refs:
                serialized = SerializationHelper.serialize_item(item, "CryptoSignatureScheme")
                if serialized is not None:
                    child_elem = ET.Element("SIGNATURE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize version
        if self.version is not None:
            serialized = SerializationHelper.serialize_item(self.version, "TlsVersionEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VERSION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TlsCryptoCipherSuite":
        """Deserialize XML element to TlsCryptoCipherSuite object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TlsCryptoCipherSuite object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TlsCryptoCipherSuite, cls).deserialize(element)

        # Parse authentication_ref
        child = SerializationHelper.find_child_element(element, "AUTHENTICATION-REF")
        if child is not None:
            authentication_ref_value = ARRef.deserialize(child)
            obj.authentication_ref = authentication_ref_value

        # Parse certificate_ref
        child = SerializationHelper.find_child_element(element, "CERTIFICATE-REF")
        if child is not None:
            certificate_ref_value = ARRef.deserialize(child)
            obj.certificate_ref = certificate_ref_value

        # Parse cipher_suite_id
        child = SerializationHelper.find_child_element(element, "CIPHER-SUITE-ID")
        if child is not None:
            cipher_suite_id_value = child.text
            obj.cipher_suite_id = cipher_suite_id_value

        # Parse cipher_suite
        child = SerializationHelper.find_child_element(element, "CIPHER-SUITE")
        if child is not None:
            cipher_suite_value = child.text
            obj.cipher_suite = cipher_suite_value

        # Parse elliptic_curf_refs (list from container "ELLIPTIC-CURFS")
        obj.elliptic_curf_refs = []
        container = SerializationHelper.find_child_element(element, "ELLIPTIC-CURFS")
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
                    obj.elliptic_curf_refs.append(child_value)

        # Parse encryption_ref
        child = SerializationHelper.find_child_element(element, "ENCRYPTION-REF")
        if child is not None:
            encryption_ref_value = ARRef.deserialize(child)
            obj.encryption_ref = encryption_ref_value

        # Parse key_exchange_refs (list from container "KEY-EXCHANGES")
        obj.key_exchange_refs = []
        container = SerializationHelper.find_child_element(element, "KEY-EXCHANGES")
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

        # Parse priority
        child = SerializationHelper.find_child_element(element, "PRIORITY")
        if child is not None:
            priority_value = child.text
            obj.priority = priority_value

        # Parse props
        child = SerializationHelper.find_child_element(element, "PROPS")
        if child is not None:
            props_value = SerializationHelper.deserialize_by_tag(child, "TlsCryptoCipherSuite")
            obj.props = props_value

        # Parse psk_identity
        child = SerializationHelper.find_child_element(element, "PSK-IDENTITY")
        if child is not None:
            psk_identity_value = SerializationHelper.deserialize_by_tag(child, "TlsPskIdentity")
            obj.psk_identity = psk_identity_value

        # Parse remote_ref
        child = SerializationHelper.find_child_element(element, "REMOTE-REF")
        if child is not None:
            remote_ref_value = ARRef.deserialize(child)
            obj.remote_ref = remote_ref_value

        # Parse signature_refs (list from container "SIGNATURES")
        obj.signature_refs = []
        container = SerializationHelper.find_child_element(element, "SIGNATURES")
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
                    obj.signature_refs.append(child_value)

        # Parse version
        child = SerializationHelper.find_child_element(element, "VERSION")
        if child is not None:
            version_value = TlsVersionEnum.deserialize(child)
            obj.version = version_value

        return obj



class TlsCryptoCipherSuiteBuilder(IdentifiableBuilder):
    """Builder for TlsCryptoCipherSuite with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TlsCryptoCipherSuite = TlsCryptoCipherSuite()


    def with_authentication(self, value: Optional[CryptoServicePrimitive]) -> "TlsCryptoCipherSuiteBuilder":
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

    def with_certificate(self, value: Optional[any (CryptoService)]) -> "TlsCryptoCipherSuiteBuilder":
        """Set certificate attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.certificate = value
        return self

    def with_cipher_suite_id(self, value: Optional[PositiveInteger]) -> "TlsCryptoCipherSuiteBuilder":
        """Set cipher_suite_id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.cipher_suite_id = value
        return self

    def with_cipher_suite(self, value: Optional[String]) -> "TlsCryptoCipherSuiteBuilder":
        """Set cipher_suite attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.cipher_suite = value
        return self

    def with_elliptic_curves(self, items: list[CryptoEllipticCurveProps]) -> "TlsCryptoCipherSuiteBuilder":
        """Set elliptic_curves list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.elliptic_curves = list(items) if items else []
        return self

    def with_encryption(self, value: Optional[CryptoServicePrimitive]) -> "TlsCryptoCipherSuiteBuilder":
        """Set encryption attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.encryption = value
        return self

    def with_key_exchanges(self, items: list[CryptoServicePrimitive]) -> "TlsCryptoCipherSuiteBuilder":
        """Set key_exchanges list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.key_exchanges = list(items) if items else []
        return self

    def with_priority(self, value: Optional[PositiveInteger]) -> "TlsCryptoCipherSuiteBuilder":
        """Set priority attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.priority = value
        return self

    def with_props(self, value: Optional[TlsCryptoCipherSuite]) -> "TlsCryptoCipherSuiteBuilder":
        """Set props attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.props = value
        return self

    def with_psk_identity(self, value: Optional[TlsPskIdentity]) -> "TlsCryptoCipherSuiteBuilder":
        """Set psk_identity attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.psk_identity = value
        return self

    def with_remote(self, value: Optional[any (CryptoService)]) -> "TlsCryptoCipherSuiteBuilder":
        """Set remote attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.remote = value
        return self

    def with_signatures(self, items: list[CryptoSignatureScheme]) -> "TlsCryptoCipherSuiteBuilder":
        """Set signatures list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.signatures = list(items) if items else []
        return self

    def with_version(self, value: Optional[TlsVersionEnum]) -> "TlsCryptoCipherSuiteBuilder":
        """Set version attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.version = value
        return self


    def add_elliptic_curf(self, item: CryptoEllipticCurveProps) -> "TlsCryptoCipherSuiteBuilder":
        """Add a single item to elliptic_curves list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.elliptic_curves.append(item)
        return self

    def clear_elliptic_curves(self) -> "TlsCryptoCipherSuiteBuilder":
        """Clear all items from elliptic_curves list.

        Returns:
            self for method chaining
        """
        self._obj.elliptic_curves = []
        return self

    def add_key_exchange(self, item: CryptoServicePrimitive) -> "TlsCryptoCipherSuiteBuilder":
        """Add a single item to key_exchanges list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.key_exchanges.append(item)
        return self

    def clear_key_exchanges(self) -> "TlsCryptoCipherSuiteBuilder":
        """Clear all items from key_exchanges list.

        Returns:
            self for method chaining
        """
        self._obj.key_exchanges = []
        return self

    def add_signature(self, item: CryptoSignatureScheme) -> "TlsCryptoCipherSuiteBuilder":
        """Add a single item to signatures list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.signatures.append(item)
        return self

    def clear_signatures(self) -> "TlsCryptoCipherSuiteBuilder":
        """Clear all items from signatures list.

        Returns:
            self for method chaining
        """
        self._obj.signatures = []
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


    def build(self) -> TlsCryptoCipherSuite:
        """Build and return the TlsCryptoCipherSuite instance with validation."""
        self._validate_instance()
        pass
        return self._obj