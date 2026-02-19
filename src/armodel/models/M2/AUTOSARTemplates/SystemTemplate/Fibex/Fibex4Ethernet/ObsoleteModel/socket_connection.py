"""SocketConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2057)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ObsoleteModel.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.describable import (
    Describable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Identifier,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.socket_address import (
    SocketAddress,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.socket_connection_ipdu_identifier_set import (
    SocketConnectionIpduIdentifierSet,
)


class SocketConnection(Describable):
    """AUTOSAR SocketConnection."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    client_ip_addr: Optional[Boolean]
    client_port: Optional[SocketAddress]
    client_port_from: Optional[Boolean]
    pdus: list[SocketConnectionIpduIdentifierSet]
    pdu_collection: Optional[TimeValue]
    runtime_ip: Optional[Any]
    runtime_port: Optional[Any]
    short_label: Optional[Identifier]
    def __init__(self) -> None:
        """Initialize SocketConnection."""
        super().__init__()
        self.client_ip_addr: Optional[Boolean] = None
        self.client_port: Optional[SocketAddress] = None
        self.client_port_from: Optional[Boolean] = None
        self.pdus: list[SocketConnectionIpduIdentifierSet] = []
        self.pdu_collection: Optional[TimeValue] = None
        self.runtime_ip: Optional[Any] = None
        self.runtime_port: Optional[Any] = None
        self.short_label: Optional[Identifier] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SocketConnection":
        """Deserialize XML element to SocketConnection object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SocketConnection object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse client_ip_addr
        child = ARObject._find_child_element(element, "CLIENT-IP-ADDR")
        if child is not None:
            client_ip_addr_value = child.text
            obj.client_ip_addr = client_ip_addr_value

        # Parse client_port
        child = ARObject._find_child_element(element, "CLIENT-PORT")
        if child is not None:
            client_port_value = ARObject._deserialize_by_tag(child, "SocketAddress")
            obj.client_port = client_port_value

        # Parse client_port_from
        child = ARObject._find_child_element(element, "CLIENT-PORT-FROM")
        if child is not None:
            client_port_from_value = child.text
            obj.client_port_from = client_port_from_value

        # Parse pdus (list)
        obj.pdus = []
        for child in ARObject._find_all_child_elements(element, "PDUS"):
            pdus_value = ARObject._deserialize_by_tag(child, "SocketConnectionIpduIdentifierSet")
            obj.pdus.append(pdus_value)

        # Parse pdu_collection
        child = ARObject._find_child_element(element, "PDU-COLLECTION")
        if child is not None:
            pdu_collection_value = child.text
            obj.pdu_collection = pdu_collection_value

        # Parse runtime_ip
        child = ARObject._find_child_element(element, "RUNTIME-IP")
        if child is not None:
            runtime_ip_value = child.text
            obj.runtime_ip = runtime_ip_value

        # Parse runtime_port
        child = ARObject._find_child_element(element, "RUNTIME-PORT")
        if child is not None:
            runtime_port_value = child.text
            obj.runtime_port = runtime_port_value

        # Parse short_label
        child = ARObject._find_child_element(element, "SHORT-LABEL")
        if child is not None:
            short_label_value = child.text
            obj.short_label = short_label_value

        return obj



class SocketConnectionBuilder:
    """Builder for SocketConnection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SocketConnection = SocketConnection()

    def build(self) -> SocketConnection:
        """Build and return SocketConnection object.

        Returns:
            SocketConnection instance
        """
        # TODO: Add validation
        return self._obj
