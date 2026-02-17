"""ObdMonitorServiceNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 324)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 797)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import (
    DiagnosticCapabilityElement,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    DiagnosticMonitorUpdateKindEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.application_data_type import (
    ApplicationDataType,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_event_needs import (
    DiagnosticEventNeeds,
)


class ObdMonitorServiceNeeds(DiagnosticCapabilityElement):
    """AUTOSAR ObdMonitorServiceNeeds."""

    application_data: Optional[ApplicationDataType]
    event_needs: Optional[DiagnosticEventNeeds]
    unit_and_scaling_id: Optional[PositiveInteger]
    update_kind: Optional[DiagnosticMonitorUpdateKindEnum]
    def __init__(self) -> None:
        """Initialize ObdMonitorServiceNeeds."""
        super().__init__()
        self.application_data: Optional[ApplicationDataType] = None
        self.event_needs: Optional[DiagnosticEventNeeds] = None
        self.unit_and_scaling_id: Optional[PositiveInteger] = None
        self.update_kind: Optional[DiagnosticMonitorUpdateKindEnum] = None


class ObdMonitorServiceNeedsBuilder:
    """Builder for ObdMonitorServiceNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ObdMonitorServiceNeeds = ObdMonitorServiceNeeds()

    def build(self) -> ObdMonitorServiceNeeds:
        """Build and return ObdMonitorServiceNeeds object.

        Returns:
            ObdMonitorServiceNeeds instance
        """
        # TODO: Add validation
        return self._obj
