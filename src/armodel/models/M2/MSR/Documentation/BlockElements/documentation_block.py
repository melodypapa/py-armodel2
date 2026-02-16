"""DocumentationBlock AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.BlockElements.ListElements.def_list import (
    DefList,
)
from armodel.models.M2.MSR.Documentation.BlockElements.ListElements.labeled_list import (
    LabeledList,
)
from armodel.models.M2.MSR.Documentation.BlockElements.ListElements.list import (
    List,
)
from armodel.models.M2.MSR.Documentation.BlockElements.Figure.ml_figure import (
    MlFigure,
)
from armodel.models.M2.MSR.Documentation.BlockElements.Formula.ml_formula import (
    MlFormula,
)
from armodel.models.M2.MSR.Documentation.MsrQuery.msr_query_p2 import (
    MsrQueryP2,
)
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multi_language_verbatim import (
    MultiLanguageVerbatim,
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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("def_list", None, False, False, DefList),  # defList
        ("figure", None, False, False, MlFigure),  # figure
        ("formula", None, False, False, MlFormula),  # formula
        ("labeled_list_label", None, False, False, LabeledList),  # labeledListLabel
        ("list", None, False, False, List),  # list
        ("msr_query_p2", None, False, False, MsrQueryP2),  # msrQueryP2
        ("note", None, False, False, Note),  # note
        ("p", None, False, False, any (MultiLanguage)),  # p
        ("structured_req", None, False, False, StructuredReq),  # structuredReq
        ("trace", None, False, False, TraceableText),  # trace
        ("verbatim", None, False, False, MultiLanguageVerbatim),  # verbatim
    ]

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

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DocumentationBlock to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DocumentationBlock":
        """Create DocumentationBlock from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DocumentationBlock instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DocumentationBlock since parent returns ARObject
        return cast("DocumentationBlock", obj)


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
