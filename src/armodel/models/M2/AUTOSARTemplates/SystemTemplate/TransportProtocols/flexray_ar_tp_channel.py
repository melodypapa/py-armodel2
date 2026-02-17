"""FlexrayArTpChannel AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 600)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import (
    FrArTpAckType,
    MaximumMessageLengthType,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
    PositiveInteger,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.flexray_ar_tp_connection import (
    FlexrayArTpConnection,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.n_pdu import (
    NPdu,
)


class FlexrayArTpChannel(ARObject):
    """AUTOSAR FlexrayArTpChannel."""

    ack_type: Optional[FrArTpAckType]
    cancellation: Optional[Boolean]
    extended: Optional[Boolean]
    max_ar: Optional[Integer]
    max_as: Optional[Integer]
    max_bs: Optional[Integer]
    max_fc_wait: Optional[PositiveInteger]
    maximum_message: Optional[MaximumMessageLengthType]
    max_retries: Optional[Integer]
    minimum: Optional[TimeValue]
    multicast: Optional[Boolean]
    n_pdus: list[NPdu]
    time_br: Optional[TimeValue]
    time_cs: Optional[TimeValue]
    timeout_ar: Optional[TimeValue]
    timeout_as: Optional[TimeValue]
    timeout_bs: Optional[TimeValue]
    timeout_cr: Optional[TimeValue]
    tp_connections: list[FlexrayArTpConnection]
    def __init__(self) -> None:
        """Initialize FlexrayArTpChannel."""
        super().__init__()
        self.ack_type: Optional[FrArTpAckType] = None
        self.cancellation: Optional[Boolean] = None
        self.extended: Optional[Boolean] = None
        self.max_ar: Optional[Integer] = None
        self.max_as: Optional[Integer] = None
        self.max_bs: Optional[Integer] = None
        self.max_fc_wait: Optional[PositiveInteger] = None
        self.maximum_message: Optional[MaximumMessageLengthType] = None
        self.max_retries: Optional[Integer] = None
        self.minimum: Optional[TimeValue] = None
        self.multicast: Optional[Boolean] = None
        self.n_pdus: list[NPdu] = []
        self.time_br: Optional[TimeValue] = None
        self.time_cs: Optional[TimeValue] = None
        self.timeout_ar: Optional[TimeValue] = None
        self.timeout_as: Optional[TimeValue] = None
        self.timeout_bs: Optional[TimeValue] = None
        self.timeout_cr: Optional[TimeValue] = None
        self.tp_connections: list[FlexrayArTpConnection] = []


class FlexrayArTpChannelBuilder:
    """Builder for FlexrayArTpChannel."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FlexrayArTpChannel = FlexrayArTpChannel()

    def build(self) -> FlexrayArTpChannel:
        """Build and return FlexrayArTpChannel object.

        Returns:
            FlexrayArTpChannel instance
        """
        # TODO: Add validation
        return self._obj
