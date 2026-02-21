"""TlsCryptoCipherSuite AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 562)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import (
    TlsVersionEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    String,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.crypto_elliptic_curve_props import (
    CryptoEllipticCurveProps,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.crypto_service_primitive import (
    CryptoServicePrimitive,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.crypto_signature_scheme import (
    CryptoSignatureScheme,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.tls_psk_identity import (
    TlsPskIdentity,
)


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
    elliptic_curve_refs: list[ARRef]
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
        self.elliptic_curve_refs: list[ARRef] = []
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

        # Serialize elliptic_curve_refs (list to container "ELLIPTIC-CURVE-REFS")
        if self.elliptic_curve_refs:
            wrapper = ET.Element("ELLIPTIC-CURVE-REFS")
            for item in self.elliptic_curve_refs:
                serialized = SerializationHelper.serialize_item(item, "CryptoEllipticCurveProps")
                if serialized is not None:
                    child_elem = ET.Element("ELLIPTIC-CURVE-REF")
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

        # Serialize signature_refs (list to container "SIGNATURE-REFS")
        if self.signature_refs:
            wrapper = ET.Element("SIGNATURE-REFS")
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

        # Parse elliptic_curve_refs (list from container "ELLIPTIC-CURVE-REFS")
        obj.elliptic_curve_refs = []
        container = SerializationHelper.find_child_element(element, "ELLIPTIC-CURVE-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.elliptic_curve_refs.append(child_value)

        # Parse encryption_ref
        child = SerializationHelper.find_child_element(element, "ENCRYPTION-REF")
        if child is not None:
            encryption_ref_value = ARRef.deserialize(child)
            obj.encryption_ref = encryption_ref_value

        # Parse key_exchange_refs (list from container "KEY-EXCHANGE-REFS")
        obj.key_exchange_refs = []
        container = SerializationHelper.find_child_element(element, "KEY-EXCHANGE-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
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

        # Parse signature_refs (list from container "SIGNATURE-REFS")
        obj.signature_refs = []
        container = SerializationHelper.find_child_element(element, "SIGNATURE-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
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



class TlsCryptoCipherSuiteBuilder:
    """Builder for TlsCryptoCipherSuite."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TlsCryptoCipherSuite = TlsCryptoCipherSuite()

    def build(self) -> TlsCryptoCipherSuite:
        """Build and return TlsCryptoCipherSuite object.

        Returns:
            TlsCryptoCipherSuite instance
        """
        # TODO: Add validation
        return self._obj
