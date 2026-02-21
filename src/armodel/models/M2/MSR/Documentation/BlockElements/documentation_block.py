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
from armodel.models.M2.MSR.Documentation.BlockElements.Figure.ml_figure import MlFigure
from armodel.models.M2.MSR.Documentation.BlockElements.Formula.ml_formula import MlFormula
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multi_language_paragraph import (
    MultiLanguageParagraph,
)
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multi_language_verbatim import (
    MultiLanguageVerbatim,
)
from armodel.serialization import SerializationHelper

if TYPE_CHECKING:
    from armodel.models.M2.MSR.Documentation.BlockElements.ListElements.ar_list import ARList
    from armodel.models.M2.MSR.Documentation.BlockElements.ListElements.def_list import DefList
    from armodel.models.M2.MSR.Documentation.BlockElements.ListElements.labeled_list import (
        LabeledList,
    )
    from armodel.models.M2.MSR.Documentation.MsrQuery.msr_query_p2 import MsrQueryP2
    from armodel.models.M2.MSR.Documentation.BlockElements.Note.note import Note
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
    figure: list[MlFigure]
    formula: Optional[MlFormula]
    labeled_list_label_ref: Optional[ARRef]
    msr_query_p2: Optional[MsrQueryP2]
    note: Optional[Note]
    p: Optional[MultiLanguageParagraph]
    list: list[ARList]
    structured_req: Optional[StructuredReq]
    trace: Optional[TraceableText]
    verbatim: Optional[MultiLanguageVerbatim]

    def __init__(self) -> None:
        """Initialize DocumentationBlock."""
        super().__init__()
        self.def_list_ref: Optional[ARRef] = None
        self.figure: list[MlFigure] = []
        self.formula: Optional[MlFormula] = None
        self.labeled_list_label_ref: Optional[ARRef] = None
        self.msr_query_p2: Optional[MsrQueryP2] = None
        self.note: Optional[Note] = None
        self.p: Optional[MultiLanguageParagraph] = None
        self.list: list[ARList] = []
        self.structured_req: Optional[StructuredReq] = None
        self.trace: Optional[TraceableText] = None
        self.verbatim: Optional[MultiLanguageVerbatim] = None

    def serialize(self) -> ET.Element:
        """Serialize DocumentationBlock to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # Call parent's serialize to handle inherited attributes (checksum, timestamp)
        parent_elem = super().serialize()
        elem.attrib.update(parent_elem.attrib)
        for child in parent_elem:
            elem.append(child)

        # Serialize def_list_ref
        if self.def_list_ref is not None:
            serialized = SerializationHelper.serialize_item(self.def_list_ref, "DefList")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DEF-LIST-REF")
                if hasattr(serialized, "attrib"):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize figure (list)
        for figure_item in self.figure:
            serialized = SerializationHelper.serialize_item(figure_item, "MlFigure")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FIGURE")
                if hasattr(serialized, "attrib"):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize formula
        if self.formula is not None:
            serialized = SerializationHelper.serialize_item(self.formula, "MlFormula")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FORMULA")
                if hasattr(serialized, "attrib"):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize labeled_list_label_ref
        if self.labeled_list_label_ref is not None:
            serialized = SerializationHelper.serialize_item(
                self.labeled_list_label_ref, "LabeledList"
            )
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LABELED-LIST-LABEL-REF")
                if hasattr(serialized, "attrib"):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize msr_query_p2
        if self.msr_query_p2 is not None:
            serialized = SerializationHelper.serialize_item(self.msr_query_p2, "MsrQueryP2")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MSR-QUERY-P2")
                if hasattr(serialized, "attrib"):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize note
        if self.note is not None:
            serialized = SerializationHelper.serialize_item(self.note, "Note")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NOTE")
                if hasattr(serialized, "attrib"):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize p - Special handling for MultiLanguageParagraph
        # The P element should contain L-1 elements directly as children
        if self.p is not None:
            # Create P element
            wrapped = ET.Element("P")
            # Serialize each LParagraph in the l1 list directly
            # This ensures L-1 elements are direct children of P
            if hasattr(self.p, "_l1") and self.p._l1:
                for lp in self.p._l1:
                    if lp is not None:
                        # Serialize the LParagraph
                        serialized_lp = lp.serialize()
                        # Wrap it in L-1 tag with L attribute
                        l1_elem = ET.Element("L-1")
                        # Copy attributes (L attribute)
                        if hasattr(serialized_lp, "attrib"):
                            l1_elem.attrib.update(serialized_lp.attrib)
                        # Copy text content
                        if serialized_lp.text:
                            l1_elem.text = serialized_lp.text
                        # Copy children
                        for child in serialized_lp:
                            l1_elem.append(child)
                        wrapped.append(l1_elem)
            elem.append(wrapped)

        # Serialize list
        if self.list:
            for ar_list_item in self.list:
                serialized = SerializationHelper.serialize_item(ar_list_item, "ARList")
                if serialized is not None:
                    # Wrap with correct tag
                    wrapped = ET.Element("LIST")
                    if hasattr(serialized, "attrib"):
                        wrapped.attrib.update(serialized.attrib)
                        if serialized.text:
                            wrapped.text = serialized.text
                    for child in serialized:
                        wrapped.append(child)
                    elem.append(wrapped)

        # Serialize structured_req
        if self.structured_req is not None:
            serialized = SerializationHelper.serialize_item(
                self.structured_req, "StructuredReq"
            )
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("STRUCTURED-REQ")
                if hasattr(serialized, "attrib"):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize trace
        if self.trace is not None:
            serialized = SerializationHelper.serialize_item(self.trace, "TraceableText")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TRACE")
                if hasattr(serialized, "attrib"):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize verbatim - Special handling for MultiLanguageVerbatim
        # Similar to p, VERBATIM should contain L-1 elements directly as children
        if self.verbatim is not None:
            # Create VERBATIM element
            wrapped = ET.Element("VERBATIM")
            # Serialize each LParagraph in the l1 list directly
            # This ensures L-1 elements are direct children of VERBATIM
            if hasattr(self.verbatim, "_l1") and self.verbatim._l1:
                for lp in self.verbatim._l1:
                    if lp is not None:
                        # Serialize the LParagraph
                        serialized_lp = lp.serialize()
                        # Wrap it in L-1 tag with L attribute
                        l1_elem = ET.Element("L-1")
                        # Copy attributes (L attribute)
                        if hasattr(serialized_lp, "attrib"):
                            l1_elem.attrib.update(serialized_lp.attrib)
                        # Copy text content
                        if serialized_lp.text:
                            l1_elem.text = serialized_lp.text
                        # Copy children
                        for child in serialized_lp:
                            l1_elem.append(child)
                        wrapped.append(l1_elem)
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
        # Call parent's deserialize first to handle inherited attributes (checksum, timestamp)
        obj = super().deserialize(element)

        # Parse def_list_ref
        child = SerializationHelper.find_child_element(element, "DEF-LIST-REF")
        if child is not None:
            def_list_ref_value = ARRef.deserialize(child)
            obj.def_list_ref = def_list_ref_value

        # Parse figure (list)
        obj.figure = []
        for child in SerializationHelper.find_all_child_elements(element, "FIGURE"):
            figure_value = SerializationHelper.deserialize_by_tag(child, "MlFigure")
            obj.figure.append(figure_value)

        # Parse formula
        child = SerializationHelper.find_child_element(element, "FORMULA")
        if child is not None:
            formula_value = SerializationHelper.deserialize_by_tag(child, "MlFormula")
            obj.formula = formula_value

        # Parse labeled_list_label_ref
        child = SerializationHelper.find_child_element(element, "LABELED-LIST-LABEL-REF")
        if child is not None:
            labeled_list_label_ref_value = ARRef.deserialize(child)
            obj.labeled_list_label_ref = labeled_list_label_ref_value

        # Parse msr_query_p2
        child = SerializationHelper.find_child_element(element, "MSR-QUERY-P2")
        if child is not None:
            msr_query_p2_value = SerializationHelper.deserialize_by_tag(child, "MsrQueryP2")
            obj.msr_query_p2 = msr_query_p2_value

        # Parse note
        child = SerializationHelper.find_child_element(element, "NOTE")
        if child is not None:
            note_value = SerializationHelper.deserialize_by_tag(child, "Note")
            obj.note = note_value

        # Parse p - Special handling for MultiLanguageParagraph
        # The P element contains L-1 elements directly as children
        child = SerializationHelper.find_child_element(element, "P")
        if child is not None:
            # Create a MultiLanguageParagraph
            p_value = MultiLanguageParagraph()
            # Find all L-1 children and deserialize them as LParagraph
            from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel.l_paragraph import (
                LParagraph,
            )

            for l1_child in child:
                if SerializationHelper.strip_namespace(l1_child.tag) == "L-1":
                    # Deserialize L-1 as LParagraph
                    lp = LParagraph.deserialize(l1_child)
                    p_value._l1.append(lp)
            obj.p = p_value

        # Parse list
        for child in SerializationHelper.find_all_child_elements(element, "LIST"):
            list_value = SerializationHelper.deserialize_by_tag(child, "ARList")
            if list_value is not None:
                obj.list.append(list_value)

        # Parse structured_req
        child = SerializationHelper.find_child_element(element, "STRUCTURED-REQ")
        if child is not None:
            structured_req_value = SerializationHelper.deserialize_by_tag(child, "StructuredReq")
            obj.structured_req = structured_req_value

        # Parse trace
        child = SerializationHelper.find_child_element(element, "TRACE")
        if child is not None:
            trace_value = SerializationHelper.deserialize_by_tag(child, "TraceableText")
            obj.trace = trace_value

        # Parse verbatim - Special handling for MultiLanguageVerbatim
        # The VERBATIM element contains L-1 elements directly as children
        child = SerializationHelper.find_child_element(element, "VERBATIM")
        if child is not None:
            # Create a MultiLanguageVerbatim
            verbatim_value = MultiLanguageVerbatim()
            # Find all L-1 children and deserialize them as LParagraph
            from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel.l_paragraph import (
                LParagraph,
            )

            for l1_child in child:
                if SerializationHelper.strip_namespace(l1_child.tag) == "L-1":
                    # Deserialize L-1 as LParagraph
                    lp = LParagraph.deserialize(l1_child)
                    verbatim_value._l1.append(lp)
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