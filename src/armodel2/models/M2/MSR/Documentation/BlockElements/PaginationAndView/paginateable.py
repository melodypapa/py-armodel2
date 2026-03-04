"""Paginateable AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 339)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_PaginationAndView.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.MSR.Documentation.BlockElements.PaginationAndView.document_view_selectable import (
    DocumentViewSelectable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.MSR.Documentation.BlockElements.PaginationAndView.document_view_selectable import DocumentViewSelectableBuilder
from armodel2.models.M2.MSR.Documentation.BlockElements.PaginationAndView import (
    ChapterEnumBreak,
    KeepWithPreviousEnum,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


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
    _DESERIALIZE_DISPATCH = {
        "BREAK": lambda obj, elem: setattr(obj, "break_", ChapterEnumBreak.deserialize(elem)),
        "KEEP-WITH": lambda obj, elem: setattr(obj, "keep_with", KeepWithPreviousEnum.deserialize(elem)),
    }


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
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Paginateable, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize break_
        if self.break_ is not None:
            serialized = SerializationHelper.serialize_item(self.break_, "ChapterEnumBreak")
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
            serialized = SerializationHelper.serialize_item(self.keep_with, "KeepWithPreviousEnum")
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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "BREAK":
                setattr(obj, "break_", ChapterEnumBreak.deserialize(child))
            elif tag == "KEEP-WITH":
                setattr(obj, "keep_with", KeepWithPreviousEnum.deserialize(child))

        return obj



class PaginateableBuilder(DocumentViewSelectableBuilder):
    """Builder for Paginateable with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: Paginateable = Paginateable()


    def with_break(self, value: Optional[ChapterEnumBreak]) -> "PaginateableBuilder":
        """Set break attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        setattr(self._obj, 'break', value)
        return self

    def with_keep_with(self, value: Optional[KeepWithPreviousEnum]) -> "PaginateableBuilder":
        """Set keep_with attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.keep_with = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "break",
        "keepWith",
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
    def build(self) -> Paginateable:
        """Build and return the Paginateable instance (abstract)."""
        raise NotImplementedError