"""MsrQueryChapter AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 343)

JSON Source: docs/json/packages/M2_MSR_Documentation_MsrQuery.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel.models.M2.MSR.Documentation.MsrQuery.msr_query_props import (
    MsrQueryProps,
)

if TYPE_CHECKING:
    from armodel.models.M2.MSR.Documentation.MsrQuery.msr_query_result_chapter import (
        MsrQueryResultChapter,
    )



class MsrQueryChapter(Paginateable):
    """AUTOSAR MsrQueryChapter."""

    def __init__(self) -> None:
        """Initialize MsrQueryChapter."""
        super().__init__()
        self.msr_query_props: MsrQueryProps = None
        self.msr_query_result_chapter: Optional[MsrQueryResultChapter] = None


class MsrQueryChapterBuilder:
    """Builder for MsrQueryChapter."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MsrQueryChapter = MsrQueryChapter()

    def build(self) -> MsrQueryChapter:
        """Build and return MsrQueryChapter object.

        Returns:
            MsrQueryChapter instance
        """
        # TODO: Add validation
        return self._obj
