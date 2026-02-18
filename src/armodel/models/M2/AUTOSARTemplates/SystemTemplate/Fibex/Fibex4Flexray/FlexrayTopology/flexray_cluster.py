"""FlexrayCluster AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 80)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Flexray_FlexrayTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Float,
    Integer,
    TimeValue,
)


class FlexrayCluster(ARObject):
    """AUTOSAR FlexrayCluster."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    action_point_offset: Optional[Integer]
    bit: Optional[TimeValue]
    cas_rx_low_max: Optional[Integer]
    cold_start: Optional[Integer]
    cycle: Optional[TimeValue]
    cycle_count_max: Optional[Integer]
    detect_nit_error: Optional[Boolean]
    dynamic_slot_idle_phase: Optional[Integer]
    ignore_after_tx: Optional[Integer]
    listen_noise: Optional[Integer]
    macro_per_cycle: Optional[Integer]
    macrotick: Optional[TimeValue]
    max_without: Optional[Integer]
    minislot_action: Optional[Integer]
    minislot_duration: Optional[Integer]
    network_idle_time: Optional[Integer]
    network: Optional[Integer]
    number_of_minislots: Optional[Integer]
    number_of_static_slots: Optional[Integer]
    offset_correction: Optional[Integer]
    payload_length: Optional[Integer]
    safety_margin: Optional[Integer]
    sample_clock_period: Optional[TimeValue]
    static_slot: Optional[Integer]
    symbol_window: Optional[Integer]
    sync_frame_id: Optional[Integer]
    tranceiver: Optional[Float]
    transmission: Optional[Integer]
    wakeup_rx_idle: Optional[Integer]
    wakeup_rx_low: Optional[Integer]
    wakeup_rx: Optional[Integer]
    wakeup_tx_active: Optional[Integer]
    wakeup_tx_idle: Optional[Integer]
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
