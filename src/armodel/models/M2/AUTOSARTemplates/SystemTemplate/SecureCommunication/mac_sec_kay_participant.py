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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.crypto_service_key import (
    CryptoServiceKey,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.mac_sec_crypto_algo_config import (
    MacSecCryptoAlgoConfig,
)


class MacSecKayParticipant(Identifiable):
    """AUTOSAR MacSecKayParticipant."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ckn: Optional[CryptoServiceKey]
    crypto_algo: Optional[MacSecCryptoAlgoConfig]
    sak: Optional[CryptoServiceKey]
    def __init__(self) -> None:
        """Initialize MacSecKayParticipant."""
        super().__init__()
        self.ckn: Optional[CryptoServiceKey] = None
        self.crypto_algo: Optional[MacSecCryptoAlgoConfig] = None
        self.sak: Optional[CryptoServiceKey] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "MacSecKayParticipant":
        """Deserialize XML element to MacSecKayParticipant object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MacSecKayParticipant object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(MacSecKayParticipant, cls).deserialize(element)

        # Parse ckn
        child = ARObject._find_child_element(element, "CKN")
        if child is not None:
            ckn_value = ARObject._deserialize_by_tag(child, "CryptoServiceKey")
            obj.ckn = ckn_value

        # Parse crypto_algo
        child = ARObject._find_child_element(element, "CRYPTO-ALGO")
        if child is not None:
            crypto_algo_value = ARObject._deserialize_by_tag(child, "MacSecCryptoAlgoConfig")
            obj.crypto_algo = crypto_algo_value

        # Parse sak
        child = ARObject._find_child_element(element, "SAK")
        if child is not None:
            sak_value = ARObject._deserialize_by_tag(child, "CryptoServiceKey")
            obj.sak = sak_value

        return obj



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
