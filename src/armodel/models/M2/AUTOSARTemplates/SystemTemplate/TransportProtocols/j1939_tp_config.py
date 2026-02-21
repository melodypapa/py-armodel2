"""J1939TpConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 623)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_config import (
    TpConfig,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.j1939_tp_connection import (
    J1939TpConnection,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.j1939_tp_node import (
    J1939TpNode,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_address import (
    TpAddress,
)


class J1939TpConfig(TpConfig):
    """AUTOSAR J1939TpConfig."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    tp_addresses: list[TpAddress]
    tp_connections: list[J1939TpConnection]
    tp_nodes: list[J1939TpNode]
    def __init__(self) -> None:
        """Initialize J1939TpConfig."""
        super().__init__()
        self.tp_addresses: list[TpAddress] = []
        self.tp_connections: list[J1939TpConnection] = []
        self.tp_nodes: list[J1939TpNode] = []

    def serialize(self) -> ET.Element:
        """Serialize J1939TpConfig to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(J1939TpConfig, self).serialize()

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
                serialized = SerializationHelper.serialize_item(item, "TpAddress")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize tp_connections (list to container "TP-CONNECTIONS")
        if self.tp_connections:
            wrapper = ET.Element("TP-CONNECTIONS")
            for item in self.tp_connections:
                serialized = SerializationHelper.serialize_item(item, "J1939TpConnection")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize tp_nodes (list to container "TP-NODES")
        if self.tp_nodes:
            wrapper = ET.Element("TP-NODES")
            for item in self.tp_nodes:
                serialized = SerializationHelper.serialize_item(item, "J1939TpNode")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "J1939TpConfig":
        """Deserialize XML element to J1939TpConfig object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized J1939TpConfig object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(J1939TpConfig, cls).deserialize(element)

        # Parse tp_addresses (list from container "TP-ADDRESSES")
        obj.tp_addresses = []
        container = SerializationHelper.find_child_element(element, "TP-ADDRESSES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.tp_addresses.append(child_value)

        # Parse tp_connections (list from container "TP-CONNECTIONS")
        obj.tp_connections = []
        container = SerializationHelper.find_child_element(element, "TP-CONNECTIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.tp_connections.append(child_value)

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



class J1939TpConfigBuilder:
    """Builder for J1939TpConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: J1939TpConfig = J1939TpConfig()

    def build(self) -> J1939TpConfig:
        """Build and return J1939TpConfig object.

        Returns:
            J1939TpConfig instance
        """
        # TODO: Add validation
        return self._obj
