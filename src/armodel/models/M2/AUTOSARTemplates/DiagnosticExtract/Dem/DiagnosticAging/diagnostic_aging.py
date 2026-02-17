"""DiagnosticAging AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 202)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticAging.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class DiagnosticAging(DiagnosticCommonElement):
    """AUTOSAR DiagnosticAging."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "aging_cycle": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (DiagnosticOperation),
        ),  # agingCycle
        "threshold": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # threshold
    }

    def __init__(self) -> None:
        """Initialize DiagnosticAging."""
        super().__init__()
        self.aging_cycle: Optional[Any] = None
        self.threshold: Optional[PositiveInteger] = None


class DiagnosticAgingBuilder:
    """Builder for DiagnosticAging."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticAging = DiagnosticAging()

    def build(self) -> DiagnosticAging:
        """Build and return DiagnosticAging object.

        Returns:
            DiagnosticAging instance
        """
        # TODO: Add validation
        return self._obj
