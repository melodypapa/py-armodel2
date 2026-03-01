"""FlexrayCluster AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 80)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Flexray_FlexrayTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel2.serialization.decorators import atp_variant

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Float,
    Integer,
    TimeValue,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


@atp_variant()

class FlexrayCluster(ARObject):
    """AUTOSAR FlexrayCluster."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "FLEXRAY-CLUSTER"


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
    _DESERIALIZE_DISPATCH = {
        "ACTION-POINT-OFFSET": lambda obj, elem: setattr(obj, "action_point_offset", SerializationHelper.deserialize_by_tag(elem, "Integer")),
        "BIT": lambda obj, elem: setattr(obj, "bit", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "CAS-RX-LOW-MAX": lambda obj, elem: setattr(obj, "cas_rx_low_max", SerializationHelper.deserialize_by_tag(elem, "Integer")),
        "COLD-START": lambda obj, elem: setattr(obj, "cold_start", SerializationHelper.deserialize_by_tag(elem, "Integer")),
        "CYCLE": lambda obj, elem: setattr(obj, "cycle", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "CYCLE-COUNT-MAX": lambda obj, elem: setattr(obj, "cycle_count_max", SerializationHelper.deserialize_by_tag(elem, "Integer")),
        "DETECT-NIT-ERROR": lambda obj, elem: setattr(obj, "detect_nit_error", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "DYNAMIC-SLOT-IDLE-PHASE": lambda obj, elem: setattr(obj, "dynamic_slot_idle_phase", SerializationHelper.deserialize_by_tag(elem, "Integer")),
        "IGNORE-AFTER-TX": lambda obj, elem: setattr(obj, "ignore_after_tx", SerializationHelper.deserialize_by_tag(elem, "Integer")),
        "LISTEN-NOISE": lambda obj, elem: setattr(obj, "listen_noise", SerializationHelper.deserialize_by_tag(elem, "Integer")),
        "MACRO-PER-CYCLE": lambda obj, elem: setattr(obj, "macro_per_cycle", SerializationHelper.deserialize_by_tag(elem, "Integer")),
        "MACROTICK": lambda obj, elem: setattr(obj, "macrotick", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "MAX-WITHOUT": lambda obj, elem: setattr(obj, "max_without", SerializationHelper.deserialize_by_tag(elem, "Integer")),
        "MINISLOT-ACTION": lambda obj, elem: setattr(obj, "minislot_action", SerializationHelper.deserialize_by_tag(elem, "Integer")),
        "MINISLOT-DURATION": lambda obj, elem: setattr(obj, "minislot_duration", SerializationHelper.deserialize_by_tag(elem, "Integer")),
        "NETWORK-IDLE-TIME": lambda obj, elem: setattr(obj, "network_idle_time", SerializationHelper.deserialize_by_tag(elem, "Integer")),
        "NETWORK": lambda obj, elem: setattr(obj, "network", SerializationHelper.deserialize_by_tag(elem, "Integer")),
        "NUMBER-OF-MINISLOTS": lambda obj, elem: setattr(obj, "number_of_minislots", SerializationHelper.deserialize_by_tag(elem, "Integer")),
        "NUMBER-OF-STATIC-SLOTS": lambda obj, elem: setattr(obj, "number_of_static_slots", SerializationHelper.deserialize_by_tag(elem, "Integer")),
        "OFFSET-CORRECTION": lambda obj, elem: setattr(obj, "offset_correction", SerializationHelper.deserialize_by_tag(elem, "Integer")),
        "PAYLOAD-LENGTH": lambda obj, elem: setattr(obj, "payload_length", SerializationHelper.deserialize_by_tag(elem, "Integer")),
        "SAFETY-MARGIN": lambda obj, elem: setattr(obj, "safety_margin", SerializationHelper.deserialize_by_tag(elem, "Integer")),
        "SAMPLE-CLOCK-PERIOD": lambda obj, elem: setattr(obj, "sample_clock_period", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "STATIC-SLOT": lambda obj, elem: setattr(obj, "static_slot", SerializationHelper.deserialize_by_tag(elem, "Integer")),
        "SYMBOL-WINDOW": lambda obj, elem: setattr(obj, "symbol_window", SerializationHelper.deserialize_by_tag(elem, "Integer")),
        "SYNC-FRAME-ID": lambda obj, elem: setattr(obj, "sync_frame_id", SerializationHelper.deserialize_by_tag(elem, "Integer")),
        "TRANCEIVER": lambda obj, elem: setattr(obj, "tranceiver", SerializationHelper.deserialize_by_tag(elem, "Float")),
        "TRANSMISSION": lambda obj, elem: setattr(obj, "transmission", SerializationHelper.deserialize_by_tag(elem, "Integer")),
        "WAKEUP-RX-IDLE": lambda obj, elem: setattr(obj, "wakeup_rx_idle", SerializationHelper.deserialize_by_tag(elem, "Integer")),
        "WAKEUP-RX-LOW": lambda obj, elem: setattr(obj, "wakeup_rx_low", SerializationHelper.deserialize_by_tag(elem, "Integer")),
        "WAKEUP-RX": lambda obj, elem: setattr(obj, "wakeup_rx", SerializationHelper.deserialize_by_tag(elem, "Integer")),
        "WAKEUP-TX-ACTIVE": lambda obj, elem: setattr(obj, "wakeup_tx_active", SerializationHelper.deserialize_by_tag(elem, "Integer")),
        "WAKEUP-TX-IDLE": lambda obj, elem: setattr(obj, "wakeup_tx_idle", SerializationHelper.deserialize_by_tag(elem, "Integer")),
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

    def serialize(self) -> ET.Element:
        """Serialize FlexrayCluster to XML element with atp_variant wrapper.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(FlexrayCluster, self).serialize()

        # Copy all attributes from parent element to outer element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element to outer element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Create inner element to hold attributes before wrapping
        inner_elem = ET.Element("INNER")

        # Copy parent's children: metadata to outer element, others to inner element
        metadata_tags = {'SHORT-NAME', 'LONG-NAME', 'DESC', 'ADMIN-DATA'}
        for child in parent_elem:
            tag = SerializationHelper.strip_namespace(child.tag)
            if tag in metadata_tags:
                # Metadata elements stay outside the atp_variant wrapper
                elem.append(child)
            else:
                # Other elements go inside the atp_variant wrapper
                inner_elem.append(child)

        # Serialize action_point_offset
        if self.action_point_offset is not None:
            serialized = SerializationHelper.serialize_item(self.action_point_offset, "Integer")
            if serialized is not None:
                wrapped = ET.Element("ACTION-POINT-OFFSET")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize bit
        if self.bit is not None:
            serialized = SerializationHelper.serialize_item(self.bit, "TimeValue")
            if serialized is not None:
                wrapped = ET.Element("BIT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize cas_rx_low_max
        if self.cas_rx_low_max is not None:
            serialized = SerializationHelper.serialize_item(self.cas_rx_low_max, "Integer")
            if serialized is not None:
                wrapped = ET.Element("CAS-RX-LOW-MAX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize cold_start
        if self.cold_start is not None:
            serialized = SerializationHelper.serialize_item(self.cold_start, "Integer")
            if serialized is not None:
                wrapped = ET.Element("COLD-START")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize cycle
        if self.cycle is not None:
            serialized = SerializationHelper.serialize_item(self.cycle, "TimeValue")
            if serialized is not None:
                wrapped = ET.Element("CYCLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize cycle_count_max
        if self.cycle_count_max is not None:
            serialized = SerializationHelper.serialize_item(self.cycle_count_max, "Integer")
            if serialized is not None:
                wrapped = ET.Element("CYCLE-COUNT-MAX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize detect_nit_error
        if self.detect_nit_error is not None:
            serialized = SerializationHelper.serialize_item(self.detect_nit_error, "Boolean")
            if serialized is not None:
                wrapped = ET.Element("DETECT-NIT-ERROR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize dynamic_slot_idle_phase
        if self.dynamic_slot_idle_phase is not None:
            serialized = SerializationHelper.serialize_item(self.dynamic_slot_idle_phase, "Integer")
            if serialized is not None:
                wrapped = ET.Element("DYNAMIC-SLOT-IDLE-PHASE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize ignore_after_tx
        if self.ignore_after_tx is not None:
            serialized = SerializationHelper.serialize_item(self.ignore_after_tx, "Integer")
            if serialized is not None:
                wrapped = ET.Element("IGNORE-AFTER-TX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize listen_noise
        if self.listen_noise is not None:
            serialized = SerializationHelper.serialize_item(self.listen_noise, "Integer")
            if serialized is not None:
                wrapped = ET.Element("LISTEN-NOISE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize macro_per_cycle
        if self.macro_per_cycle is not None:
            serialized = SerializationHelper.serialize_item(self.macro_per_cycle, "Integer")
            if serialized is not None:
                wrapped = ET.Element("MACRO-PER-CYCLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize macrotick
        if self.macrotick is not None:
            serialized = SerializationHelper.serialize_item(self.macrotick, "TimeValue")
            if serialized is not None:
                wrapped = ET.Element("MACROTICK")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize max_without
        if self.max_without is not None:
            serialized = SerializationHelper.serialize_item(self.max_without, "Integer")
            if serialized is not None:
                wrapped = ET.Element("MAX-WITHOUT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize minislot_action
        if self.minislot_action is not None:
            serialized = SerializationHelper.serialize_item(self.minislot_action, "Integer")
            if serialized is not None:
                wrapped = ET.Element("MINISLOT-ACTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize minislot_duration
        if self.minislot_duration is not None:
            serialized = SerializationHelper.serialize_item(self.minislot_duration, "Integer")
            if serialized is not None:
                wrapped = ET.Element("MINISLOT-DURATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize network_idle_time
        if self.network_idle_time is not None:
            serialized = SerializationHelper.serialize_item(self.network_idle_time, "Integer")
            if serialized is not None:
                wrapped = ET.Element("NETWORK-IDLE-TIME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize network
        if self.network is not None:
            serialized = SerializationHelper.serialize_item(self.network, "Integer")
            if serialized is not None:
                wrapped = ET.Element("NETWORK")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize number_of_minislots
        if self.number_of_minislots is not None:
            serialized = SerializationHelper.serialize_item(self.number_of_minislots, "Integer")
            if serialized is not None:
                wrapped = ET.Element("NUMBER-OF-MINISLOTS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize number_of_static_slots
        if self.number_of_static_slots is not None:
            serialized = SerializationHelper.serialize_item(self.number_of_static_slots, "Integer")
            if serialized is not None:
                wrapped = ET.Element("NUMBER-OF-STATIC-SLOTS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize offset_correction
        if self.offset_correction is not None:
            serialized = SerializationHelper.serialize_item(self.offset_correction, "Integer")
            if serialized is not None:
                wrapped = ET.Element("OFFSET-CORRECTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize payload_length
        if self.payload_length is not None:
            serialized = SerializationHelper.serialize_item(self.payload_length, "Integer")
            if serialized is not None:
                wrapped = ET.Element("PAYLOAD-LENGTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize safety_margin
        if self.safety_margin is not None:
            serialized = SerializationHelper.serialize_item(self.safety_margin, "Integer")
            if serialized is not None:
                wrapped = ET.Element("SAFETY-MARGIN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize sample_clock_period
        if self.sample_clock_period is not None:
            serialized = SerializationHelper.serialize_item(self.sample_clock_period, "TimeValue")
            if serialized is not None:
                wrapped = ET.Element("SAMPLE-CLOCK-PERIOD")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize static_slot
        if self.static_slot is not None:
            serialized = SerializationHelper.serialize_item(self.static_slot, "Integer")
            if serialized is not None:
                wrapped = ET.Element("STATIC-SLOT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize symbol_window
        if self.symbol_window is not None:
            serialized = SerializationHelper.serialize_item(self.symbol_window, "Integer")
            if serialized is not None:
                wrapped = ET.Element("SYMBOL-WINDOW")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize sync_frame_id
        if self.sync_frame_id is not None:
            serialized = SerializationHelper.serialize_item(self.sync_frame_id, "Integer")
            if serialized is not None:
                wrapped = ET.Element("SYNC-FRAME-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize tranceiver
        if self.tranceiver is not None:
            serialized = SerializationHelper.serialize_item(self.tranceiver, "Float")
            if serialized is not None:
                wrapped = ET.Element("TRANCEIVER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize transmission
        if self.transmission is not None:
            serialized = SerializationHelper.serialize_item(self.transmission, "Integer")
            if serialized is not None:
                wrapped = ET.Element("TRANSMISSION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize wakeup_rx_idle
        if self.wakeup_rx_idle is not None:
            serialized = SerializationHelper.serialize_item(self.wakeup_rx_idle, "Integer")
            if serialized is not None:
                wrapped = ET.Element("WAKEUP-RX-IDLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize wakeup_rx_low
        if self.wakeup_rx_low is not None:
            serialized = SerializationHelper.serialize_item(self.wakeup_rx_low, "Integer")
            if serialized is not None:
                wrapped = ET.Element("WAKEUP-RX-LOW")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize wakeup_rx
        if self.wakeup_rx is not None:
            serialized = SerializationHelper.serialize_item(self.wakeup_rx, "Integer")
            if serialized is not None:
                wrapped = ET.Element("WAKEUP-RX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize wakeup_tx_active
        if self.wakeup_tx_active is not None:
            serialized = SerializationHelper.serialize_item(self.wakeup_tx_active, "Integer")
            if serialized is not None:
                wrapped = ET.Element("WAKEUP-TX-ACTIVE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize wakeup_tx_idle
        if self.wakeup_tx_idle is not None:
            serialized = SerializationHelper.serialize_item(self.wakeup_tx_idle, "Integer")
            if serialized is not None:
                wrapped = ET.Element("WAKEUP-TX-IDLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Wrap inner element in atp_variant VARIANTS/CONDITIONAL structure
        wrapped = SerializationHelper.serialize_with_atp_variant(inner_elem, "FlexrayCluster")
        elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlexrayCluster":
        """Deserialize XML element to FlexrayCluster object with atp_variant unwrapping.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FlexrayCluster object
        """
        # Unwrap atp_variant VARIANTS/CONDITIONAL structure
        inner_elem = SerializationHelper.deserialize_from_atp_variant(element, "FlexrayCluster")
        if inner_elem is None:
            # No wrapper structure found, create instance with default values
            obj = cls.__new__(cls)
            obj.__init__()
            return obj

        # Temporarily copy children from inner element to outer element
        # so parent's deserialize can find inherited attributes
        for child in list(inner_elem):
            element.append(child)

        # Call parent's deserialize with outer element (now contains parent's children)
        obj = super(FlexrayCluster, cls).deserialize(element)

        # Clean up: remove the temporarily copied children from outer element
        # (they are now in obj, so we don't need them in element anymore)
        for child in list(inner_elem):
            element.remove(child)

        # Parse action_point_offset
        child = SerializationHelper.find_child_element(inner_elem, "ACTION-POINT-OFFSET")
        if child is not None:
            action_point_offset_value = child.text
            obj.action_point_offset = action_point_offset_value

        # Parse bit
        child = SerializationHelper.find_child_element(inner_elem, "BIT")
        if child is not None:
            bit_value = child.text
            obj.bit = bit_value

        # Parse cas_rx_low_max
        child = SerializationHelper.find_child_element(inner_elem, "CAS-RX-LOW-MAX")
        if child is not None:
            cas_rx_low_max_value = child.text
            obj.cas_rx_low_max = cas_rx_low_max_value

        # Parse cold_start
        child = SerializationHelper.find_child_element(inner_elem, "COLD-START")
        if child is not None:
            cold_start_value = child.text
            obj.cold_start = cold_start_value

        # Parse cycle
        child = SerializationHelper.find_child_element(inner_elem, "CYCLE")
        if child is not None:
            cycle_value = child.text
            obj.cycle = cycle_value

        # Parse cycle_count_max
        child = SerializationHelper.find_child_element(inner_elem, "CYCLE-COUNT-MAX")
        if child is not None:
            cycle_count_max_value = child.text
            obj.cycle_count_max = cycle_count_max_value

        # Parse detect_nit_error
        child = SerializationHelper.find_child_element(inner_elem, "DETECT-NIT-ERROR")
        if child is not None:
            detect_nit_error_value = child.text
            obj.detect_nit_error = detect_nit_error_value

        # Parse dynamic_slot_idle_phase
        child = SerializationHelper.find_child_element(inner_elem, "DYNAMIC-SLOT-IDLE-PHASE")
        if child is not None:
            dynamic_slot_idle_phase_value = child.text
            obj.dynamic_slot_idle_phase = dynamic_slot_idle_phase_value

        # Parse ignore_after_tx
        child = SerializationHelper.find_child_element(inner_elem, "IGNORE-AFTER-TX")
        if child is not None:
            ignore_after_tx_value = child.text
            obj.ignore_after_tx = ignore_after_tx_value

        # Parse listen_noise
        child = SerializationHelper.find_child_element(inner_elem, "LISTEN-NOISE")
        if child is not None:
            listen_noise_value = child.text
            obj.listen_noise = listen_noise_value

        # Parse macro_per_cycle
        child = SerializationHelper.find_child_element(inner_elem, "MACRO-PER-CYCLE")
        if child is not None:
            macro_per_cycle_value = child.text
            obj.macro_per_cycle = macro_per_cycle_value

        # Parse macrotick
        child = SerializationHelper.find_child_element(inner_elem, "MACROTICK")
        if child is not None:
            macrotick_value = child.text
            obj.macrotick = macrotick_value

        # Parse max_without
        child = SerializationHelper.find_child_element(inner_elem, "MAX-WITHOUT")
        if child is not None:
            max_without_value = child.text
            obj.max_without = max_without_value

        # Parse minislot_action
        child = SerializationHelper.find_child_element(inner_elem, "MINISLOT-ACTION")
        if child is not None:
            minislot_action_value = child.text
            obj.minislot_action = minislot_action_value

        # Parse minislot_duration
        child = SerializationHelper.find_child_element(inner_elem, "MINISLOT-DURATION")
        if child is not None:
            minislot_duration_value = child.text
            obj.minislot_duration = minislot_duration_value

        # Parse network_idle_time
        child = SerializationHelper.find_child_element(inner_elem, "NETWORK-IDLE-TIME")
        if child is not None:
            network_idle_time_value = child.text
            obj.network_idle_time = network_idle_time_value

        # Parse network
        child = SerializationHelper.find_child_element(inner_elem, "NETWORK")
        if child is not None:
            network_value = child.text
            obj.network = network_value

        # Parse number_of_minislots
        child = SerializationHelper.find_child_element(inner_elem, "NUMBER-OF-MINISLOTS")
        if child is not None:
            number_of_minislots_value = child.text
            obj.number_of_minislots = number_of_minislots_value

        # Parse number_of_static_slots
        child = SerializationHelper.find_child_element(inner_elem, "NUMBER-OF-STATIC-SLOTS")
        if child is not None:
            number_of_static_slots_value = child.text
            obj.number_of_static_slots = number_of_static_slots_value

        # Parse offset_correction
        child = SerializationHelper.find_child_element(inner_elem, "OFFSET-CORRECTION")
        if child is not None:
            offset_correction_value = child.text
            obj.offset_correction = offset_correction_value

        # Parse payload_length
        child = SerializationHelper.find_child_element(inner_elem, "PAYLOAD-LENGTH")
        if child is not None:
            payload_length_value = child.text
            obj.payload_length = payload_length_value

        # Parse safety_margin
        child = SerializationHelper.find_child_element(inner_elem, "SAFETY-MARGIN")
        if child is not None:
            safety_margin_value = child.text
            obj.safety_margin = safety_margin_value

        # Parse sample_clock_period
        child = SerializationHelper.find_child_element(inner_elem, "SAMPLE-CLOCK-PERIOD")
        if child is not None:
            sample_clock_period_value = child.text
            obj.sample_clock_period = sample_clock_period_value

        # Parse static_slot
        child = SerializationHelper.find_child_element(inner_elem, "STATIC-SLOT")
        if child is not None:
            static_slot_value = child.text
            obj.static_slot = static_slot_value

        # Parse symbol_window
        child = SerializationHelper.find_child_element(inner_elem, "SYMBOL-WINDOW")
        if child is not None:
            symbol_window_value = child.text
            obj.symbol_window = symbol_window_value

        # Parse sync_frame_id
        child = SerializationHelper.find_child_element(inner_elem, "SYNC-FRAME-ID")
        if child is not None:
            sync_frame_id_value = child.text
            obj.sync_frame_id = sync_frame_id_value

        # Parse tranceiver
        child = SerializationHelper.find_child_element(inner_elem, "TRANCEIVER")
        if child is not None:
            tranceiver_value = child.text
            obj.tranceiver = tranceiver_value

        # Parse transmission
        child = SerializationHelper.find_child_element(inner_elem, "TRANSMISSION")
        if child is not None:
            transmission_value = child.text
            obj.transmission = transmission_value

        # Parse wakeup_rx_idle
        child = SerializationHelper.find_child_element(inner_elem, "WAKEUP-RX-IDLE")
        if child is not None:
            wakeup_rx_idle_value = child.text
            obj.wakeup_rx_idle = wakeup_rx_idle_value

        # Parse wakeup_rx_low
        child = SerializationHelper.find_child_element(inner_elem, "WAKEUP-RX-LOW")
        if child is not None:
            wakeup_rx_low_value = child.text
            obj.wakeup_rx_low = wakeup_rx_low_value

        # Parse wakeup_rx
        child = SerializationHelper.find_child_element(inner_elem, "WAKEUP-RX")
        if child is not None:
            wakeup_rx_value = child.text
            obj.wakeup_rx = wakeup_rx_value

        # Parse wakeup_tx_active
        child = SerializationHelper.find_child_element(inner_elem, "WAKEUP-TX-ACTIVE")
        if child is not None:
            wakeup_tx_active_value = child.text
            obj.wakeup_tx_active = wakeup_tx_active_value

        # Parse wakeup_tx_idle
        child = SerializationHelper.find_child_element(inner_elem, "WAKEUP-TX-IDLE")
        if child is not None:
            wakeup_tx_idle_value = child.text
            obj.wakeup_tx_idle = wakeup_tx_idle_value

        return obj



class FlexrayClusterBuilder(BuilderBase):
    """Builder for FlexrayCluster with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: FlexrayCluster = FlexrayCluster()


    def with_action_point_offset(self, value: Optional[Integer]) -> "FlexrayClusterBuilder":
        """Set action_point_offset attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.action_point_offset = value
        return self

    def with_bit(self, value: Optional[TimeValue]) -> "FlexrayClusterBuilder":
        """Set bit attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.bit = value
        return self

    def with_cas_rx_low_max(self, value: Optional[Integer]) -> "FlexrayClusterBuilder":
        """Set cas_rx_low_max attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.cas_rx_low_max = value
        return self

    def with_cold_start(self, value: Optional[Integer]) -> "FlexrayClusterBuilder":
        """Set cold_start attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.cold_start = value
        return self

    def with_cycle(self, value: Optional[TimeValue]) -> "FlexrayClusterBuilder":
        """Set cycle attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.cycle = value
        return self

    def with_cycle_count_max(self, value: Optional[Integer]) -> "FlexrayClusterBuilder":
        """Set cycle_count_max attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.cycle_count_max = value
        return self

    def with_detect_nit_error(self, value: Optional[Boolean]) -> "FlexrayClusterBuilder":
        """Set detect_nit_error attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.detect_nit_error = value
        return self

    def with_dynamic_slot_idle_phase(self, value: Optional[Integer]) -> "FlexrayClusterBuilder":
        """Set dynamic_slot_idle_phase attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.dynamic_slot_idle_phase = value
        return self

    def with_ignore_after_tx(self, value: Optional[Integer]) -> "FlexrayClusterBuilder":
        """Set ignore_after_tx attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ignore_after_tx = value
        return self

    def with_listen_noise(self, value: Optional[Integer]) -> "FlexrayClusterBuilder":
        """Set listen_noise attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.listen_noise = value
        return self

    def with_macro_per_cycle(self, value: Optional[Integer]) -> "FlexrayClusterBuilder":
        """Set macro_per_cycle attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.macro_per_cycle = value
        return self

    def with_macrotick(self, value: Optional[TimeValue]) -> "FlexrayClusterBuilder":
        """Set macrotick attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.macrotick = value
        return self

    def with_max_without(self, value: Optional[Integer]) -> "FlexrayClusterBuilder":
        """Set max_without attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.max_without = value
        return self

    def with_minislot_action(self, value: Optional[Integer]) -> "FlexrayClusterBuilder":
        """Set minislot_action attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.minislot_action = value
        return self

    def with_minislot_duration(self, value: Optional[Integer]) -> "FlexrayClusterBuilder":
        """Set minislot_duration attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.minislot_duration = value
        return self

    def with_network_idle_time(self, value: Optional[Integer]) -> "FlexrayClusterBuilder":
        """Set network_idle_time attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.network_idle_time = value
        return self

    def with_network(self, value: Optional[Integer]) -> "FlexrayClusterBuilder":
        """Set network attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.network = value
        return self

    def with_number_of_minislots(self, value: Optional[Integer]) -> "FlexrayClusterBuilder":
        """Set number_of_minislots attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.number_of_minislots = value
        return self

    def with_number_of_static_slots(self, value: Optional[Integer]) -> "FlexrayClusterBuilder":
        """Set number_of_static_slots attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.number_of_static_slots = value
        return self

    def with_offset_correction(self, value: Optional[Integer]) -> "FlexrayClusterBuilder":
        """Set offset_correction attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.offset_correction = value
        return self

    def with_payload_length(self, value: Optional[Integer]) -> "FlexrayClusterBuilder":
        """Set payload_length attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.payload_length = value
        return self

    def with_safety_margin(self, value: Optional[Integer]) -> "FlexrayClusterBuilder":
        """Set safety_margin attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.safety_margin = value
        return self

    def with_sample_clock_period(self, value: Optional[TimeValue]) -> "FlexrayClusterBuilder":
        """Set sample_clock_period attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sample_clock_period = value
        return self

    def with_static_slot(self, value: Optional[Integer]) -> "FlexrayClusterBuilder":
        """Set static_slot attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.static_slot = value
        return self

    def with_symbol_window(self, value: Optional[Integer]) -> "FlexrayClusterBuilder":
        """Set symbol_window attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.symbol_window = value
        return self

    def with_sync_frame_id(self, value: Optional[Integer]) -> "FlexrayClusterBuilder":
        """Set sync_frame_id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sync_frame_id = value
        return self

    def with_tranceiver(self, value: Optional[Float]) -> "FlexrayClusterBuilder":
        """Set tranceiver attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tranceiver = value
        return self

    def with_transmission(self, value: Optional[Integer]) -> "FlexrayClusterBuilder":
        """Set transmission attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.transmission = value
        return self

    def with_wakeup_rx_idle(self, value: Optional[Integer]) -> "FlexrayClusterBuilder":
        """Set wakeup_rx_idle attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.wakeup_rx_idle = value
        return self

    def with_wakeup_rx_low(self, value: Optional[Integer]) -> "FlexrayClusterBuilder":
        """Set wakeup_rx_low attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.wakeup_rx_low = value
        return self

    def with_wakeup_rx(self, value: Optional[Integer]) -> "FlexrayClusterBuilder":
        """Set wakeup_rx attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.wakeup_rx = value
        return self

    def with_wakeup_tx_active(self, value: Optional[Integer]) -> "FlexrayClusterBuilder":
        """Set wakeup_tx_active attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.wakeup_tx_active = value
        return self

    def with_wakeup_tx_idle(self, value: Optional[Integer]) -> "FlexrayClusterBuilder":
        """Set wakeup_tx_idle attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.wakeup_tx_idle = value
        return self




    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Get type hints for the class
        try:
            type_hints_dict = get_type_hints(type(self._obj))
        except Exception:
            # Cannot resolve type hints (e.g., forward references), skip validation
            return

        for attr_name, attr_type in type_hints_dict.items():
            if attr_name.startswith("_"):
                continue

            value = getattr(self._obj, attr_name)

            # Check required fields (not Optional)
            if value is None and not self._is_optional_type(attr_type):
                if mode == BuilderValidationMode.STRICT:
                    raise ValueError(
                        f"Required attribute '{attr_name}' is None"
                    )
                elif mode == BuilderValidationMode.LENIENT:
                    import warnings
                    warnings.warn(
                        f"Required attribute '{attr_name}' is None",
                        UserWarning
                    )

    @staticmethod
    def _is_optional_type(type_hint: Any) -> bool:
        """Check if a type hint is Optional.

        Args:
            type_hint: Type hint to check

        Returns:
            True if type is Optional, False otherwise
        """
        origin = getattr(type_hint, "__origin__", None)
        return origin is Union

    @staticmethod
    def _get_expected_type(type_hint: Any) -> type:
        """Extract expected type from type hint.

        Args:
            type_hint: Type hint to extract from

        Returns:
            Expected type
        """
        if isinstance(type_hint, str):
            return object
        origin = getattr(type_hint, "__origin__", None)
        if origin is Union:
            args = getattr(type_hint, "__args__", [])
            for arg in args:
                if arg is not type(None):
                    return arg
        elif origin is list:
            args = getattr(type_hint, "__args__", [object])
            return args[0] if args else object
        return type_hint if isinstance(type_hint, type) else object


    def build(self) -> FlexrayCluster:
        """Build and return the FlexrayCluster instance with validation."""
        self._validate_instance()
        pass
        return self._obj