"""EthGlobalTimeManagedCouplingPort AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
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
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("coupling_port", None, False, False, CouplingPort),  # couplingPort
        ("global_time_port_role", None, False, False, GlobalTimePortRoleEnum),  # globalTimePortRole
        ("global_time_tx_period", None, True, False, None),  # globalTimeTxPeriod
        ("pdelay_latency", None, True, False, None),  # pdelayLatency
        ("pdelay_request", None, True, False, None),  # pdelayRequest
        ("pdelay_resp_and", None, True, False, None),  # pdelayRespAnd
        ("pdelay", None, True, False, None),  # pdelay
    ]

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

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EthGlobalTimeManagedCouplingPort to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EthGlobalTimeManagedCouplingPort":
        """Create EthGlobalTimeManagedCouplingPort from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EthGlobalTimeManagedCouplingPort instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EthGlobalTimeManagedCouplingPort since parent returns ARObject
        return cast("EthGlobalTimeManagedCouplingPort", obj)


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
