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
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse do_ip_logic_address_addresses (list)
        obj.do_ip_logic_address_addresses = []
        for child in ARObject._find_all_child_elements(element, "DO-IP-LOGIC-ADDRESS-ADDRESSES"):
            do_ip_logic_address_addresses_value = ARObject._deserialize_by_tag(child, "DoIpLogicAddress")
            obj.do_ip_logic_address_addresses.append(do_ip_logic_address_addresses_value)

        # Parse tp_connections (list)
        obj.tp_connections = []
        for child in ARObject._find_all_child_elements(element, "TP-CONNECTIONS"):
            tp_connections_value = ARObject._deserialize_by_tag(child, "DoIpTpConnection")
            obj.tp_connections.append(tp_connections_value)

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
