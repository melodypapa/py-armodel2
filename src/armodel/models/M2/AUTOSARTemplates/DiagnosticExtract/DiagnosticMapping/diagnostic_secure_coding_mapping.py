"""DiagnosticSecureCodingMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import (
    DiagnosticMapping,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_start_routine import (
    DiagnosticStartRoutine,
)


class DiagnosticSecureCodingMapping(DiagnosticMapping):
    """AUTOSAR DiagnosticSecureCodingMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("data_identifiers", None, False, True, any (DiagnosticWriteDataBy)),  # dataIdentifiers
        ("validation", None, False, False, DiagnosticStartRoutine),  # validation
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticSecureCodingMapping."""
        super().__init__()
        self.data_identifiers: list[Any] = []
        self.validation: Optional[DiagnosticStartRoutine] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticSecureCodingMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticSecureCodingMapping":
        """Create DiagnosticSecureCodingMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticSecureCodingMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticSecureCodingMapping since parent returns ARObject
        return cast("DiagnosticSecureCodingMapping", obj)


class DiagnosticSecureCodingMappingBuilder:
    """Builder for DiagnosticSecureCodingMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticSecureCodingMapping = DiagnosticSecureCodingMapping()

    def build(self) -> DiagnosticSecureCodingMapping:
        """Build and return DiagnosticSecureCodingMapping object.

        Returns:
            DiagnosticSecureCodingMapping instance
        """
        # TODO: Add validation
        return self._obj
