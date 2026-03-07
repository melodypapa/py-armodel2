"""ScheduleTableEntry AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 433)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
    TimeValue,
)
from armodel2.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


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
    _DESERIALIZE_DISPATCH = {
        "DELAY": lambda obj, elem: setattr(obj, "delay", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "INTRODUCTION": lambda obj, elem: setattr(obj, "introduction", SerializationHelper.deserialize_by_tag(elem, "DocumentationBlock")),
        "POSITION-IN-TABLE": lambda obj, elem: setattr(obj, "position_in_table", SerializationHelper.deserialize_by_tag(elem, "Integer")),
    }


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
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DELAY":
                setattr(obj, "delay", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "INTRODUCTION":
                setattr(obj, "introduction", SerializationHelper.deserialize_by_tag(child, "DocumentationBlock"))
            elif tag == "POSITION-IN-TABLE":
                setattr(obj, "position_in_table", SerializationHelper.deserialize_by_tag(child, "Integer"))

        return obj



class ScheduleTableEntryBuilder(BuilderBase, ABC):
    """Builder for ScheduleTableEntry with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ScheduleTableEntry = ScheduleTableEntry()


    def with_delay(self, value: Optional[TimeValue]) -> "ScheduleTableEntryBuilder":
        """Set delay attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'delay' is required and cannot be None")
        self._obj.delay = value
        return self

    def with_introduction(self, value: Optional[DocumentationBlock]) -> "ScheduleTableEntryBuilder":
        """Set introduction attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'introduction' is required and cannot be None")
        self._obj.introduction = value
        return self

    def with_position_in_table(self, value: Optional[Integer]) -> "ScheduleTableEntryBuilder":
        """Set position_in_table attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'position_in_table' is required and cannot be None")
        self._obj.position_in_table = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "delay",
        "introduction",
        "positionInTable",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    @abstractmethod
    def build(self) -> ScheduleTableEntry:
        """Build and return the ScheduleTableEntry instance (abstract)."""
        raise NotImplementedError