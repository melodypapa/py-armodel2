"""CpSoftwareClusterServiceResource AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster_resource import (
    CpSoftwareClusterResource,
)
from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.ecuc_container_value import (
    EcucContainerValue,
)


class CpSoftwareClusterServiceResource(CpSoftwareClusterResource):
    """AUTOSAR CpSoftwareClusterServiceResource."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("resource_needses", None, False, True, EcucContainerValue),  # resourceNeedses
    ]

    def __init__(self) -> None:
        """Initialize CpSoftwareClusterServiceResource."""
        super().__init__()
        self.resource_needses: list[EcucContainerValue] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CpSoftwareClusterServiceResource to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CpSoftwareClusterServiceResource":
        """Create CpSoftwareClusterServiceResource from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CpSoftwareClusterServiceResource instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CpSoftwareClusterServiceResource since parent returns ARObject
        return cast("CpSoftwareClusterServiceResource", obj)


class CpSoftwareClusterServiceResourceBuilder:
    """Builder for CpSoftwareClusterServiceResource."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CpSoftwareClusterServiceResource = CpSoftwareClusterServiceResource()

    def build(self) -> CpSoftwareClusterServiceResource:
        """Build and return CpSoftwareClusterServiceResource object.

        Returns:
            CpSoftwareClusterServiceResource instance
        """
        # TODO: Add validation
        return self._obj
