"""DiagnosticEventPortMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 249)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_sw_mapping import (
    DiagnosticSwMapping,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_event import (
    DiagnosticEvent,
)


class DiagnosticEventPortMapping(DiagnosticSwMapping):
    """AUTOSAR DiagnosticEventPortMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "bsw_service": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (BswService),
        ),  # bswService
        "diagnostic_event": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DiagnosticEvent,
        ),  # diagnosticEvent
        "swc_flat_service": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (SwcService),
        ),  # swcFlatService
        "swc_service": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (SwcService),
        ),  # swcService
    }

    def __init__(self) -> None:
        """Initialize DiagnosticEventPortMapping."""
        super().__init__()
        self.bsw_service: Optional[Any] = None
        self.diagnostic_event: Optional[DiagnosticEvent] = None
        self.swc_flat_service: Optional[Any] = None
        self.swc_service: Optional[Any] = None


class DiagnosticEventPortMappingBuilder:
    """Builder for DiagnosticEventPortMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEventPortMapping = DiagnosticEventPortMapping()

    def build(self) -> DiagnosticEventPortMapping:
        """Build and return DiagnosticEventPortMapping object.

        Returns:
            DiagnosticEventPortMapping instance
        """
        # TODO: Add validation
        return self._obj
