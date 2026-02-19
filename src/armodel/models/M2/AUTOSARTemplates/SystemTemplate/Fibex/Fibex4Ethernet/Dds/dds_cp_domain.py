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
    def serialize(self) -> ET.Element:
        """Serialize DdsCpDomain to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DdsCpDomain, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize dds_partitions (list to container "DDS-PARTITIONS")
        if self.dds_partitions:
            wrapper = ET.Element("DDS-PARTITIONS")
            for item in self.dds_partitions:
                serialized = ARObject._serialize_item(item, "DdsCpPartition")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize dds_topics (list to container "DDS-TOPICS")
        if self.dds_topics:
            wrapper = ET.Element("DDS-TOPICS")
            for item in self.dds_topics:
                serialized = ARObject._serialize_item(item, "DdsCpTopic")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize domain_id
        if self.domain_id is not None:
            serialized = ARObject._serialize_item(self.domain_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DOMAIN-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DdsCpDomain":
        """Deserialize XML element to DdsCpDomain object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DdsCpDomain object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DdsCpDomain, cls).deserialize(element)

        # Parse dds_partitions (list from container "DDS-PARTITIONS")
        obj.dds_partitions = []
        container = ARObject._find_child_element(element, "DDS-PARTITIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.dds_partitions.append(child_value)

        # Parse dds_topics (list from container "DDS-TOPICS")
        obj.dds_topics = []
        container = ARObject._find_child_element(element, "DDS-TOPICS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.dds_topics.append(child_value)

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
