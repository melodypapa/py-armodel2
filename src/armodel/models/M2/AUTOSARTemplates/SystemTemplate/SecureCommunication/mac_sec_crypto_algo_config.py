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
    def serialize(self) -> ET.Element:
        """Serialize MacSecCryptoAlgoConfig to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # Serialize capability
        if self.capability is not None:
            serialized = ARObject._serialize_item(self.capability, "MacSecCapabilityEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CAPABILITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize cipher_suite
        if self.cipher_suite is not None:
            serialized = ARObject._serialize_item(self.cipher_suite, "MacSecCipherSuiteConfig")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CIPHER-SUITE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize confidentiality
        if self.confidentiality is not None:
            serialized = ARObject._serialize_item(self.confidentiality, "MacSecConfidentialityOffsetEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONFIDENTIALITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize replay_protection
        if self.replay_protection is not None:
            serialized = ARObject._serialize_item(self.replay_protection, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REPLAY-PROTECTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

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
            capability_value = MacSecCapabilityEnum.deserialize(child)
            obj.capability = capability_value

        # Parse cipher_suite
        child = ARObject._find_child_element(element, "CIPHER-SUITE")
        if child is not None:
            cipher_suite_value = ARObject._deserialize_by_tag(child, "MacSecCipherSuiteConfig")
            obj.cipher_suite = cipher_suite_value

        # Parse confidentiality
        child = ARObject._find_child_element(element, "CONFIDENTIALITY")
        if child is not None:
            confidentiality_value = MacSecConfidentialityOffsetEnum.deserialize(child)
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
