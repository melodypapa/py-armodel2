"""MacSecCipherSuiteConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 175)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class MacSecCipherSuiteConfig(ARObject):
    """AUTOSAR MacSecCipherSuiteConfig."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    cipher_suite: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize MacSecCipherSuiteConfig."""
        super().__init__()
        self.cipher_suite: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize MacSecCipherSuiteConfig to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize cipher_suite
        if self.cipher_suite is not None:
            serialized = ARObject._serialize_item(self.cipher_suite, "PositiveInteger")
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
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse cipher_suite
        child = ARObject._find_child_element(element, "CIPHER-SUITE")
        if child is not None:
            cipher_suite_value = child.text
            obj.cipher_suite = cipher_suite_value

        return obj



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
