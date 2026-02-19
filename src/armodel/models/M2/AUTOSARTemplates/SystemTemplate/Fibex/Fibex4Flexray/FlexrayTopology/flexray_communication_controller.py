"""FlexrayCommunicationController AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 84)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 446)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Flexray_FlexrayTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
    PositiveInteger,
    TimeValue,
)


class FlexrayCommunicationController(ARObject):
    """AUTOSAR FlexrayCommunicationController."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    accepted: Optional[Integer]
    allow_halt_due_to: Optional[Boolean]
    allow_passive_to: Optional[Integer]
    cluster_drift: Optional[Integer]
    decoding: Optional[Integer]
    delay: Optional[Integer]
    external_sync: Optional[Boolean]
    extern_offset: Optional[Integer]
    extern_rate: Optional[Integer]
    fall_back_internal: Optional[Boolean]
    flexray_fifos: list[Any]
    key_slot_id: Optional[PositiveInteger]
    key_slot_only: Optional[Boolean]
    key_slot_used_for: Optional[Boolean]
    latest_tx: Optional[Integer]
    listen_timeout: Optional[Integer]
    macro_initial: Optional[Integer]
    maximum: Optional[Integer]
    micro_initial: Optional[Integer]
    micro_per_cycle: Optional[Integer]
    microtick: Optional[TimeValue]
    nm_vector_early: Optional[Boolean]
    offset_correction: Optional[Integer]
    rate_correction: Optional[Integer]
    samples_per_microtick: Optional[Integer]
    second_key_slot: Optional[PositiveInteger]
    two_key_slot: Optional[Boolean]
    wake_up_pattern: Optional[Integer]
    def __init__(self) -> None:
        """Initialize FlexrayCommunicationController."""
        super().__init__()
        self.accepted: Optional[Integer] = None
        self.allow_halt_due_to: Optional[Boolean] = None
        self.allow_passive_to: Optional[Integer] = None
        self.cluster_drift: Optional[Integer] = None
        self.decoding: Optional[Integer] = None
        self.delay: Optional[Integer] = None
        self.external_sync: Optional[Boolean] = None
        self.extern_offset: Optional[Integer] = None
        self.extern_rate: Optional[Integer] = None
        self.fall_back_internal: Optional[Boolean] = None
        self.flexray_fifos: list[Any] = []
        self.key_slot_id: Optional[PositiveInteger] = None
        self.key_slot_only: Optional[Boolean] = None
        self.key_slot_used_for: Optional[Boolean] = None
        self.latest_tx: Optional[Integer] = None
        self.listen_timeout: Optional[Integer] = None
        self.macro_initial: Optional[Integer] = None
        self.maximum: Optional[Integer] = None
        self.micro_initial: Optional[Integer] = None
        self.micro_per_cycle: Optional[Integer] = None
        self.microtick: Optional[TimeValue] = None
        self.nm_vector_early: Optional[Boolean] = None
        self.offset_correction: Optional[Integer] = None
        self.rate_correction: Optional[Integer] = None
        self.samples_per_microtick: Optional[Integer] = None
        self.second_key_slot: Optional[PositiveInteger] = None
        self.two_key_slot: Optional[Boolean] = None
        self.wake_up_pattern: Optional[Integer] = None
    def serialize(self) -> ET.Element:
        """Serialize FlexrayCommunicationController to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # Serialize accepted
        if self.accepted is not None:
            serialized = ARObject._serialize_item(self.accepted, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ACCEPTED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize allow_halt_due_to
        if self.allow_halt_due_to is not None:
            serialized = ARObject._serialize_item(self.allow_halt_due_to, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ALLOW-HALT-DUE-TO")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize allow_passive_to
        if self.allow_passive_to is not None:
            serialized = ARObject._serialize_item(self.allow_passive_to, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ALLOW-PASSIVE-TO")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize cluster_drift
        if self.cluster_drift is not None:
            serialized = ARObject._serialize_item(self.cluster_drift, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CLUSTER-DRIFT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize decoding
        if self.decoding is not None:
            serialized = ARObject._serialize_item(self.decoding, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DECODING")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize delay
        if self.delay is not None:
            serialized = ARObject._serialize_item(self.delay, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DELAY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize external_sync
        if self.external_sync is not None:
            serialized = ARObject._serialize_item(self.external_sync, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EXTERNAL-SYNC")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize extern_offset
        if self.extern_offset is not None:
            serialized = ARObject._serialize_item(self.extern_offset, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EXTERN-OFFSET")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize extern_rate
        if self.extern_rate is not None:
            serialized = ARObject._serialize_item(self.extern_rate, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EXTERN-RATE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize fall_back_internal
        if self.fall_back_internal is not None:
            serialized = ARObject._serialize_item(self.fall_back_internal, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FALL-BACK-INTERNAL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize flexray_fifos (list to container "FLEXRAY-FIFOS")
        if self.flexray_fifos:
            wrapper = ET.Element("FLEXRAY-FIFOS")
            for item in self.flexray_fifos:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize key_slot_id
        if self.key_slot_id is not None:
            serialized = ARObject._serialize_item(self.key_slot_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("KEY-SLOT-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize key_slot_only
        if self.key_slot_only is not None:
            serialized = ARObject._serialize_item(self.key_slot_only, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("KEY-SLOT-ONLY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize key_slot_used_for
        if self.key_slot_used_for is not None:
            serialized = ARObject._serialize_item(self.key_slot_used_for, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("KEY-SLOT-USED-FOR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize latest_tx
        if self.latest_tx is not None:
            serialized = ARObject._serialize_item(self.latest_tx, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LATEST-TX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize listen_timeout
        if self.listen_timeout is not None:
            serialized = ARObject._serialize_item(self.listen_timeout, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LISTEN-TIMEOUT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize macro_initial
        if self.macro_initial is not None:
            serialized = ARObject._serialize_item(self.macro_initial, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MACRO-INITIAL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize maximum
        if self.maximum is not None:
            serialized = ARObject._serialize_item(self.maximum, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAXIMUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize micro_initial
        if self.micro_initial is not None:
            serialized = ARObject._serialize_item(self.micro_initial, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MICRO-INITIAL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize micro_per_cycle
        if self.micro_per_cycle is not None:
            serialized = ARObject._serialize_item(self.micro_per_cycle, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MICRO-PER-CYCLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize microtick
        if self.microtick is not None:
            serialized = ARObject._serialize_item(self.microtick, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MICROTICK")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_vector_early
        if self.nm_vector_early is not None:
            serialized = ARObject._serialize_item(self.nm_vector_early, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-VECTOR-EARLY")
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

        # Serialize rate_correction
        if self.rate_correction is not None:
            serialized = ARObject._serialize_item(self.rate_correction, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RATE-CORRECTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize samples_per_microtick
        if self.samples_per_microtick is not None:
            serialized = ARObject._serialize_item(self.samples_per_microtick, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SAMPLES-PER-MICROTICK")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize second_key_slot
        if self.second_key_slot is not None:
            serialized = ARObject._serialize_item(self.second_key_slot, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SECOND-KEY-SLOT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize two_key_slot
        if self.two_key_slot is not None:
            serialized = ARObject._serialize_item(self.two_key_slot, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TWO-KEY-SLOT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize wake_up_pattern
        if self.wake_up_pattern is not None:
            serialized = ARObject._serialize_item(self.wake_up_pattern, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("WAKE-UP-PATTERN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlexrayCommunicationController":
        """Deserialize XML element to FlexrayCommunicationController object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FlexrayCommunicationController object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse accepted
        child = ARObject._find_child_element(element, "ACCEPTED")
        if child is not None:
            accepted_value = child.text
            obj.accepted = accepted_value

        # Parse allow_halt_due_to
        child = ARObject._find_child_element(element, "ALLOW-HALT-DUE-TO")
        if child is not None:
            allow_halt_due_to_value = child.text
            obj.allow_halt_due_to = allow_halt_due_to_value

        # Parse allow_passive_to
        child = ARObject._find_child_element(element, "ALLOW-PASSIVE-TO")
        if child is not None:
            allow_passive_to_value = child.text
            obj.allow_passive_to = allow_passive_to_value

        # Parse cluster_drift
        child = ARObject._find_child_element(element, "CLUSTER-DRIFT")
        if child is not None:
            cluster_drift_value = child.text
            obj.cluster_drift = cluster_drift_value

        # Parse decoding
        child = ARObject._find_child_element(element, "DECODING")
        if child is not None:
            decoding_value = child.text
            obj.decoding = decoding_value

        # Parse delay
        child = ARObject._find_child_element(element, "DELAY")
        if child is not None:
            delay_value = child.text
            obj.delay = delay_value

        # Parse external_sync
        child = ARObject._find_child_element(element, "EXTERNAL-SYNC")
        if child is not None:
            external_sync_value = child.text
            obj.external_sync = external_sync_value

        # Parse extern_offset
        child = ARObject._find_child_element(element, "EXTERN-OFFSET")
        if child is not None:
            extern_offset_value = child.text
            obj.extern_offset = extern_offset_value

        # Parse extern_rate
        child = ARObject._find_child_element(element, "EXTERN-RATE")
        if child is not None:
            extern_rate_value = child.text
            obj.extern_rate = extern_rate_value

        # Parse fall_back_internal
        child = ARObject._find_child_element(element, "FALL-BACK-INTERNAL")
        if child is not None:
            fall_back_internal_value = child.text
            obj.fall_back_internal = fall_back_internal_value

        # Parse flexray_fifos (list from container "FLEXRAY-FIFOS")
        obj.flexray_fifos = []
        container = ARObject._find_child_element(element, "FLEXRAY-FIFOS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.flexray_fifos.append(child_value)

        # Parse key_slot_id
        child = ARObject._find_child_element(element, "KEY-SLOT-ID")
        if child is not None:
            key_slot_id_value = child.text
            obj.key_slot_id = key_slot_id_value

        # Parse key_slot_only
        child = ARObject._find_child_element(element, "KEY-SLOT-ONLY")
        if child is not None:
            key_slot_only_value = child.text
            obj.key_slot_only = key_slot_only_value

        # Parse key_slot_used_for
        child = ARObject._find_child_element(element, "KEY-SLOT-USED-FOR")
        if child is not None:
            key_slot_used_for_value = child.text
            obj.key_slot_used_for = key_slot_used_for_value

        # Parse latest_tx
        child = ARObject._find_child_element(element, "LATEST-TX")
        if child is not None:
            latest_tx_value = child.text
            obj.latest_tx = latest_tx_value

        # Parse listen_timeout
        child = ARObject._find_child_element(element, "LISTEN-TIMEOUT")
        if child is not None:
            listen_timeout_value = child.text
            obj.listen_timeout = listen_timeout_value

        # Parse macro_initial
        child = ARObject._find_child_element(element, "MACRO-INITIAL")
        if child is not None:
            macro_initial_value = child.text
            obj.macro_initial = macro_initial_value

        # Parse maximum
        child = ARObject._find_child_element(element, "MAXIMUM")
        if child is not None:
            maximum_value = child.text
            obj.maximum = maximum_value

        # Parse micro_initial
        child = ARObject._find_child_element(element, "MICRO-INITIAL")
        if child is not None:
            micro_initial_value = child.text
            obj.micro_initial = micro_initial_value

        # Parse micro_per_cycle
        child = ARObject._find_child_element(element, "MICRO-PER-CYCLE")
        if child is not None:
            micro_per_cycle_value = child.text
            obj.micro_per_cycle = micro_per_cycle_value

        # Parse microtick
        child = ARObject._find_child_element(element, "MICROTICK")
        if child is not None:
            microtick_value = child.text
            obj.microtick = microtick_value

        # Parse nm_vector_early
        child = ARObject._find_child_element(element, "NM-VECTOR-EARLY")
        if child is not None:
            nm_vector_early_value = child.text
            obj.nm_vector_early = nm_vector_early_value

        # Parse offset_correction
        child = ARObject._find_child_element(element, "OFFSET-CORRECTION")
        if child is not None:
            offset_correction_value = child.text
            obj.offset_correction = offset_correction_value

        # Parse rate_correction
        child = ARObject._find_child_element(element, "RATE-CORRECTION")
        if child is not None:
            rate_correction_value = child.text
            obj.rate_correction = rate_correction_value

        # Parse samples_per_microtick
        child = ARObject._find_child_element(element, "SAMPLES-PER-MICROTICK")
        if child is not None:
            samples_per_microtick_value = child.text
            obj.samples_per_microtick = samples_per_microtick_value

        # Parse second_key_slot
        child = ARObject._find_child_element(element, "SECOND-KEY-SLOT")
        if child is not None:
            second_key_slot_value = child.text
            obj.second_key_slot = second_key_slot_value

        # Parse two_key_slot
        child = ARObject._find_child_element(element, "TWO-KEY-SLOT")
        if child is not None:
            two_key_slot_value = child.text
            obj.two_key_slot = two_key_slot_value

        # Parse wake_up_pattern
        child = ARObject._find_child_element(element, "WAKE-UP-PATTERN")
        if child is not None:
            wake_up_pattern_value = child.text
            obj.wake_up_pattern = wake_up_pattern_value

        return obj



class FlexrayCommunicationControllerBuilder:
    """Builder for FlexrayCommunicationController."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FlexrayCommunicationController = FlexrayCommunicationController()

    def build(self) -> FlexrayCommunicationController:
        """Build and return FlexrayCommunicationController object.

        Returns:
            FlexrayCommunicationController instance
        """
        # TODO: Add validation
        return self._obj
