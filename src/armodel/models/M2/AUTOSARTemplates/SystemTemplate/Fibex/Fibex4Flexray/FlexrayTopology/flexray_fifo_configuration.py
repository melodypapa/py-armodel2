"""FlexrayFifoConfiguration AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 87)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Flexray_FlexrayTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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
    channel_ref: Optional[ARRef]
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
        self.channel_ref: Optional[ARRef] = None
        self.cycle_repetition: Optional[Integer] = None
        self.fifo_depth: Optional[Integer] = None
        self.fifo_ranges: list[FlexrayFifoRange] = []
        self.msg_id_mask: Optional[Integer] = None
        self.msg_id_match: Optional[Integer] = None

    def serialize(self) -> ET.Element:
        """Serialize FlexrayFifoConfiguration to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize admit_without
        if self.admit_without is not None:
            serialized = ARObject._serialize_item(self.admit_without, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ADMIT-WITHOUT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize base_cycle
        if self.base_cycle is not None:
            serialized = ARObject._serialize_item(self.base_cycle, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BASE-CYCLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize channel_ref
        if self.channel_ref is not None:
            serialized = ARObject._serialize_item(self.channel_ref, "FlexrayPhysicalChannel")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CHANNEL-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize cycle_repetition
        if self.cycle_repetition is not None:
            serialized = ARObject._serialize_item(self.cycle_repetition, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CYCLE-REPETITION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize fifo_depth
        if self.fifo_depth is not None:
            serialized = ARObject._serialize_item(self.fifo_depth, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FIFO-DEPTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize fifo_ranges (list to container "FIFO-RANGES")
        if self.fifo_ranges:
            wrapper = ET.Element("FIFO-RANGES")
            for item in self.fifo_ranges:
                serialized = ARObject._serialize_item(item, "FlexrayFifoRange")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize msg_id_mask
        if self.msg_id_mask is not None:
            serialized = ARObject._serialize_item(self.msg_id_mask, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MSG-ID-MASK")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize msg_id_match
        if self.msg_id_match is not None:
            serialized = ARObject._serialize_item(self.msg_id_match, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MSG-ID-MATCH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

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

        # Parse channel_ref
        child = ARObject._find_child_element(element, "CHANNEL-REF")
        if child is not None:
            channel_ref_value = ARRef.deserialize(child)
            obj.channel_ref = channel_ref_value

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

        # Parse fifo_ranges (list from container "FIFO-RANGES")
        obj.fifo_ranges = []
        container = ARObject._find_child_element(element, "FIFO-RANGES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.fifo_ranges.append(child_value)

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
