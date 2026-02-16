"""EthernetCommunicationController AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
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
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("can_xl_config", None, False, False, any (AbstractCan)),  # canXlConfig
        ("coupling_ports", None, False, True, CouplingPort),  # couplingPorts
        ("mac_layer_type", None, False, False, EthernetMacLayerTypeEnum),  # macLayerType
        ("mac_unicast", None, True, False, None),  # macUnicast
        ("maximum", None, True, False, None),  # maximum
        ("slave_act_as", None, True, False, None),  # slaveActAs
        ("slave_qualified", None, True, False, None),  # slaveQualified
    ]

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

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EthernetCommunicationController to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EthernetCommunicationController":
        """Create EthernetCommunicationController from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EthernetCommunicationController instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EthernetCommunicationController since parent returns ARObject
        return cast("EthernetCommunicationController", obj)


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
