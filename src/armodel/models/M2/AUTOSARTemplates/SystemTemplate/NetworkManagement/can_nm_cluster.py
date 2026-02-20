"""CanNmCluster AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 682)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_NetworkManagement.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_cluster import (
    NmCluster,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
    PositiveInteger,
    TimeValue,
)


class CanNmCluster(NmCluster):
    """AUTOSAR CanNmCluster."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    nm_busload: Optional[Boolean]
    nm_car_wake_up: Optional[PositiveInteger]
    nm_car_wake_up_filter_node_id: Optional[PositiveInteger]
    nm_cbv_position: Optional[Integer]
    nm_immediate: Optional[PositiveInteger]
    nm_message: Optional[TimeValue]
    nm_msg_cycle: Optional[TimeValue]
    nm_network: Optional[TimeValue]
    nm_nid_position: Optional[Integer]
    nm_remote: Optional[TimeValue]
    nm_repeat: Optional[TimeValue]
    nm_wait_bus: Optional[TimeValue]
    def __init__(self) -> None:
        """Initialize CanNmCluster."""
        super().__init__()
        self.nm_busload: Optional[Boolean] = None
        self.nm_car_wake_up: Optional[PositiveInteger] = None
        self.nm_car_wake_up_filter_node_id: Optional[PositiveInteger] = None
        self.nm_cbv_position: Optional[Integer] = None
        self.nm_immediate: Optional[PositiveInteger] = None
        self.nm_message: Optional[TimeValue] = None
        self.nm_msg_cycle: Optional[TimeValue] = None
        self.nm_network: Optional[TimeValue] = None
        self.nm_nid_position: Optional[Integer] = None
        self.nm_remote: Optional[TimeValue] = None
        self.nm_repeat: Optional[TimeValue] = None
        self.nm_wait_bus: Optional[TimeValue] = None

    def serialize(self) -> ET.Element:
        """Serialize CanNmCluster to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CanNmCluster, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize nm_busload
        if self.nm_busload is not None:
            serialized = ARObject._serialize_item(self.nm_busload, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-BUSLOAD")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_car_wake_up
        if self.nm_car_wake_up is not None:
            serialized = ARObject._serialize_item(self.nm_car_wake_up, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-CAR-WAKE-UP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_car_wake_up_filter_node_id
        if self.nm_car_wake_up_filter_node_id is not None:
            serialized = ARObject._serialize_item(self.nm_car_wake_up_filter_node_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-CAR-WAKE-UP-FILTER-NODE-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_cbv_position
        if self.nm_cbv_position is not None:
            serialized = ARObject._serialize_item(self.nm_cbv_position, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-CBV-POSITION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_immediate
        if self.nm_immediate is not None:
            serialized = ARObject._serialize_item(self.nm_immediate, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-IMMEDIATE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_message
        if self.nm_message is not None:
            serialized = ARObject._serialize_item(self.nm_message, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-MESSAGE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_msg_cycle
        if self.nm_msg_cycle is not None:
            serialized = ARObject._serialize_item(self.nm_msg_cycle, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-MSG-CYCLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_network
        if self.nm_network is not None:
            serialized = ARObject._serialize_item(self.nm_network, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-NETWORK")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_nid_position
        if self.nm_nid_position is not None:
            serialized = ARObject._serialize_item(self.nm_nid_position, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-NID-POSITION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_remote
        if self.nm_remote is not None:
            serialized = ARObject._serialize_item(self.nm_remote, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-REMOTE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_repeat
        if self.nm_repeat is not None:
            serialized = ARObject._serialize_item(self.nm_repeat, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-REPEAT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_wait_bus
        if self.nm_wait_bus is not None:
            serialized = ARObject._serialize_item(self.nm_wait_bus, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-WAIT-BUS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CanNmCluster":
        """Deserialize XML element to CanNmCluster object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CanNmCluster object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CanNmCluster, cls).deserialize(element)

        # Parse nm_busload
        child = ARObject._find_child_element(element, "NM-BUSLOAD")
        if child is not None:
            nm_busload_value = child.text
            obj.nm_busload = nm_busload_value

        # Parse nm_car_wake_up
        child = ARObject._find_child_element(element, "NM-CAR-WAKE-UP")
        if child is not None:
            nm_car_wake_up_value = child.text
            obj.nm_car_wake_up = nm_car_wake_up_value

        # Parse nm_car_wake_up_filter_node_id
        child = ARObject._find_child_element(element, "NM-CAR-WAKE-UP-FILTER-NODE-ID")
        if child is not None:
            nm_car_wake_up_filter_node_id_value = child.text
            obj.nm_car_wake_up_filter_node_id = nm_car_wake_up_filter_node_id_value

        # Parse nm_cbv_position
        child = ARObject._find_child_element(element, "NM-CBV-POSITION")
        if child is not None:
            nm_cbv_position_value = child.text
            obj.nm_cbv_position = nm_cbv_position_value

        # Parse nm_immediate
        child = ARObject._find_child_element(element, "NM-IMMEDIATE")
        if child is not None:
            nm_immediate_value = child.text
            obj.nm_immediate = nm_immediate_value

        # Parse nm_message
        child = ARObject._find_child_element(element, "NM-MESSAGE")
        if child is not None:
            nm_message_value = child.text
            obj.nm_message = nm_message_value

        # Parse nm_msg_cycle
        child = ARObject._find_child_element(element, "NM-MSG-CYCLE")
        if child is not None:
            nm_msg_cycle_value = child.text
            obj.nm_msg_cycle = nm_msg_cycle_value

        # Parse nm_network
        child = ARObject._find_child_element(element, "NM-NETWORK")
        if child is not None:
            nm_network_value = child.text
            obj.nm_network = nm_network_value

        # Parse nm_nid_position
        child = ARObject._find_child_element(element, "NM-NID-POSITION")
        if child is not None:
            nm_nid_position_value = child.text
            obj.nm_nid_position = nm_nid_position_value

        # Parse nm_remote
        child = ARObject._find_child_element(element, "NM-REMOTE")
        if child is not None:
            nm_remote_value = child.text
            obj.nm_remote = nm_remote_value

        # Parse nm_repeat
        child = ARObject._find_child_element(element, "NM-REPEAT")
        if child is not None:
            nm_repeat_value = child.text
            obj.nm_repeat = nm_repeat_value

        # Parse nm_wait_bus
        child = ARObject._find_child_element(element, "NM-WAIT-BUS")
        if child is not None:
            nm_wait_bus_value = child.text
            obj.nm_wait_bus = nm_wait_bus_value

        return obj



class CanNmClusterBuilder:
    """Builder for CanNmCluster."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanNmCluster = CanNmCluster()

    def build(self) -> CanNmCluster:
        """Build and return CanNmCluster object.

        Returns:
            CanNmCluster instance
        """
        # TODO: Add validation
        return self._obj
