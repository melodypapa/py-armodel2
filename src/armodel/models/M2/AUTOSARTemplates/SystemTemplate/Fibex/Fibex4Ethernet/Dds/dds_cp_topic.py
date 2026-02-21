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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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

    dds_partition_ref: Optional[ARRef]
    topic_name: Optional[String]
    def __init__(self) -> None:
        """Initialize DdsCpTopic."""
        super().__init__()
        self.dds_partition_ref: Optional[ARRef] = None
        self.topic_name: Optional[String] = None

    def serialize(self) -> ET.Element:
        """Serialize DdsCpTopic to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DdsCpTopic, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize dds_partition_ref
        if self.dds_partition_ref is not None:
            serialized = ARObject._serialize_item(self.dds_partition_ref, "DdsCpPartition")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DDS-PARTITION-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize topic_name
        if self.topic_name is not None:
            serialized = ARObject._serialize_item(self.topic_name, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TOPIC-NAME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DdsCpTopic":
        """Deserialize XML element to DdsCpTopic object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DdsCpTopic object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DdsCpTopic, cls).deserialize(element)

        # Parse dds_partition_ref
        child = ARObject._find_child_element(element, "DDS-PARTITION-REF")
        if child is not None:
            dds_partition_ref_value = ARRef.deserialize(child)
            obj.dds_partition_ref = dds_partition_ref_value

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
