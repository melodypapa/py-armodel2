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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DdsCpTopic":
        """Deserialize XML element to DdsCpTopic object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DdsCpTopic object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse dds_partition
        child = ARObject._find_child_element(element, "DDS-PARTITION")
        if child is not None:
            dds_partition_value = ARObject._deserialize_by_tag(child, "DdsCpPartition")
            obj.dds_partition = dds_partition_value

        # Parse topic_name
        child = ARObject._find_child_element(element, "TOPIC-NAME")
        if child is not None:
            topic_name_value = child.text
            obj.topic_name = topic_name_value

        return obj



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
