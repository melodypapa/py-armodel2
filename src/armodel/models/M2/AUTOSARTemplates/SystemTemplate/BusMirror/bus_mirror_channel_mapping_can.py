"""BusMirrorChannelMappingCan AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 700)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_BusMirror.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.BusMirror.bus_mirror_channel_mapping import (
    BusMirrorChannelMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.BusMirror.bus_mirror_can_id_range_mapping import (
    BusMirrorCanIdRangeMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.BusMirror.bus_mirror_can_id_to_can_id_mapping import (
    BusMirrorCanIdToCanIdMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.BusMirror.bus_mirror_lin_pid_to_can_id_mapping import (
    BusMirrorLinPidToCanIdMapping,
)


class BusMirrorChannelMappingCan(BusMirrorChannelMapping):
    """AUTOSAR BusMirrorChannelMappingCan."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    can_id_ranges: list[BusMirrorCanIdRangeMapping]
    can_id_to_can_ids: list[BusMirrorCanIdToCanIdMapping]
    lin_pid_to_can_ids: list[BusMirrorLinPidToCanIdMapping]
    mirror_source_lin: Optional[PositiveInteger]
    mirror_status: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize BusMirrorChannelMappingCan."""
        super().__init__()
        self.can_id_ranges: list[BusMirrorCanIdRangeMapping] = []
        self.can_id_to_can_ids: list[BusMirrorCanIdToCanIdMapping] = []
        self.lin_pid_to_can_ids: list[BusMirrorLinPidToCanIdMapping] = []
        self.mirror_source_lin: Optional[PositiveInteger] = None
        self.mirror_status: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize BusMirrorChannelMappingCan to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BusMirrorChannelMappingCan, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize can_id_ranges (list to container "CAN-ID-RANGES")
        if self.can_id_ranges:
            wrapper = ET.Element("CAN-ID-RANGES")
            for item in self.can_id_ranges:
                serialized = ARObject._serialize_item(item, "BusMirrorCanIdRangeMapping")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize can_id_to_can_ids (list to container "CAN-ID-TO-CAN-IDS")
        if self.can_id_to_can_ids:
            wrapper = ET.Element("CAN-ID-TO-CAN-IDS")
            for item in self.can_id_to_can_ids:
                serialized = ARObject._serialize_item(item, "BusMirrorCanIdToCanIdMapping")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize lin_pid_to_can_ids (list to container "LIN-PID-TO-CAN-IDS")
        if self.lin_pid_to_can_ids:
            wrapper = ET.Element("LIN-PID-TO-CAN-IDS")
            for item in self.lin_pid_to_can_ids:
                serialized = ARObject._serialize_item(item, "BusMirrorLinPidToCanIdMapping")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize mirror_source_lin
        if self.mirror_source_lin is not None:
            serialized = ARObject._serialize_item(self.mirror_source_lin, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MIRROR-SOURCE-LIN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mirror_status
        if self.mirror_status is not None:
            serialized = ARObject._serialize_item(self.mirror_status, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MIRROR-STATUS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BusMirrorChannelMappingCan":
        """Deserialize XML element to BusMirrorChannelMappingCan object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BusMirrorChannelMappingCan object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BusMirrorChannelMappingCan, cls).deserialize(element)

        # Parse can_id_ranges (list from container "CAN-ID-RANGES")
        obj.can_id_ranges = []
        container = ARObject._find_child_element(element, "CAN-ID-RANGES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.can_id_ranges.append(child_value)

        # Parse can_id_to_can_ids (list from container "CAN-ID-TO-CAN-IDS")
        obj.can_id_to_can_ids = []
        container = ARObject._find_child_element(element, "CAN-ID-TO-CAN-IDS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.can_id_to_can_ids.append(child_value)

        # Parse lin_pid_to_can_ids (list from container "LIN-PID-TO-CAN-IDS")
        obj.lin_pid_to_can_ids = []
        container = ARObject._find_child_element(element, "LIN-PID-TO-CAN-IDS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.lin_pid_to_can_ids.append(child_value)

        # Parse mirror_source_lin
        child = ARObject._find_child_element(element, "MIRROR-SOURCE-LIN")
        if child is not None:
            mirror_source_lin_value = child.text
            obj.mirror_source_lin = mirror_source_lin_value

        # Parse mirror_status
        child = ARObject._find_child_element(element, "MIRROR-STATUS")
        if child is not None:
            mirror_status_value = child.text
            obj.mirror_status = mirror_status_value

        return obj



class BusMirrorChannelMappingCanBuilder:
    """Builder for BusMirrorChannelMappingCan."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BusMirrorChannelMappingCan = BusMirrorChannelMappingCan()

    def build(self) -> BusMirrorChannelMappingCan:
        """Build and return BusMirrorChannelMappingCan object.

        Returns:
            BusMirrorChannelMappingCan instance
        """
        # TODO: Add validation
        return self._obj
