"""FlexrayArTpConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 599)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_config import (
    TpConfig,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.flexray_ar_tp_channel import (
    FlexrayArTpChannel,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.flexray_ar_tp_node import (
    FlexrayArTpNode,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_address import (
    TpAddress,
)


class FlexrayArTpConfig(TpConfig):
    """AUTOSAR FlexrayArTpConfig."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    tp_addresses: list[TpAddress]
    tp_channels: list[FlexrayArTpChannel]
    tp_nodes: list[FlexrayArTpNode]
    def __init__(self) -> None:
        """Initialize FlexrayArTpConfig."""
        super().__init__()
        self.tp_addresses: list[TpAddress] = []
        self.tp_channels: list[FlexrayArTpChannel] = []
        self.tp_nodes: list[FlexrayArTpNode] = []
    def serialize(self) -> ET.Element:
        """Serialize FlexrayArTpConfig to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(FlexrayArTpConfig, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize tp_addresses (list to container "TP-ADDRESSES")
        if self.tp_addresses:
            wrapper = ET.Element("TP-ADDRESSES")
            for item in self.tp_addresses:
                serialized = ARObject._serialize_item(item, "TpAddress")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize tp_channels (list to container "TP-CHANNELS")
        if self.tp_channels:
            wrapper = ET.Element("TP-CHANNELS")
            for item in self.tp_channels:
                serialized = ARObject._serialize_item(item, "FlexrayArTpChannel")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize tp_nodes (list to container "TP-NODES")
        if self.tp_nodes:
            wrapper = ET.Element("TP-NODES")
            for item in self.tp_nodes:
                serialized = ARObject._serialize_item(item, "FlexrayArTpNode")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlexrayArTpConfig":
        """Deserialize XML element to FlexrayArTpConfig object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FlexrayArTpConfig object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(FlexrayArTpConfig, cls).deserialize(element)

        # Parse tp_addresses (list from container "TP-ADDRESSES")
        obj.tp_addresses = []
        container = ARObject._find_child_element(element, "TP-ADDRESSES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.tp_addresses.append(child_value)

        # Parse tp_channels (list from container "TP-CHANNELS")
        obj.tp_channels = []
        container = ARObject._find_child_element(element, "TP-CHANNELS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.tp_channels.append(child_value)

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



class FlexrayArTpConfigBuilder:
    """Builder for FlexrayArTpConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FlexrayArTpConfig = FlexrayArTpConfig()

    def build(self) -> FlexrayArTpConfig:
        """Build and return FlexrayArTpConfig object.

        Returns:
            FlexrayArTpConfig instance
        """
        # TODO: Add validation
        return self._obj
