"""NmNode AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_ecu import (
    NmEcu,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.nm_pdu import (
    NmPdu,
)


class NmNode(Identifiable):
    """AUTOSAR NmNode."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("controller", None, False, False, any (Communication)),  # controller
        ("nm_coord_cluster", None, True, False, None),  # nmCoordCluster
        ("nm_coordinator_role", None, False, False, NmCoordinatorRoleEnum),  # nmCoordinatorRole
        ("nm_if_ecu", None, False, False, NmEcu),  # nmIfEcu
        ("nm_node_id", None, True, False, None),  # nmNodeId
        ("nm_passive", None, True, False, None),  # nmPassive
        ("rx_nm_pdus", None, False, True, NmPdu),  # rxNmPdus
        ("tx_nm_pdus", None, False, True, NmPdu),  # txNmPdus
    ]

    def __init__(self) -> None:
        """Initialize NmNode."""
        super().__init__()
        self.controller: Optional[Any] = None
        self.nm_coord_cluster: Optional[PositiveInteger] = None
        self.nm_coordinator_role: Optional[NmCoordinatorRoleEnum] = None
        self.nm_if_ecu: Optional[NmEcu] = None
        self.nm_node_id: Optional[Integer] = None
        self.nm_passive: Optional[Boolean] = None
        self.rx_nm_pdus: list[NmPdu] = []
        self.tx_nm_pdus: list[NmPdu] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert NmNode to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "NmNode":
        """Create NmNode from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            NmNode instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to NmNode since parent returns ARObject
        return cast("NmNode", obj)


class NmNodeBuilder:
    """Builder for NmNode."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: NmNode = NmNode()

    def build(self) -> NmNode:
        """Build and return NmNode object.

        Returns:
            NmNode instance
        """
        # TODO: Add validation
        return self._obj
