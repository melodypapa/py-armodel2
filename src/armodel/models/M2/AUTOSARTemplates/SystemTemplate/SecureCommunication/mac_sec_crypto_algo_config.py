"""MacSecCryptoAlgoConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 175)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.mac_sec_cipher_suite_config import (
    MacSecCipherSuiteConfig,
)


class MacSecCryptoAlgoConfig(ARObject):
    """AUTOSAR MacSecCryptoAlgoConfig."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "capability": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=MacSecCapabilityEnum,
        ),  # capability
        "cipher_suite": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=MacSecCipherSuiteConfig,
        ),  # cipherSuite
        "confidentiality": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=MacSecConfidentialityOffsetEnum,
        ),  # confidentiality
        "replay_protection": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # replayProtection
    }

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
