"""FlexrayFifoConfiguration AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("admit_without", None, True, False, None),  # admitWithout
        ("base_cycle", None, True, False, None),  # baseCycle
        ("channel", None, False, False, FlexrayPhysicalChannel),  # channel
        ("cycle_repetition", None, True, False, None),  # cycleRepetition
        ("fifo_depth", None, True, False, None),  # fifoDepth
        ("fifo_ranges", None, False, True, FlexrayFifoRange),  # fifoRanges
        ("msg_id_mask", None, True, False, None),  # msgIdMask
        ("msg_id_match", None, True, False, None),  # msgIdMatch
    ]

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

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert FlexrayFifoConfiguration to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlexrayFifoConfiguration":
        """Create FlexrayFifoConfiguration from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            FlexrayFifoConfiguration instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to FlexrayFifoConfiguration since parent returns ARObject
        return cast("FlexrayFifoConfiguration", obj)


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
