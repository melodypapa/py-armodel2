"""LinTpConnection AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection.tp_connection import (
    TpConnection,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu import (
    IPdu,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.lin_tp_node import (
    LinTpNode,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.n_pdu import (
    NPdu,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_address import (
    TpAddress,
)


class LinTpConnection(TpConnection):
    """AUTOSAR LinTpConnection."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "data_pdu": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=NPdu,
        ),  # dataPdu
        "flow_control": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=NPdu,
        ),  # flowControl
        "lin_tp_n_sdu": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=IPdu,
        ),  # linTpNSdu
        "multicast": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=TpAddress,
        ),  # multicast
        "receivers": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=LinTpNode,
        ),  # receivers
        "timeout_as": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # timeoutAs
        "timeout_cr": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # timeoutCr
        "timeout_cs": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # timeoutCs
        "transmitter": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=LinTpNode,
        ),  # transmitter
    }

    def __init__(self) -> None:
        """Initialize LinTpConnection."""
        super().__init__()
        self.data_pdu: Optional[NPdu] = None
        self.flow_control: Optional[NPdu] = None
        self.lin_tp_n_sdu: Optional[IPdu] = None
        self.multicast: Optional[TpAddress] = None
        self.receivers: list[LinTpNode] = []
        self.timeout_as: Optional[TimeValue] = None
        self.timeout_cr: Optional[TimeValue] = None
        self.timeout_cs: Optional[TimeValue] = None
        self.transmitter: Optional[LinTpNode] = None


class LinTpConnectionBuilder:
    """Builder for LinTpConnection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LinTpConnection = LinTpConnection()

    def build(self) -> LinTpConnection:
        """Build and return LinTpConnection object.

        Returns:
            LinTpConnection instance
        """
        # TODO: Add validation
        return self._obj
