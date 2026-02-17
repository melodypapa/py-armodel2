"""FlexrayFifoConfiguration AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 87)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Flexray_FlexrayTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayTopology.flexray_fifo_range import (
    FlexrayFifoRange,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayTopology.flexray_physical_channel import (
    FlexrayPhysicalChannel,
)


class FlexrayFifoConfiguration(ARObject):
    """AUTOSAR FlexrayFifoConfiguration."""

    admit_without: Optional[Boolean]
    base_cycle: Optional[Integer]
    channel: Optional[FlexrayPhysicalChannel]
    cycle_repetition: Optional[Integer]
    fifo_depth: Optional[Integer]
    fifo_ranges: list[FlexrayFifoRange]
    msg_id_mask: Optional[Integer]
    msg_id_match: Optional[Integer]
    def __init__(self) -> None:
        """Initialize FlexrayFifoConfiguration."""
        super().__init__()
        self.admit_without: Optional[Boolean] = None
        self.base_cycle: Optional[Integer] = None
        self.channel: Optional[FlexrayPhysicalChannel] = None
        self.cycle_repetition: Optional[Integer] = None
        self.fifo_depth: Optional[Integer] = None
        self.fifo_ranges: list[FlexrayFifoRange] = []
        self.msg_id_mask: Optional[Integer] = None
        self.msg_id_match: Optional[Integer] = None


class FlexrayFifoConfigurationBuilder:
    """Builder for FlexrayFifoConfiguration."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FlexrayFifoConfiguration = FlexrayFifoConfiguration()

    def build(self) -> FlexrayFifoConfiguration:
        """Build and return FlexrayFifoConfiguration object.

        Returns:
            FlexrayFifoConfiguration instance
        """
        # TODO: Add validation
        return self._obj
