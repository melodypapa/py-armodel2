"""FlexrayCommunicationController AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 84)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 446)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Flexray_FlexrayTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET
from armodel.serialization.decorators import atp_variant

from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
    PositiveInteger,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


@atp_variant()

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
        """Serialize FlexrayCommunicationController to XML element with atp_variant wrapper.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(FlexrayCommunicationController, self).serialize()

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

        # Serialize accepted
        if self.accepted is not None:
            serialized = SerializationHelper.serialize_item(self.accepted, "Integer")
            if serialized is not None:
                wrapped = ET.Element("ACCEPTED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize allow_halt_due_to
        if self.allow_halt_due_to is not None:
            serialized = SerializationHelper.serialize_item(self.allow_halt_due_to, "Boolean")
            if serialized is not None:
                wrapped = ET.Element("ALLOW-HALT-DUE-TO")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize allow_passive_to
        if self.allow_passive_to is not None:
            serialized = SerializationHelper.serialize_item(self.allow_passive_to, "Integer")
            if serialized is not None:
                wrapped = ET.Element("ALLOW-PASSIVE-TO")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize cluster_drift
        if self.cluster_drift is not None:
            serialized = SerializationHelper.serialize_item(self.cluster_drift, "Integer")
            if serialized is not None:
                wrapped = ET.Element("CLUSTER-DRIFT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize decoding
        if self.decoding is not None:
            serialized = SerializationHelper.serialize_item(self.decoding, "Integer")
            if serialized is not None:
                wrapped = ET.Element("DECODING")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize delay
        if self.delay is not None:
            serialized = SerializationHelper.serialize_item(self.delay, "Integer")
            if serialized is not None:
                wrapped = ET.Element("DELAY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize external_sync
        if self.external_sync is not None:
            serialized = SerializationHelper.serialize_item(self.external_sync, "Boolean")
            if serialized is not None:
                wrapped = ET.Element("EXTERNAL-SYNC")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize extern_offset
        if self.extern_offset is not None:
            serialized = SerializationHelper.serialize_item(self.extern_offset, "Integer")
            if serialized is not None:
                wrapped = ET.Element("EXTERN-OFFSET")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize extern_rate
        if self.extern_rate is not None:
            serialized = SerializationHelper.serialize_item(self.extern_rate, "Integer")
            if serialized is not None:
                wrapped = ET.Element("EXTERN-RATE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize fall_back_internal
        if self.fall_back_internal is not None:
            serialized = SerializationHelper.serialize_item(self.fall_back_internal, "Boolean")
            if serialized is not None:
                wrapped = ET.Element("FALL-BACK-INTERNAL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize flexray_fifos (list from container "FLEXRAY-FIFOS")
        if self.flexray_fifos:
            container = ET.Element("FLEXRAY-FIFOS")
            for item in self.flexray_fifos:
                if is_ref:
                    # For reference lists, serialize as reference
                    if hasattr(item, "serialize"):
                        container.append(item.serialize())
                elif is_primitive_type("any (FlexrayFifo)", package_data):
                    # Simple primitive type
                    child = ET.Element("FLEXRAY-FIFO")
                    child.text = str(item)
                    container.append(child)
                elif is_enum_type("any (FlexrayFifo)", package_data):
                    # Enum type - use serialize method
                    if hasattr(item, "serialize"):
                        container.append(item.serialize())
                else:
                    # Complex object type
                    if hasattr(item, "serialize"):
                        container.append(item.serialize())
            inner_elem.append(container)

        # Serialize key_slot_id
        if self.key_slot_id is not None:
            serialized = SerializationHelper.serialize_item(self.key_slot_id, "PositiveInteger")
            if serialized is not None:
                wrapped = ET.Element("KEY-SLOT-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize key_slot_only
        if self.key_slot_only is not None:
            serialized = SerializationHelper.serialize_item(self.key_slot_only, "Boolean")
            if serialized is not None:
                wrapped = ET.Element("KEY-SLOT-ONLY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize key_slot_used_for
        if self.key_slot_used_for is not None:
            serialized = SerializationHelper.serialize_item(self.key_slot_used_for, "Boolean")
            if serialized is not None:
                wrapped = ET.Element("KEY-SLOT-USED-FOR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize latest_tx
        if self.latest_tx is not None:
            serialized = SerializationHelper.serialize_item(self.latest_tx, "Integer")
            if serialized is not None:
                wrapped = ET.Element("LATEST-TX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize listen_timeout
        if self.listen_timeout is not None:
            serialized = SerializationHelper.serialize_item(self.listen_timeout, "Integer")
            if serialized is not None:
                wrapped = ET.Element("LISTEN-TIMEOUT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize macro_initial
        if self.macro_initial is not None:
            serialized = SerializationHelper.serialize_item(self.macro_initial, "Integer")
            if serialized is not None:
                wrapped = ET.Element("MACRO-INITIAL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize maximum
        if self.maximum is not None:
            serialized = SerializationHelper.serialize_item(self.maximum, "Integer")
            if serialized is not None:
                wrapped = ET.Element("MAXIMUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize micro_initial
        if self.micro_initial is not None:
            serialized = SerializationHelper.serialize_item(self.micro_initial, "Integer")
            if serialized is not None:
                wrapped = ET.Element("MICRO-INITIAL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize micro_per_cycle
        if self.micro_per_cycle is not None:
            serialized = SerializationHelper.serialize_item(self.micro_per_cycle, "Integer")
            if serialized is not None:
                wrapped = ET.Element("MICRO-PER-CYCLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize microtick
        if self.microtick is not None:
            serialized = SerializationHelper.serialize_item(self.microtick, "TimeValue")
            if serialized is not None:
                wrapped = ET.Element("MICROTICK")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize nm_vector_early
        if self.nm_vector_early is not None:
            serialized = SerializationHelper.serialize_item(self.nm_vector_early, "Boolean")
            if serialized is not None:
                wrapped = ET.Element("NM-VECTOR-EARLY")
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

        # Serialize rate_correction
        if self.rate_correction is not None:
            serialized = SerializationHelper.serialize_item(self.rate_correction, "Integer")
            if serialized is not None:
                wrapped = ET.Element("RATE-CORRECTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize samples_per_microtick
        if self.samples_per_microtick is not None:
            serialized = SerializationHelper.serialize_item(self.samples_per_microtick, "Integer")
            if serialized is not None:
                wrapped = ET.Element("SAMPLES-PER-MICROTICK")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize second_key_slot
        if self.second_key_slot is not None:
            serialized = SerializationHelper.serialize_item(self.second_key_slot, "PositiveInteger")
            if serialized is not None:
                wrapped = ET.Element("SECOND-KEY-SLOT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize two_key_slot
        if self.two_key_slot is not None:
            serialized = SerializationHelper.serialize_item(self.two_key_slot, "Boolean")
            if serialized is not None:
                wrapped = ET.Element("TWO-KEY-SLOT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize wake_up_pattern
        if self.wake_up_pattern is not None:
            serialized = SerializationHelper.serialize_item(self.wake_up_pattern, "Integer")
            if serialized is not None:
                wrapped = ET.Element("WAKE-UP-PATTERN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Wrap inner element in atp_variant VARIANTS/CONDITIONAL structure
        wrapped = SerializationHelper.serialize_with_atp_variant(inner_elem, "FlexrayCommunicationController")
        elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlexrayCommunicationController":
        """Deserialize XML element to FlexrayCommunicationController object with atp_variant unwrapping.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FlexrayCommunicationController object
        """
        # Unwrap atp_variant VARIANTS/CONDITIONAL structure
        inner_elem = SerializationHelper.deserialize_from_atp_variant(element, "FlexrayCommunicationController")
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
        obj = super(FlexrayCommunicationController, cls).deserialize(element)

        # Clean up: remove the temporarily copied children from outer element
        # (they are now in obj, so we don't need them in element anymore)
        for child in list(inner_elem):
            element.remove(child)

        # Parse accepted
        child = SerializationHelper.find_child_element(inner_elem, "ACCEPTED")
        if child is not None:
            accepted_value = child.text
            obj.accepted = accepted_value

        # Parse allow_halt_due_to
        child = SerializationHelper.find_child_element(inner_elem, "ALLOW-HALT-DUE-TO")
        if child is not None:
            allow_halt_due_to_value = child.text
            obj.allow_halt_due_to = allow_halt_due_to_value

        # Parse allow_passive_to
        child = SerializationHelper.find_child_element(inner_elem, "ALLOW-PASSIVE-TO")
        if child is not None:
            allow_passive_to_value = child.text
            obj.allow_passive_to = allow_passive_to_value

        # Parse cluster_drift
        child = SerializationHelper.find_child_element(inner_elem, "CLUSTER-DRIFT")
        if child is not None:
            cluster_drift_value = child.text
            obj.cluster_drift = cluster_drift_value

        # Parse decoding
        child = SerializationHelper.find_child_element(inner_elem, "DECODING")
        if child is not None:
            decoding_value = child.text
            obj.decoding = decoding_value

        # Parse delay
        child = SerializationHelper.find_child_element(inner_elem, "DELAY")
        if child is not None:
            delay_value = child.text
            obj.delay = delay_value

        # Parse external_sync
        child = SerializationHelper.find_child_element(inner_elem, "EXTERNAL-SYNC")
        if child is not None:
            external_sync_value = child.text
            obj.external_sync = external_sync_value

        # Parse extern_offset
        child = SerializationHelper.find_child_element(inner_elem, "EXTERN-OFFSET")
        if child is not None:
            extern_offset_value = child.text
            obj.extern_offset = extern_offset_value

        # Parse extern_rate
        child = SerializationHelper.find_child_element(inner_elem, "EXTERN-RATE")
        if child is not None:
            extern_rate_value = child.text
            obj.extern_rate = extern_rate_value

        # Parse fall_back_internal
        child = SerializationHelper.find_child_element(inner_elem, "FALL-BACK-INTERNAL")
        if child is not None:
            fall_back_internal_value = child.text
            obj.fall_back_internal = fall_back_internal_value

        # Parse flexray_fifos (list from container "FLEXRAY-FIFOS")
        obj.flexray_fifos = []
        container = SerializationHelper.find_child_element(inner_elem, "FLEXRAY-FIFOS")
        if container is not None:
            for child in container:
                if is_ref:
                    # Use the child_tag from decorator if specified to match specific child tag
                    if child_tag:
                        child_element_tag = SerializationHelper.strip_namespace(child.tag)
                        if child_element_tag == "None":
                            child_value = ARRef.deserialize(child)
                        else:
                            child_value = SerializationHelper.deserialize_by_tag(child, None)
                    else:
                        child_element_tag = SerializationHelper.strip_namespace(child.tag)
                        if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                            child_value = ARRef.deserialize(child)
                        else:
                            child_value = SerializationHelper.deserialize_by_tag(child, None)
                elif is_primitive_type("any (FlexrayFifo)", package_data):
                    child_value = child.text
                elif is_enum_type("any (FlexrayFifo)", package_data):
                    child_value = any (FlexrayFifo).deserialize(child)
                else:
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.flexray_fifos.append(child_value)

        # Parse key_slot_id
        child = SerializationHelper.find_child_element(inner_elem, "KEY-SLOT-ID")
        if child is not None:
            key_slot_id_value = child.text
            obj.key_slot_id = key_slot_id_value

        # Parse key_slot_only
        child = SerializationHelper.find_child_element(inner_elem, "KEY-SLOT-ONLY")
        if child is not None:
            key_slot_only_value = child.text
            obj.key_slot_only = key_slot_only_value

        # Parse key_slot_used_for
        child = SerializationHelper.find_child_element(inner_elem, "KEY-SLOT-USED-FOR")
        if child is not None:
            key_slot_used_for_value = child.text
            obj.key_slot_used_for = key_slot_used_for_value

        # Parse latest_tx
        child = SerializationHelper.find_child_element(inner_elem, "LATEST-TX")
        if child is not None:
            latest_tx_value = child.text
            obj.latest_tx = latest_tx_value

        # Parse listen_timeout
        child = SerializationHelper.find_child_element(inner_elem, "LISTEN-TIMEOUT")
        if child is not None:
            listen_timeout_value = child.text
            obj.listen_timeout = listen_timeout_value

        # Parse macro_initial
        child = SerializationHelper.find_child_element(inner_elem, "MACRO-INITIAL")
        if child is not None:
            macro_initial_value = child.text
            obj.macro_initial = macro_initial_value

        # Parse maximum
        child = SerializationHelper.find_child_element(inner_elem, "MAXIMUM")
        if child is not None:
            maximum_value = child.text
            obj.maximum = maximum_value

        # Parse micro_initial
        child = SerializationHelper.find_child_element(inner_elem, "MICRO-INITIAL")
        if child is not None:
            micro_initial_value = child.text
            obj.micro_initial = micro_initial_value

        # Parse micro_per_cycle
        child = SerializationHelper.find_child_element(inner_elem, "MICRO-PER-CYCLE")
        if child is not None:
            micro_per_cycle_value = child.text
            obj.micro_per_cycle = micro_per_cycle_value

        # Parse microtick
        child = SerializationHelper.find_child_element(inner_elem, "MICROTICK")
        if child is not None:
            microtick_value = child.text
            obj.microtick = microtick_value

        # Parse nm_vector_early
        child = SerializationHelper.find_child_element(inner_elem, "NM-VECTOR-EARLY")
        if child is not None:
            nm_vector_early_value = child.text
            obj.nm_vector_early = nm_vector_early_value

        # Parse offset_correction
        child = SerializationHelper.find_child_element(inner_elem, "OFFSET-CORRECTION")
        if child is not None:
            offset_correction_value = child.text
            obj.offset_correction = offset_correction_value

        # Parse rate_correction
        child = SerializationHelper.find_child_element(inner_elem, "RATE-CORRECTION")
        if child is not None:
            rate_correction_value = child.text
            obj.rate_correction = rate_correction_value

        # Parse samples_per_microtick
        child = SerializationHelper.find_child_element(inner_elem, "SAMPLES-PER-MICROTICK")
        if child is not None:
            samples_per_microtick_value = child.text
            obj.samples_per_microtick = samples_per_microtick_value

        # Parse second_key_slot
        child = SerializationHelper.find_child_element(inner_elem, "SECOND-KEY-SLOT")
        if child is not None:
            second_key_slot_value = child.text
            obj.second_key_slot = second_key_slot_value

        # Parse two_key_slot
        child = SerializationHelper.find_child_element(inner_elem, "TWO-KEY-SLOT")
        if child is not None:
            two_key_slot_value = child.text
            obj.two_key_slot = two_key_slot_value

        # Parse wake_up_pattern
        child = SerializationHelper.find_child_element(inner_elem, "WAKE-UP-PATTERN")
        if child is not None:
            wake_up_pattern_value = child.text
            obj.wake_up_pattern = wake_up_pattern_value

        return obj



class FlexrayCommunicationControllerBuilder(BuilderBase):
    """Builder for FlexrayCommunicationController with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: FlexrayCommunicationController = FlexrayCommunicationController()


    def with_accepted(self, value: Optional[Integer]) -> "FlexrayCommunicationControllerBuilder":
        """Set accepted attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.accepted = value
        return self

    def with_allow_halt_due_to(self, value: Optional[Boolean]) -> "FlexrayCommunicationControllerBuilder":
        """Set allow_halt_due_to attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.allow_halt_due_to = value
        return self

    def with_allow_passive_to(self, value: Optional[Integer]) -> "FlexrayCommunicationControllerBuilder":
        """Set allow_passive_to attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.allow_passive_to = value
        return self

    def with_cluster_drift(self, value: Optional[Integer]) -> "FlexrayCommunicationControllerBuilder":
        """Set cluster_drift attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.cluster_drift = value
        return self

    def with_decoding(self, value: Optional[Integer]) -> "FlexrayCommunicationControllerBuilder":
        """Set decoding attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.decoding = value
        return self

    def with_delay(self, value: Optional[Integer]) -> "FlexrayCommunicationControllerBuilder":
        """Set delay attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.delay = value
        return self

    def with_external_sync(self, value: Optional[Boolean]) -> "FlexrayCommunicationControllerBuilder":
        """Set external_sync attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.external_sync = value
        return self

    def with_extern_offset(self, value: Optional[Integer]) -> "FlexrayCommunicationControllerBuilder":
        """Set extern_offset attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.extern_offset = value
        return self

    def with_extern_rate(self, value: Optional[Integer]) -> "FlexrayCommunicationControllerBuilder":
        """Set extern_rate attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.extern_rate = value
        return self

    def with_fall_back_internal(self, value: Optional[Boolean]) -> "FlexrayCommunicationControllerBuilder":
        """Set fall_back_internal attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.fall_back_internal = value
        return self

    def with_flexray_fifos(self, items: list[any (FlexrayFifo)]) -> "FlexrayCommunicationControllerBuilder":
        """Set flexray_fifos list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.flexray_fifos = list(items) if items else []
        return self

    def with_key_slot_id(self, value: Optional[PositiveInteger]) -> "FlexrayCommunicationControllerBuilder":
        """Set key_slot_id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.key_slot_id = value
        return self

    def with_key_slot_only(self, value: Optional[Boolean]) -> "FlexrayCommunicationControllerBuilder":
        """Set key_slot_only attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.key_slot_only = value
        return self

    def with_key_slot_used_for(self, value: Optional[Boolean]) -> "FlexrayCommunicationControllerBuilder":
        """Set key_slot_used_for attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.key_slot_used_for = value
        return self

    def with_latest_tx(self, value: Optional[Integer]) -> "FlexrayCommunicationControllerBuilder":
        """Set latest_tx attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.latest_tx = value
        return self

    def with_listen_timeout(self, value: Optional[Integer]) -> "FlexrayCommunicationControllerBuilder":
        """Set listen_timeout attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.listen_timeout = value
        return self

    def with_macro_initial(self, value: Optional[Integer]) -> "FlexrayCommunicationControllerBuilder":
        """Set macro_initial attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.macro_initial = value
        return self

    def with_maximum(self, value: Optional[Integer]) -> "FlexrayCommunicationControllerBuilder":
        """Set maximum attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.maximum = value
        return self

    def with_micro_initial(self, value: Optional[Integer]) -> "FlexrayCommunicationControllerBuilder":
        """Set micro_initial attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.micro_initial = value
        return self

    def with_micro_per_cycle(self, value: Optional[Integer]) -> "FlexrayCommunicationControllerBuilder":
        """Set micro_per_cycle attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.micro_per_cycle = value
        return self

    def with_microtick(self, value: Optional[TimeValue]) -> "FlexrayCommunicationControllerBuilder":
        """Set microtick attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.microtick = value
        return self

    def with_nm_vector_early(self, value: Optional[Boolean]) -> "FlexrayCommunicationControllerBuilder":
        """Set nm_vector_early attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.nm_vector_early = value
        return self

    def with_offset_correction(self, value: Optional[Integer]) -> "FlexrayCommunicationControllerBuilder":
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

    def with_rate_correction(self, value: Optional[Integer]) -> "FlexrayCommunicationControllerBuilder":
        """Set rate_correction attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.rate_correction = value
        return self

    def with_samples_per_microtick(self, value: Optional[Integer]) -> "FlexrayCommunicationControllerBuilder":
        """Set samples_per_microtick attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.samples_per_microtick = value
        return self

    def with_second_key_slot(self, value: Optional[PositiveInteger]) -> "FlexrayCommunicationControllerBuilder":
        """Set second_key_slot attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.second_key_slot = value
        return self

    def with_two_key_slot(self, value: Optional[Boolean]) -> "FlexrayCommunicationControllerBuilder":
        """Set two_key_slot attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.two_key_slot = value
        return self

    def with_wake_up_pattern(self, value: Optional[Integer]) -> "FlexrayCommunicationControllerBuilder":
        """Set wake_up_pattern attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.wake_up_pattern = value
        return self


    def add_flexray_fifo(self, item: any (FlexrayFifo)) -> "FlexrayCommunicationControllerBuilder":
        """Add a single item to flexray_fifos list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.flexray_fifos.append(item)
        return self

    def clear_flexray_fifos(self) -> "FlexrayCommunicationControllerBuilder":
        """Clear all items from flexray_fifos list.

        Returns:
            self for method chaining
        """
        self._obj.flexray_fifos = []
        return self



    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel.core import GlobalSettingsManager, BuilderValidationMode

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


    def build(self) -> FlexrayCommunicationController:
        """Build and return the FlexrayCommunicationController instance with validation."""
        self._validate_instance()
        pass
        return self._obj