"""CanTpConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 606)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_config import (
    TpConfig,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.can_tp_address import (
    CanTpAddress,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.can_tp_channel import (
    CanTpChannel,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.can_tp_connection import (
    CanTpConnection,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.can_tp_ecu import (
    CanTpEcu,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.can_tp_node import (
    CanTpNode,
)


class CanTpConfig(TpConfig):
    """AUTOSAR CanTpConfig."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    tp_addresses: list[CanTpAddress]
    tp_channels: list[CanTpChannel]
    tp_connections: list[CanTpConnection]
    tp_ecus: list[CanTpEcu]
    tp_nodes: list[CanTpNode]
    def __init__(self) -> None:
        """Initialize CanTpConfig."""
        super().__init__()
        self.tp_addresses: list[CanTpAddress] = []
        self.tp_channels: list[CanTpChannel] = []
        self.tp_connections: list[CanTpConnection] = []
        self.tp_ecus: list[CanTpEcu] = []
        self.tp_nodes: list[CanTpNode] = []

    def serialize(self) -> ET.Element:
        """Serialize CanTpConfig to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CanTpConfig, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize tp_addresses (list to container "TP-ADDRESSES")
        if self.tp_addresses:
            wrapper = ET.Element("TP-ADDRESSES")
            for item in self.tp_addresses:
                serialized = SerializationHelper.serialize_item(item, "CanTpAddress")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize tp_channels (list to container "TP-CHANNELS")
        if self.tp_channels:
            wrapper = ET.Element("TP-CHANNELS")
            for item in self.tp_channels:
                serialized = SerializationHelper.serialize_item(item, "CanTpChannel")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize tp_connections (list to container "TP-CONNECTIONS")
        if self.tp_connections:
            wrapper = ET.Element("TP-CONNECTIONS")
            for item in self.tp_connections:
                serialized = SerializationHelper.serialize_item(item, "CanTpConnection")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize tp_ecus (list to container "TP-ECUS")
        if self.tp_ecus:
            wrapper = ET.Element("TP-ECUS")
            for item in self.tp_ecus:
                serialized = SerializationHelper.serialize_item(item, "CanTpEcu")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize tp_nodes (list to container "TP-NODES")
        if self.tp_nodes:
            wrapper = ET.Element("TP-NODES")
            for item in self.tp_nodes:
                serialized = SerializationHelper.serialize_item(item, "CanTpNode")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CanTpConfig":
        """Deserialize XML element to CanTpConfig object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CanTpConfig object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CanTpConfig, cls).deserialize(element)

        # Parse tp_addresses (list from container "TP-ADDRESSES")
        obj.tp_addresses = []
        container = SerializationHelper.find_child_element(element, "TP-ADDRESSES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.tp_addresses.append(child_value)

        # Parse tp_channels (list from container "TP-CHANNELS")
        obj.tp_channels = []
        container = SerializationHelper.find_child_element(element, "TP-CHANNELS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.tp_channels.append(child_value)

        # Parse tp_connections (list from container "TP-CONNECTIONS")
        obj.tp_connections = []
        container = SerializationHelper.find_child_element(element, "TP-CONNECTIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.tp_connections.append(child_value)

        # Parse tp_ecus (list from container "TP-ECUS")
        obj.tp_ecus = []
        container = SerializationHelper.find_child_element(element, "TP-ECUS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.tp_ecus.append(child_value)

        # Parse tp_nodes (list from container "TP-NODES")
        obj.tp_nodes = []
        container = SerializationHelper.find_child_element(element, "TP-NODES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.tp_nodes.append(child_value)

        return obj



class CanTpConfigBuilder:
    """Builder for CanTpConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanTpConfig = CanTpConfig()

    def build(self) -> CanTpConfig:
        """Build and return CanTpConfig object.

        Returns:
            CanTpConfig instance
        """
        # TODO: Add validation
        return self._obj
