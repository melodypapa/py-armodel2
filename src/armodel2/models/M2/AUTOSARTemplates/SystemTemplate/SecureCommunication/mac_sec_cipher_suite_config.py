"""MacSecCipherSuiteConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 175)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class MacSecCipherSuiteConfig(ARObject):
    """AUTOSAR MacSecCipherSuiteConfig."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "MAC-SEC-CIPHER-SUITE-CONFIG"


    cipher_suite: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "CIPHER-SUITE": lambda obj, elem: setattr(obj, "cipher_suite", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize MacSecCipherSuiteConfig."""
        super().__init__()
        self.cipher_suite: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize MacSecCipherSuiteConfig to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(MacSecCipherSuiteConfig, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize cipher_suite
        if self.cipher_suite is not None:
            serialized = SerializationHelper.serialize_item(self.cipher_suite, "PositiveInteger")
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

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MacSecCipherSuiteConfig":
        """Deserialize XML element to MacSecCipherSuiteConfig object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MacSecCipherSuiteConfig object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(MacSecCipherSuiteConfig, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CIPHER-SUITE":
                setattr(obj, "cipher_suite", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class MacSecCipherSuiteConfigBuilder(BuilderBase):
    """Builder for MacSecCipherSuiteConfig with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: MacSecCipherSuiteConfig = MacSecCipherSuiteConfig()


    def with_cipher_suite(self, value: Optional[PositiveInteger]) -> "MacSecCipherSuiteConfigBuilder":
        """Set cipher_suite attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.cipher_suite = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "cipherSuite",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> MacSecCipherSuiteConfig:
        """Build and return the MacSecCipherSuiteConfig instance with validation."""
        self._validate_instance()
        return self._obj