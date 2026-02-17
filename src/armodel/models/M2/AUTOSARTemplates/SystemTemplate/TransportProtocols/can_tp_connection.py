"""CanTpConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 608)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection.tp_connection import (
    TpConnection,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import (
    CanTpAddressingFormatType,
    NetworkTargetAddressType,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.can_tp_address import (
    CanTpAddress,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.can_tp_channel import (
    CanTpChannel,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.can_tp_node import (
    CanTpNode,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu import (
    IPdu,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.n_pdu import (
    NPdu,
)


class CanTpConnection(TpConnection):
    """AUTOSAR CanTpConnection."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "addressing": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=CanTpAddressingFormatType,
        ),  # addressing
        "cancellation": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # cancellation
        "can_tp_channel": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=CanTpChannel,
        ),  # canTpChannel
        "data_pdu": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=NPdu,
        ),  # dataPdu
        "flow_control_pdu": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=NPdu,
        ),  # flowControlPdu
        "max_block_size": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # maxBlockSize
        "multicast": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=CanTpAddress,
        ),  # multicast
        "padding": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # padding
        "receivers": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=CanTpNode,
        ),  # receivers
        "ta_type_type": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=NetworkTargetAddressType,
        ),  # taTypeType
        "timeout_br": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # timeoutBr
        "timeout_bs": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # timeoutBs
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
        "tp_sdu": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=IPdu,
        ),  # tpSdu
        "transmitter": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=CanTpNode,
        ),  # transmitter
    }

    def __init__(self) -> None:
        """Initialize CanTpConnection."""
        super().__init__()
        self.addressing: Optional[CanTpAddressingFormatType] = None
        self.cancellation: Optional[Boolean] = None
        self.can_tp_channel: Optional[CanTpChannel] = None
        self.data_pdu: Optional[NPdu] = None
        self.flow_control_pdu: Optional[NPdu] = None
        self.max_block_size: Optional[Integer] = None
        self.multicast: Optional[CanTpAddress] = None
        self.padding: Optional[Boolean] = None
        self.receivers: list[CanTpNode] = []
        self.ta_type_type: Optional[NetworkTargetAddressType] = None
        self.timeout_br: Optional[TimeValue] = None
        self.timeout_bs: Optional[TimeValue] = None
        self.timeout_cr: Optional[TimeValue] = None
        self.timeout_cs: Optional[TimeValue] = None
        self.tp_sdu: Optional[IPdu] = None
        self.transmitter: Optional[CanTpNode] = None


class CanTpConnectionBuilder:
    """Builder for CanTpConnection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanTpConnection = CanTpConnection()

    def build(self) -> CanTpConnection:
        """Build and return CanTpConnection object.

        Returns:
            CanTpConnection instance
        """
        # TODO: Add validation
        return self._obj
