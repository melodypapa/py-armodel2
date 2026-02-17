"""DiagnosticEventInfoNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 312)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 760)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import (
    DiagnosticCapabilityElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class DiagnosticEventInfoNeeds(DiagnosticCapabilityElement):
    """AUTOSAR DiagnosticEventInfoNeeds."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "obd_dtc_number": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # obdDtcNumber
        "uds_dtc_number": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # udsDtcNumber
    }

    def __init__(self) -> None:
        """Initialize DiagnosticEventInfoNeeds."""
        super().__init__()
        self.obd_dtc_number: Optional[PositiveInteger] = None
        self.uds_dtc_number: Optional[PositiveInteger] = None


class DiagnosticEventInfoNeedsBuilder:
    """Builder for DiagnosticEventInfoNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEventInfoNeeds = DiagnosticEventInfoNeeds()

    def build(self) -> DiagnosticEventInfoNeeds:
        """Build and return DiagnosticEventInfoNeeds object.

        Returns:
            DiagnosticEventInfoNeeds instance
        """
        # TODO: Add validation
        return self._obj
