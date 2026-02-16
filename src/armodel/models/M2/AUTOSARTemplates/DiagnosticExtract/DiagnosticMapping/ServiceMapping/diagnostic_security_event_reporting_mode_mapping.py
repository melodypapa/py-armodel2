"""DiagnosticSecurityEventReportingModeMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import (
    DiagnosticMapping,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_data_element import (
    DiagnosticDataElement,
)


class DiagnosticSecurityEventReportingModeMapping(DiagnosticMapping):
    """AUTOSAR DiagnosticSecurityEventReportingModeMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("data_element", None, False, False, DiagnosticDataElement),  # dataElement
        ("security_event_context", None, False, False, any (SecurityEventContext)),  # securityEventContext
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticSecurityEventReportingModeMapping."""
        super().__init__()
        self.data_element: Optional[DiagnosticDataElement] = None
        self.security_event_context: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticSecurityEventReportingModeMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticSecurityEventReportingModeMapping":
        """Create DiagnosticSecurityEventReportingModeMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticSecurityEventReportingModeMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticSecurityEventReportingModeMapping since parent returns ARObject
        return cast("DiagnosticSecurityEventReportingModeMapping", obj)


class DiagnosticSecurityEventReportingModeMappingBuilder:
    """Builder for DiagnosticSecurityEventReportingModeMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticSecurityEventReportingModeMapping = DiagnosticSecurityEventReportingModeMapping()

    def build(self) -> DiagnosticSecurityEventReportingModeMapping:
        """Build and return DiagnosticSecurityEventReportingModeMapping object.

        Returns:
            DiagnosticSecurityEventReportingModeMapping instance
        """
        # TODO: Add validation
        return self._obj
