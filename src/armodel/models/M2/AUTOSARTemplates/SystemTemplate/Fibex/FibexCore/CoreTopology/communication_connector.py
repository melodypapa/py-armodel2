"""CommunicationConnector AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.comm_connector_port import (
    CommConnectorPort,
)


class CommunicationConnector(Identifiable):
    """AUTOSAR CommunicationConnector."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("comm_controller", None, False, False, any (Communication)),  # commController
        ("create_ecu", None, True, False, None),  # createEcu
        ("dynamic_pnc_to", None, True, False, None),  # dynamicPncTo
        ("ecu_comm_ports", None, False, True, CommConnectorPort),  # ecuCommPorts
        ("pnc_filter_arrays", None, False, True, None),  # pncFilterArrays
        ("pnc_gateway_type_enum", None, False, False, PncGatewayTypeEnum),  # pncGatewayTypeEnum
    ]

    def __init__(self) -> None:
        """Initialize CommunicationConnector."""
        super().__init__()
        self.comm_controller: Optional[Any] = None
        self.create_ecu: Optional[Boolean] = None
        self.dynamic_pnc_to: Optional[Boolean] = None
        self.ecu_comm_ports: list[CommConnectorPort] = []
        self.pnc_filter_arrays: list[PositiveInteger] = []
        self.pnc_gateway_type_enum: Optional[PncGatewayTypeEnum] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CommunicationConnector to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CommunicationConnector":
        """Create CommunicationConnector from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CommunicationConnector instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CommunicationConnector since parent returns ARObject
        return cast("CommunicationConnector", obj)


class CommunicationConnectorBuilder:
    """Builder for CommunicationConnector."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CommunicationConnector = CommunicationConnector()

    def build(self) -> CommunicationConnector:
        """Build and return CommunicationConnector object.

        Returns:
            CommunicationConnector instance
        """
        # TODO: Add validation
        return self._obj
