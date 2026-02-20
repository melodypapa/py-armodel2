"""DocumentationBlock AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 52)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 983)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 285)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 181)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.MSR.Documentation.BlockElements.Figure.ml_figure import (
    MlFigure,
)
from armodel.models.M2.MSR.Documentation.BlockElements.Formula.ml_formula import (
    MlFormula,
)
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multi_language_paragraph import (
    MultiLanguageParagraph,
)
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multi_language_verbatim import (
    MultiLanguageVerbatim,
)

if TYPE_CHECKING:
    from armodel.models.M2.MSR.Documentation.BlockElements.ListElements.ar_list import (
        ARList,
    )
    from armodel.models.M2.MSR.Documentation.BlockElements.ListElements.def_list import (
        DefList,
    )
    from armodel.models.M2.MSR.Documentation.BlockElements.ListElements.labeled_list import (
        LabeledList,
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

    def_list_ref: Optional[ARRef]
    figure: Optional[MlFigure]
    formula: Optional[MlFormula]
    labeled_list_label_ref: Optional[ARRef]
    msr_query_p2: Optional[MsrQueryP2]
    note: Optional[Note]
    p: Optional[MultiLanguageParagraph]
    list: Optional[ARList]
    structured_req: Optional[StructuredReq]
    trace: Optional[TraceableText]
    verbatim: Optional[MultiLanguageVerbatim]
    def __init__(self) -> None:
        """Initialize DocumentationBlock."""
        super().__init__()
        self.def_list_ref: Optional[ARRef] = None
        self.figure: Optional[MlFigure] = None
        self.formula: Optional[MlFormula] = None
        self.labeled_list_label_ref: Optional[ARRef] = None
        self.msr_query_p2: Optional[MsrQueryP2] = None
        self.note: Optional[Note] = None
        self.p: Optional[MultiLanguageParagraph] = None
        self.list: Optional[ARList] = None
        self.structured_req: Optional[StructuredReq] = None
        self.trace: Optional[TraceableText] = None
        self.verbatim: Optional[MultiLanguageVerbatim] = None

    def serialize(self) -> ET.Element:
        """Serialize DocumentationBlock to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize def_list_ref
        if self.def_list_ref is not None:
            serialized = ARObject._serialize_item(self.def_list_ref, "DefList")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DEF-LIST-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize figure
        if self.figure is not None:
            serialized = ARObject._serialize_item(self.figure, "MlFigure")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FIGURE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize formula
        if self.formula is not None:
            serialized = ARObject._serialize_item(self.formula, "MlFormula")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FORMULA")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize labeled_list_label_ref
        if self.labeled_list_label_ref is not None:
            serialized = ARObject._serialize_item(self.labeled_list_label_ref, "LabeledList")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LABELED-LIST-LABEL-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize msr_query_p2
        if self.msr_query_p2 is not None:
            serialized = ARObject._serialize_item(self.msr_query_p2, "MsrQueryP2")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MSR-QUERY-P2")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize note
        if self.note is not None:
            serialized = ARObject._serialize_item(self.note, "Note")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NOTE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize p
        if self.p is not None:
            serialized = ARObject._serialize_item(self.p, "MultiLanguageParagraph")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("P")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize list
        if self.list is not None:
            serialized = ARObject._serialize_item(self.list, "ARList")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LIST")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize structured_req
        if self.structured_req is not None:
            serialized = ARObject._serialize_item(self.structured_req, "StructuredReq")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("STRUCTURED-REQ")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize trace
        if self.trace is not None:
            serialized = ARObject._serialize_item(self.trace, "TraceableText")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TRACE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize verbatim
        if self.verbatim is not None:
            serialized = ARObject._serialize_item(self.verbatim, "MultiLanguageVerbatim")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VERBATIM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DocumentationBlock":
        """Deserialize XML element to DocumentationBlock object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DocumentationBlock object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse def_list_ref
        child = ARObject._find_child_element(element, "DEF-LIST-REF")
        if child is not None:
            def_list_ref_value = ARRef.deserialize(child)
            obj.def_list_ref = def_list_ref_value

        # Parse figure
        child = ARObject._find_child_element(element, "FIGURE")
        if child is not None:
            figure_value = ARObject._deserialize_by_tag(child, "MlFigure")
            obj.figure = figure_value

        # Parse formula
        child = ARObject._find_child_element(element, "FORMULA")
        if child is not None:
            formula_value = ARObject._deserialize_by_tag(child, "MlFormula")
            obj.formula = formula_value

        # Parse labeled_list_label_ref
        child = ARObject._find_child_element(element, "LABELED-LIST-LABEL-REF")
        if child is not None:
            labeled_list_label_ref_value = ARRef.deserialize(child)
            obj.labeled_list_label_ref = labeled_list_label_ref_value

        # Parse msr_query_p2
        child = ARObject._find_child_element(element, "MSR-QUERY-P2")
        if child is not None:
            msr_query_p2_value = ARObject._deserialize_by_tag(child, "MsrQueryP2")
            obj.msr_query_p2 = msr_query_p2_value

        # Parse note
        child = ARObject._find_child_element(element, "NOTE")
        if child is not None:
            note_value = ARObject._deserialize_by_tag(child, "Note")
            obj.note = note_value

        # Parse p
        child = ARObject._find_child_element(element, "P")
        if child is not None:
            p_value = ARObject._deserialize_with_type(child, "MultiLanguageParagraph")
            obj.p = p_value

        # Parse list
        child = ARObject._find_child_element(element, "LIST")
        if child is not None:
            list_value = ARObject._deserialize_by_tag(child, "ARList")
            obj.list = list_value

        # Parse structured_req
        child = ARObject._find_child_element(element, "STRUCTURED-REQ")
        if child is not None:
            structured_req_value = ARObject._deserialize_by_tag(child, "StructuredReq")
            obj.structured_req = structured_req_value

        # Parse trace
        child = ARObject._find_child_element(element, "TRACE")
        if child is not None:
            trace_value = ARObject._deserialize_by_tag(child, "TraceableText")
            obj.trace = trace_value

        # Parse verbatim
        child = ARObject._find_child_element(element, "VERBATIM")
        if child is not None:
            verbatim_value = ARObject._deserialize_with_type(child, "MultiLanguageVerbatim")
            obj.verbatim = verbatim_value

        return obj



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
