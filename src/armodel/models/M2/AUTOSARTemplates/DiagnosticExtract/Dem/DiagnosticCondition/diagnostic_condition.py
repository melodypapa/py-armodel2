"""DiagnosticCondition AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 194)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticCondition.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class DiagnosticCondition(DiagnosticCommonElement):
    """AUTOSAR DiagnosticCondition."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "init_value": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # initValue
    }

    def __init__(self) -> None:
        """Initialize DiagnosticCondition."""
        super().__init__()
        self.init_value: Optional[Boolean] = None


class DiagnosticConditionBuilder:
    """Builder for DiagnosticCondition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticCondition = DiagnosticCondition()

    def build(self) -> DiagnosticCondition:
        """Build and return DiagnosticCondition object.

        Returns:
            DiagnosticCondition instance
        """
        # TODO: Add validation
        return self._obj
