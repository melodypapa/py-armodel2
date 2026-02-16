"""DdsCpDomain AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds.dds_cp_partition import (
    DdsCpPartition,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds.dds_cp_topic import (
    DdsCpTopic,
)


class DdsCpDomain(Identifiable):
    """AUTOSAR DdsCpDomain."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("dds_partitions", None, False, True, DdsCpPartition),  # ddsPartitions
        ("dds_topics", None, False, True, DdsCpTopic),  # ddsTopics
        ("domain_id", None, True, False, None),  # domainId
    ]

    def __init__(self) -> None:
        """Initialize DdsCpDomain."""
        super().__init__()
        self.dds_partitions: list[DdsCpPartition] = []
        self.dds_topics: list[DdsCpTopic] = []
        self.domain_id: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DdsCpDomain to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DdsCpDomain":
        """Create DdsCpDomain from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DdsCpDomain instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DdsCpDomain since parent returns ARObject
        return cast("DdsCpDomain", obj)


class DdsCpDomainBuilder:
    """Builder for DdsCpDomain."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsCpDomain = DdsCpDomain()

    def build(self) -> DdsCpDomain:
        """Build and return DdsCpDomain object.

        Returns:
            DdsCpDomain instance
        """
        # TODO: Add validation
        return self._obj
