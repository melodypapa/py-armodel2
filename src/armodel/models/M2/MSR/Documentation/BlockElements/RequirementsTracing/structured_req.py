"""StructuredReq AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 168)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 49)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 313)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 208)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_RequirementsTracing.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.DocumentationOnM1 import (
    StandardNameEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    DateTime,
    String,
)
from armodel.models.M2.MSR.Documentation.BlockElements.RequirementsTracing.traceable import (
    Traceable,
)

if TYPE_CHECKING:
    from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
        DocumentationBlock,
    )



class StructuredReq(Paginateable):
    """AUTOSAR StructuredReq."""

    applies_tos: list[StandardNameEnum]
    conflicts: Optional[DocumentationBlock]
    date: DateTime
    dependencies: Optional[DocumentationBlock]
    description: Optional[DocumentationBlock]
    importance: String
    issued_by: String
    rationale: Optional[DocumentationBlock]
    remark: Optional[DocumentationBlock]
    supporting: Optional[DocumentationBlock]
    tested_items: list[Traceable]
    type: String
    use_case: Optional[DocumentationBlock]
    def __init__(self) -> None:
        """Initialize StructuredReq."""
        super().__init__()
        self.applies_tos: list[StandardNameEnum] = []
        self.conflicts: Optional[DocumentationBlock] = None
        self.date: DateTime = None
        self.dependencies: Optional[DocumentationBlock] = None
        self.description: Optional[DocumentationBlock] = None
        self.importance: String = None
        self.issued_by: String = None
        self.rationale: Optional[DocumentationBlock] = None
        self.remark: Optional[DocumentationBlock] = None
        self.supporting: Optional[DocumentationBlock] = None
        self.tested_items: list[Traceable] = []
        self.type: String = None
        self.use_case: Optional[DocumentationBlock] = None


class StructuredReqBuilder:
    """Builder for StructuredReq."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: StructuredReq = StructuredReq()

    def build(self) -> StructuredReq:
        """Build and return StructuredReq object.

        Returns:
            StructuredReq instance
        """
        # TODO: Add validation
        return self._obj
