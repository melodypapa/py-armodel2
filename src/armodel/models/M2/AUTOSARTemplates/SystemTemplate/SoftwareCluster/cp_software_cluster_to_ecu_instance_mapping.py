"""CpSoftwareClusterToEcuInstanceMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster import (
    CpSoftwareCluster,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.ecu_instance import (
    EcuInstance,
)


class CpSoftwareClusterToEcuInstanceMapping(Identifiable):
    """AUTOSAR CpSoftwareClusterToEcuInstanceMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("ecu_instance", None, False, False, EcuInstance),  # ecuInstance
        ("machine_id", None, True, False, None),  # machineId
        ("sw_clusters", None, False, True, CpSoftwareCluster),  # swClusters
    ]

    def __init__(self) -> None:
        """Initialize CpSoftwareClusterToEcuInstanceMapping."""
        super().__init__()
        self.ecu_instance: Optional[EcuInstance] = None
        self.machine_id: Optional[PositiveInteger] = None
        self.sw_clusters: list[CpSoftwareCluster] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CpSoftwareClusterToEcuInstanceMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CpSoftwareClusterToEcuInstanceMapping":
        """Create CpSoftwareClusterToEcuInstanceMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CpSoftwareClusterToEcuInstanceMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CpSoftwareClusterToEcuInstanceMapping since parent returns ARObject
        return cast("CpSoftwareClusterToEcuInstanceMapping", obj)


class CpSoftwareClusterToEcuInstanceMappingBuilder:
    """Builder for CpSoftwareClusterToEcuInstanceMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CpSoftwareClusterToEcuInstanceMapping = CpSoftwareClusterToEcuInstanceMapping()

    def build(self) -> CpSoftwareClusterToEcuInstanceMapping:
        """Build and return CpSoftwareClusterToEcuInstanceMapping object.

        Returns:
            CpSoftwareClusterToEcuInstanceMapping instance
        """
        # TODO: Add validation
        return self._obj
