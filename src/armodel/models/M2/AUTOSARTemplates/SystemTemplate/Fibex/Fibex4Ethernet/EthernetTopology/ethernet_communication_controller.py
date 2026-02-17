"""EthernetCommunicationController AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 115)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    EthernetMacLayerTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
    MacAddressString,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_port import (
    CouplingPort,
)


class EthernetCommunicationController(ARObject):
    """AUTOSAR EthernetCommunicationController."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "can_xl_config": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (AbstractCan),
        ),  # canXlConfig
        "coupling_ports": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=CouplingPort,
        ),  # couplingPorts
        "mac_layer_type": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=EthernetMacLayerTypeEnum,
        ),  # macLayerType
        "mac_unicast": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # macUnicast
        "maximum": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # maximum
        "slave_act_as": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # slaveActAs
        "slave_qualified": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # slaveQualified
    }

    def __init__(self) -> None:
        """Initialize EthernetCommunicationController."""
        super().__init__()
        self.can_xl_config: Optional[Any] = None
        self.coupling_ports: list[CouplingPort] = []
        self.mac_layer_type: Optional[EthernetMacLayerTypeEnum] = None
        self.mac_unicast: Optional[MacAddressString] = None
        self.maximum: Optional[Integer] = None
        self.slave_act_as: Optional[Boolean] = None
        self.slave_qualified: Optional[TimeValue] = None


class EthernetCommunicationControllerBuilder:
    """Builder for EthernetCommunicationController."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EthernetCommunicationController = EthernetCommunicationController()

    def build(self) -> EthernetCommunicationController:
        """Build and return EthernetCommunicationController object.

        Returns:
            EthernetCommunicationController instance
        """
        # TODO: Add validation
        return self._obj
