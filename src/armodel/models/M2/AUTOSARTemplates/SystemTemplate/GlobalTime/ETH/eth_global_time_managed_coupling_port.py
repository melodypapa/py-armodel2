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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "EthGlobalTimeManagedCouplingPort":
        """Deserialize XML element to EthGlobalTimeManagedCouplingPort object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EthGlobalTimeManagedCouplingPort object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse coupling_port
        child = ARObject._find_child_element(element, "COUPLING-PORT")
        if child is not None:
            coupling_port_value = ARObject._deserialize_by_tag(child, "CouplingPort")
            obj.coupling_port = coupling_port_value

        # Parse global_time_port_role
        child = ARObject._find_child_element(element, "GLOBAL-TIME-PORT-ROLE")
        if child is not None:
            global_time_port_role_value = child.text
            obj.global_time_port_role = global_time_port_role_value

        # Parse global_time_tx_period
        child = ARObject._find_child_element(element, "GLOBAL-TIME-TX-PERIOD")
        if child is not None:
            global_time_tx_period_value = child.text
            obj.global_time_tx_period = global_time_tx_period_value

        # Parse pdelay_latency
        child = ARObject._find_child_element(element, "PDELAY-LATENCY")
        if child is not None:
            pdelay_latency_value = child.text
            obj.pdelay_latency = pdelay_latency_value

        # Parse pdelay_request
        child = ARObject._find_child_element(element, "PDELAY-REQUEST")
        if child is not None:
            pdelay_request_value = child.text
            obj.pdelay_request = pdelay_request_value

        # Parse pdelay_resp_and
        child = ARObject._find_child_element(element, "PDELAY-RESP-AND")
        if child is not None:
            pdelay_resp_and_value = child.text
            obj.pdelay_resp_and = pdelay_resp_and_value

        # Parse pdelay
        child = ARObject._find_child_element(element, "PDELAY")
        if child is not None:
            pdelay_value = child.text
            obj.pdelay = pdelay_value

        return obj



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
