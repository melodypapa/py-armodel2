"""MacSecKayParticipant AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.crypto_service_key import (
    CryptoServiceKey,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.mac_sec_crypto_algo_config import (
    MacSecCryptoAlgoConfig,
)


class MacSecKayParticipant(Identifiable):
    """AUTOSAR MacSecKayParticipant."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("ckn", None, False, False, CryptoServiceKey),  # ckn
        ("crypto_algo", None, False, False, MacSecCryptoAlgoConfig),  # cryptoAlgo
        ("sak", None, False, False, CryptoServiceKey),  # sak
    ]

    def __init__(self) -> None:
        """Initialize MacSecKayParticipant."""
        super().__init__()
        self.ckn: Optional[CryptoServiceKey] = None
        self.crypto_algo: Optional[MacSecCryptoAlgoConfig] = None
        self.sak: Optional[CryptoServiceKey] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert MacSecKayParticipant to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MacSecKayParticipant":
        """Create MacSecKayParticipant from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            MacSecKayParticipant instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to MacSecKayParticipant since parent returns ARObject
        return cast("MacSecKayParticipant", obj)


class MacSecKayParticipantBuilder:
    """Builder for MacSecKayParticipant."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MacSecKayParticipant = MacSecKayParticipant()

    def build(self) -> MacSecKayParticipant:
        """Build and return MacSecKayParticipant object.

        Returns:
            MacSecKayParticipant instance
        """
        # TODO: Add validation
        return self._obj
