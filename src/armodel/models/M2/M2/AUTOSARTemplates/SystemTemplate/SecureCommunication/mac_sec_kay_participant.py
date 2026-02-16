"""MacSecKayParticipant AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "ckn": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=CryptoServiceKey,
        ),  # ckn
        "crypto_algo": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=MacSecCryptoAlgoConfig,
        ),  # cryptoAlgo
        "sak": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=CryptoServiceKey,
        ),  # sak
    }

    def __init__(self) -> None:
        """Initialize MacSecKayParticipant."""
        super().__init__()
        self.ckn: Optional[CryptoServiceKey] = None
        self.crypto_algo: Optional[MacSecCryptoAlgoConfig] = None
        self.sak: Optional[CryptoServiceKey] = None


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
