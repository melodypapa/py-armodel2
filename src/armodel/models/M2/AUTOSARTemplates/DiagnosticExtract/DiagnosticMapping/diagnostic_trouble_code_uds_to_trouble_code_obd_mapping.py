"""DiagnosticTroubleCodeUdsToTroubleCodeObdMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 188)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import (
    DiagnosticMapping,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTroubleCode.diagnostic_trouble_code import (
    DiagnosticTroubleCode,
)


class DiagnosticTroubleCodeUdsToTroubleCodeObdMapping(DiagnosticMapping):
    """AUTOSAR DiagnosticTroubleCodeUdsToTroubleCodeObdMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "trouble_code": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DiagnosticTroubleCode,
        ),  # troubleCode
        "trouble_code_uds": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DiagnosticTroubleCode,
        ),  # troubleCodeUds
    }

    def __init__(self) -> None:
        """Initialize DiagnosticTroubleCodeUdsToTroubleCodeObdMapping."""
        super().__init__()
        self.trouble_code: Optional[DiagnosticTroubleCode] = None
        self.trouble_code_uds: Optional[DiagnosticTroubleCode] = None


class DiagnosticTroubleCodeUdsToTroubleCodeObdMappingBuilder:
    """Builder for DiagnosticTroubleCodeUdsToTroubleCodeObdMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticTroubleCodeUdsToTroubleCodeObdMapping = DiagnosticTroubleCodeUdsToTroubleCodeObdMapping()

    def build(self) -> DiagnosticTroubleCodeUdsToTroubleCodeObdMapping:
        """Build and return DiagnosticTroubleCodeUdsToTroubleCodeObdMapping object.

        Returns:
            DiagnosticTroubleCodeUdsToTroubleCodeObdMapping instance
        """
        # TODO: Add validation
        return self._obj
