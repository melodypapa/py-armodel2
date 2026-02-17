"""TDEventCom AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 65)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description_event import (
    TimingDescriptionEvent,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.ecu_instance import (
    EcuInstance,
)


class TDEventCom(TimingDescriptionEvent):
    """AUTOSAR TDEventCom."""
    """Abstract base class - do not instantiate directly."""

    ecu_instance: Optional[EcuInstance]
    def __init__(self) -> None:
        """Initialize TDEventCom."""
        super().__init__()
        self.ecu_instance: Optional[EcuInstance] = None


class TDEventComBuilder:
    """Builder for TDEventCom."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventCom = TDEventCom()

    def build(self) -> TDEventCom:
        """Build and return TDEventCom object.

        Returns:
            TDEventCom instance
        """
        # TODO: Add validation
        return self._obj
