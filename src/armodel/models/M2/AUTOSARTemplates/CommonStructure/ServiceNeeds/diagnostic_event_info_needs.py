"""DiagnosticEventInfoNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 312)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 760)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import (
    DiagnosticCapabilityElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class DiagnosticEventInfoNeeds(DiagnosticCapabilityElement):
    """AUTOSAR DiagnosticEventInfoNeeds."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    obd_dtc_number: Optional[PositiveInteger]
    uds_dtc_number: Optional[PositiveInteger]
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
