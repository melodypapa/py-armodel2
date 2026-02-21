"""MsrQueryResultChapter AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 344)

JSON Source: docs/json/packages/M2_MSR_Documentation_MsrQuery.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper

if TYPE_CHECKING:
    from armodel.models.M2.MSR.Documentation.Chapters.chapter import (
        Chapter,
    )



class MsrQueryResultChapter(ARObject):
    """AUTOSAR MsrQueryResultChapter."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    chapters: list[Chapter]
    def __init__(self) -> None:
        """Initialize MsrQueryResultChapter."""
        super().__init__()
        self.chapters: list[Chapter] = []

    def serialize(self) -> ET.Element:
        """Serialize MsrQueryResultChapter to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

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

        # Parse chapters (list from container "CHAPTERS")
        obj.chapters = []
        container = SerializationHelper.find_child_element(element, "CHAPTERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.chapters.append(child_value)

        return obj



class MsrQueryResultChapterBuilder:
    """Builder for MsrQueryResultChapter."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MsrQueryResultChapter = MsrQueryResultChapter()

    def build(self) -> MsrQueryResultChapter:
        """Build and return MsrQueryResultChapter object.

        Returns:
            MsrQueryResultChapter instance
        """
        # TODO: Add validation
        return self._obj
