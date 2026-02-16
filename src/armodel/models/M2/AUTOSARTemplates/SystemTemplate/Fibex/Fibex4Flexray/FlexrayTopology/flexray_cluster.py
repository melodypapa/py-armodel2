"""FlexrayCluster AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Float,
    Integer,
    TimeValue,
)


class FlexrayCluster(ARObject):
    """AUTOSAR FlexrayCluster."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("action_point_offset", None, True, False, None),  # actionPointOffset
        ("bit", None, True, False, None),  # bit
        ("cas_rx_low_max", None, True, False, None),  # casRxLowMax
        ("cold_start", None, True, False, None),  # coldStart
        ("cycle", None, True, False, None),  # cycle
        ("cycle_count_max", None, True, False, None),  # cycleCountMax
        ("detect_nit_error", None, True, False, None),  # detectNitError
        ("dynamic_slot_idle_phase", None, True, False, None),  # dynamicSlotIdlePhase
        ("ignore_after_tx", None, True, False, None),  # ignoreAfterTx
        ("listen_noise", None, True, False, None),  # listenNoise
        ("macro_per_cycle", None, True, False, None),  # macroPerCycle
        ("macrotick", None, True, False, None),  # macrotick
        ("max_without", None, True, False, None),  # maxWithout
        ("minislot_action", None, True, False, None),  # minislotAction
        ("minislot_duration", None, True, False, None),  # minislotDuration
        ("network_idle_time", None, True, False, None),  # networkIdleTime
        ("network", None, True, False, None),  # network
        ("number_of_minislots", None, True, False, None),  # numberOfMinislots
        ("number_of_static_slots", None, True, False, None),  # numberOfStaticSlots
        ("offset_correction", None, True, False, None),  # offsetCorrection
        ("payload_length", None, True, False, None),  # payloadLength
        ("safety_margin", None, True, False, None),  # safetyMargin
        ("sample_clock_period", None, True, False, None),  # sampleClockPeriod
        ("static_slot", None, True, False, None),  # staticSlot
        ("symbol_window", None, True, False, None),  # symbolWindow
        ("sync_frame_id", None, True, False, None),  # syncFrameId
        ("tranceiver", None, True, False, None),  # tranceiver
        ("transmission", None, True, False, None),  # transmission
        ("wakeup_rx_idle", None, True, False, None),  # wakeupRxIdle
        ("wakeup_rx_low", None, True, False, None),  # wakeupRxLow
        ("wakeup_rx", None, True, False, None),  # wakeupRx
        ("wakeup_tx_active", None, True, False, None),  # wakeupTxActive
        ("wakeup_tx_idle", None, True, False, None),  # wakeupTxIdle
    ]

    def __init__(self) -> None:
        """Initialize FlexrayCluster."""
        super().__init__()
        self.action_point_offset: Optional[Integer] = None
        self.bit: Optional[TimeValue] = None
        self.cas_rx_low_max: Optional[Integer] = None
        self.cold_start: Optional[Integer] = None
        self.cycle: Optional[TimeValue] = None
        self.cycle_count_max: Optional[Integer] = None
        self.detect_nit_error: Optional[Boolean] = None
        self.dynamic_slot_idle_phase: Optional[Integer] = None
        self.ignore_after_tx: Optional[Integer] = None
        self.listen_noise: Optional[Integer] = None
        self.macro_per_cycle: Optional[Integer] = None
        self.macrotick: Optional[TimeValue] = None
        self.max_without: Optional[Integer] = None
        self.minislot_action: Optional[Integer] = None
        self.minislot_duration: Optional[Integer] = None
        self.network_idle_time: Optional[Integer] = None
        self.network: Optional[Integer] = None
        self.number_of_minislots: Optional[Integer] = None
        self.number_of_static_slots: Optional[Integer] = None
        self.offset_correction: Optional[Integer] = None
        self.payload_length: Optional[Integer] = None
        self.safety_margin: Optional[Integer] = None
        self.sample_clock_period: Optional[TimeValue] = None
        self.static_slot: Optional[Integer] = None
        self.symbol_window: Optional[Integer] = None
        self.sync_frame_id: Optional[Integer] = None
        self.tranceiver: Optional[Float] = None
        self.transmission: Optional[Integer] = None
        self.wakeup_rx_idle: Optional[Integer] = None
        self.wakeup_rx_low: Optional[Integer] = None
        self.wakeup_rx: Optional[Integer] = None
        self.wakeup_tx_active: Optional[Integer] = None
        self.wakeup_tx_idle: Optional[Integer] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert FlexrayCluster to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlexrayCluster":
        """Create FlexrayCluster from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            FlexrayCluster instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to FlexrayCluster since parent returns ARObject
        return cast("FlexrayCluster", obj)


class FlexrayClusterBuilder:
    """Builder for FlexrayCluster."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FlexrayCluster = FlexrayCluster()

    def build(self) -> FlexrayCluster:
        """Build and return FlexrayCluster object.

        Returns:
            FlexrayCluster instance
        """
        # TODO: Add validation
        return self._obj
