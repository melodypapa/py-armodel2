"""WorstCaseStackUsage AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.StackUsage.stack_usage import (
    StackUsage,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class WorstCaseStackUsage(StackUsage):
    """AUTOSAR WorstCaseStackUsage."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("memory_consumption", None, True, False, None),  # memoryConsumption
    ]

    def __init__(self) -> None:
        """Initialize WorstCaseStackUsage."""
        super().__init__()
        self.memory_consumption: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert WorstCaseStackUsage to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "WorstCaseStackUsage":
        """Create WorstCaseStackUsage from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            WorstCaseStackUsage instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to WorstCaseStackUsage since parent returns ARObject
        return cast("WorstCaseStackUsage", obj)


class WorstCaseStackUsageBuilder:
    """Builder for WorstCaseStackUsage."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: WorstCaseStackUsage = WorstCaseStackUsage()

    def build(self) -> WorstCaseStackUsage:
        """Build and return WorstCaseStackUsage object.

        Returns:
            WorstCaseStackUsage instance
        """
        # TODO: Add validation
        return self._obj
