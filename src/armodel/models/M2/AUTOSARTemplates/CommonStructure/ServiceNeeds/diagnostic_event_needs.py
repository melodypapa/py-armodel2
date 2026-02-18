"""DiagnosticEventNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 258)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 311)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 756)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import (
    DiagnosticCapabilityElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.function_inhibition_needs import (
    FunctionInhibitionNeeds,
)


class DiagnosticEventNeeds(DiagnosticCapabilityElement):
    """AUTOSAR DiagnosticEventNeeds."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    deferring_fids: list[FunctionInhibitionNeeds]
    diag_event_debounce: Optional[Any]
    inhibiting_fid: Optional[FunctionInhibitionNeeds]
    inhibitings: list[FunctionInhibitionNeeds]
    prestored: Optional[Boolean]
    uses_monitor: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize DiagnosticEventNeeds."""
        super().__init__()
        self.deferring_fids: list[FunctionInhibitionNeeds] = []
        self.diag_event_debounce: Optional[Any] = None
        self.inhibiting_fid: Optional[FunctionInhibitionNeeds] = None
        self.inhibitings: list[FunctionInhibitionNeeds] = []
        self.prestored: Optional[Boolean] = None
        self.uses_monitor: Optional[Boolean] = None


class DiagnosticEventNeedsBuilder:
    """Builder for DiagnosticEventNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEventNeeds = DiagnosticEventNeeds()

    def build(self) -> DiagnosticEventNeeds:
        """Build and return DiagnosticEventNeeds object.

        Returns:
            DiagnosticEventNeeds instance
        """
        # TODO: Add validation
        return self._obj
