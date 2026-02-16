"""FlexrayArTpConfig AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_config import (
    TpConfig,
)
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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("tp_addresses", None, False, True, TpAddress),  # tpAddresses
        ("tp_channels", None, False, True, FlexrayArTpChannel),  # tpChannels
        ("tp_nodes", None, False, True, FlexrayArTpNode),  # tpNodes
    ]

    def __init__(self) -> None:
        """Initialize FlexrayArTpConfig."""
        super().__init__()
        self.tp_addresses: list[TpAddress] = []
        self.tp_channels: list[FlexrayArTpChannel] = []
        self.tp_nodes: list[FlexrayArTpNode] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert FlexrayArTpConfig to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlexrayArTpConfig":
        """Create FlexrayArTpConfig from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            FlexrayArTpConfig instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to FlexrayArTpConfig since parent returns ARObject
        return cast("FlexrayArTpConfig", obj)


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
