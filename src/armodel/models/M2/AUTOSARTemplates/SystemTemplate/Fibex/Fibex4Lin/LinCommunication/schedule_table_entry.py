"""ScheduleTableEntry AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
    TimeValue,
)
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)


class ScheduleTableEntry(ARObject):
    """AUTOSAR ScheduleTableEntry."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("delay", None, True, False, None),  # delay
        ("introduction", None, False, False, DocumentationBlock),  # introduction
        ("position_in_table", None, True, False, None),  # positionInTable
    ]

    def __init__(self) -> None:
        """Initialize ScheduleTableEntry."""
        super().__init__()
        self.delay: Optional[TimeValue] = None
        self.introduction: Optional[DocumentationBlock] = None
        self.position_in_table: Optional[Integer] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ScheduleTableEntry to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ScheduleTableEntry":
        """Create ScheduleTableEntry from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ScheduleTableEntry instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ScheduleTableEntry since parent returns ARObject
        return cast("ScheduleTableEntry", obj)


class ScheduleTableEntryBuilder:
    """Builder for ScheduleTableEntry."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ScheduleTableEntry = ScheduleTableEntry()

    def build(self) -> ScheduleTableEntry:
        """Build and return ScheduleTableEntry object.

        Returns:
            ScheduleTableEntry instance
        """
        # TODO: Add validation
        return self._obj
