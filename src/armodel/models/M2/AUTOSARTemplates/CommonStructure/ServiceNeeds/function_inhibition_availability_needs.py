"""FunctionInhibitionAvailabilityNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 318)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 751)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_needs import (
    ServiceNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.function_inhibition_needs import (
    FunctionInhibitionNeeds,
)


class FunctionInhibitionAvailabilityNeeds(ServiceNeeds):
    """AUTOSAR FunctionInhibitionAvailabilityNeeds."""

    controlled_fid: Optional[FunctionInhibitionNeeds]
    def __init__(self) -> None:
        """Initialize FunctionInhibitionAvailabilityNeeds."""
        super().__init__()
        self.controlled_fid: Optional[FunctionInhibitionNeeds] = None


class FunctionInhibitionAvailabilityNeedsBuilder:
    """Builder for FunctionInhibitionAvailabilityNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FunctionInhibitionAvailabilityNeeds = FunctionInhibitionAvailabilityNeeds()

    def build(self) -> FunctionInhibitionAvailabilityNeeds:
        """Build and return FunctionInhibitionAvailabilityNeeds object.

        Returns:
            FunctionInhibitionAvailabilityNeeds instance
        """
        # TODO: Add validation
        return self._obj
