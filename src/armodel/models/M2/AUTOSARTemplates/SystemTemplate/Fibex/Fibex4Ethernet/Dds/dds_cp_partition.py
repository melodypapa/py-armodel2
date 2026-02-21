"""DdsCpPartition AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 527)

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


class DdsCpPartition(Identifiable):
    """AUTOSAR DdsCpPartition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    partition_name: Optional[String]
    def __init__(self) -> None:
        """Initialize DdsCpPartition."""
        super().__init__()
        self.partition_name: Optional[String] = None

    def serialize(self) -> ET.Element:
        """Serialize DdsCpPartition to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DdsCpPartition, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize partition_name
        if self.partition_name is not None:
            serialized = ARObject._serialize_item(self.partition_name, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PARTITION-NAME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DdsCpPartition":
        """Deserialize XML element to DdsCpPartition object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DdsCpPartition object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DdsCpPartition, cls).deserialize(element)

        # Parse partition_name
        child = ARObject._find_child_element(element, "PARTITION-NAME")
        if child is not None:
            partition_name_value = child.text
            obj.partition_name = partition_name_value

        return obj



class DdsCpPartitionBuilder:
    """Builder for DdsCpPartition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsCpPartition = DdsCpPartition()

    def build(self) -> DdsCpPartition:
        """Build and return DdsCpPartition object.

        Returns:
            DdsCpPartition instance
        """
        # TODO: Add validation
        return self._obj
