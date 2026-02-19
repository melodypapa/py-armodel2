"""DdsCpDomain AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 526)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_Dds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    dds_partitions: list[DdsCpPartition]
    dds_topics: list[DdsCpTopic]
    domain_id: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize DdsCpDomain."""
        super().__init__()
        self.dds_partitions: list[DdsCpPartition] = []
        self.dds_topics: list[DdsCpTopic] = []
        self.domain_id: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DdsCpDomain":
        """Deserialize XML element to DdsCpDomain object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DdsCpDomain object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse dds_partitions (list)
        obj.dds_partitions = []
        for child in ARObject._find_all_child_elements(element, "DDS-PARTITIONS"):
            dds_partitions_value = ARObject._deserialize_by_tag(child, "DdsCpPartition")
            obj.dds_partitions.append(dds_partitions_value)

        # Parse dds_topics (list)
        obj.dds_topics = []
        for child in ARObject._find_all_child_elements(element, "DDS-TOPICS"):
            dds_topics_value = ARObject._deserialize_by_tag(child, "DdsCpTopic")
            obj.dds_topics.append(dds_topics_value)

        # Parse domain_id
        child = ARObject._find_child_element(element, "DOMAIN-ID")
        if child is not None:
            domain_id_value = child.text
            obj.domain_id = domain_id_value

        return obj



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
