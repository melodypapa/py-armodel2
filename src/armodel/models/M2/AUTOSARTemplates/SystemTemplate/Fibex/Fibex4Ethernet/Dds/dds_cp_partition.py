"""DdsCpPartition AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class DdsCpPartition(Identifiable):
    """AUTOSAR DdsCpPartition."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("partition_name", None, True, False, None),  # partitionName
    ]

    def __init__(self) -> None:
        """Initialize DdsCpPartition."""
        super().__init__()
        self.partition_name: Optional[String] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DdsCpPartition to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DdsCpPartition":
        """Create DdsCpPartition from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DdsCpPartition instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DdsCpPartition since parent returns ARObject
        return cast("DdsCpPartition", obj)


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
