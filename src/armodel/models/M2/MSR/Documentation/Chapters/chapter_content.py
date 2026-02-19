"""ChapterContent AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 330)

JSON Source: docs/json/packages/M2_MSR_Documentation_Chapters.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.BlockElements.GerneralParameters.prms import (
    Prms,
)
from armodel.models.M2.MSR.Documentation.Chapters.topic_content_or_msr_query import (
    TopicContentOrMsrQuery,
)


class ChapterContent(ARObject):
    """AUTOSAR ChapterContent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    prms: Prms
    topic_content_or_msr: Optional[TopicContentOrMsrQuery]
    def __init__(self) -> None:
        """Initialize ChapterContent."""
        super().__init__()
        self.prms: Prms = None
        self.topic_content_or_msr: Optional[TopicContentOrMsrQuery] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ChapterContent":
        """Deserialize XML element to ChapterContent object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ChapterContent object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse prms
        child = ARObject._find_child_element(element, "PRMS")
        if child is not None:
            prms_value = ARObject._deserialize_by_tag(child, "Prms")
            obj.prms = prms_value

        # Parse topic_content_or_msr
        child = ARObject._find_child_element(element, "TOPIC-CONTENT-OR-MSR")
        if child is not None:
            topic_content_or_msr_value = ARObject._deserialize_by_tag(child, "TopicContentOrMsrQuery")
            obj.topic_content_or_msr = topic_content_or_msr_value

        return obj



class ChapterContentBuilder:
    """Builder for ChapterContent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ChapterContent = ChapterContent()

    def build(self) -> ChapterContent:
        """Build and return ChapterContent object.

        Returns:
            ChapterContent instance
        """
        # TODO: Add validation
        return self._obj
