"""DiagnosticMemoryDestinationPrimary AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 184)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticMemoryDestination.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticMemoryDestination.diagnostic_memory_destination import (
    DiagnosticMemoryDestination,
)


class DiagnosticMemoryDestinationPrimary(DiagnosticMemoryDestination):
    """AUTOSAR DiagnosticMemoryDestinationPrimary."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "type_of_dtc": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DiagnosticTypeOfDtcSupportedEnum,
        ),  # typeOfDtc
    }

    def __init__(self) -> None:
        """Initialize DiagnosticMemoryDestinationPrimary."""
        super().__init__()
        self.type_of_dtc: Optional[DiagnosticTypeOfDtcSupportedEnum] = None


class DiagnosticMemoryDestinationPrimaryBuilder:
    """Builder for DiagnosticMemoryDestinationPrimary."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticMemoryDestinationPrimary = DiagnosticMemoryDestinationPrimary()

    def build(self) -> DiagnosticMemoryDestinationPrimary:
        """Build and return DiagnosticMemoryDestinationPrimary object.

        Returns:
            DiagnosticMemoryDestinationPrimary instance
        """
        # TODO: Add validation
        return self._obj
