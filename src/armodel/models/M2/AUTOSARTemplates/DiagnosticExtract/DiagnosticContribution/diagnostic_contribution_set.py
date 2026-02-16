"""DiagnosticContributionSet AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticContribution.diagnostic_service_table import (
    DiagnosticServiceTable,
)


class DiagnosticContributionSet(ARElement):
    """AUTOSAR DiagnosticContributionSet."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("common", None, False, False, any (DiagnosticCommon)),  # common
        ("elements", None, False, True, any (DiagnosticCommon)),  # elements
        ("service_tables", None, False, True, DiagnosticServiceTable),  # serviceTables
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticContributionSet."""
        super().__init__()
        self.common: Optional[Any] = None
        self.elements: list[Any] = []
        self.service_tables: list[DiagnosticServiceTable] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticContributionSet to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticContributionSet":
        """Create DiagnosticContributionSet from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticContributionSet instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticContributionSet since parent returns ARObject
        return cast("DiagnosticContributionSet", obj)


class DiagnosticContributionSetBuilder:
    """Builder for DiagnosticContributionSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticContributionSet = DiagnosticContributionSet()

    def build(self) -> DiagnosticContributionSet:
        """Build and return DiagnosticContributionSet object.

        Returns:
            DiagnosticContributionSet instance
        """
        # TODO: Add validation
        return self._obj
