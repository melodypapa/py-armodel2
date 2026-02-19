"""DoIpTpConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 555)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_config import (
    TpConfig,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.do_ip_logic_address import (
    DoIpLogicAddress,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection.do_ip_tp_connection import (
    DoIpTpConnection,
)


class DoIpTpConfig(TpConfig):
    """AUTOSAR DoIpTpConfig."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    do_ip_logic_address_addresses: list[DoIpLogicAddress]
    tp_connections: list[DoIpTpConnection]
    def __init__(self) -> None:
        """Initialize DoIpTpConfig."""
        super().__init__()
        self.do_ip_logic_address_addresses: list[DoIpLogicAddress] = []
        self.tp_connections: list[DoIpTpConnection] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DoIpTpConfig":
        """Deserialize XML element to DoIpTpConfig object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DoIpTpConfig object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DoIpTpConfig, cls).deserialize(element)

        # Parse do_ip_logic_address_addresses (list from container "DO-IP-LOGIC-ADDRESS-ADDRESSES")
        obj.do_ip_logic_address_addresses = []
        container = ARObject._find_child_element(element, "DO-IP-LOGIC-ADDRESS-ADDRESSES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.do_ip_logic_address_addresses.append(child_value)

        # Parse tp_connections (list from container "TP-CONNECTIONS")
        obj.tp_connections = []
        container = ARObject._find_child_element(element, "TP-CONNECTIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.tp_connections.append(child_value)

        return obj



class DoIpTpConfigBuilder:
    """Builder for DoIpTpConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DoIpTpConfig = DoIpTpConfig()

    def build(self) -> DoIpTpConfig:
        """Build and return DoIpTpConfig object.

        Returns:
            DoIpTpConfig instance
        """
        # TODO: Add validation
        return self._obj
