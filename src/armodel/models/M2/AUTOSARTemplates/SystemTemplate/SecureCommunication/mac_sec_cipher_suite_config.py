"""MacSecCipherSuiteConfig AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class MacSecCipherSuiteConfig(ARObject):
    """AUTOSAR MacSecCipherSuiteConfig."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("cipher_suite", None, True, False, None),  # cipherSuite
    ]

    def __init__(self) -> None:
        """Initialize MacSecCipherSuiteConfig."""
        super().__init__()
        self.cipher_suite: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert MacSecCipherSuiteConfig to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MacSecCipherSuiteConfig":
        """Create MacSecCipherSuiteConfig from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            MacSecCipherSuiteConfig instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to MacSecCipherSuiteConfig since parent returns ARObject
        return cast("MacSecCipherSuiteConfig", obj)


class MacSecCipherSuiteConfigBuilder:
    """Builder for MacSecCipherSuiteConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MacSecCipherSuiteConfig = MacSecCipherSuiteConfig()

    def build(self) -> MacSecCipherSuiteConfig:
        """Build and return MacSecCipherSuiteConfig object.

        Returns:
            MacSecCipherSuiteConfig instance
        """
        # TODO: Add validation
        return self._obj
