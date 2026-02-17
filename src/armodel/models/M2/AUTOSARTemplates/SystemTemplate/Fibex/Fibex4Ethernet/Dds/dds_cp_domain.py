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

    dds_partitions: list[DdsCpPartition]
    dds_topics: list[DdsCpTopic]
    domain_id: Optional[PositiveInteger]
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
