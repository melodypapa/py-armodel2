"""StaticSocketConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 543)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ServiceInstances.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import (
    TcpRoleEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.so_con_i_pdu_identifier import (
    SoConIPduIdentifier,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.socket_address import (
    SocketAddress,
)


class StaticSocketConnection(Identifiable):
    """AUTOSAR StaticSocketConnection."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "i_pdu_identifiers": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=SoConIPduIdentifier,
        ),  # iPduIdentifiers
        "remote_address": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SocketAddress,
        ),  # remoteAddress
        "tcp_connect": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # tcpConnect
        "tcp_role": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=TcpRoleEnum,
        ),  # tcpRole
    }

    def __init__(self) -> None:
        """Initialize StaticSocketConnection."""
        super().__init__()
        self.i_pdu_identifiers: list[SoConIPduIdentifier] = []
        self.remote_address: Optional[SocketAddress] = None
        self.tcp_connect: Optional[TimeValue] = None
        self.tcp_role: Optional[TcpRoleEnum] = None


class StaticSocketConnectionBuilder:
    """Builder for StaticSocketConnection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: StaticSocketConnection = StaticSocketConnection()

    def build(self) -> StaticSocketConnection:
        """Build and return StaticSocketConnection object.

        Returns:
            StaticSocketConnection instance
        """
        # TODO: Add validation
        return self._obj
