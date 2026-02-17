"""TopicContentOrMsrQuery AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 342)

JSON Source: docs/json/packages/M2_MSR_Documentation_Chapters.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.MsrQuery.msr_query_p1 import (
    MsrQueryP1,
)
from armodel.models.M2.MSR.Documentation.Chapters.topic_content import (
    TopicContent,
)


class TopicContentOrMsrQuery(ARObject):
    """AUTOSAR TopicContentOrMsrQuery."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "msr_query_p1": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=MsrQueryP1,
        ),  # msrQueryP1
        "topic_content": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=TopicContent,
        ),  # topicContent
    }

    def __init__(self) -> None:
        """Initialize TopicContentOrMsrQuery."""
        super().__init__()
        self.msr_query_p1: MsrQueryP1 = None
        self.topic_content: TopicContent = None


class TopicContentOrMsrQueryBuilder:
    """Builder for TopicContentOrMsrQuery."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TopicContentOrMsrQuery = TopicContentOrMsrQuery()

    def build(self) -> TopicContentOrMsrQuery:
        """Build and return TopicContentOrMsrQuery object.

        Returns:
            TopicContentOrMsrQuery instance
        """
        # TODO: Add validation
        return self._obj
