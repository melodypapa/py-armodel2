"""FlexrayCluster AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "action_point_offset": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # actionPointOffset
        "bit": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # bit
        "cas_rx_low_max": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # casRxLowMax
        "cold_start": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # coldStart
        "cycle": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # cycle
        "cycle_count_max": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # cycleCountMax
        "detect_nit_error": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # detectNitError
        "dynamic_slot_idle_phase": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # dynamicSlotIdlePhase
        "ignore_after_tx": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # ignoreAfterTx
        "listen_noise": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # listenNoise
        "macro_per_cycle": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # macroPerCycle
        "macrotick": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # macrotick
        "max_without": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # maxWithout
        "minislot_action": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # minislotAction
        "minislot_duration": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # minislotDuration
        "network_idle_time": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # networkIdleTime
        "network": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # network
        "number_of_minislots": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # numberOfMinislots
        "number_of_static_slots": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # numberOfStaticSlots
        "offset_correction": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # offsetCorrection
        "payload_length": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # payloadLength
        "safety_margin": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # safetyMargin
        "sample_clock_period": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # sampleClockPeriod
        "static_slot": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # staticSlot
        "symbol_window": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # symbolWindow
        "sync_frame_id": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # syncFrameId
        "tranceiver": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # tranceiver
        "transmission": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # transmission
        "wakeup_rx_idle": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # wakeupRxIdle
        "wakeup_rx_low": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # wakeupRxLow
        "wakeup_rx": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # wakeupRx
        "wakeup_tx_active": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # wakeupTxActive
        "wakeup_tx_idle": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # wakeupTxIdle
    }

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
