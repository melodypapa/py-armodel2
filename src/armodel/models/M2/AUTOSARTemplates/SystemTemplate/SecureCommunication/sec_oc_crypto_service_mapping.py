"""SecOcCryptoServiceMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 375)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    authentication: Optional[CryptoServicePrimitive]
    crypto_service_key: Optional[CryptoServiceKey]
    crypto_service_queue: Optional[CryptoServiceQueue]
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
