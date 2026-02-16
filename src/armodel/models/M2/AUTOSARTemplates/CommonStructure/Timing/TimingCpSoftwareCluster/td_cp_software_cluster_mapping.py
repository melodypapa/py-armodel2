"""TDCpSoftwareClusterMapping AUTOSAR element."""

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


class TDCpSoftwareClusterMapping(Identifiable):
    """AUTOSAR TDCpSoftwareClusterMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("provider", None, False, False, CpSoftwareCluster),  # provider
        ("requestors", None, False, True, CpSoftwareCluster),  # requestors
        ("timing", None, False, False, TimingDescription),  # timing
    ]

    def __init__(self) -> None:
        """Initialize TDCpSoftwareClusterMapping."""
        super().__init__()
        self.provider: Optional[CpSoftwareCluster] = None
        self.requestors: list[CpSoftwareCluster] = []
        self.timing: Optional[TimingDescription] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TDCpSoftwareClusterMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDCpSoftwareClusterMapping":
        """Create TDCpSoftwareClusterMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TDCpSoftwareClusterMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TDCpSoftwareClusterMapping since parent returns ARObject
        return cast("TDCpSoftwareClusterMapping", obj)


class TDCpSoftwareClusterMappingBuilder:
    """Builder for TDCpSoftwareClusterMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDCpSoftwareClusterMapping = TDCpSoftwareClusterMapping()

    def build(self) -> TDCpSoftwareClusterMapping:
        """Build and return TDCpSoftwareClusterMapping object.

        Returns:
            TDCpSoftwareClusterMapping instance
        """
        # TODO: Add validation
        return self._obj
