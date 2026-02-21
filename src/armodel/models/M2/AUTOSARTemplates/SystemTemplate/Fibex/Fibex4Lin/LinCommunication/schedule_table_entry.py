"""ScheduleTableEntry AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 433)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
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

    def serialize(self) -> ET.Element:
        """Serialize ScheduleTableEntry to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ScheduleTableEntry, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize delay
        if self.delay is not None:
            serialized = SerializationHelper.serialize_item(self.delay, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DELAY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize introduction
        if self.introduction is not None:
            serialized = SerializationHelper.serialize_item(self.introduction, "DocumentationBlock")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INTRODUCTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize position_in_table
        if self.position_in_table is not None:
            serialized = SerializationHelper.serialize_item(self.position_in_table, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("POSITION-IN-TABLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ScheduleTableEntry":
        """Deserialize XML element to ScheduleTableEntry object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ScheduleTableEntry object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ScheduleTableEntry, cls).deserialize(element)

        # Parse delay
        child = SerializationHelper.find_child_element(element, "DELAY")
        if child is not None:
            delay_value = child.text
            obj.delay = delay_value

        # Parse introduction
        child = SerializationHelper.find_child_element(element, "INTRODUCTION")
        if child is not None:
            introduction_value = SerializationHelper.deserialize_by_tag(child, "DocumentationBlock")
            obj.introduction = introduction_value

        # Parse position_in_table
        child = SerializationHelper.find_child_element(element, "POSITION-IN-TABLE")
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
