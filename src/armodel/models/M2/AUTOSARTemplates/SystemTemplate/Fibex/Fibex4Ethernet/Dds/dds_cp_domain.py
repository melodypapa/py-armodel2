"""DdsCpDomain AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "dds_partitions": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=DdsCpPartition,
        ),  # ddsPartitions
        "dds_topics": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=DdsCpTopic,
        ),  # ddsTopics
        "domain_id": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # domainId
    }

    def __init__(self) -> None:
        """Initialize DdsCpDomain."""
        super().__init__()
        self.dds_partitions: list[DdsCpPartition] = []
        self.dds_topics: list[DdsCpTopic] = []
        self.domain_id: Optional[PositiveInteger] = None


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
