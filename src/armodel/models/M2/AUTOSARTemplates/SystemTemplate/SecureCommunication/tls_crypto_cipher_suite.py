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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "TlsCryptoCipherSuite":
        """Deserialize XML element to TlsCryptoCipherSuite object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TlsCryptoCipherSuite object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

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

        # Parse elliptic_curves (list)
        obj.elliptic_curves = []
        for child in ARObject._find_all_child_elements(element, "ELLIPTIC-CURVES"):
            elliptic_curves_value = ARObject._deserialize_by_tag(child, "CryptoEllipticCurveProps")
            obj.elliptic_curves.append(elliptic_curves_value)

        # Parse encryption
        child = ARObject._find_child_element(element, "ENCRYPTION")
        if child is not None:
            encryption_value = ARObject._deserialize_by_tag(child, "CryptoServicePrimitive")
            obj.encryption = encryption_value

        # Parse key_exchanges (list)
        obj.key_exchanges = []
        for child in ARObject._find_all_child_elements(element, "KEY-EXCHANGES"):
            key_exchanges_value = ARObject._deserialize_by_tag(child, "CryptoServicePrimitive")
            obj.key_exchanges.append(key_exchanges_value)

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

        # Parse signatures (list)
        obj.signatures = []
        for child in ARObject._find_all_child_elements(element, "SIGNATURES"):
            signatures_value = ARObject._deserialize_by_tag(child, "CryptoSignatureScheme")
            obj.signatures.append(signatures_value)

        # Parse version
        child = ARObject._find_child_element(element, "VERSION")
        if child is not None:
            version_value = child.text
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
