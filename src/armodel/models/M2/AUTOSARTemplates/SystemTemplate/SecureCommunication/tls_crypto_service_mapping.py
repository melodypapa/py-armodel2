"""TlsCryptoServiceMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 559)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.crypto_service_mapping import (
    CryptoServiceMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.crypto_service_primitive import (
    CryptoServicePrimitive,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.tls_crypto_cipher_suite import (
    TlsCryptoCipherSuite,
)


class TlsCryptoServiceMapping(CryptoServiceMapping):
    """AUTOSAR TlsCryptoServiceMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "key_exchanges": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=CryptoServicePrimitive,
        ),  # keyExchanges
        "tls_cipher_suites": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=TlsCryptoCipherSuite,
        ),  # tlsCipherSuites
        "use_client": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # useClient
        "use_security": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # useSecurity
    }

    def __init__(self) -> None:
        """Initialize TlsCryptoServiceMapping."""
        super().__init__()
        self.key_exchanges: list[CryptoServicePrimitive] = []
        self.tls_cipher_suites: list[TlsCryptoCipherSuite] = []
        self.use_client: Optional[Boolean] = None
        self.use_security: Optional[Boolean] = None


class TlsCryptoServiceMappingBuilder:
    """Builder for TlsCryptoServiceMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TlsCryptoServiceMapping = TlsCryptoServiceMapping()

    def build(self) -> TlsCryptoServiceMapping:
        """Build and return TlsCryptoServiceMapping object.

        Returns:
            TlsCryptoServiceMapping instance
        """
        # TODO: Add validation
        return self._obj
