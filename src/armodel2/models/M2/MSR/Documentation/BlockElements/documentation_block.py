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

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.MSR.Documentation.BlockElements.Figure.ml_figure import MlFigure
from armodel2.models.M2.MSR.Documentation.BlockElements.Formula.ml_formula import MlFormula
from armodel2.models.M2.MSR.Documentation.TextModel.MultilanguageData.multi_language_paragraph import (
    MultiLanguageParagraph,
)
from armodel2.models.M2.MSR.Documentation.TextModel.MultilanguageData.multi_language_verbatim import (
    MultiLanguageVerbatim,
)
from armodel2.serialization import SerializationHelper

if TYPE_CHECKING:
    from armodel2.models.M2.MSR.Documentation.BlockElements.ListElements.ar_list import ARList
    from armodel2.models.M2.MSR.Documentation.BlockElements.ListElements.def_list import DefList
    from armodel2.models.M2.MSR.Documentation.BlockElements.ListElements.labeled_list import (
        LabeledList,
    )
    from armodel2.models.M2.MSR.Documentation.MsrQuery.msr_query_p2 import MsrQueryP2
    from armodel2.models.M2.MSR.Documentation.BlockElements.Note.note import Note
    from armodel2.models.M2.MSR.Documentation.BlockElements.RequirementsTracing.structured_req import (
        StructuredReq,
    )
    from armodel2.models.M2.MSR.Documentation.BlockElements.RequirementsTracing.traceable_text import (
        TraceableText,
    )


class DocumentationBlock(ARObject):
    """AUTOSAR DocumentationBlock."""

    _XML_TAG = "DOCUMENTATION-BLOCK"

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
        elem = ET.Element(self._XML_TAG)

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

    _DESERIALIZE_DISPATCH = {
        "DEF-LIST-REF": lambda obj, elem: setattr(obj, 'def_list_ref', ARRef.deserialize(elem)),
        "FIGURE": lambda obj, elem: obj.figure.append(
            SerializationHelper.deserialize_by_tag(elem, "MlFigure")
        ),
        "FORMULA": lambda obj, elem: setattr(
            obj, 'formula', SerializationHelper.deserialize_by_tag(elem, "MlFormula")
        ),
        "LABELED-LIST-LABEL-REF": lambda obj, elem: setattr(
            obj, 'labeled_list_label_ref', ARRef.deserialize(elem)
        ),
        "MSR-QUERY-P2": lambda obj, elem: setattr(
            obj, 'msr_query_p2', SerializationHelper.deserialize_by_tag(elem, "MsrQueryP2")
        ),
        "NOTE": lambda obj, elem: setattr(
            obj, 'note', SerializationHelper.deserialize_by_tag(elem, "Note")
        ),
        "P": lambda obj, elem: setattr(obj, 'p', DocumentationBlock._deserialize_p(elem)),
        "LIST": lambda obj, elem: obj.list.append(
            SerializationHelper.deserialize_by_tag(elem, "ARList")
        ),
        "STRUCTURED-REQ": lambda obj, elem: setattr(
            obj, 'structured_req', SerializationHelper.deserialize_by_tag(elem, "StructuredReq")
        ),
        "TRACE": lambda obj, elem: setattr(
            obj, 'trace', SerializationHelper.deserialize_by_tag(elem, "TraceableText")
        ),
        "VERBATIM": lambda obj, elem: setattr(
            obj, 'verbatim', DocumentationBlock._deserialize_verbatim(elem)
        ),
    }

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DocumentationBlock":
        """Deserialize XML element to DocumentationBlock object.

        Uses static dispatch table for O(1) tag-to-handler lookup.
        Calls super().deserialize() first to handle inherited attributes from ARObject.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DocumentationBlock object
        """
        # First, deserialize inherited attributes from ARObject (checksum, timestamp)
        obj = super(DocumentationBlock, cls).deserialize(element)

        # Then process DocumentationBlock-specific elements with dispatch table
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            handler = cls._DESERIALIZE_DISPATCH.get(tag)
            if handler is not None:
                handler(obj, child)

        return obj

    @staticmethod
    def _deserialize_p(element: ET.Element) -> Optional[MultiLanguageParagraph]:
        """Deserialize P element with L-1 children."""
        from armodel2.models.M2.MSR.Documentation.TextModel.LanguageDataModel.l_paragraph import LParagraph

        p_value = MultiLanguageParagraph()
        for l1_child in element:
            if SerializationHelper.strip_namespace(l1_child.tag) == "L-1":
                lp = LParagraph.deserialize(l1_child)
                p_value._l1.append(lp)
        return p_value if len(p_value._l1) > 0 else None

    @staticmethod
    def _deserialize_verbatim(element: ET.Element) -> Optional[MultiLanguageVerbatim]:
        """Deserialize VERBATIM element with L-1 children."""
        from armodel2.models.M2.MSR.Documentation.TextModel.LanguageDataModel.l_paragraph import LParagraph

        verbatim_value = MultiLanguageVerbatim()
        for l1_child in element:
            if SerializationHelper.strip_namespace(l1_child.tag) == "L-1":
                lp = LParagraph.deserialize(l1_child)
                verbatim_value._l1.append(lp)
        return verbatim_value if len(verbatim_value._l1) > 0 else None


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
        return self._obj