"""TlsPskIdentity AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.crypto_service_key import (
    CryptoServiceKey,
)


class TlsPskIdentity(ARObject):
    """AUTOSAR TlsPskIdentity."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("pre_shared_key", None, False, False, CryptoServiceKey),  # preSharedKey
        ("psk_identity", None, True, False, None),  # pskIdentity
        ("psk_identity_hint", None, True, False, None),  # pskIdentityHint
    ]

    def __init__(self) -> None:
        """Initialize TlsPskIdentity."""
        super().__init__()
        self.pre_shared_key: Optional[CryptoServiceKey] = None
        self.psk_identity: Optional[String] = None
        self.psk_identity_hint: Optional[String] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TlsPskIdentity to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TlsPskIdentity":
        """Create TlsPskIdentity from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TlsPskIdentity instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TlsPskIdentity since parent returns ARObject
        return cast("TlsPskIdentity", obj)


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
