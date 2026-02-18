"""TopicContent AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 478)

JSON Source: docs/json/packages/M2_MSR_Documentation_Chapters.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)
from armodel.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable.table import (
    Table,
)


class TopicContent(ARObject):
    """AUTOSAR TopicContent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    block_level: DocumentationBlock
    table: Optional[Table]
    traceable_table: Any
    def __init__(self) -> None:
        """Initialize TopicContent."""
        super().__init__()
        self.block_level: DocumentationBlock = None
        self.table: Optional[Table] = None
        self.traceable_table: Any = None


class TopicContentBuilder:
    """Builder for TopicContent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TopicContent = TopicContent()

    def build(self) -> TopicContent:
        """Build and return TopicContent object.

        Returns:
            TopicContent instance
        """
        # TODO: Add validation
        return self._obj
