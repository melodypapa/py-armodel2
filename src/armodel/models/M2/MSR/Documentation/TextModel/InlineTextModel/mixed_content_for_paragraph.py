"""MixedContentForParagraph AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 289)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_InlineTextModel.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements import (
    Superscript,
)
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements.br import (
    Br,
)
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements.emphasis_text import (
    EmphasisText,
)
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements.index_entry import (
    IndexEntry,
)
from armodel.models.M2.MSR.Documentation.TextModel.SingleLanguageData.sl_paragraph import (
    SlParagraph,
)
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements.std import (
    Std,
)
from armodel.models.M2.MSR.Documentation.BlockElements.RequirementsTracing.traceable import (
    Traceable,
)
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements.tt import (
    Tt,
)
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements.xdoc import (
    Xdoc,
)
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements.xfile import (
    Xfile,
)
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements.xref import (
    Xref,
)
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements.xref_target import (
    XrefTarget,
)
from abc import ABC, abstractmethod


class MixedContentForParagraph(ARObject, ABC):
    """AUTOSAR MixedContentForParagraph."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    br: Br
    e: EmphasisText
    ft: SlParagraph
    ie: IndexEntry
    std: Std
    sub: Superscript
    sup: Superscript
    trace_ref: ARRef
    tt: Tt
    xdoc: Xdoc
    xfile: Xfile
    xref: Xref
    xref_target: XrefTarget
    def __init__(self) -> None:
        """Initialize MixedContentForParagraph."""
        super().__init__()
        self.br: Br = None
        self.e: EmphasisText = None
        self.ft: SlParagraph = None
        self.ie: IndexEntry = None
        self.std: Std = None
        self.sub: Superscript = None
        self.sup: Superscript = None
        self.trace_ref: ARRef = None
        self.tt: Tt = None
        self.xdoc: Xdoc = None
        self.xfile: Xfile = None
        self.xref: Xref = None
        self.xref_target: XrefTarget = None

    def serialize(self) -> ET.Element:
        """Serialize MixedContentForParagraph to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize br
        if self.br is not None:
            serialized = ARObject._serialize_item(self.br, "Br")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize e
        if self.e is not None:
            serialized = ARObject._serialize_item(self.e, "EmphasisText")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("E")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ft
        if self.ft is not None:
            serialized = ARObject._serialize_item(self.ft, "SlParagraph")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ie
        if self.ie is not None:
            serialized = ARObject._serialize_item(self.ie, "IndexEntry")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize std
        if self.std is not None:
            serialized = ARObject._serialize_item(self.std, "Std")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("STD")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sub
        if self.sub is not None:
            serialized = ARObject._serialize_item(self.sub, "Superscript")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SUB")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sup
        if self.sup is not None:
            serialized = ARObject._serialize_item(self.sup, "Superscript")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SUP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize trace_ref
        if self.trace_ref is not None:
            serialized = ARObject._serialize_item(self.trace_ref, "Traceable")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TRACE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tt
        if self.tt is not None:
            serialized = ARObject._serialize_item(self.tt, "Tt")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize xdoc
        if self.xdoc is not None:
            serialized = ARObject._serialize_item(self.xdoc, "Xdoc")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("XDOC")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize xfile
        if self.xfile is not None:
            serialized = ARObject._serialize_item(self.xfile, "Xfile")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("XFILE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize xref
        if self.xref is not None:
            serialized = ARObject._serialize_item(self.xref, "Xref")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("XREF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize xref_target
        if self.xref_target is not None:
            serialized = ARObject._serialize_item(self.xref_target, "XrefTarget")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("XREF-TARGET")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MixedContentForParagraph":
        """Deserialize XML element to MixedContentForParagraph object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MixedContentForParagraph object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse br
        child = ARObject._find_child_element(element, "BR")
        if child is not None:
            br_value = ARObject._deserialize_by_tag(child, "Br")
            obj.br = br_value

        # Parse e
        child = ARObject._find_child_element(element, "E")
        if child is not None:
            e_value = ARObject._deserialize_by_tag(child, "EmphasisText")
            obj.e = e_value

        # Parse ft
        child = ARObject._find_child_element(element, "FT")
        if child is not None:
            ft_value = ARObject._deserialize_by_tag(child, "SlParagraph")
            obj.ft = ft_value

        # Parse ie
        child = ARObject._find_child_element(element, "IE")
        if child is not None:
            ie_value = ARObject._deserialize_by_tag(child, "IndexEntry")
            obj.ie = ie_value

        # Parse std
        child = ARObject._find_child_element(element, "STD")
        if child is not None:
            std_value = ARObject._deserialize_by_tag(child, "Std")
            obj.std = std_value

        # Parse sub
        child = ARObject._find_child_element(element, "SUB")
        if child is not None:
            sub_value = child.text
            obj.sub = sub_value

        # Parse sup
        child = ARObject._find_child_element(element, "SUP")
        if child is not None:
            sup_value = child.text
            obj.sup = sup_value

        # Parse trace_ref
        child = ARObject._find_child_element(element, "TRACE-REF")
        if child is not None:
            trace_ref_value = ARRef.deserialize(child)
            obj.trace_ref = trace_ref_value

        # Parse tt
        child = ARObject._find_child_element(element, "TT")
        if child is not None:
            tt_value = ARObject._deserialize_by_tag(child, "Tt")
            obj.tt = tt_value

        # Parse xdoc
        child = ARObject._find_child_element(element, "XDOC")
        if child is not None:
            xdoc_value = ARObject._deserialize_by_tag(child, "Xdoc")
            obj.xdoc = xdoc_value

        # Parse xfile
        child = ARObject._find_child_element(element, "XFILE")
        if child is not None:
            xfile_value = ARObject._deserialize_by_tag(child, "Xfile")
            obj.xfile = xfile_value

        # Parse xref
        child = ARObject._find_child_element(element, "XREF")
        if child is not None:
            xref_value = ARObject._deserialize_by_tag(child, "Xref")
            obj.xref = xref_value

        # Parse xref_target
        child = ARObject._find_child_element(element, "XREF-TARGET")
        if child is not None:
            xref_target_value = ARObject._deserialize_by_tag(child, "XrefTarget")
            obj.xref_target = xref_target_value

        return obj



class MixedContentForParagraphBuilder:
    """Builder for MixedContentForParagraph."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MixedContentForParagraph = MixedContentForParagraph()

    def build(self) -> MixedContentForParagraph:
        """Build and return MixedContentForParagraph object.

        Returns:
            MixedContentForParagraph instance
        """
        # TODO: Add validation
        return self._obj
