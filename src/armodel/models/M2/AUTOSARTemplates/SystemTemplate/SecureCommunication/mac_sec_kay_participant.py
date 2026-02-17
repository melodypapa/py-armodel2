"""MacSecKayParticipant AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 175)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
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

    ckn: Optional[CryptoServiceKey]
    crypto_algo: Optional[MacSecCryptoAlgoConfig]
    sak: Optional[CryptoServiceKey]
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
