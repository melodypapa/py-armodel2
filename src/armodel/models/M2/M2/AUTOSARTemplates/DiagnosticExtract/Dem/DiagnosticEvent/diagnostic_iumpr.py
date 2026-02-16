"""DiagnosticIumpr AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_event import (
    DiagnosticEvent,
)


class DiagnosticIumpr(DiagnosticCommonElement):
    """AUTOSAR DiagnosticIumpr."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "event": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DiagnosticEvent,
        ),  # event
        "ratio_kind": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DiagnosticIumprKindEnum,
        ),  # ratioKind
    }

    def __init__(self) -> None:
        """Initialize DiagnosticIumpr."""
        super().__init__()
        self.event: Optional[DiagnosticEvent] = None
        self.ratio_kind: Optional[DiagnosticIumprKindEnum] = None


class DiagnosticIumprBuilder:
    """Builder for DiagnosticIumpr."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticIumpr = DiagnosticIumpr()

    def build(self) -> DiagnosticIumpr:
        """Build and return DiagnosticIumpr object.

        Returns:
            DiagnosticIumpr instance
        """
        # TODO: Add validation
        return self._obj
