"""DiagnosticWriteDataByIdentifier AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.DataByIdentifier.diagnostic_data_by_identifier import (
    DiagnosticDataByIdentifier,
)


class DiagnosticWriteDataByIdentifier(DiagnosticDataByIdentifier):
    """AUTOSAR DiagnosticWriteDataByIdentifier."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("write_class", None, False, False, any (DiagnosticWriteDataBy)),  # writeClass
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticWriteDataByIdentifier."""
        super().__init__()
        self.write_class: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticWriteDataByIdentifier to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticWriteDataByIdentifier":
        """Create DiagnosticWriteDataByIdentifier from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticWriteDataByIdentifier instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticWriteDataByIdentifier since parent returns ARObject
        return cast("DiagnosticWriteDataByIdentifier", obj)


class DiagnosticWriteDataByIdentifierBuilder:
    """Builder for DiagnosticWriteDataByIdentifier."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticWriteDataByIdentifier = DiagnosticWriteDataByIdentifier()

    def build(self) -> DiagnosticWriteDataByIdentifier:
        """Build and return DiagnosticWriteDataByIdentifier object.

        Returns:
            DiagnosticWriteDataByIdentifier instance
        """
        # TODO: Add validation
        return self._obj
