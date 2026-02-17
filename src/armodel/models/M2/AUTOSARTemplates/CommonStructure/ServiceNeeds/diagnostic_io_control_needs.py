"""DiagnosticIoControlNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 248)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 119)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 781)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import (
    DiagnosticCapabilityElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_value_needs import (
    DiagnosticValueNeeds,
)


class DiagnosticIoControlNeeds(DiagnosticCapabilityElement):
    """AUTOSAR DiagnosticIoControlNeeds."""

    current_value: Optional[DiagnosticValueNeeds]
    freeze_current: Optional[Boolean]
    reset_to_default: Optional[Boolean]
    short_term: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize DiagnosticIoControlNeeds."""
        super().__init__()
        self.current_value: Optional[DiagnosticValueNeeds] = None
        self.freeze_current: Optional[Boolean] = None
        self.reset_to_default: Optional[Boolean] = None
        self.short_term: Optional[Boolean] = None


class DiagnosticIoControlNeedsBuilder:
    """Builder for DiagnosticIoControlNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticIoControlNeeds = DiagnosticIoControlNeeds()

    def build(self) -> DiagnosticIoControlNeeds:
        """Build and return DiagnosticIoControlNeeds object.

        Returns:
            DiagnosticIoControlNeeds instance
        """
        # TODO: Add validation
        return self._obj
