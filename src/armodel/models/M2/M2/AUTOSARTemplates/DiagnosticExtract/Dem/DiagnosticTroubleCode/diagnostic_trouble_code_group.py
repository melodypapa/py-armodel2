"""DiagnosticTroubleCodeGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 177)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticTroubleCode.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTroubleCode.diagnostic_trouble_code import (
    DiagnosticTroubleCode,
)


class DiagnosticTroubleCodeGroup(DiagnosticCommonElement):
    """AUTOSAR DiagnosticTroubleCodeGroup."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "dtcs": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=DiagnosticTroubleCode,
        ),  # dtcs
        "group_number": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # groupNumber
    }

    def __init__(self) -> None:
        """Initialize DiagnosticTroubleCodeGroup."""
        super().__init__()
        self.dtcs: list[DiagnosticTroubleCode] = []
        self.group_number: Optional[PositiveInteger] = None


class DiagnosticTroubleCodeGroupBuilder:
    """Builder for DiagnosticTroubleCodeGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticTroubleCodeGroup = DiagnosticTroubleCodeGroup()

    def build(self) -> DiagnosticTroubleCodeGroup:
        """Build and return DiagnosticTroubleCodeGroup object.

        Returns:
            DiagnosticTroubleCodeGroup instance
        """
        # TODO: Add validation
        return self._obj
