"""DiagnosticAuthTransmitCertificate AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 100)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_Authentication.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.Authentication.diagnostic_authentication import (
    DiagnosticAuthentication,
)


class DiagnosticAuthTransmitCertificate(DiagnosticAuthentication):
    """AUTOSAR DiagnosticAuthTransmitCertificate."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "certificates": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=any (DiagnosticAuthTransmit),
        ),  # certificates
    }

    def __init__(self) -> None:
        """Initialize DiagnosticAuthTransmitCertificate."""
        super().__init__()
        self.certificates: list[Any] = []


class DiagnosticAuthTransmitCertificateBuilder:
    """Builder for DiagnosticAuthTransmitCertificate."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticAuthTransmitCertificate = DiagnosticAuthTransmitCertificate()

    def build(self) -> DiagnosticAuthTransmitCertificate:
        """Build and return DiagnosticAuthTransmitCertificate object.

        Returns:
            DiagnosticAuthTransmitCertificate instance
        """
        # TODO: Add validation
        return self._obj
