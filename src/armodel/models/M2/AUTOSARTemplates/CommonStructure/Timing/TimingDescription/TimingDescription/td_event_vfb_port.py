"""TDEventVfbPort AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 52)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 221)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_vfb import (
    TDEventVfb,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.BlueprintDedicated.Port.port_prototype_blueprint import (
    PortPrototypeBlueprint,
)


class TDEventVfbPort(TDEventVfb):
    """AUTOSAR TDEventVfbPort."""
    """Abstract base class - do not instantiate directly."""

    def __init__(self) -> None:
        """Initialize TDEventVfbPort."""
        super().__init__()
        self.is_external: Optional[Boolean] = None
        self.port: Optional[PortPrototype] = None
        self.port_prototype: Optional[PortPrototypeBlueprint] = None


class TDEventVfbPortBuilder:
    """Builder for TDEventVfbPort."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventVfbPort = TDEventVfbPort()

    def build(self) -> TDEventVfbPort:
        """Build and return TDEventVfbPort object.

        Returns:
            TDEventVfbPort instance
        """
        # TODO: Add validation
        return self._obj
