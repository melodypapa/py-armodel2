"""EthernetCommunicationController AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 115)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET
from armodel.serialization.decorators import atp_variant

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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


@atp_variant()

class EthernetCommunicationController(ARObject):
    """AUTOSAR EthernetCommunicationController."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    can_xl_config_ref: Optional[Any]
    coupling_ports: list[CouplingPort]
    mac_layer_type: Optional[EthernetMacLayerTypeEnum]
    mac_unicast: Optional[MacAddressString]
    maximum: Optional[Integer]
    slave_act_as: Optional[Boolean]
    slave_qualified: Optional[TimeValue]
    def __init__(self) -> None:
        """Initialize EthernetCommunicationController."""
        super().__init__()
        self.can_xl_config_ref: Optional[Any] = None
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
