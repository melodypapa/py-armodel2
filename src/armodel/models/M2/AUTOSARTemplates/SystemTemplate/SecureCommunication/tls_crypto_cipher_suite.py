"""TlsCryptoCipherSuite AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
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
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.tls_crypto_cipher_suite import (
    TlsCryptoCipherSuite,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.tls_psk_identity import (
    TlsPskIdentity,
)


class TlsCryptoCipherSuite(Identifiable):
    """AUTOSAR TlsCryptoCipherSuite."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("authentication", None, False, False, CryptoServicePrimitive),  # authentication
        ("certificate", None, False, False, any (CryptoService)),  # certificate
        ("cipher_suite_id", None, True, False, None),  # cipherSuiteId
        ("cipher_suite", None, True, False, None),  # cipherSuite
        ("elliptic_curves", None, False, True, CryptoEllipticCurveProps),  # ellipticCurves
        ("encryption", None, False, False, CryptoServicePrimitive),  # encryption
        ("key_exchanges", None, False, True, CryptoServicePrimitive),  # keyExchanges
        ("priority", None, True, False, None),  # priority
        ("props", None, False, False, TlsCryptoCipherSuite),  # props
        ("psk_identity", None, False, False, TlsPskIdentity),  # pskIdentity
        ("remote", None, False, False, any (CryptoService)),  # remote
        ("signatures", None, False, True, CryptoSignatureScheme),  # signatures
        ("version", None, False, False, TlsVersionEnum),  # version
    ]

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

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TlsCryptoCipherSuite to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TlsCryptoCipherSuite":
        """Create TlsCryptoCipherSuite from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TlsCryptoCipherSuite instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TlsCryptoCipherSuite since parent returns ARObject
        return cast("TlsCryptoCipherSuite", obj)


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
