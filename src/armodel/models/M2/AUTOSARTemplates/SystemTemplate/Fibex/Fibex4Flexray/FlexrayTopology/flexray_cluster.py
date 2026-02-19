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
    def serialize(self) -> ET.Element:
        """Serialize FlexrayCluster to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize action_point_offset
        if self.action_point_offset is not None:
            serialized = ARObject._serialize_item(self.action_point_offset, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ACTION-POINT-OFFSET")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize bit
        if self.bit is not None:
            serialized = ARObject._serialize_item(self.bit, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BIT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize cas_rx_low_max
        if self.cas_rx_low_max is not None:
            serialized = ARObject._serialize_item(self.cas_rx_low_max, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CAS-RX-LOW-MAX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize cold_start
        if self.cold_start is not None:
            serialized = ARObject._serialize_item(self.cold_start, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COLD-START")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize cycle
        if self.cycle is not None:
            serialized = ARObject._serialize_item(self.cycle, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CYCLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize cycle_count_max
        if self.cycle_count_max is not None:
            serialized = ARObject._serialize_item(self.cycle_count_max, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CYCLE-COUNT-MAX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize detect_nit_error
        if self.detect_nit_error is not None:
            serialized = ARObject._serialize_item(self.detect_nit_error, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DETECT-NIT-ERROR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize dynamic_slot_idle_phase
        if self.dynamic_slot_idle_phase is not None:
            serialized = ARObject._serialize_item(self.dynamic_slot_idle_phase, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DYNAMIC-SLOT-IDLE-PHASE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ignore_after_tx
        if self.ignore_after_tx is not None:
            serialized = ARObject._serialize_item(self.ignore_after_tx, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IGNORE-AFTER-TX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize listen_noise
        if self.listen_noise is not None:
            serialized = ARObject._serialize_item(self.listen_noise, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LISTEN-NOISE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize macro_per_cycle
        if self.macro_per_cycle is not None:
            serialized = ARObject._serialize_item(self.macro_per_cycle, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MACRO-PER-CYCLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize macrotick
        if self.macrotick is not None:
            serialized = ARObject._serialize_item(self.macrotick, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MACROTICK")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_without
        if self.max_without is not None:
            serialized = ARObject._serialize_item(self.max_without, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-WITHOUT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize minislot_action
        if self.minislot_action is not None:
            serialized = ARObject._serialize_item(self.minislot_action, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MINISLOT-ACTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize minislot_duration
        if self.minislot_duration is not None:
            serialized = ARObject._serialize_item(self.minislot_duration, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MINISLOT-DURATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize network_idle_time
        if self.network_idle_time is not None:
            serialized = ARObject._serialize_item(self.network_idle_time, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NETWORK-IDLE-TIME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize network
        if self.network is not None:
            serialized = ARObject._serialize_item(self.network, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NETWORK")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize number_of_minislots
        if self.number_of_minislots is not None:
            serialized = ARObject._serialize_item(self.number_of_minislots, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NUMBER-OF-MINISLOTS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize number_of_static_slots
        if self.number_of_static_slots is not None:
            serialized = ARObject._serialize_item(self.number_of_static_slots, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NUMBER-OF-STATIC-SLOTS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize offset_correction
        if self.offset_correction is not None:
            serialized = ARObject._serialize_item(self.offset_correction, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("OFFSET-CORRECTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize payload_length
        if self.payload_length is not None:
            serialized = ARObject._serialize_item(self.payload_length, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PAYLOAD-LENGTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize safety_margin
        if self.safety_margin is not None:
            serialized = ARObject._serialize_item(self.safety_margin, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SAFETY-MARGIN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sample_clock_period
        if self.sample_clock_period is not None:
            serialized = ARObject._serialize_item(self.sample_clock_period, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SAMPLE-CLOCK-PERIOD")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize static_slot
        if self.static_slot is not None:
            serialized = ARObject._serialize_item(self.static_slot, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("STATIC-SLOT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize symbol_window
        if self.symbol_window is not None:
            serialized = ARObject._serialize_item(self.symbol_window, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SYMBOL-WINDOW")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sync_frame_id
        if self.sync_frame_id is not None:
            serialized = ARObject._serialize_item(self.sync_frame_id, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SYNC-FRAME-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tranceiver
        if self.tranceiver is not None:
            serialized = ARObject._serialize_item(self.tranceiver, "Float")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TRANCEIVER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize transmission
        if self.transmission is not None:
            serialized = ARObject._serialize_item(self.transmission, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TRANSMISSION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize wakeup_rx_idle
        if self.wakeup_rx_idle is not None:
            serialized = ARObject._serialize_item(self.wakeup_rx_idle, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("WAKEUP-RX-IDLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize wakeup_rx_low
        if self.wakeup_rx_low is not None:
            serialized = ARObject._serialize_item(self.wakeup_rx_low, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("WAKEUP-RX-LOW")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize wakeup_rx
        if self.wakeup_rx is not None:
            serialized = ARObject._serialize_item(self.wakeup_rx, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("WAKEUP-RX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize wakeup_tx_active
        if self.wakeup_tx_active is not None:
            serialized = ARObject._serialize_item(self.wakeup_tx_active, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("WAKEUP-TX-ACTIVE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize wakeup_tx_idle
        if self.wakeup_tx_idle is not None:
            serialized = ARObject._serialize_item(self.wakeup_tx_idle, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("WAKEUP-TX-IDLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlexrayCluster":
        """Deserialize XML element to FlexrayCluster object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FlexrayCluster object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse action_point_offset
        child = ARObject._find_child_element(element, "ACTION-POINT-OFFSET")
        if child is not None:
            action_point_offset_value = child.text
            obj.action_point_offset = action_point_offset_value

        # Parse bit
        child = ARObject._find_child_element(element, "BIT")
        if child is not None:
            bit_value = child.text
            obj.bit = bit_value

        # Parse cas_rx_low_max
        child = ARObject._find_child_element(element, "CAS-RX-LOW-MAX")
        if child is not None:
            cas_rx_low_max_value = child.text
            obj.cas_rx_low_max = cas_rx_low_max_value

        # Parse cold_start
        child = ARObject._find_child_element(element, "COLD-START")
        if child is not None:
            cold_start_value = child.text
            obj.cold_start = cold_start_value

        # Parse cycle
        child = ARObject._find_child_element(element, "CYCLE")
        if child is not None:
            cycle_value = child.text
            obj.cycle = cycle_value

        # Parse cycle_count_max
        child = ARObject._find_child_element(element, "CYCLE-COUNT-MAX")
        if child is not None:
            cycle_count_max_value = child.text
            obj.cycle_count_max = cycle_count_max_value

        # Parse detect_nit_error
        child = ARObject._find_child_element(element, "DETECT-NIT-ERROR")
        if child is not None:
            detect_nit_error_value = child.text
            obj.detect_nit_error = detect_nit_error_value

        # Parse dynamic_slot_idle_phase
        child = ARObject._find_child_element(element, "DYNAMIC-SLOT-IDLE-PHASE")
        if child is not None:
            dynamic_slot_idle_phase_value = child.text
            obj.dynamic_slot_idle_phase = dynamic_slot_idle_phase_value

        # Parse ignore_after_tx
        child = ARObject._find_child_element(element, "IGNORE-AFTER-TX")
        if child is not None:
            ignore_after_tx_value = child.text
            obj.ignore_after_tx = ignore_after_tx_value

        # Parse listen_noise
        child = ARObject._find_child_element(element, "LISTEN-NOISE")
        if child is not None:
            listen_noise_value = child.text
            obj.listen_noise = listen_noise_value

        # Parse macro_per_cycle
        child = ARObject._find_child_element(element, "MACRO-PER-CYCLE")
        if child is not None:
            macro_per_cycle_value = child.text
            obj.macro_per_cycle = macro_per_cycle_value

        # Parse macrotick
        child = ARObject._find_child_element(element, "MACROTICK")
        if child is not None:
            macrotick_value = child.text
            obj.macrotick = macrotick_value

        # Parse max_without
        child = ARObject._find_child_element(element, "MAX-WITHOUT")
        if child is not None:
            max_without_value = child.text
            obj.max_without = max_without_value

        # Parse minislot_action
        child = ARObject._find_child_element(element, "MINISLOT-ACTION")
        if child is not None:
            minislot_action_value = child.text
            obj.minislot_action = minislot_action_value

        # Parse minislot_duration
        child = ARObject._find_child_element(element, "MINISLOT-DURATION")
        if child is not None:
            minislot_duration_value = child.text
            obj.minislot_duration = minislot_duration_value

        # Parse network_idle_time
        child = ARObject._find_child_element(element, "NETWORK-IDLE-TIME")
        if child is not None:
            network_idle_time_value = child.text
            obj.network_idle_time = network_idle_time_value

        # Parse network
        child = ARObject._find_child_element(element, "NETWORK")
        if child is not None:
            network_value = child.text
            obj.network = network_value

        # Parse number_of_minislots
        child = ARObject._find_child_element(element, "NUMBER-OF-MINISLOTS")
        if child is not None:
            number_of_minislots_value = child.text
            obj.number_of_minislots = number_of_minislots_value

        # Parse number_of_static_slots
        child = ARObject._find_child_element(element, "NUMBER-OF-STATIC-SLOTS")
        if child is not None:
            number_of_static_slots_value = child.text
            obj.number_of_static_slots = number_of_static_slots_value

        # Parse offset_correction
        child = ARObject._find_child_element(element, "OFFSET-CORRECTION")
        if child is not None:
            offset_correction_value = child.text
            obj.offset_correction = offset_correction_value

        # Parse payload_length
        child = ARObject._find_child_element(element, "PAYLOAD-LENGTH")
        if child is not None:
            payload_length_value = child.text
            obj.payload_length = payload_length_value

        # Parse safety_margin
        child = ARObject._find_child_element(element, "SAFETY-MARGIN")
        if child is not None:
            safety_margin_value = child.text
            obj.safety_margin = safety_margin_value

        # Parse sample_clock_period
        child = ARObject._find_child_element(element, "SAMPLE-CLOCK-PERIOD")
        if child is not None:
            sample_clock_period_value = child.text
            obj.sample_clock_period = sample_clock_period_value

        # Parse static_slot
        child = ARObject._find_child_element(element, "STATIC-SLOT")
        if child is not None:
            static_slot_value = child.text
            obj.static_slot = static_slot_value

        # Parse symbol_window
        child = ARObject._find_child_element(element, "SYMBOL-WINDOW")
        if child is not None:
            symbol_window_value = child.text
            obj.symbol_window = symbol_window_value

        # Parse sync_frame_id
        child = ARObject._find_child_element(element, "SYNC-FRAME-ID")
        if child is not None:
            sync_frame_id_value = child.text
            obj.sync_frame_id = sync_frame_id_value

        # Parse tranceiver
        child = ARObject._find_child_element(element, "TRANCEIVER")
        if child is not None:
            tranceiver_value = child.text
            obj.tranceiver = tranceiver_value

        # Parse transmission
        child = ARObject._find_child_element(element, "TRANSMISSION")
        if child is not None:
            transmission_value = child.text
            obj.transmission = transmission_value

        # Parse wakeup_rx_idle
        child = ARObject._find_child_element(element, "WAKEUP-RX-IDLE")
        if child is not None:
            wakeup_rx_idle_value = child.text
            obj.wakeup_rx_idle = wakeup_rx_idle_value

        # Parse wakeup_rx_low
        child = ARObject._find_child_element(element, "WAKEUP-RX-LOW")
        if child is not None:
            wakeup_rx_low_value = child.text
            obj.wakeup_rx_low = wakeup_rx_low_value

        # Parse wakeup_rx
        child = ARObject._find_child_element(element, "WAKEUP-RX")
        if child is not None:
            wakeup_rx_value = child.text
            obj.wakeup_rx = wakeup_rx_value

        # Parse wakeup_tx_active
        child = ARObject._find_child_element(element, "WAKEUP-TX-ACTIVE")
        if child is not None:
            wakeup_tx_active_value = child.text
            obj.wakeup_tx_active = wakeup_tx_active_value

        # Parse wakeup_tx_idle
        child = ARObject._find_child_element(element, "WAKEUP-TX-IDLE")
        if child is not None:
            wakeup_tx_idle_value = child.text
            obj.wakeup_tx_idle = wakeup_tx_idle_value

        return obj



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
