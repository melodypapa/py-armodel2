"""DocumentationBlock AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 52)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 983)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 285)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 181)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.BlockElements.Figure.ml_figure import (
    MlFigure,
)
from armodel.models.M2.MSR.Documentation.BlockElements.Formula.ml_formula import (
    MlFormula,
)
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multi_language_verbatim import (
    MultiLanguageVerbatim,
)

if TYPE_CHECKING:
    from armodel.models.M2.MSR.Documentation.BlockElements.ListElements.def_list import (
        DefList,
    )
    from armodel.models.M2.MSR.Documentation.BlockElements.ListElements.labeled_list import (
        LabeledList,
    )
    from armodel.models.M2.MSR.Documentation.BlockElements.ListElements.list import (
        List,
    )
    from armodel.models.M2.MSR.Documentation.MsrQuery.msr_query_p2 import (
        MsrQueryP2,
    )
    from armodel.models.M2.MSR.Documentation.BlockElements.Note.note import (
        Note,
    )
    from armodel.models.M2.MSR.Documentation.BlockElements.RequirementsTracing.structured_req import (
        StructuredReq,
    )
    from armodel.models.M2.MSR.Documentation.BlockElements.RequirementsTracing.traceable_text import (
        TraceableText,
    )



class DocumentationBlock(ARObject):
    """AUTOSAR DocumentationBlock."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def_list: Optional[DefList]
    figure: Optional[MlFigure]
    formula: Optional[MlFormula]
    labeled_list_label: Optional[LabeledList]
    list: Optional[List]
    msr_query_p2: Optional[MsrQueryP2]
    note: Optional[Note]
    p: Optional[Any]
    structured_req: Optional[StructuredReq]
    trace: Optional[TraceableText]
    verbatim: Optional[MultiLanguageVerbatim]
    def __init__(self) -> None:
        """Initialize DocumentationBlock."""
        super().__init__()
        self.def_list: Optional[DefList] = None
        self.figure: Optional[MlFigure] = None
        self.formula: Optional[MlFormula] = None
        self.labeled_list_label: Optional[LabeledList] = None
        self.list: Optional[List] = None
        self.msr_query_p2: Optional[MsrQueryP2] = None
        self.note: Optional[Note] = None
        self.p: Optional[Any] = None
        self.structured_req: Optional[StructuredReq] = None
        self.trace: Optional[TraceableText] = None
        self.verbatim: Optional[MultiLanguageVerbatim] = None


class DocumentationBlockBuilder:
    """Builder for DocumentationBlock."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DocumentationBlock = DocumentationBlock()

    def build(self) -> DocumentationBlock:
        """Build and return DocumentationBlock object.

        Returns:
            DocumentationBlock instance
        """
        # TODO: Add validation
        return self._obj
