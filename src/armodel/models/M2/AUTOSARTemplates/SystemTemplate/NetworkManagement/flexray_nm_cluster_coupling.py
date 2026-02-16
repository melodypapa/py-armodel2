"""FlexrayNmClusterCoupling AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_cluster_coupling import (
    NmClusterCoupling,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.flexray_nm_cluster import (
    FlexrayNmCluster,
)


class FlexrayNmClusterCoupling(NmClusterCoupling):
    """AUTOSAR FlexrayNmClusterCoupling."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("coupled_clusters", None, False, True, FlexrayNmCluster),  # coupledClusters
        ("nm_schedule", None, False, False, FlexrayNmScheduleVariant),  # nmSchedule
    ]

    def __init__(self) -> None:
        """Initialize FlexrayNmClusterCoupling."""
        super().__init__()
        self.coupled_clusters: list[FlexrayNmCluster] = []
        self.nm_schedule: Optional[FlexrayNmScheduleVariant] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert FlexrayNmClusterCoupling to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlexrayNmClusterCoupling":
        """Create FlexrayNmClusterCoupling from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            FlexrayNmClusterCoupling instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to FlexrayNmClusterCoupling since parent returns ARObject
        return cast("FlexrayNmClusterCoupling", obj)


class FlexrayNmClusterCouplingBuilder:
    """Builder for FlexrayNmClusterCoupling."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FlexrayNmClusterCoupling = FlexrayNmClusterCoupling()

    def build(self) -> FlexrayNmClusterCoupling:
        """Build and return FlexrayNmClusterCoupling object.

        Returns:
            FlexrayNmClusterCoupling instance
        """
        # TODO: Add validation
        return self._obj
