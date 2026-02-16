"""CryptoServiceCertificate AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    String,
)


class CryptoServiceCertificate(ARElement):
    """AUTOSAR CryptoServiceCertificate."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("algorithm_family", None, False, False, any (CryptoCertificate)),  # algorithmFamily
        ("format", None, False, False, CryptoCertificateFormatEnum),  # format
        ("maximum", None, True, False, None),  # maximum
        ("next_higher", None, False, False, any (CryptoService)),  # nextHigher
        ("server_name", None, True, False, None),  # serverName
    ]

    def __init__(self) -> None:
        """Initialize CryptoServiceCertificate."""
        super().__init__()
        self.algorithm_family: Optional[Any] = None
        self.format: Optional[CryptoCertificateFormatEnum] = None
        self.maximum: Optional[PositiveInteger] = None
        self.next_higher: Optional[Any] = None
        self.server_name: Optional[String] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CryptoServiceCertificate to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CryptoServiceCertificate":
        """Create CryptoServiceCertificate from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CryptoServiceCertificate instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CryptoServiceCertificate since parent returns ARObject
        return cast("CryptoServiceCertificate", obj)


class CryptoServiceCertificateBuilder:
    """Builder for CryptoServiceCertificate."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CryptoServiceCertificate = CryptoServiceCertificate()

    def build(self) -> CryptoServiceCertificate:
        """Build and return CryptoServiceCertificate object.

        Returns:
            CryptoServiceCertificate instance
        """
        # TODO: Add validation
        return self._obj
