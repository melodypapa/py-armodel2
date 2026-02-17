"""Topic1 AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 338)

JSON Source: docs/json/packages/M2_MSR_Documentation_Chapters.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.MSR.Documentation.Chapters.topic_content_or_msr_query import (
    TopicContentOrMsrQuery,
)


class Topic1(Paginateable):
    """AUTOSAR Topic1."""

    def __init__(self) -> None:
        """Initialize Topic1."""
        super().__init__()
        self.help_entry: Optional[String] = None
        self.topic_content_or_msr: Optional[TopicContentOrMsrQuery] = None


class Topic1Builder:
    """Builder for Topic1."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Topic1 = Topic1()

    def build(self) -> Topic1:
        """Build and return Topic1 object.

        Returns:
            Topic1 instance
        """
        # TODO: Add validation
        return self._obj
