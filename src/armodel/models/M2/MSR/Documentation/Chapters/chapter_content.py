"""ChapterContent AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 330)

JSON Source: docs/json/packages/M2_MSR_Documentation_Chapters.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.BlockElements.GerneralParameters.prms import (
    Prms,
)
from armodel.models.M2.MSR.Documentation.Chapters.topic_content_or_msr_query import (
    TopicContentOrMsrQuery,
)


class ChapterContent(ARObject):
    """AUTOSAR ChapterContent."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "prms": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=Prms,
        ),  # prms
        "topic_content_or_msr": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=TopicContentOrMsrQuery,
        ),  # topicContentOrMsr
    }

    def __init__(self) -> None:
        """Initialize ChapterContent."""
        super().__init__()
        self.prms: Prms = None
        self.topic_content_or_msr: Optional[TopicContentOrMsrQuery] = None


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
