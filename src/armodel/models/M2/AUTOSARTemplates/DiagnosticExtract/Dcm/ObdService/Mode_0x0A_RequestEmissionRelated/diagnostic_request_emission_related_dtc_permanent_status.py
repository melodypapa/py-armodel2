"""DiagnosticRequestEmissionRelatedDTCPermanentStatus AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 161)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_ObdService_Mode_0x0A_RequestEmissionRelated.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)


class DiagnosticRequestEmissionRelatedDTCPermanentStatus(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticRequestEmissionRelatedDTCPermanentStatus."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "request": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (DiagnosticRequest),
        ),  # request
    }

    def __init__(self) -> None:
        """Initialize DiagnosticRequestEmissionRelatedDTCPermanentStatus."""
        super().__init__()
        self.request: Optional[Any] = None


class DiagnosticRequestEmissionRelatedDTCPermanentStatusBuilder:
    """Builder for DiagnosticRequestEmissionRelatedDTCPermanentStatus."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticRequestEmissionRelatedDTCPermanentStatus = DiagnosticRequestEmissionRelatedDTCPermanentStatus()

    def build(self) -> DiagnosticRequestEmissionRelatedDTCPermanentStatus:
        """Build and return DiagnosticRequestEmissionRelatedDTCPermanentStatus object.

        Returns:
            DiagnosticRequestEmissionRelatedDTCPermanentStatus instance
        """
        # TODO: Add validation
        return self._obj
