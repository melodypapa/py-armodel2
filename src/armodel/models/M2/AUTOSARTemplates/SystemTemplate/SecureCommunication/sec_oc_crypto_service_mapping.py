"""SecOcCryptoServiceMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.crypto_service_mapping import (
    CryptoServiceMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.crypto_service_key import (
    CryptoServiceKey,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.crypto_service_primitive import (
    CryptoServicePrimitive,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.crypto_service_queue import (
    CryptoServiceQueue,
)


class SecOcCryptoServiceMapping(CryptoServiceMapping):
    """AUTOSAR SecOcCryptoServiceMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("authentication", None, False, False, CryptoServicePrimitive),  # authentication
        ("crypto_service_key", None, False, False, CryptoServiceKey),  # cryptoServiceKey
        ("crypto_service_queue", None, False, False, CryptoServiceQueue),  # cryptoServiceQueue
    ]

    def __init__(self) -> None:
        """Initialize SecOcCryptoServiceMapping."""
        super().__init__()
        self.authentication: Optional[CryptoServicePrimitive] = None
        self.crypto_service_key: Optional[CryptoServiceKey] = None
        self.crypto_service_queue: Optional[CryptoServiceQueue] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SecOcCryptoServiceMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SecOcCryptoServiceMapping":
        """Create SecOcCryptoServiceMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SecOcCryptoServiceMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SecOcCryptoServiceMapping since parent returns ARObject
        return cast("SecOcCryptoServiceMapping", obj)


class SecOcCryptoServiceMappingBuilder:
    """Builder for SecOcCryptoServiceMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SecOcCryptoServiceMapping = SecOcCryptoServiceMapping()

    def build(self) -> SecOcCryptoServiceMapping:
        """Build and return SecOcCryptoServiceMapping object.

        Returns:
            SecOcCryptoServiceMapping instance
        """
        # TODO: Add validation
        return self._obj
