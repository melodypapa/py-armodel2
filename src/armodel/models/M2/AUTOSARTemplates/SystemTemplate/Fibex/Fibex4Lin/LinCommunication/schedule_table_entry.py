"""ScheduleTableEntry AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 433)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
    TimeValue,
)
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)
from abc import ABC, abstractmethod


class ScheduleTableEntry(ARObject, ABC):
    """AUTOSAR ScheduleTableEntry."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    delay: Optional[TimeValue]
    introduction: Optional[DocumentationBlock]
    position_in_table: Optional[Integer]
    def __init__(self) -> None:
        """Initialize ScheduleTableEntry."""
        super().__init__()
        self.delay: Optional[TimeValue] = None
        self.introduction: Optional[DocumentationBlock] = None
        self.position_in_table: Optional[Integer] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ScheduleTableEntry":
        """Deserialize XML element to ScheduleTableEntry object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ScheduleTableEntry object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse delay
        child = ARObject._find_child_element(element, "DELAY")
        if child is not None:
            delay_value = child.text
            obj.delay = delay_value

        # Parse introduction
        child = ARObject._find_child_element(element, "INTRODUCTION")
        if child is not None:
            introduction_value = ARObject._deserialize_by_tag(child, "DocumentationBlock")
            obj.introduction = introduction_value

        # Parse position_in_table
        child = ARObject._find_child_element(element, "POSITION-IN-TABLE")
        if child is not None:
            position_in_table_value = child.text
            obj.position_in_table = position_in_table_value

        return obj



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
