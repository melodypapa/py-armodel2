"""CanTpConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 608)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    addressing: Optional[CanTpAddressingFormatType]
    cancellation: Optional[Boolean]
    can_tp_channel: Optional[CanTpChannel]
    data_pdu: Optional[NPdu]
    flow_control_pdu: Optional[NPdu]
    max_block_size: Optional[Integer]
    multicast: Optional[CanTpAddress]
    padding: Optional[Boolean]
    receivers: list[CanTpNode]
    ta_type_type: Optional[NetworkTargetAddressType]
    timeout_br: Optional[TimeValue]
    timeout_bs: Optional[TimeValue]
    timeout_cr: Optional[TimeValue]
    timeout_cs: Optional[TimeValue]
    tp_sdu: Optional[IPdu]
    transmitter: Optional[CanTpNode]
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
