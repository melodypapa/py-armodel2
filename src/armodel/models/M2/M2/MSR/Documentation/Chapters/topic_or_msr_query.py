"""TopicOrMsrQuery AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 342)

JSON Source: docs/json/packages/M2_MSR_Documentation_Chapters.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.MsrQuery.msr_query_topic1 import (
    MsrQueryTopic1,
)
from armodel.models.M2.MSR.Documentation.Chapters.topic1 import (
    Topic1,
)


class TopicOrMsrQuery(ARObject):
    """AUTOSAR TopicOrMsrQuery."""

    def __init__(self) -> None:
        """Initialize TopicOrMsrQuery."""
        super().__init__()
        self.msr_query: MsrQueryTopic1 = None
        self.topic1: Topic1 = None


class TopicOrMsrQueryBuilder:
    """Builder for TopicOrMsrQuery."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TopicOrMsrQuery = TopicOrMsrQuery()

    def build(self) -> TopicOrMsrQuery:
        """Build and return TopicOrMsrQuery object.

        Returns:
            TopicOrMsrQuery instance
        """
        # TODO: Add validation
        return self._obj
