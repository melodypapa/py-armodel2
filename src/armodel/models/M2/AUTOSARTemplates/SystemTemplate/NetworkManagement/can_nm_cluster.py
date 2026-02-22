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
from armodel.serialization import SerializationHelper
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
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CanNmCluster, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize nm_busload
        if self.nm_busload is not None:
            serialized = SerializationHelper.serialize_item(self.nm_busload, "Boolean")
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
            serialized = SerializationHelper.serialize_item(self.nm_car_wake_up, "PositiveInteger")
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
            serialized = SerializationHelper.serialize_item(self.nm_car_wake_up_filter_node_id, "PositiveInteger")
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
            serialized = SerializationHelper.serialize_item(self.nm_cbv_position, "Integer")
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
            serialized = SerializationHelper.serialize_item(self.nm_immediate, "PositiveInteger")
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
            serialized = SerializationHelper.serialize_item(self.nm_message, "TimeValue")
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
            serialized = SerializationHelper.serialize_item(self.nm_msg_cycle, "TimeValue")
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
            serialized = SerializationHelper.serialize_item(self.nm_network, "TimeValue")
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
            serialized = SerializationHelper.serialize_item(self.nm_nid_position, "Integer")
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
            serialized = SerializationHelper.serialize_item(self.nm_remote, "TimeValue")
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
            serialized = SerializationHelper.serialize_item(self.nm_repeat, "TimeValue")
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
            serialized = SerializationHelper.serialize_item(self.nm_wait_bus, "TimeValue")
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
        child = SerializationHelper.find_child_element(element, "NM-BUSLOAD")
        if child is not None:
            nm_busload_value = child.text
            obj.nm_busload = nm_busload_value

        # Parse nm_car_wake_up
        child = SerializationHelper.find_child_element(element, "NM-CAR-WAKE-UP")
        if child is not None:
            nm_car_wake_up_value = child.text
            obj.nm_car_wake_up = nm_car_wake_up_value

        # Parse nm_car_wake_up_filter_node_id
        child = SerializationHelper.find_child_element(element, "NM-CAR-WAKE-UP-FILTER-NODE-ID")
        if child is not None:
            nm_car_wake_up_filter_node_id_value = child.text
            obj.nm_car_wake_up_filter_node_id = nm_car_wake_up_filter_node_id_value

        # Parse nm_cbv_position
        child = SerializationHelper.find_child_element(element, "NM-CBV-POSITION")
        if child is not None:
            nm_cbv_position_value = child.text
            obj.nm_cbv_position = nm_cbv_position_value

        # Parse nm_immediate
        child = SerializationHelper.find_child_element(element, "NM-IMMEDIATE")
        if child is not None:
            nm_immediate_value = child.text
            obj.nm_immediate = nm_immediate_value

        # Parse nm_message
        child = SerializationHelper.find_child_element(element, "NM-MESSAGE")
        if child is not None:
            nm_message_value = child.text
            obj.nm_message = nm_message_value

        # Parse nm_msg_cycle
        child = SerializationHelper.find_child_element(element, "NM-MSG-CYCLE")
        if child is not None:
            nm_msg_cycle_value = child.text
            obj.nm_msg_cycle = nm_msg_cycle_value

        # Parse nm_network
        child = SerializationHelper.find_child_element(element, "NM-NETWORK")
        if child is not None:
            nm_network_value = child.text
            obj.nm_network = nm_network_value

        # Parse nm_nid_position
        child = SerializationHelper.find_child_element(element, "NM-NID-POSITION")
        if child is not None:
            nm_nid_position_value = child.text
            obj.nm_nid_position = nm_nid_position_value

        # Parse nm_remote
        child = SerializationHelper.find_child_element(element, "NM-REMOTE")
        if child is not None:
            nm_remote_value = child.text
            obj.nm_remote = nm_remote_value

        # Parse nm_repeat
        child = SerializationHelper.find_child_element(element, "NM-REPEAT")
        if child is not None:
            nm_repeat_value = child.text
            obj.nm_repeat = nm_repeat_value

        # Parse nm_wait_bus
        child = SerializationHelper.find_child_element(element, "NM-WAIT-BUS")
        if child is not None:
            nm_wait_bus_value = child.text
            obj.nm_wait_bus = nm_wait_bus_value

        return obj



class CanNmClusterBuilder:
    """Builder for CanNmCluster with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: CanNmCluster = CanNmCluster()


    def with_short_name(self, value: Identifier) -> "CanNmClusterBuilder":
        """Set short_name attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.short_name = value
        return self

    def with_short_name_fragments(self, items: list[ShortNameFragment]) -> "CanNmClusterBuilder":
        """Set short_name_fragments list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = list(items) if items else []
        return self

    def with_long_name(self, value: Optional[MultilanguageLongName]) -> "CanNmClusterBuilder":
        """Set long_name attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.long_name = value
        return self

    def with_admin_data(self, value: Optional[AdminData]) -> "CanNmClusterBuilder":
        """Set admin_data attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.admin_data = value
        return self

    def with_annotations(self, items: list[Annotation]) -> "CanNmClusterBuilder":
        """Set annotations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.annotations = list(items) if items else []
        return self

    def with_desc(self, value: Optional[MultiLanguageOverviewParagraph]) -> "CanNmClusterBuilder":
        """Set desc attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.desc = value
        return self

    def with_category(self, value: Optional[CategoryString]) -> "CanNmClusterBuilder":
        """Set category attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.category = value
        return self

    def with_introduction(self, value: Optional[DocumentationBlock]) -> "CanNmClusterBuilder":
        """Set introduction attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.introduction = value
        return self

    def with_uuid(self, value: Optional[String]) -> "CanNmClusterBuilder":
        """Set uuid attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.uuid = value
        return self

    def with_communication_cluster(self, value: Optional[CommunicationCluster]) -> "CanNmClusterBuilder":
        """Set communication_cluster attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.communication_cluster = value
        return self

    def with_nm_channel(self, value: Optional[Boolean]) -> "CanNmClusterBuilder":
        """Set nm_channel attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.nm_channel = value
        return self

    def with_nm_node(self, value: Optional[Boolean]) -> "CanNmClusterBuilder":
        """Set nm_node attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.nm_node = value
        return self

    def with_nm_node_id_enabled(self, value: Optional[Boolean]) -> "CanNmClusterBuilder":
        """Set nm_node_id_enabled attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.nm_node_id_enabled = value
        return self

    def with_nm_pnc(self, value: Optional[Boolean]) -> "CanNmClusterBuilder":
        """Set nm_pnc attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.nm_pnc = value
        return self

    def with_nm_repeat_msg_ind_enabled(self, value: Optional[Boolean]) -> "CanNmClusterBuilder":
        """Set nm_repeat_msg_ind_enabled attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.nm_repeat_msg_ind_enabled = value
        return self

    def with_nm(self, value: Optional[Boolean]) -> "CanNmClusterBuilder":
        """Set nm attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.nm = value
        return self

    def with_pnc_cluster(self, value: Optional[PositiveInteger]) -> "CanNmClusterBuilder":
        """Set pnc_cluster attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.pnc_cluster = value
        return self

    def with_nm_busload(self, value: Optional[Boolean]) -> "CanNmClusterBuilder":
        """Set nm_busload attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.nm_busload = value
        return self

    def with_nm_car_wake_up(self, value: Optional[PositiveInteger]) -> "CanNmClusterBuilder":
        """Set nm_car_wake_up attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.nm_car_wake_up = value
        return self

    def with_nm_car_wake_up_filter_node_id(self, value: Optional[PositiveInteger]) -> "CanNmClusterBuilder":
        """Set nm_car_wake_up_filter_node_id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.nm_car_wake_up_filter_node_id = value
        return self

    def with_nm_cbv_position(self, value: Optional[Integer]) -> "CanNmClusterBuilder":
        """Set nm_cbv_position attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.nm_cbv_position = value
        return self

    def with_nm_immediate(self, value: Optional[PositiveInteger]) -> "CanNmClusterBuilder":
        """Set nm_immediate attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.nm_immediate = value
        return self

    def with_nm_message(self, value: Optional[TimeValue]) -> "CanNmClusterBuilder":
        """Set nm_message attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.nm_message = value
        return self

    def with_nm_msg_cycle(self, value: Optional[TimeValue]) -> "CanNmClusterBuilder":
        """Set nm_msg_cycle attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.nm_msg_cycle = value
        return self

    def with_nm_network(self, value: Optional[TimeValue]) -> "CanNmClusterBuilder":
        """Set nm_network attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.nm_network = value
        return self

    def with_nm_nid_position(self, value: Optional[Integer]) -> "CanNmClusterBuilder":
        """Set nm_nid_position attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.nm_nid_position = value
        return self

    def with_nm_remote(self, value: Optional[TimeValue]) -> "CanNmClusterBuilder":
        """Set nm_remote attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.nm_remote = value
        return self

    def with_nm_repeat(self, value: Optional[TimeValue]) -> "CanNmClusterBuilder":
        """Set nm_repeat attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.nm_repeat = value
        return self

    def with_nm_wait_bus(self, value: Optional[TimeValue]) -> "CanNmClusterBuilder":
        """Set nm_wait_bus attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.nm_wait_bus = value
        return self


    def add_short_name_fragment(self, item: ShortNameFragment) -> "CanNmClusterBuilder":
        """Add a single item to short_name_fragments list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments.append(item)
        return self

    def clear_short_name_fragments(self) -> "CanNmClusterBuilder":
        """Clear all items from short_name_fragments list.

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = []
        return self

    def add_annotation(self, item: Annotation) -> "CanNmClusterBuilder":
        """Add a single item to annotations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.annotations.append(item)
        return self

    def clear_annotations(self) -> "CanNmClusterBuilder":
        """Clear all items from annotations list.

        Returns:
            self for method chaining
        """
        self._obj.annotations = []
        return self


    @staticmethod
    def _coerce_to_int(value: Any) -> int:
        """Coerce value to int.

        Args:
            value: Value to coerce

        Returns:
            Integer value

        Raises:
            ValueError: If value cannot be coerced to int
        """
        if isinstance(value, int):
            return value
        if isinstance(value, str) and value.isdigit():
            return int(value)
        if isinstance(value, float):
            return int(value)
        if isinstance(value, bool):
            return int(value)
        raise ValueError(f"Cannot coerce {type(value).__name__} to int: {value}")

    @staticmethod
    def _coerce_to_float(value: Any) -> float:
        """Coerce value to float.

        Args:
            value: Value to coerce

        Returns:
            Float value

        Raises:
            ValueError: If value cannot be coerced to float
        """
        if isinstance(value, float):
            return value
        if isinstance(value, int):
            return float(value)
        if isinstance(value, str):
            try:
                return float(value)
            except ValueError:
                pass
        raise ValueError(f"Cannot coerce {type(value).__name__} to float: {value}")

    @staticmethod
    def _coerce_to_bool(value: Any) -> bool:
        """Coerce value to bool.

        Args:
            value: Value to coerce

        Returns:
            Boolean value

        Raises:
            ValueError: If value cannot be coerced to bool
        """
        if isinstance(value, bool):
            return value
        if isinstance(value, int):
            return bool(value)
        if isinstance(value, str):
            if value.lower() in ("true", "1", "yes"):
                return True
            if value.lower() in ("false", "0", "no"):
                return False
        raise ValueError(f"Cannot coerce {type(value).__name__} to bool: {value}")

    @staticmethod
    def _coerce_to_str(value: Any) -> str:
        """Coerce value to str.

        Args:
            value: Value to coerce

        Returns:
            String value
        """
        return str(value)


    @staticmethod
    def _coerce_to_list(value: Any, item_type: str) -> list:
        """Coerce value to list.

        Args:
            value: Value to coerce
            item_type: Expected item type (for error messages)

        Returns:
            List value

        Raises:
            ValueError: If value cannot be coerced to list
        """
        if isinstance(value, list):
            return value
        if isinstance(value, tuple):
            return list(value)
        raise ValueError(f"Cannot coerce {type(value).__name__} to list[{item_type}]: {value}")


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


    def build(self) -> CanNmCluster:
        """Build and return the CanNmCluster instance with validation."""
        self._validate_instance()
        pass
        return self._obj