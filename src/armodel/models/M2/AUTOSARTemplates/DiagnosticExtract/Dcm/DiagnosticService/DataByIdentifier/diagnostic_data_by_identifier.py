"""DiagnosticDataByIdentifier AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_abstract_data_identifier import (
    DiagnosticAbstractDataIdentifier,
)


class DiagnosticDataByIdentifier(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticDataByIdentifier."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("data_identifier", None, False, False, DiagnosticAbstractDataIdentifier),  # dataIdentifier
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticDataByIdentifier."""
        super().__init__()
        self.data_identifier: Optional[DiagnosticAbstractDataIdentifier] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticDataByIdentifier to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticDataByIdentifier":
        """Create DiagnosticDataByIdentifier from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticDataByIdentifier instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticDataByIdentifier since parent returns ARObject
        return cast("DiagnosticDataByIdentifier", obj)


class DiagnosticDataByIdentifierBuilder:
    """Builder for DiagnosticDataByIdentifier."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticDataByIdentifier = DiagnosticDataByIdentifier()

    def build(self) -> DiagnosticDataByIdentifier:
        """Build and return DiagnosticDataByIdentifier object.

        Returns:
            DiagnosticDataByIdentifier instance
        """
        # TODO: Add validation
        return self._obj
