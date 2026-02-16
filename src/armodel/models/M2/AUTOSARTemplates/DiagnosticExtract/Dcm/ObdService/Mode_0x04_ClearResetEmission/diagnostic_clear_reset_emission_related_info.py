"""DiagnosticClearResetEmissionRelatedInfo AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)


class DiagnosticClearResetEmissionRelatedInfo(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticClearResetEmissionRelatedInfo."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "clear_reset": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (DiagnosticClearReset),
        ),  # clearReset
    }

    def __init__(self) -> None:
        """Initialize DiagnosticClearResetEmissionRelatedInfo."""
        super().__init__()
        self.clear_reset: Optional[Any] = None


class DiagnosticClearResetEmissionRelatedInfoBuilder:
    """Builder for DiagnosticClearResetEmissionRelatedInfo."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticClearResetEmissionRelatedInfo = DiagnosticClearResetEmissionRelatedInfo()

    def build(self) -> DiagnosticClearResetEmissionRelatedInfo:
        """Build and return DiagnosticClearResetEmissionRelatedInfo object.

        Returns:
            DiagnosticClearResetEmissionRelatedInfo instance
        """
        # TODO: Add validation
        return self._obj
