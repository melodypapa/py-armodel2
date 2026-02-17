"""TraceableText AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 178)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 313)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 222)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_RequirementsTracing.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)

if TYPE_CHECKING:
    from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
        DocumentationBlock,
    )



class TraceableText(Paginateable):
    """AUTOSAR TraceableText."""

    def __init__(self) -> None:
        """Initialize TraceableText."""
        super().__init__()
        self.text: DocumentationBlock = None


class TraceableTextBuilder:
    """Builder for TraceableText."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TraceableText = TraceableText()

    def build(self) -> TraceableText:
        """Build and return TraceableText object.

        Returns:
            TraceableText instance
        """
        # TODO: Add validation
        return self._obj
