"""CouplingPort AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("connection", None, False, False, EthernetConnectionNegotiationEnum),  # connection
        ("coupling_port_details", None, False, False, CouplingPortDetails),  # couplingPortDetails
        ("coupling_port_role_enum", None, False, False, CouplingPortRoleEnum),  # couplingPortRoleEnum
        ("default_vlan", None, False, False, any (EthernetPhysical)),  # defaultVlan
        ("mac_layer_type_enum", None, False, False, EthernetMacLayerTypeEnum),  # macLayerTypeEnum
        ("mac_multicast_groups", None, False, True, MacMulticastGroup),  # macMulticastGroups
        ("mac_sec_propses", None, False, True, MacSecProps),  # macSecPropses
        ("physical_layer", None, False, False, EthernetPhysicalLayerTypeEnum),  # physicalLayer
        ("plca_props", None, False, False, PlcaProps),  # plcaProps
        ("pnc_mapping_idents", None, False, True, PncMappingIdent),  # pncMappingIdents
        ("receive_activity", None, False, False, any (EthernetSwitchVlan)),  # receiveActivity
        ("vlans", None, False, True, VlanMembership),  # vlans
        ("vlan_modifier", None, False, False, any (EthernetPhysical)),  # vlanModifier
        ("wakeup_sleep", None, False, False, any (EthernetWakeupSleep)),  # wakeupSleep
    ]

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

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CouplingPort to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CouplingPort":
        """Create CouplingPort from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CouplingPort instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CouplingPort since parent returns ARObject
        return cast("CouplingPort", obj)


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
