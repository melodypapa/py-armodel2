"""Paginateable AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 339)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_PaginationAndView.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.document_view_selectable import (
    DocumentViewSelectable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView import (
    ChapterEnumBreak,
    KeepWithPreviousEnum,
)
from abc import ABC, abstractmethod


class Paginateable(DocumentViewSelectable, ABC):
    """AUTOSAR Paginateable."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    break_: Optional[ChapterEnumBreak]
    keep_with: Optional[KeepWithPreviousEnum]
    def __init__(self) -> None:
        """Initialize Paginateable."""
        super().__init__()
        self.break_: Optional[ChapterEnumBreak] = None
        self.keep_with: Optional[KeepWithPreviousEnum] = None
    def serialize(self) -> ET.Element:
        """Serialize Paginateable to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Paginateable, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize break_
        if self.break_ is not None:
            serialized = ARObject._serialize_item(self.break_, "ChapterEnumBreak")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BREAK")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize keep_with
        if self.keep_with is not None:
            serialized = ARObject._serialize_item(self.keep_with, "KeepWithPreviousEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("KEEP-WITH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Paginateable":
        """Deserialize XML element to Paginateable object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Paginateable object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Paginateable, cls).deserialize(element)

        # Parse break_
        child = ARObject._find_child_element(element, "BREAK")
        if child is not None:
            break__value = ChapterEnumBreak.deserialize(child)
            obj.break_ = break__value

        # Parse keep_with
        child = ARObject._find_child_element(element, "KEEP-WITH")
        if child is not None:
            keep_with_value = KeepWithPreviousEnum.deserialize(child)
            obj.keep_with = keep_with_value

        return obj



class PaginateableBuilder:
    """Builder for Paginateable."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Paginateable = Paginateable()

    def build(self) -> Paginateable:
        """Build and return Paginateable object.

        Returns:
            Paginateable instance
        """
        # TODO: Add validation
        return self._obj
