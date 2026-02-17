"""DiagnosticSecureCodingMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 312)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import (
    DiagnosticMapping,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_start_routine import (
    DiagnosticStartRoutine,
)


class DiagnosticSecureCodingMapping(DiagnosticMapping):
    """AUTOSAR DiagnosticSecureCodingMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "data_identifiers": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=any (DiagnosticWriteDataBy),
        ),  # dataIdentifiers
        "validation": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DiagnosticStartRoutine,
        ),  # validation
    }

    def __init__(self) -> None:
        """Initialize DiagnosticSecureCodingMapping."""
        super().__init__()
        self.data_identifiers: list[Any] = []
        self.validation: Optional[DiagnosticStartRoutine] = None


class DiagnosticSecureCodingMappingBuilder:
    """Builder for DiagnosticSecureCodingMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticSecureCodingMapping = DiagnosticSecureCodingMapping()

    def build(self) -> DiagnosticSecureCodingMapping:
        """Build and return DiagnosticSecureCodingMapping object.

        Returns:
            DiagnosticSecureCodingMapping instance
        """
        # TODO: Add validation
        return self._obj
