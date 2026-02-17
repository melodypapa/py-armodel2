"""DiagnosticReadDTCInformation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 136)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_ReadDTCInformation.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)


class DiagnosticReadDTCInformation(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticReadDTCInformation."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "read": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (DiagnosticReadDTC),
        ),  # read
    }

    def __init__(self) -> None:
        """Initialize DiagnosticReadDTCInformation."""
        super().__init__()
        self.read: Optional[Any] = None


class DiagnosticReadDTCInformationBuilder:
    """Builder for DiagnosticReadDTCInformation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticReadDTCInformation = DiagnosticReadDTCInformation()

    def build(self) -> DiagnosticReadDTCInformation:
        """Build and return DiagnosticReadDTCInformation object.

        Returns:
            DiagnosticReadDTCInformation instance
        """
        # TODO: Add validation
        return self._obj
