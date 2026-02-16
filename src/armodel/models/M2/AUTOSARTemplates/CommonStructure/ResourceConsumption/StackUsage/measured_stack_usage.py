"""MeasuredStackUsage AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.StackUsage.stack_usage import (
    StackUsage,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    String,
)


class MeasuredStackUsage(StackUsage):
    """AUTOSAR MeasuredStackUsage."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("average_memory_consumption", None, True, False, None),  # averageMemoryConsumption
        ("maximum_memory_consumption", None, True, False, None),  # maximumMemoryConsumption
        ("minimum_memory_consumption", None, True, False, None),  # minimumMemoryConsumption
        ("test_pattern", None, True, False, None),  # testPattern
    ]

    def __init__(self) -> None:
        """Initialize MeasuredStackUsage."""
        super().__init__()
        self.average_memory_consumption: Optional[PositiveInteger] = None
        self.maximum_memory_consumption: Optional[PositiveInteger] = None
        self.minimum_memory_consumption: Optional[PositiveInteger] = None
        self.test_pattern: Optional[String] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert MeasuredStackUsage to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MeasuredStackUsage":
        """Create MeasuredStackUsage from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            MeasuredStackUsage instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to MeasuredStackUsage since parent returns ARObject
        return cast("MeasuredStackUsage", obj)


class MeasuredStackUsageBuilder:
    """Builder for MeasuredStackUsage."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MeasuredStackUsage = MeasuredStackUsage()

    def build(self) -> MeasuredStackUsage:
        """Build and return MeasuredStackUsage object.

        Returns:
            MeasuredStackUsage instance
        """
        # TODO: Add validation
        return self._obj
