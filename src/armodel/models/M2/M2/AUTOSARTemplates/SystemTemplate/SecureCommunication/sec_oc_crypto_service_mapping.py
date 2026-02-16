"""SecOcCryptoServiceMapping AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "authentication": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=CryptoServicePrimitive,
        ),  # authentication
        "crypto_service_key": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=CryptoServiceKey,
        ),  # cryptoServiceKey
        "crypto_service_queue": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=CryptoServiceQueue,
        ),  # cryptoServiceQueue
    }

    def __init__(self) -> None:
        """Initialize SecOcCryptoServiceMapping."""
        super().__init__()
        self.authentication: Optional[CryptoServicePrimitive] = None
        self.crypto_service_key: Optional[CryptoServiceKey] = None
        self.crypto_service_queue: Optional[CryptoServiceQueue] = None


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
