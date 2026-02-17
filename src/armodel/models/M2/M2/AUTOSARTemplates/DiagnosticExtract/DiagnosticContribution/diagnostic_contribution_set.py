"""DiagnosticContributionSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 56)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticContribution.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticContribution.diagnostic_service_table import (
    DiagnosticServiceTable,
)


class DiagnosticContributionSet(ARElement):
    """AUTOSAR DiagnosticContributionSet."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "common": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=Any,
        ),  # common
        "elements": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=Any,
        ),  # elements
        "service_tables": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=DiagnosticServiceTable,
        ),  # serviceTables
    }

    def __init__(self) -> None:
        """Initialize DiagnosticContributionSet."""
        super().__init__()
        self.common: Optional[Any] = None
        self.elements: list[Any] = []
        self.service_tables: list[DiagnosticServiceTable] = []


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
