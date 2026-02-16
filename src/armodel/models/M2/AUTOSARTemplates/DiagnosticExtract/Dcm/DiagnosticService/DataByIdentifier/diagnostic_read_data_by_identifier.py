"""DiagnosticReadDataByIdentifier AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.DataByIdentifier.diagnostic_data_by_identifier import (
    DiagnosticDataByIdentifier,
)


class DiagnosticReadDataByIdentifier(DiagnosticDataByIdentifier):
    """AUTOSAR DiagnosticReadDataByIdentifier."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("read_class", None, False, False, any (DiagnosticReadDataBy)),  # readClass
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticReadDataByIdentifier."""
        super().__init__()
        self.read_class: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticReadDataByIdentifier to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticReadDataByIdentifier":
        """Create DiagnosticReadDataByIdentifier from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticReadDataByIdentifier instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticReadDataByIdentifier since parent returns ARObject
        return cast("DiagnosticReadDataByIdentifier", obj)


class DiagnosticReadDataByIdentifierBuilder:
    """Builder for DiagnosticReadDataByIdentifier."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticReadDataByIdentifier = DiagnosticReadDataByIdentifier()

    def build(self) -> DiagnosticReadDataByIdentifier:
        """Build and return DiagnosticReadDataByIdentifier object.

        Returns:
            DiagnosticReadDataByIdentifier instance
        """
        # TODO: Add validation
        return self._obj
