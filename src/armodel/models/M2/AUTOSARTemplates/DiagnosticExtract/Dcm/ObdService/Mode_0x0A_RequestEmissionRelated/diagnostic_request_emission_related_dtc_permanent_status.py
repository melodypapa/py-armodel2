"""DiagnosticRequestEmissionRelatedDTCPermanentStatus AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)


class DiagnosticRequestEmissionRelatedDTCPermanentStatus(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticRequestEmissionRelatedDTCPermanentStatus."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("request", None, False, False, any (DiagnosticRequest)),  # request
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticRequestEmissionRelatedDTCPermanentStatus."""
        super().__init__()
        self.request: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticRequestEmissionRelatedDTCPermanentStatus to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticRequestEmissionRelatedDTCPermanentStatus":
        """Create DiagnosticRequestEmissionRelatedDTCPermanentStatus from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticRequestEmissionRelatedDTCPermanentStatus instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticRequestEmissionRelatedDTCPermanentStatus since parent returns ARObject
        return cast("DiagnosticRequestEmissionRelatedDTCPermanentStatus", obj)


class DiagnosticRequestEmissionRelatedDTCPermanentStatusBuilder:
    """Builder for DiagnosticRequestEmissionRelatedDTCPermanentStatus."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticRequestEmissionRelatedDTCPermanentStatus = DiagnosticRequestEmissionRelatedDTCPermanentStatus()

    def build(self) -> DiagnosticRequestEmissionRelatedDTCPermanentStatus:
        """Build and return DiagnosticRequestEmissionRelatedDTCPermanentStatus object.

        Returns:
            DiagnosticRequestEmissionRelatedDTCPermanentStatus instance
        """
        # TODO: Add validation
        return self._obj
