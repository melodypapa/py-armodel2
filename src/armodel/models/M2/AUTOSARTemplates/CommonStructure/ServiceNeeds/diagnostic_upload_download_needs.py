"""DiagnosticUploadDownloadNeeds AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import (
    DiagnosticCapabilityElement,
)


class DiagnosticUploadDownloadNeeds(DiagnosticCapabilityElement):
    """AUTOSAR DiagnosticUploadDownloadNeeds."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticUploadDownloadNeeds."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticUploadDownloadNeeds to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticUploadDownloadNeeds":
        """Create DiagnosticUploadDownloadNeeds from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticUploadDownloadNeeds instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticUploadDownloadNeeds since parent returns ARObject
        return cast("DiagnosticUploadDownloadNeeds", obj)


class DiagnosticUploadDownloadNeedsBuilder:
    """Builder for DiagnosticUploadDownloadNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticUploadDownloadNeeds = DiagnosticUploadDownloadNeeds()

    def build(self) -> DiagnosticUploadDownloadNeeds:
        """Build and return DiagnosticUploadDownloadNeeds object.

        Returns:
            DiagnosticUploadDownloadNeeds instance
        """
        # TODO: Add validation
        return self._obj
