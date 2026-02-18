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
