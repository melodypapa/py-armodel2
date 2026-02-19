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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    capability: Optional[MacSecCapabilityEnum]
    cipher_suite: MacSecCipherSuiteConfig
    confidentiality: Optional[MacSecConfidentialityOffsetEnum]
    replay_protection: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize MacSecCryptoAlgoConfig."""
        super().__init__()
        self.capability: Optional[MacSecCapabilityEnum] = None
        self.cipher_suite: MacSecCipherSuiteConfig = None
        self.confidentiality: Optional[MacSecConfidentialityOffsetEnum] = None
        self.replay_protection: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "MacSecCryptoAlgoConfig":
        """Deserialize XML element to MacSecCryptoAlgoConfig object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MacSecCryptoAlgoConfig object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse capability
        child = ARObject._find_child_element(element, "CAPABILITY")
        if child is not None:
            capability_value = child.text
            obj.capability = capability_value

        # Parse cipher_suite
        child = ARObject._find_child_element(element, "CIPHER-SUITE")
        if child is not None:
            cipher_suite_value = ARObject._deserialize_by_tag(child, "MacSecCipherSuiteConfig")
            obj.cipher_suite = cipher_suite_value

        # Parse confidentiality
        child = ARObject._find_child_element(element, "CONFIDENTIALITY")
        if child is not None:
            confidentiality_value = child.text
            obj.confidentiality = confidentiality_value

        # Parse replay_protection
        child = ARObject._find_child_element(element, "REPLAY-PROTECTION")
        if child is not None:
            replay_protection_value = child.text
            obj.replay_protection = replay_protection_value

        return obj



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
