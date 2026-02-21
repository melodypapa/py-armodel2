"""AbstractValueRestriction AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 103)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 87)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_ModelRestrictionTypes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Limit,
    PositiveInteger,
    RegularExpression,
)
from abc import ABC, abstractmethod


class AbstractValueRestriction(ARObject, ABC):
    """AUTOSAR AbstractValueRestriction."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    max: Optional[Limit]
    max_length: Optional[PositiveInteger]
    min: Optional[Limit]
    min_length: Optional[PositiveInteger]
    pattern: Optional[RegularExpression]
    def __init__(self) -> None:
        """Initialize AbstractValueRestriction."""
        super().__init__()
        self.max: Optional[Limit] = None
        self.max_length: Optional[PositiveInteger] = None
        self.min: Optional[Limit] = None
        self.min_length: Optional[PositiveInteger] = None
        self.pattern: Optional[RegularExpression] = None

    def serialize(self) -> ET.Element:
        """Serialize AbstractValueRestriction to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AbstractValueRestriction, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize max
        if self.max is not None:
            serialized = SerializationHelper.serialize_item(self.max, "Limit")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_length
        if self.max_length is not None:
            serialized = SerializationHelper.serialize_item(self.max_length, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-LENGTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize min
        if self.min is not None:
            serialized = SerializationHelper.serialize_item(self.min, "Limit")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MIN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize min_length
        if self.min_length is not None:
            serialized = SerializationHelper.serialize_item(self.min_length, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MIN-LENGTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize pattern
        if self.pattern is not None:
            serialized = SerializationHelper.serialize_item(self.pattern, "RegularExpression")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PATTERN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AbstractValueRestriction":
        """Deserialize XML element to AbstractValueRestriction object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AbstractValueRestriction object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AbstractValueRestriction, cls).deserialize(element)

        # Parse max
        child = SerializationHelper.find_child_element(element, "MAX")
        if child is not None:
            max_value = SerializationHelper.deserialize_by_tag(child, "Limit")
            obj.max = max_value

        # Parse max_length
        child = SerializationHelper.find_child_element(element, "MAX-LENGTH")
        if child is not None:
            max_length_value = child.text
            obj.max_length = max_length_value

        # Parse min
        child = SerializationHelper.find_child_element(element, "MIN")
        if child is not None:
            min_value = SerializationHelper.deserialize_by_tag(child, "Limit")
            obj.min = min_value

        # Parse min_length
        child = SerializationHelper.find_child_element(element, "MIN-LENGTH")
        if child is not None:
            min_length_value = child.text
            obj.min_length = min_length_value

        # Parse pattern
        child = SerializationHelper.find_child_element(element, "PATTERN")
        if child is not None:
            pattern_value = child.text
            obj.pattern = pattern_value

        return obj



class AbstractValueRestrictionBuilder:
    """Builder for AbstractValueRestriction."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AbstractValueRestriction = AbstractValueRestriction()

    def build(self) -> AbstractValueRestriction:
        """Build and return AbstractValueRestriction object.

        Returns:
            AbstractValueRestriction instance
        """
        # TODO: Add validation
        return self._obj
