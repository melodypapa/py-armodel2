"""NmCluster AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_cluster import (
    CommunicationCluster,
)


class NmCluster(Identifiable):
    """AUTOSAR NmCluster."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("communication_cluster", None, False, False, CommunicationCluster),  # communicationCluster
        ("nm_channel", None, True, False, None),  # nmChannel
        ("nm_node", None, True, False, None),  # nmNode
        ("nm_node_id_enabled", None, True, False, None),  # nmNodeIdEnabled
        ("nm_pnc", None, True, False, None),  # nmPnc
        ("nm_repeat_msg_ind_enabled", None, True, False, None),  # nmRepeatMsgIndEnabled
        ("nm", None, True, False, None),  # nm
        ("pnc_cluster", None, True, False, None),  # pncCluster
    ]

    def __init__(self) -> None:
        """Initialize NmCluster."""
        super().__init__()
        self.communication_cluster: Optional[CommunicationCluster] = None
        self.nm_channel: Optional[Boolean] = None
        self.nm_node: Optional[Boolean] = None
        self.nm_node_id_enabled: Optional[Boolean] = None
        self.nm_pnc: Optional[Boolean] = None
        self.nm_repeat_msg_ind_enabled: Optional[Boolean] = None
        self.nm: Optional[Boolean] = None
        self.pnc_cluster: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert NmCluster to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "NmCluster":
        """Create NmCluster from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            NmCluster instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to NmCluster since parent returns ARObject
        return cast("NmCluster", obj)


class NmClusterBuilder:
    """Builder for NmCluster."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: NmCluster = NmCluster()

    def build(self) -> NmCluster:
        """Build and return NmCluster object.

        Returns:
            NmCluster instance
        """
        # TODO: Add validation
        return self._obj
