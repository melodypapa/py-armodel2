"""TlsCryptoServiceMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
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
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("key_exchanges", None, False, True, CryptoServicePrimitive),  # keyExchanges
        ("tls_cipher_suites", None, False, True, TlsCryptoCipherSuite),  # tlsCipherSuites
        ("use_client", None, True, False, None),  # useClient
        ("use_security", None, True, False, None),  # useSecurity
    ]

    def __init__(self) -> None:
        """Initialize TlsCryptoServiceMapping."""
        super().__init__()
        self.key_exchanges: list[CryptoServicePrimitive] = []
        self.tls_cipher_suites: list[TlsCryptoCipherSuite] = []
        self.use_client: Optional[Boolean] = None
        self.use_security: Optional[Boolean] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TlsCryptoServiceMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TlsCryptoServiceMapping":
        """Create TlsCryptoServiceMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TlsCryptoServiceMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TlsCryptoServiceMapping since parent returns ARObject
        return cast("TlsCryptoServiceMapping", obj)


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
