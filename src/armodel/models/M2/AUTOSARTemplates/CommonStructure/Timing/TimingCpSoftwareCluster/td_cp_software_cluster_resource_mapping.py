"""TDCpSoftwareClusterResourceMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster import (
    CpSoftwareCluster,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description import (
    TimingDescription,
)


class TDCpSoftwareClusterResourceMapping(Identifiable):
    """AUTOSAR TDCpSoftwareClusterResourceMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("resource", None, False, False, CpSoftwareCluster),  # resource
        ("timing", None, False, False, TimingDescription),  # timing
    ]

    def __init__(self) -> None:
        """Initialize TDCpSoftwareClusterResourceMapping."""
        super().__init__()
        self.resource: Optional[CpSoftwareCluster] = None
        self.timing: Optional[TimingDescription] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TDCpSoftwareClusterResourceMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDCpSoftwareClusterResourceMapping":
        """Create TDCpSoftwareClusterResourceMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TDCpSoftwareClusterResourceMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TDCpSoftwareClusterResourceMapping since parent returns ARObject
        return cast("TDCpSoftwareClusterResourceMapping", obj)


class TDCpSoftwareClusterResourceMappingBuilder:
    """Builder for TDCpSoftwareClusterResourceMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDCpSoftwareClusterResourceMapping = TDCpSoftwareClusterResourceMapping()

    def build(self) -> TDCpSoftwareClusterResourceMapping:
        """Build and return TDCpSoftwareClusterResourceMapping object.

        Returns:
            TDCpSoftwareClusterResourceMapping instance
        """
        # TODO: Add validation
        return self._obj
