"""DiagnosticOperationCycleNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 761)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import (
    DiagnosticCapabilityElement,
)


class DiagnosticOperationCycleNeeds(DiagnosticCapabilityElement):
    """AUTOSAR DiagnosticOperationCycleNeeds."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "operation_cycle": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (OperationCycleType),
        ),  # operationCycle
    }

    def __init__(self) -> None:
        """Initialize DiagnosticOperationCycleNeeds."""
        super().__init__()
        self.operation_cycle: Optional[Any] = None


class DiagnosticOperationCycleNeedsBuilder:
    """Builder for DiagnosticOperationCycleNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticOperationCycleNeeds = DiagnosticOperationCycleNeeds()

    def build(self) -> DiagnosticOperationCycleNeeds:
        """Build and return DiagnosticOperationCycleNeeds object.

        Returns:
            DiagnosticOperationCycleNeeds instance
        """
        # TODO: Add validation
        return self._obj
