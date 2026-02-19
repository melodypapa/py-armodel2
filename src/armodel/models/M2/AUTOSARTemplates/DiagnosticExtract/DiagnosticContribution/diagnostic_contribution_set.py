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
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticContributionSet, cls).deserialize(element)

        # Parse common
        child = ARObject._find_child_element(element, "COMMON")
        if child is not None:
            common_value = child.text
            obj.common = common_value

        # Parse elements (list from container "ELEMENTS")
        obj.elements = []
        container = ARObject._find_child_element(element, "ELEMENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.elements.append(child_value)

        # Parse service_tables (list from container "SERVICE-TABLES")
        obj.service_tables = []
        container = ARObject._find_child_element(element, "SERVICE-TABLES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.service_tables.append(child_value)

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
