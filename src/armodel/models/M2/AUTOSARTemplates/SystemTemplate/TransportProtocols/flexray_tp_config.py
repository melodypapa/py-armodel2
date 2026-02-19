"""FlexrayTpConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 592)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_config import (
    TpConfig,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.flexray_tp_connection import (
    FlexrayTpConnection,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.flexray_tp_ecu import (
    FlexrayTpEcu,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.flexray_tp_node import (
    FlexrayTpNode,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.flexray_tp_pdu_pool import (
    FlexrayTpPduPool,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_address import (
    TpAddress,
)


class FlexrayTpConfig(TpConfig):
    """AUTOSAR FlexrayTpConfig."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    pdu_pools: list[FlexrayTpPduPool]
    tp_addresses: list[TpAddress]
    tp_connections: list[FlexrayTpConnection]
    tp_ecus: list[FlexrayTpEcu]
    tp_nodes: list[FlexrayTpNode]
    def __init__(self) -> None:
        """Initialize FlexrayTpConfig."""
        super().__init__()
        self.pdu_pools: list[FlexrayTpPduPool] = []
        self.tp_addresses: list[TpAddress] = []
        self.tp_connections: list[FlexrayTpConnection] = []
        self.tp_ecus: list[FlexrayTpEcu] = []
        self.tp_nodes: list[FlexrayTpNode] = []
    def serialize(self) -> ET.Element:
        """Serialize FlexrayTpConfig to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(FlexrayTpConfig, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize pdu_pools (list to container "PDU-POOLS")
        if self.pdu_pools:
            wrapper = ET.Element("PDU-POOLS")
            for item in self.pdu_pools:
                serialized = ARObject._serialize_item(item, "FlexrayTpPduPool")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize tp_addresses (list to container "TP-ADDRESSES")
        if self.tp_addresses:
            wrapper = ET.Element("TP-ADDRESSES")
            for item in self.tp_addresses:
                serialized = ARObject._serialize_item(item, "TpAddress")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize tp_connections (list to container "TP-CONNECTIONS")
        if self.tp_connections:
            wrapper = ET.Element("TP-CONNECTIONS")
            for item in self.tp_connections:
                serialized = ARObject._serialize_item(item, "FlexrayTpConnection")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize tp_ecus (list to container "TP-ECUS")
        if self.tp_ecus:
            wrapper = ET.Element("TP-ECUS")
            for item in self.tp_ecus:
                serialized = ARObject._serialize_item(item, "FlexrayTpEcu")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize tp_nodes (list to container "TP-NODES")
        if self.tp_nodes:
            wrapper = ET.Element("TP-NODES")
            for item in self.tp_nodes:
                serialized = ARObject._serialize_item(item, "FlexrayTpNode")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlexrayTpConfig":
        """Deserialize XML element to FlexrayTpConfig object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FlexrayTpConfig object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(FlexrayTpConfig, cls).deserialize(element)

        # Parse pdu_pools (list from container "PDU-POOLS")
        obj.pdu_pools = []
        container = ARObject._find_child_element(element, "PDU-POOLS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.pdu_pools.append(child_value)

        # Parse tp_addresses (list from container "TP-ADDRESSES")
        obj.tp_addresses = []
        container = ARObject._find_child_element(element, "TP-ADDRESSES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.tp_addresses.append(child_value)

        # Parse tp_connections (list from container "TP-CONNECTIONS")
        obj.tp_connections = []
        container = ARObject._find_child_element(element, "TP-CONNECTIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.tp_connections.append(child_value)

        # Parse tp_ecus (list from container "TP-ECUS")
        obj.tp_ecus = []
        container = ARObject._find_child_element(element, "TP-ECUS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.tp_ecus.append(child_value)

        # Parse tp_nodes (list from container "TP-NODES")
        obj.tp_nodes = []
        container = ARObject._find_child_element(element, "TP-NODES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.tp_nodes.append(child_value)

        return obj



class FlexrayTpConfigBuilder:
    """Builder for FlexrayTpConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FlexrayTpConfig = FlexrayTpConfig()

    def build(self) -> FlexrayTpConfig:
        """Build and return FlexrayTpConfig object.

        Returns:
            FlexrayTpConfig instance
        """
        # TODO: Add validation
        return self._obj
