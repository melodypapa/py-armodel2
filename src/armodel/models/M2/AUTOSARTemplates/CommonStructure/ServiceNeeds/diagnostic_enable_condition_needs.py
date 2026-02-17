"""DiagnosticEnableConditionNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 762)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import (
    DiagnosticCapabilityElement,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    EventAcceptanceStatusEnum,
)


class DiagnosticEnableConditionNeeds(DiagnosticCapabilityElement):
    """AUTOSAR DiagnosticEnableConditionNeeds."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "initial_status": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=EventAcceptanceStatusEnum,
        ),  # initialStatus
    }

    def __init__(self) -> None:
        """Initialize DiagnosticEnableConditionNeeds."""
        super().__init__()
        self.initial_status: Optional[EventAcceptanceStatusEnum] = None


class DiagnosticEnableConditionNeedsBuilder:
    """Builder for DiagnosticEnableConditionNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEnableConditionNeeds = DiagnosticEnableConditionNeeds()

    def build(self) -> DiagnosticEnableConditionNeeds:
        """Build and return DiagnosticEnableConditionNeeds object.

        Returns:
            DiagnosticEnableConditionNeeds instance
        """
        # TODO: Add validation
        return self._obj
