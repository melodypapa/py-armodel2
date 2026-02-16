"""DiagnosticAuthTransmitCertificateMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import (
    DiagnosticMapping,
)


class DiagnosticAuthTransmitCertificateMapping(DiagnosticMapping):
    """AUTOSAR DiagnosticAuthTransmitCertificateMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("crypto_services", None, False, True, any (CryptoService)),  # cryptoServices
        ("service_instance", None, False, False, any (DiagnosticAuthTransmit)),  # serviceInstance
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticAuthTransmitCertificateMapping."""
        super().__init__()
        self.crypto_services: list[Any] = []
        self.service_instance: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticAuthTransmitCertificateMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticAuthTransmitCertificateMapping":
        """Create DiagnosticAuthTransmitCertificateMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticAuthTransmitCertificateMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticAuthTransmitCertificateMapping since parent returns ARObject
        return cast("DiagnosticAuthTransmitCertificateMapping", obj)


class DiagnosticAuthTransmitCertificateMappingBuilder:
    """Builder for DiagnosticAuthTransmitCertificateMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticAuthTransmitCertificateMapping = DiagnosticAuthTransmitCertificateMapping()

    def build(self) -> DiagnosticAuthTransmitCertificateMapping:
        """Build and return DiagnosticAuthTransmitCertificateMapping object.

        Returns:
            DiagnosticAuthTransmitCertificateMapping instance
        """
        # TODO: Add validation
        return self._obj
