"""DiagnosticReadDataByIdentifier AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.DataByIdentifier.diagnostic_data_by_identifier import (
    DiagnosticDataByIdentifier,
)


class DiagnosticReadDataByIdentifier(DiagnosticDataByIdentifier):
    """AUTOSAR DiagnosticReadDataByIdentifier."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "read_class": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (DiagnosticReadDataBy),
        ),  # readClass
    }

    def __init__(self) -> None:
        """Initialize DiagnosticReadDataByIdentifier."""
        super().__init__()
        self.read_class: Optional[Any] = None


class DiagnosticReadDataByIdentifierBuilder:
    """Builder for DiagnosticReadDataByIdentifier."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticReadDataByIdentifier = DiagnosticReadDataByIdentifier()

    def build(self) -> DiagnosticReadDataByIdentifier:
        """Build and return DiagnosticReadDataByIdentifier object.

        Returns:
            DiagnosticReadDataByIdentifier instance
        """
        # TODO: Add validation
        return self._obj
