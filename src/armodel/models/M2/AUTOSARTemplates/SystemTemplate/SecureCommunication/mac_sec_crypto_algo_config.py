"""MacSecCryptoAlgoConfig AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
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
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("capability", None, False, False, MacSecCapabilityEnum),  # capability
        ("cipher_suite", None, False, False, MacSecCipherSuiteConfig),  # cipherSuite
        ("confidentiality", None, False, False, MacSecConfidentialityOffsetEnum),  # confidentiality
        ("replay_protection", None, True, False, None),  # replayProtection
    ]

    def __init__(self) -> None:
        """Initialize MacSecCryptoAlgoConfig."""
        super().__init__()
        self.capability: Optional[MacSecCapabilityEnum] = None
        self.cipher_suite: MacSecCipherSuiteConfig = None
        self.confidentiality: Optional[MacSecConfidentialityOffsetEnum] = None
        self.replay_protection: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert MacSecCryptoAlgoConfig to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MacSecCryptoAlgoConfig":
        """Create MacSecCryptoAlgoConfig from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            MacSecCryptoAlgoConfig instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to MacSecCryptoAlgoConfig since parent returns ARObject
        return cast("MacSecCryptoAlgoConfig", obj)


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
