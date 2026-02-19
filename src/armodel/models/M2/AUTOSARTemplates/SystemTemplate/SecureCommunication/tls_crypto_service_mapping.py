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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    key_exchanges: list[CryptoServicePrimitive]
    tls_cipher_suites: list[TlsCryptoCipherSuite]
    use_client: Optional[Boolean]
    use_security: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize TlsCryptoServiceMapping."""
        super().__init__()
        self.key_exchanges: list[CryptoServicePrimitive] = []
        self.tls_cipher_suites: list[TlsCryptoCipherSuite] = []
        self.use_client: Optional[Boolean] = None
        self.use_security: Optional[Boolean] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "TlsCryptoServiceMapping":
        """Deserialize XML element to TlsCryptoServiceMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TlsCryptoServiceMapping object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse key_exchanges (list)
        obj.key_exchanges = []
        for child in ARObject._find_all_child_elements(element, "KEY-EXCHANGES"):
            key_exchanges_value = ARObject._deserialize_by_tag(child, "CryptoServicePrimitive")
            obj.key_exchanges.append(key_exchanges_value)

        # Parse tls_cipher_suites (list)
        obj.tls_cipher_suites = []
        for child in ARObject._find_all_child_elements(element, "TLS-CIPHER-SUITES"):
            tls_cipher_suites_value = ARObject._deserialize_by_tag(child, "TlsCryptoCipherSuite")
            obj.tls_cipher_suites.append(tls_cipher_suites_value)

        # Parse use_client
        child = ARObject._find_child_element(element, "USE-CLIENT")
        if child is not None:
            use_client_value = child.text
            obj.use_client = use_client_value

        # Parse use_security
        child = ARObject._find_child_element(element, "USE-SECURITY")
        if child is not None:
            use_security_value = child.text
            obj.use_security = use_security_value

        return obj



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
