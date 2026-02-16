"""TlsCryptoCipherSuite AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "authentication": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=CryptoServicePrimitive,
        ),  # authentication
        "certificate": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (CryptoService),
        ),  # certificate
        "cipher_suite_id": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # cipherSuiteId
        "cipher_suite": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # cipherSuite
        "elliptic_curves": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=CryptoEllipticCurveProps,
        ),  # ellipticCurves
        "encryption": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=CryptoServicePrimitive,
        ),  # encryption
        "key_exchanges": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=CryptoServicePrimitive,
        ),  # keyExchanges
        "priority": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # priority
        "props": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=TlsCryptoCipherSuite,
        ),  # props
        "psk_identity": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=TlsPskIdentity,
        ),  # pskIdentity
        "remote": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (CryptoService),
        ),  # remote
        "signatures": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=CryptoSignatureScheme,
        ),  # signatures
        "version": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=TlsVersionEnum,
        ),  # version
    }

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
