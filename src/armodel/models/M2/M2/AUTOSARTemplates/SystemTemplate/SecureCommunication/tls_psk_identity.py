"""TlsPskIdentity AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 563)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.crypto_service_key import (
    CryptoServiceKey,
)


class TlsPskIdentity(ARObject):
    """AUTOSAR TlsPskIdentity."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "pre_shared_key": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=CryptoServiceKey,
        ),  # preSharedKey
        "psk_identity": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # pskIdentity
        "psk_identity_hint": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # pskIdentityHint
    }

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
