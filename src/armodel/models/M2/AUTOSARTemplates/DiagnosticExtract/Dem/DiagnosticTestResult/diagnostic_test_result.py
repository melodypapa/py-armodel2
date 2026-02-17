"""DiagnosticTestResult AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 204)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 804)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticTestResult.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_event import (
    DiagnosticEvent,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTestResult.diagnostic_test_identifier import (
    DiagnosticTestIdentifier,
)


class DiagnosticTestResult(DiagnosticCommonElement):
    """AUTOSAR DiagnosticTestResult."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "diagnostic_event": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DiagnosticEvent,
        ),  # diagnosticEvent
        "monitored": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (Diagnostic),
        ),  # monitored
        "test_identifier": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DiagnosticTestIdentifier,
        ),  # testIdentifier
        "update_kind": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DiagnosticTestResult,
        ),  # updateKind
    }

    def __init__(self) -> None:
        """Initialize DiagnosticTestResult."""
        super().__init__()
        self.diagnostic_event: Optional[DiagnosticEvent] = None
        self.monitored: Optional[Any] = None
        self.test_identifier: Optional[DiagnosticTestIdentifier] = None
        self.update_kind: Optional[DiagnosticTestResult] = None


class DiagnosticTestResultBuilder:
    """Builder for DiagnosticTestResult."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticTestResult = DiagnosticTestResult()

    def build(self) -> DiagnosticTestResult:
        """Build and return DiagnosticTestResult object.

        Returns:
            DiagnosticTestResult instance
        """
        # TODO: Add validation
        return self._obj
