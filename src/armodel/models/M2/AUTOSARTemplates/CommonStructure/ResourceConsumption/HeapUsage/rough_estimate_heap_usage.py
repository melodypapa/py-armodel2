"""RoughEstimateHeapUsage AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.HeapUsage.heap_usage import (
    HeapUsage,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class RoughEstimateHeapUsage(HeapUsage):
    """AUTOSAR RoughEstimateHeapUsage."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("memory_consumption", None, True, False, None),  # memoryConsumption
    ]

    def __init__(self) -> None:
        """Initialize RoughEstimateHeapUsage."""
        super().__init__()
        self.memory_consumption: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert RoughEstimateHeapUsage to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RoughEstimateHeapUsage":
        """Create RoughEstimateHeapUsage from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            RoughEstimateHeapUsage instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to RoughEstimateHeapUsage since parent returns ARObject
        return cast("RoughEstimateHeapUsage", obj)


class RoughEstimateHeapUsageBuilder:
    """Builder for RoughEstimateHeapUsage."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RoughEstimateHeapUsage = RoughEstimateHeapUsage()

    def build(self) -> RoughEstimateHeapUsage:
        """Build and return RoughEstimateHeapUsage object.

        Returns:
            RoughEstimateHeapUsage instance
        """
        # TODO: Add validation
        return self._obj
