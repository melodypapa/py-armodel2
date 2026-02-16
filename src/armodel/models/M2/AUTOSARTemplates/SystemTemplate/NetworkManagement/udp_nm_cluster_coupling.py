"""UdpNmClusterCoupling AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_cluster_coupling import (
    NmClusterCoupling,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.udp_nm_cluster import (
    UdpNmCluster,
)


class UdpNmClusterCoupling(NmClusterCoupling):
    """AUTOSAR UdpNmClusterCoupling."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("coupled_clusters", None, False, True, UdpNmCluster),  # coupledClusters
        ("nm_immediate", None, True, False, None),  # nmImmediate
    ]

    def __init__(self) -> None:
        """Initialize UdpNmClusterCoupling."""
        super().__init__()
        self.coupled_clusters: list[UdpNmCluster] = []
        self.nm_immediate: Optional[Boolean] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert UdpNmClusterCoupling to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "UdpNmClusterCoupling":
        """Create UdpNmClusterCoupling from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            UdpNmClusterCoupling instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to UdpNmClusterCoupling since parent returns ARObject
        return cast("UdpNmClusterCoupling", obj)


class UdpNmClusterCouplingBuilder:
    """Builder for UdpNmClusterCoupling."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: UdpNmClusterCoupling = UdpNmClusterCoupling()

    def build(self) -> UdpNmClusterCoupling:
        """Build and return UdpNmClusterCoupling object.

        Returns:
            UdpNmClusterCoupling instance
        """
        # TODO: Add validation
        return self._obj
