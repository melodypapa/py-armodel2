"""TlsPskIdentity AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 563)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.crypto_service_key import (
    CryptoServiceKey,
)


class TlsPskIdentity(ARObject):
    """AUTOSAR TlsPskIdentity."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    pre_shared_key: Optional[CryptoServiceKey]
    psk_identity: Optional[String]
    psk_identity_hint: Optional[String]
    def __init__(self) -> None:
        """Initialize TlsPskIdentity."""
        super().__init__()
        self.pre_shared_key: Optional[CryptoServiceKey] = None
        self.psk_identity: Optional[String] = None
        self.psk_identity_hint: Optional[String] = None


class TlsPskIdentityBuilder:
    """Builder for TlsPskIdentity."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TlsPskIdentity = TlsPskIdentity()

    def build(self) -> TlsPskIdentity:
        """Build and return TlsPskIdentity object.

        Returns:
            TlsPskIdentity instance
        """
        # TODO: Add validation
        return self._obj
