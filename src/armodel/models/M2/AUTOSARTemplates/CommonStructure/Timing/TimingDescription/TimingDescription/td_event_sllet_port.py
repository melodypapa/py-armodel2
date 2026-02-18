"""TDEventSLLETPort AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 79)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_sllet import (
    TDEventSLLET,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)


class TDEventSLLETPort(TDEventSLLET):
    """AUTOSAR TDEventSLLETPort."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    port: Optional[PortPrototype]
    def __init__(self) -> None:
        """Initialize TDEventSLLETPort."""
        super().__init__()
        self.port: Optional[PortPrototype] = None


class TDEventSLLETPortBuilder:
    """Builder for TDEventSLLETPort."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventSLLETPort = TDEventSLLETPort()

    def build(self) -> TDEventSLLETPort:
        """Build and return TDEventSLLETPort object.

        Returns:
            TDEventSLLETPort instance
        """
        # TODO: Add validation
        return self._obj
