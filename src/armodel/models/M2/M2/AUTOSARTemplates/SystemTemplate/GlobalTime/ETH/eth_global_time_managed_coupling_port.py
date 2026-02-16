"""EthGlobalTimeManagedCouplingPort AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_port import (
    CouplingPort,
)


class EthGlobalTimeManagedCouplingPort(ARObject):
    """AUTOSAR EthGlobalTimeManagedCouplingPort."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "coupling_port": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=CouplingPort,
        ),  # couplingPort
        "global_time_port_role": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=GlobalTimePortRoleEnum,
        ),  # globalTimePortRole
        "global_time_tx_period": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # globalTimeTxPeriod
        "pdelay_latency": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # pdelayLatency
        "pdelay_request": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # pdelayRequest
        "pdelay_resp_and": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # pdelayRespAnd
        "pdelay": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # pdelay
    }

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
