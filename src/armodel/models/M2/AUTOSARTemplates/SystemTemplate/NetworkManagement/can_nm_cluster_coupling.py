"""CanNmClusterCoupling AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_cluster_coupling import (
    NmClusterCoupling,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.can_nm_cluster import (
    CanNmCluster,
)


class CanNmClusterCoupling(NmClusterCoupling):
    """AUTOSAR CanNmClusterCoupling."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("coupled_clusters", None, False, True, CanNmCluster),  # coupledClusters
        ("nm_busload_reduction", None, False, False, any (BooleanEnabled)),  # nmBusloadReduction
        ("nm_immediate", None, True, False, None),  # nmImmediate
    ]

    def __init__(self) -> None:
        """Initialize CanNmClusterCoupling."""
        super().__init__()
        self.coupled_clusters: list[CanNmCluster] = []
        self.nm_busload_reduction: Optional[Any] = None
        self.nm_immediate: Optional[Boolean] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CanNmClusterCoupling to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CanNmClusterCoupling":
        """Create CanNmClusterCoupling from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CanNmClusterCoupling instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CanNmClusterCoupling since parent returns ARObject
        return cast("CanNmClusterCoupling", obj)


class CanNmClusterCouplingBuilder:
    """Builder for CanNmClusterCoupling."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanNmClusterCoupling = CanNmClusterCoupling()

    def build(self) -> CanNmClusterCoupling:
        """Build and return CanNmClusterCoupling object.

        Returns:
            CanNmClusterCoupling instance
        """
        # TODO: Add validation
        return self._obj
