"""MeasuredHeapUsage AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.HeapUsage.heap_usage import (
    HeapUsage,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    String,
)


class MeasuredHeapUsage(HeapUsage):
    """AUTOSAR MeasuredHeapUsage."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("average_memory_consumption", None, True, False, None),  # averageMemoryConsumption
        ("maximum_memory_consumption", None, True, False, None),  # maximumMemoryConsumption
        ("minimum_memory_consumption", None, True, False, None),  # minimumMemoryConsumption
        ("test_pattern", None, True, False, None),  # testPattern
    ]

    def __init__(self) -> None:
        """Initialize MeasuredHeapUsage."""
        super().__init__()
        self.average_memory_consumption: Optional[PositiveInteger] = None
        self.maximum_memory_consumption: Optional[PositiveInteger] = None
        self.minimum_memory_consumption: Optional[PositiveInteger] = None
        self.test_pattern: Optional[String] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert MeasuredHeapUsage to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MeasuredHeapUsage":
        """Create MeasuredHeapUsage from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            MeasuredHeapUsage instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to MeasuredHeapUsage since parent returns ARObject
        return cast("MeasuredHeapUsage", obj)


class MeasuredHeapUsageBuilder:
    """Builder for MeasuredHeapUsage."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MeasuredHeapUsage = MeasuredHeapUsage()

    def build(self) -> MeasuredHeapUsage:
        """Build and return MeasuredHeapUsage object.

        Returns:
            MeasuredHeapUsage instance
        """
        # TODO: Add validation
        return self._obj
