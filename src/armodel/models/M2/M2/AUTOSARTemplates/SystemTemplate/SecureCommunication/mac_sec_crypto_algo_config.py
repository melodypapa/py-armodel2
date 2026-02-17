"""MacSecCryptoAlgoConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 175)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import (
    MacSecCapabilityEnum,
    MacSecConfidentialityOffsetEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.mac_sec_cipher_suite_config import (
    MacSecCipherSuiteConfig,
)


class MacSecCryptoAlgoConfig(ARObject):
    """AUTOSAR MacSecCryptoAlgoConfig."""

    def __init__(self) -> None:
        """Initialize MacSecCryptoAlgoConfig."""
        super().__init__()
        self.capability: Optional[MacSecCapabilityEnum] = None
        self.cipher_suite: MacSecCipherSuiteConfig = None
        self.confidentiality: Optional[MacSecConfidentialityOffsetEnum] = None
        self.replay_protection: Optional[PositiveInteger] = None


class MacSecCryptoAlgoConfigBuilder:
    """Builder for MacSecCryptoAlgoConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MacSecCryptoAlgoConfig = MacSecCryptoAlgoConfig()

    def build(self) -> MacSecCryptoAlgoConfig:
        """Build and return MacSecCryptoAlgoConfig object.

        Returns:
            MacSecCryptoAlgoConfig instance
        """
        # TODO: Add validation
        return self._obj
