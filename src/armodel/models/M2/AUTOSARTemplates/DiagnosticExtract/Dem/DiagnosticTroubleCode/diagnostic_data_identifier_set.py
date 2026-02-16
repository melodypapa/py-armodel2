"""DiagnosticDataIdentifierSet AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_data_identifier import (
    DiagnosticDataIdentifier,
)


class DiagnosticDataIdentifierSet(DiagnosticCommonElement):
    """AUTOSAR DiagnosticDataIdentifierSet."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("data_identifiers", None, False, True, DiagnosticDataIdentifier),  # dataIdentifiers
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticDataIdentifierSet."""
        super().__init__()
        self.data_identifiers: list[DiagnosticDataIdentifier] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticDataIdentifierSet to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticDataIdentifierSet":
        """Create DiagnosticDataIdentifierSet from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticDataIdentifierSet instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticDataIdentifierSet since parent returns ARObject
        return cast("DiagnosticDataIdentifierSet", obj)


class DiagnosticDataIdentifierSetBuilder:
    """Builder for DiagnosticDataIdentifierSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticDataIdentifierSet = DiagnosticDataIdentifierSet()

    def build(self) -> DiagnosticDataIdentifierSet:
        """Build and return DiagnosticDataIdentifierSet object.

        Returns:
            DiagnosticDataIdentifierSet instance
        """
        # TODO: Add validation
        return self._obj
