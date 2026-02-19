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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlexrayFifoConfiguration":
        """Deserialize XML element to FlexrayFifoConfiguration object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FlexrayFifoConfiguration object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse admit_without
        child = ARObject._find_child_element(element, "ADMIT-WITHOUT")
        if child is not None:
            admit_without_value = child.text
            obj.admit_without = admit_without_value

        # Parse base_cycle
        child = ARObject._find_child_element(element, "BASE-CYCLE")
        if child is not None:
            base_cycle_value = child.text
            obj.base_cycle = base_cycle_value

        # Parse channel
        child = ARObject._find_child_element(element, "CHANNEL")
        if child is not None:
            channel_value = ARObject._deserialize_by_tag(child, "FlexrayPhysicalChannel")
            obj.channel = channel_value

        # Parse cycle_repetition
        child = ARObject._find_child_element(element, "CYCLE-REPETITION")
        if child is not None:
            cycle_repetition_value = child.text
            obj.cycle_repetition = cycle_repetition_value

        # Parse fifo_depth
        child = ARObject._find_child_element(element, "FIFO-DEPTH")
        if child is not None:
            fifo_depth_value = child.text
            obj.fifo_depth = fifo_depth_value

        # Parse fifo_ranges (list)
        obj.fifo_ranges = []
        for child in ARObject._find_all_child_elements(element, "FIFO-RANGES"):
            fifo_ranges_value = ARObject._deserialize_by_tag(child, "FlexrayFifoRange")
            obj.fifo_ranges.append(fifo_ranges_value)

        # Parse msg_id_mask
        child = ARObject._find_child_element(element, "MSG-ID-MASK")
        if child is not None:
            msg_id_mask_value = child.text
            obj.msg_id_mask = msg_id_mask_value

        # Parse msg_id_match
        child = ARObject._find_child_element(element, "MSG-ID-MATCH")
        if child is not None:
            msg_id_match_value = child.text
            obj.msg_id_match = msg_id_match_value

        return obj



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
