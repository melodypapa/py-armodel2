"""MsrQueryResultChapter AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 344)

JSON Source: docs/json/packages/M2_MSR_Documentation_MsrQuery.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject

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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "MsrQueryResultChapter":
        """Deserialize XML element to MsrQueryResultChapter object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MsrQueryResultChapter object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse chapters (list from container "CHAPTERS")
        obj.chapters = []
        container = ARObject._find_child_element(element, "CHAPTERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
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
