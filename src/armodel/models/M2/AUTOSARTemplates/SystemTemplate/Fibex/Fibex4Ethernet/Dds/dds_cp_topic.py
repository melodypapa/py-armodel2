"""DdsCpTopic AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 526)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_Dds.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "dds_partition": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DdsCpPartition,
        ),  # ddsPartition
        "topic_name": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # topicName
    }

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
