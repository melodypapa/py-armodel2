"""DdsCpTopic AUTOSAR element.

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
    String,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds.dds_cp_partition import (
    DdsCpPartition,
)


class DdsCpTopic(Identifiable):
    """AUTOSAR DdsCpTopic."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    dds_partition: Optional[DdsCpPartition]
    topic_name: Optional[String]
    def __init__(self) -> None:
        """Initialize DdsCpTopic."""
        super().__init__()
        self.dds_partition: Optional[DdsCpPartition] = None
        self.topic_name: Optional[String] = None


class DdsCpTopicBuilder:
    """Builder for DdsCpTopic."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsCpTopic = DdsCpTopic()

    def build(self) -> DdsCpTopic:
        """Build and return DdsCpTopic object.

        Returns:
            DdsCpTopic instance
        """
        # TODO: Add validation
        return self._obj
