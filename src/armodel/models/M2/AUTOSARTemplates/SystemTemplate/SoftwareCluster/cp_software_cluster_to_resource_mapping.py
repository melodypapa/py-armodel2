"""CpSoftwareClusterToResourceMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster import (
    CpSoftwareCluster,
)


class CpSoftwareClusterToResourceMapping(Identifiable):
    """AUTOSAR CpSoftwareClusterToResourceMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("provider", None, False, False, CpSoftwareCluster),  # provider
        ("requesters", None, False, True, CpSoftwareCluster),  # requesters
        ("service", None, False, False, CpSoftwareCluster),  # service
    ]

    def __init__(self) -> None:
        """Initialize CpSoftwareClusterToResourceMapping."""
        super().__init__()
        self.provider: Optional[CpSoftwareCluster] = None
        self.requesters: list[CpSoftwareCluster] = []
        self.service: Optional[CpSoftwareCluster] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CpSoftwareClusterToResourceMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CpSoftwareClusterToResourceMapping":
        """Create CpSoftwareClusterToResourceMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CpSoftwareClusterToResourceMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CpSoftwareClusterToResourceMapping since parent returns ARObject
        return cast("CpSoftwareClusterToResourceMapping", obj)


class CpSoftwareClusterToResourceMappingBuilder:
    """Builder for CpSoftwareClusterToResourceMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CpSoftwareClusterToResourceMapping = CpSoftwareClusterToResourceMapping()

    def build(self) -> CpSoftwareClusterToResourceMapping:
        """Build and return CpSoftwareClusterToResourceMapping object.

        Returns:
            CpSoftwareClusterToResourceMapping instance
        """
        # TODO: Add validation
        return self._obj
