"""ScheduleTableEntry AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "delay": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # delay
        "introduction": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DocumentationBlock,
        ),  # introduction
        "position_in_table": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # positionInTable
    }

    def __init__(self) -> None:
        """Initialize ScheduleTableEntry."""
        super().__init__()
        self.delay: Optional[TimeValue] = None
        self.introduction: Optional[DocumentationBlock] = None
        self.position_in_table: Optional[Integer] = None


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
