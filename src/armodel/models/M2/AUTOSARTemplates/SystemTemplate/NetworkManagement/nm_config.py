"""NmConfig AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_cluster import (
    NmCluster,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_cluster_coupling import (
    NmClusterCoupling,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_ecu import (
    NmEcu,
)


class NmConfig(FibexElement):
    """AUTOSAR NmConfig."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("nm_clusters", None, False, True, NmCluster),  # nmClusters
        ("nm_cluster_couplings", None, False, True, NmClusterCoupling),  # nmClusterCouplings
        ("nm_if_ecus", None, False, True, NmEcu),  # nmIfEcus
    ]

    def __init__(self) -> None:
        """Initialize NmConfig."""
        super().__init__()
        self.nm_clusters: list[NmCluster] = []
        self.nm_cluster_couplings: list[NmClusterCoupling] = []
        self.nm_if_ecus: list[NmEcu] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert NmConfig to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "NmConfig":
        """Create NmConfig from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            NmConfig instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to NmConfig since parent returns ARObject
        return cast("NmConfig", obj)


class NmConfigBuilder:
    """Builder for NmConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: NmConfig = NmConfig()

    def build(self) -> NmConfig:
        """Build and return NmConfig object.

        Returns:
            NmConfig instance
        """
        # TODO: Add validation
        return self._obj
