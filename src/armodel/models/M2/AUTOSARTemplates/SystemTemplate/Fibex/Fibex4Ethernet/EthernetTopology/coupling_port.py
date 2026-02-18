"""CouplingPort AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 109)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    CouplingPortRoleEnum,
    EthernetConnectionNegotiationEnum,
    EthernetMacLayerTypeEnum,
    EthernetPhysicalLayerTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_port_details import (
    CouplingPortDetails,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.mac_multicast_group import (
    MacMulticastGroup,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.mac_sec_props import (
    MacSecProps,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.plca_props import (
    PlcaProps,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.PncMapping.pnc_mapping_ident import (
    PncMappingIdent,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.vlan_membership import (
    VlanMembership,
)


class CouplingPort(Identifiable):
    """AUTOSAR CouplingPort."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    connection: Optional[EthernetConnectionNegotiationEnum]
    coupling_port_details: Optional[CouplingPortDetails]
    coupling_port_role_enum: Optional[CouplingPortRoleEnum]
    default_vlan: Optional[Any]
    mac_layer_type_enum: Optional[EthernetMacLayerTypeEnum]
    mac_multicast_groups: list[MacMulticastGroup]
    mac_sec_propses: list[MacSecProps]
    physical_layer: Optional[EthernetPhysicalLayerTypeEnum]
    plca_props: Optional[PlcaProps]
    pnc_mapping_idents: list[PncMappingIdent]
    receive_activity: Optional[Any]
    vlans: list[VlanMembership]
    vlan_modifier: Optional[Any]
    wakeup_sleep: Optional[Any]
    def __init__(self) -> None:
        """Initialize CouplingPort."""
        super().__init__()
        self.connection: Optional[EthernetConnectionNegotiationEnum] = None
        self.coupling_port_details: Optional[CouplingPortDetails] = None
        self.coupling_port_role_enum: Optional[CouplingPortRoleEnum] = None
        self.default_vlan: Optional[Any] = None
        self.mac_layer_type_enum: Optional[EthernetMacLayerTypeEnum] = None
        self.mac_multicast_groups: list[MacMulticastGroup] = []
        self.mac_sec_propses: list[MacSecProps] = []
        self.physical_layer: Optional[EthernetPhysicalLayerTypeEnum] = None
        self.plca_props: Optional[PlcaProps] = None
        self.pnc_mapping_idents: list[PncMappingIdent] = []
        self.receive_activity: Optional[Any] = None
        self.vlans: list[VlanMembership] = []
        self.vlan_modifier: Optional[Any] = None
        self.wakeup_sleep: Optional[Any] = None


class CouplingPortBuilder:
    """Builder for CouplingPort."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CouplingPort = CouplingPort()

    def build(self) -> CouplingPort:
        """Build and return CouplingPort object.

        Returns:
            CouplingPort instance
        """
        # TODO: Add validation
        return self._obj
