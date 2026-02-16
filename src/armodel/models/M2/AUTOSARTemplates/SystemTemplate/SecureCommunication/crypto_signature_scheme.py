"""CryptoSignatureScheme AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class CryptoSignatureScheme(ARElement):
    """AUTOSAR CryptoSignatureScheme."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("signature", None, True, False, None),  # signature
    ]

    def __init__(self) -> None:
        """Initialize CryptoSignatureScheme."""
        super().__init__()
        self.signature: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CryptoSignatureScheme to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CryptoSignatureScheme":
        """Create CryptoSignatureScheme from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CryptoSignatureScheme instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CryptoSignatureScheme since parent returns ARObject
        return cast("CryptoSignatureScheme", obj)


class CryptoSignatureSchemeBuilder:
    """Builder for CryptoSignatureScheme."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CryptoSignatureScheme = CryptoSignatureScheme()

    def build(self) -> CryptoSignatureScheme:
        """Build and return CryptoSignatureScheme object.

        Returns:
            CryptoSignatureScheme instance
        """
        # TODO: Add validation
        return self._obj
