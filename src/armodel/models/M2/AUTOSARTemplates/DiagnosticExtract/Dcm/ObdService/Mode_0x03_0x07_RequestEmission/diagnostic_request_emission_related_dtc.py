"""DiagnosticRequestEmissionRelatedDTC AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)


class DiagnosticRequestEmissionRelatedDTC(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticRequestEmissionRelatedDTC."""

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
        """Initialize DiagnosticRequestEmissionRelatedDTC."""
        super().__init__()
        self.request: Optional[Any] = None


class DiagnosticRequestEmissionRelatedDTCBuilder:
    """Builder for DiagnosticRequestEmissionRelatedDTC."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticRequestEmissionRelatedDTC = DiagnosticRequestEmissionRelatedDTC()

    def build(self) -> DiagnosticRequestEmissionRelatedDTC:
        """Build and return DiagnosticRequestEmissionRelatedDTC object.

        Returns:
            DiagnosticRequestEmissionRelatedDTC instance
        """
        # TODO: Add validation
        return self._obj
