"""DiagnosticRequestEmissionRelatedDTC AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)


class DiagnosticRequestEmissionRelatedDTC(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticRequestEmissionRelatedDTC."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("request", None, False, False, any (DiagnosticRequest)),  # request
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticRequestEmissionRelatedDTC."""
        super().__init__()
        self.request: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticRequestEmissionRelatedDTC to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticRequestEmissionRelatedDTC":
        """Create DiagnosticRequestEmissionRelatedDTC from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticRequestEmissionRelatedDTC instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticRequestEmissionRelatedDTC since parent returns ARObject
        return cast("DiagnosticRequestEmissionRelatedDTC", obj)


class DiagnosticRequestEmissionRelatedDTCBuilder:
    """Builder for DiagnosticRequestEmissionRelatedDTC."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticRequestEmissionRelatedDTC = DiagnosticRequestEmissionRelatedDTC()

    def build(self) -> DiagnosticRequestEmissionRelatedDTC:
        """Build and return DiagnosticRequestEmissionRelatedDTC object.

        Returns:
            DiagnosticRequestEmissionRelatedDTC instance
        """
        # TODO: Add validation
        return self._obj
