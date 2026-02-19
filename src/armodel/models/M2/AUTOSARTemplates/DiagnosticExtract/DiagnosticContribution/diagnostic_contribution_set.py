"""DiagnosticContributionSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 56)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticContribution.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticContribution.diagnostic_service_table import (
    DiagnosticServiceTable,
)


class DiagnosticContributionSet(ARElement):
    """AUTOSAR DiagnosticContributionSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    common: Optional[Any]
    elements: list[Any]
    service_tables: list[DiagnosticServiceTable]
    def __init__(self) -> None:
        """Initialize DiagnosticContributionSet."""
        super().__init__()
        self.common: Optional[Any] = None
        self.elements: list[Any] = []
        self.service_tables: list[DiagnosticServiceTable] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticContributionSet":
        """Deserialize XML element to DiagnosticContributionSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticContributionSet object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse common
        child = ARObject._find_child_element(element, "COMMON")
        if child is not None:
            common_value = child.text
            obj.common = common_value

        # Parse elements (list)
        obj.elements = []
        for child in ARObject._find_all_child_elements(element, "ELEMENTS"):
            elements_value = child.text
            obj.elements.append(elements_value)

        # Parse service_tables (list)
        obj.service_tables = []
        for child in ARObject._find_all_child_elements(element, "SERVICE-TABLES"):
            service_tables_value = ARObject._deserialize_by_tag(child, "DiagnosticServiceTable")
            obj.service_tables.append(service_tables_value)

        return obj



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
