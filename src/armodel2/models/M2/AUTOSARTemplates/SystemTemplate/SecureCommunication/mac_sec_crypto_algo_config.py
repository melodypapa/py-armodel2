"""MacSecCryptoAlgoConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 175)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import (
    MacSecCapabilityEnum,
    MacSecConfidentialityOffsetEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.mac_sec_cipher_suite_config import (
    MacSecCipherSuiteConfig,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class MacSecCryptoAlgoConfig(ARObject):
    """AUTOSAR MacSecCryptoAlgoConfig."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "MAC-SEC-CRYPTO-ALGO-CONFIG"


    capability: Optional[MacSecCapabilityEnum]
    cipher_suite: MacSecCipherSuiteConfig
    confidentiality: Optional[MacSecConfidentialityOffsetEnum]
    replay_protection: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "CAPABILITY": lambda obj, elem: setattr(obj, "capability", MacSecCapabilityEnum.deserialize(elem)),
        "CIPHER-SUITE": lambda obj, elem: setattr(obj, "cipher_suite", SerializationHelper.deserialize_by_tag(elem, "MacSecCipherSuiteConfig")),
        "CONFIDENTIALITY": lambda obj, elem: setattr(obj, "confidentiality", MacSecConfidentialityOffsetEnum.deserialize(elem)),
        "REPLAY-PROTECTION": lambda obj, elem: setattr(obj, "replay_protection", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


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
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(MacSecCryptoAlgoConfig, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize capability
        if self.capability is not None:
            serialized = SerializationHelper.serialize_item(self.capability, "MacSecCapabilityEnum")
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
            serialized = SerializationHelper.serialize_item(self.cipher_suite, "MacSecCipherSuiteConfig")
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
            serialized = SerializationHelper.serialize_item(self.confidentiality, "MacSecConfidentialityOffsetEnum")
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
            serialized = SerializationHelper.serialize_item(self.replay_protection, "PositiveInteger")
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
        # First, call parent's deserialize to handle inherited attributes
        obj = super(MacSecCryptoAlgoConfig, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CAPABILITY":
                setattr(obj, "capability", MacSecCapabilityEnum.deserialize(child))
            elif tag == "CIPHER-SUITE":
                setattr(obj, "cipher_suite", SerializationHelper.deserialize_by_tag(child, "MacSecCipherSuiteConfig"))
            elif tag == "CONFIDENTIALITY":
                setattr(obj, "confidentiality", MacSecConfidentialityOffsetEnum.deserialize(child))
            elif tag == "REPLAY-PROTECTION":
                setattr(obj, "replay_protection", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class MacSecCryptoAlgoConfigBuilder(BuilderBase):
    """Builder for MacSecCryptoAlgoConfig with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: MacSecCryptoAlgoConfig = MacSecCryptoAlgoConfig()


    def with_capability(self, value: Optional[MacSecCapabilityEnum]) -> "MacSecCryptoAlgoConfigBuilder":
        """Set capability attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.capability = value
        return self

    def with_cipher_suite(self, value: MacSecCipherSuiteConfig) -> "MacSecCryptoAlgoConfigBuilder":
        """Set cipher_suite attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.cipher_suite = value
        return self

    def with_confidentiality(self, value: Optional[MacSecConfidentialityOffsetEnum]) -> "MacSecCryptoAlgoConfigBuilder":
        """Set confidentiality attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.confidentiality = value
        return self

    def with_replay_protection(self, value: Optional[PositiveInteger]) -> "MacSecCryptoAlgoConfigBuilder":
        """Set replay_protection attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.replay_protection = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _REQUIRED_ATTRIBUTES = {
        "cipherSuite",
    }
    _OPTIONAL_ATTRIBUTES = {
        "capability",
        "confidentiality",
        "replayProtection",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Validate required attributes using pre-computed constants (O(1) lookup)
        # This is much faster than calling get_type_hints() at runtime
        if getattr(self._obj, "cipherSuite", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError(f"Required attribute 'cipherSuite' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn(f"Required attribute 'cipherSuite' is None", UserWarning)


    def build(self) -> MacSecCryptoAlgoConfig:
        """Build and return the MacSecCryptoAlgoConfig instance with validation."""
        self._validate_instance()
        return self._obj