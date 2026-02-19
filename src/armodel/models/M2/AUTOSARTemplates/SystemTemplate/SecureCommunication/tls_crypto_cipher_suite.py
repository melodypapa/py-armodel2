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

    authentication: Optional[CryptoServicePrimitive]
    certificate: Optional[Any]
    cipher_suite_id: Optional[PositiveInteger]
    cipher_suite: Optional[String]
    elliptic_curves: list[CryptoEllipticCurveProps]
    encryption: Optional[CryptoServicePrimitive]
    key_exchanges: list[CryptoServicePrimitive]
    priority: Optional[PositiveInteger]
    props: Optional[TlsCryptoCipherSuite]
    psk_identity: Optional[TlsPskIdentity]
    remote: Optional[Any]
    signatures: list[CryptoSignatureScheme]
    version: Optional[TlsVersionEnum]
    def __init__(self) -> None:
        """Initialize TlsCryptoCipherSuite."""
        super().__init__()
        self.authentication: Optional[CryptoServicePrimitive] = None
        self.certificate: Optional[Any] = None
        self.cipher_suite_id: Optional[PositiveInteger] = None
        self.cipher_suite: Optional[String] = None
        self.elliptic_curves: list[CryptoEllipticCurveProps] = []
        self.encryption: Optional[CryptoServicePrimitive] = None
        self.key_exchanges: list[CryptoServicePrimitive] = []
        self.priority: Optional[PositiveInteger] = None
        self.props: Optional[TlsCryptoCipherSuite] = None
        self.psk_identity: Optional[TlsPskIdentity] = None
        self.remote: Optional[Any] = None
        self.signatures: list[CryptoSignatureScheme] = []
        self.version: Optional[TlsVersionEnum] = None
    def serialize(self) -> ET.Element:
        """Serialize TlsCryptoCipherSuite to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TlsCryptoCipherSuite, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize authentication
        if self.authentication is not None:
            serialized = ARObject._serialize_item(self.authentication, "CryptoServicePrimitive")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("AUTHENTICATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize certificate
        if self.certificate is not None:
            serialized = ARObject._serialize_item(self.certificate, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CERTIFICATE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize cipher_suite_id
        if self.cipher_suite_id is not None:
            serialized = ARObject._serialize_item(self.cipher_suite_id, "PositiveInteger")
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
            serialized = ARObject._serialize_item(self.cipher_suite, "String")
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

        # Serialize elliptic_curves (list to container "ELLIPTIC-CURVES")
        if self.elliptic_curves:
            wrapper = ET.Element("ELLIPTIC-CURVES")
            for item in self.elliptic_curves:
                serialized = ARObject._serialize_item(item, "CryptoEllipticCurveProps")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize encryption
        if self.encryption is not None:
            serialized = ARObject._serialize_item(self.encryption, "CryptoServicePrimitive")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ENCRYPTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize key_exchanges (list to container "KEY-EXCHANGES")
        if self.key_exchanges:
            wrapper = ET.Element("KEY-EXCHANGES")
            for item in self.key_exchanges:
                serialized = ARObject._serialize_item(item, "CryptoServicePrimitive")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize priority
        if self.priority is not None:
            serialized = ARObject._serialize_item(self.priority, "PositiveInteger")
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
            serialized = ARObject._serialize_item(self.props, "TlsCryptoCipherSuite")
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
            serialized = ARObject._serialize_item(self.psk_identity, "TlsPskIdentity")
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

        # Serialize remote
        if self.remote is not None:
            serialized = ARObject._serialize_item(self.remote, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REMOTE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize signatures (list to container "SIGNATURES")
        if self.signatures:
            wrapper = ET.Element("SIGNATURES")
            for item in self.signatures:
                serialized = ARObject._serialize_item(item, "CryptoSignatureScheme")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize version
        if self.version is not None:
            serialized = ARObject._serialize_item(self.version, "TlsVersionEnum")
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

        # Parse authentication
        child = ARObject._find_child_element(element, "AUTHENTICATION")
        if child is not None:
            authentication_value = ARObject._deserialize_by_tag(child, "CryptoServicePrimitive")
            obj.authentication = authentication_value

        # Parse certificate
        child = ARObject._find_child_element(element, "CERTIFICATE")
        if child is not None:
            certificate_value = child.text
            obj.certificate = certificate_value

        # Parse cipher_suite_id
        child = ARObject._find_child_element(element, "CIPHER-SUITE-ID")
        if child is not None:
            cipher_suite_id_value = child.text
            obj.cipher_suite_id = cipher_suite_id_value

        # Parse cipher_suite
        child = ARObject._find_child_element(element, "CIPHER-SUITE")
        if child is not None:
            cipher_suite_value = child.text
            obj.cipher_suite = cipher_suite_value

        # Parse elliptic_curves (list from container "ELLIPTIC-CURVES")
        obj.elliptic_curves = []
        container = ARObject._find_child_element(element, "ELLIPTIC-CURVES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.elliptic_curves.append(child_value)

        # Parse encryption
        child = ARObject._find_child_element(element, "ENCRYPTION")
        if child is not None:
            encryption_value = ARObject._deserialize_by_tag(child, "CryptoServicePrimitive")
            obj.encryption = encryption_value

        # Parse key_exchanges (list from container "KEY-EXCHANGES")
        obj.key_exchanges = []
        container = ARObject._find_child_element(element, "KEY-EXCHANGES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.key_exchanges.append(child_value)

        # Parse priority
        child = ARObject._find_child_element(element, "PRIORITY")
        if child is not None:
            priority_value = child.text
            obj.priority = priority_value

        # Parse props
        child = ARObject._find_child_element(element, "PROPS")
        if child is not None:
            props_value = ARObject._deserialize_by_tag(child, "TlsCryptoCipherSuite")
            obj.props = props_value

        # Parse psk_identity
        child = ARObject._find_child_element(element, "PSK-IDENTITY")
        if child is not None:
            psk_identity_value = ARObject._deserialize_by_tag(child, "TlsPskIdentity")
            obj.psk_identity = psk_identity_value

        # Parse remote
        child = ARObject._find_child_element(element, "REMOTE")
        if child is not None:
            remote_value = child.text
            obj.remote = remote_value

        # Parse signatures (list from container "SIGNATURES")
        obj.signatures = []
        container = ARObject._find_child_element(element, "SIGNATURES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.signatures.append(child_value)

        # Parse version
        child = ARObject._find_child_element(element, "VERSION")
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
