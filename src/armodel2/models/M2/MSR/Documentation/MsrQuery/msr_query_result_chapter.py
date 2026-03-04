"""MsrQueryResultChapter AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 344)

JSON Source: docs/json/packages/M2_MSR_Documentation_MsrQuery.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase

if TYPE_CHECKING:
    from armodel2.models.M2.MSR.Documentation.Chapters.chapter import (
        Chapter,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class MsrQueryResultChapter(ARObject):
    """AUTOSAR MsrQueryResultChapter."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "MSR-QUERY-RESULT-CHAPTER"


    chapters: list[Chapter]
    _DESERIALIZE_DISPATCH = {
        "CHAPTERS": lambda obj, elem: obj.chapters.append(SerializationHelper.deserialize_by_tag(elem, "Chapter")),
    }


    def __init__(self) -> None:
        """Initialize MsrQueryResultChapter."""
        super().__init__()
        self.chapters: list[Chapter] = []

    def serialize(self) -> ET.Element:
        """Serialize MsrQueryResultChapter to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(MsrQueryResultChapter, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize chapters (list to container "CHAPTERS")
        if self.chapters:
            wrapper = ET.Element("CHAPTERS")
            for item in self.chapters:
                serialized = SerializationHelper.serialize_item(item, "Chapter")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MsrQueryResultChapter":
        """Deserialize XML element to MsrQueryResultChapter object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MsrQueryResultChapter object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(MsrQueryResultChapter, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CHAPTERS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.chapters.append(SerializationHelper.deserialize_by_tag(item_elem, "Chapter"))

        return obj



class MsrQueryResultChapterBuilder(BuilderBase):
    """Builder for MsrQueryResultChapter with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: MsrQueryResultChapter = MsrQueryResultChapter()


    def with_chapters(self, items: list[Chapter]) -> "MsrQueryResultChapterBuilder":
        """Set chapters list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.chapters = list(items) if items else []
        return self


    def add_chapter(self, item: Chapter) -> "MsrQueryResultChapterBuilder":
        """Add a single item to chapters list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.chapters.append(item)
        return self

    def clear_chapters(self) -> "MsrQueryResultChapterBuilder":
        """Clear all items from chapters list.

        Returns:
            self for method chaining
        """
        self._obj.chapters = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "chapter",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> MsrQueryResultChapter:
        """Build and return the MsrQueryResultChapter instance with validation."""
        self._validate_instance()
        return self._obj