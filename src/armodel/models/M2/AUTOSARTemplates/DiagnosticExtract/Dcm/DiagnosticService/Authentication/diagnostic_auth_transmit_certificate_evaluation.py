"""DiagnosticAuthTransmitCertificateEvaluation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 101)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_Authentication.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    String,
)


class DiagnosticAuthTransmitCertificateEvaluation(Identifiable):
    """AUTOSAR DiagnosticAuthTransmitCertificateEvaluation."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "evaluation_id": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # evaluationId
        "function": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # function
    }

    def __init__(self) -> None:
        """Initialize DiagnosticAuthTransmitCertificateEvaluation."""
        super().__init__()
        self.evaluation_id: Optional[PositiveInteger] = None
        self.function: Optional[String] = None


class DiagnosticAuthTransmitCertificateEvaluationBuilder:
    """Builder for DiagnosticAuthTransmitCertificateEvaluation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticAuthTransmitCertificateEvaluation = DiagnosticAuthTransmitCertificateEvaluation()

    def build(self) -> DiagnosticAuthTransmitCertificateEvaluation:
        """Build and return DiagnosticAuthTransmitCertificateEvaluation object.

        Returns:
            DiagnosticAuthTransmitCertificateEvaluation instance
        """
        # TODO: Add validation
        return self._obj
