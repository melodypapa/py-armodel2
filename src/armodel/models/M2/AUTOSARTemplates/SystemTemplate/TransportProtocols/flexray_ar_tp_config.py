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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlexrayArTpConfig":
        """Deserialize XML element to FlexrayArTpConfig object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FlexrayArTpConfig object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse tp_addresses (list)
        obj.tp_addresses = []
        for child in ARObject._find_all_child_elements(element, "TP-ADDRESSES"):
            tp_addresses_value = ARObject._deserialize_by_tag(child, "TpAddress")
            obj.tp_addresses.append(tp_addresses_value)

        # Parse tp_channels (list)
        obj.tp_channels = []
        for child in ARObject._find_all_child_elements(element, "TP-CHANNELS"):
            tp_channels_value = ARObject._deserialize_by_tag(child, "FlexrayArTpChannel")
            obj.tp_channels.append(tp_channels_value)

        # Parse tp_nodes (list)
        obj.tp_nodes = []
        for child in ARObject._find_all_child_elements(element, "TP-NODES"):
            tp_nodes_value = ARObject._deserialize_by_tag(child, "FlexrayArTpNode")
            obj.tp_nodes.append(tp_nodes_value)

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
