"""EthGlobalTimeManagedCouplingPort AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 874)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_GlobalTime_ETH.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.ETH import (
    GlobalTimePortRoleEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_port import (
    CouplingPort,
)


class EthGlobalTimeManagedCouplingPort(ARObject):
    """AUTOSAR EthGlobalTimeManagedCouplingPort."""

    coupling_port: Optional[CouplingPort]
    global_time_port_role: Optional[GlobalTimePortRoleEnum]
    global_time_tx_period: Optional[TimeValue]
    pdelay_latency: Optional[TimeValue]
    pdelay_request: Optional[TimeValue]
    pdelay_resp_and: Optional[TimeValue]
    pdelay: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize EthGlobalTimeManagedCouplingPort."""
        super().__init__()
        self.coupling_port: Optional[CouplingPort] = None
        self.global_time_port_role: Optional[GlobalTimePortRoleEnum] = None
        self.global_time_tx_period: Optional[TimeValue] = None
        self.pdelay_latency: Optional[TimeValue] = None
        self.pdelay_request: Optional[TimeValue] = None
        self.pdelay_resp_and: Optional[TimeValue] = None
        self.pdelay: Optional[Boolean] = None


class EthGlobalTimeManagedCouplingPortBuilder:
    """Builder for EthGlobalTimeManagedCouplingPort."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EthGlobalTimeManagedCouplingPort = EthGlobalTimeManagedCouplingPort()

    def build(self) -> EthGlobalTimeManagedCouplingPort:
        """Build and return EthGlobalTimeManagedCouplingPort object.

        Returns:
            EthGlobalTimeManagedCouplingPort instance
        """
        # TODO: Add validation
        return self._obj
