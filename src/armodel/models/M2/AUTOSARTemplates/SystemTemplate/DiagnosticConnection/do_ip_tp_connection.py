"""DoIpTpConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 555)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_DiagnosticConnection.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection.tp_connection import (
    TpConnection,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.do_ip_logic_address import (
    DoIpLogicAddress,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)


class DoIpTpConnection(TpConnection):
    """AUTOSAR DoIpTpConnection."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "do_ip_source": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DoIpLogicAddress,
        ),  # doIpSource
        "do_ip_target": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DoIpLogicAddress,
        ),  # doIpTarget
        "tp_sdu": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=PduTriggering,
        ),  # tpSdu
    }

    def __init__(self) -> None:
        """Initialize DoIpTpConnection."""
        super().__init__()
        self.do_ip_source: Optional[DoIpLogicAddress] = None
        self.do_ip_target: Optional[DoIpLogicAddress] = None
        self.tp_sdu: Optional[PduTriggering] = None


class DoIpTpConnectionBuilder:
    """Builder for DoIpTpConnection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DoIpTpConnection = DoIpTpConnection()

    def build(self) -> DoIpTpConnection:
        """Build and return DoIpTpConnection object.

        Returns:
            DoIpTpConnection instance
        """
        # TODO: Add validation
        return self._obj
