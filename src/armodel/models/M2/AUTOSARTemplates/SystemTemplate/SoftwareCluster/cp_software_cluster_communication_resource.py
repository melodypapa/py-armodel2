"""CpSoftwareClusterCommunicationResource AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster_resource import (
    CpSoftwareClusterResource,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster import (
    CpSoftwareCluster,
)


class CpSoftwareClusterCommunicationResource(CpSoftwareClusterResource):
    """AUTOSAR CpSoftwareClusterCommunicationResource."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("communication", None, False, False, CpSoftwareCluster),  # communication
    ]

    def __init__(self) -> None:
        """Initialize CpSoftwareClusterCommunicationResource."""
        super().__init__()
        self.communication: Optional[CpSoftwareCluster] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CpSoftwareClusterCommunicationResource to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CpSoftwareClusterCommunicationResource":
        """Create CpSoftwareClusterCommunicationResource from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CpSoftwareClusterCommunicationResource instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CpSoftwareClusterCommunicationResource since parent returns ARObject
        return cast("CpSoftwareClusterCommunicationResource", obj)


class CpSoftwareClusterCommunicationResourceBuilder:
    """Builder for CpSoftwareClusterCommunicationResource."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CpSoftwareClusterCommunicationResource = CpSoftwareClusterCommunicationResource()

    def build(self) -> CpSoftwareClusterCommunicationResource:
        """Build and return CpSoftwareClusterCommunicationResource object.

        Returns:
            CpSoftwareClusterCommunicationResource instance
        """
        # TODO: Add validation
        return self._obj
