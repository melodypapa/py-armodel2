"""DiagnosticReadDTCInformation AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)


class DiagnosticReadDTCInformation(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticReadDTCInformation."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("read", None, False, False, any (DiagnosticReadDTC)),  # read
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticReadDTCInformation."""
        super().__init__()
        self.read: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticReadDTCInformation to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticReadDTCInformation":
        """Create DiagnosticReadDTCInformation from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticReadDTCInformation instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticReadDTCInformation since parent returns ARObject
        return cast("DiagnosticReadDTCInformation", obj)


class DiagnosticReadDTCInformationBuilder:
    """Builder for DiagnosticReadDTCInformation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticReadDTCInformation = DiagnosticReadDTCInformation()

    def build(self) -> DiagnosticReadDTCInformation:
        """Build and return DiagnosticReadDTCInformation object.

        Returns:
            DiagnosticReadDTCInformation instance
        """
        # TODO: Add validation
        return self._obj
