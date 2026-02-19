"""MlFigure AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 307)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_Figure.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable import (
    FrameEnum,
    PgwideEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.MSR.Documentation.BlockElements.caption import (
    Caption,
)
from armodel.models.M2.MSR.Documentation.BlockElements.Figure.l_graphic import (
    LGraphic,
)
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multi_language_verbatim import (
    MultiLanguageVerbatim,
)


class MlFigure(Paginateable):
    """AUTOSAR MlFigure."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    figure_caption: Optional[Caption]
    frame: Optional[FrameEnum]
    help_entry: Optional[String]
    l_graphics: list[LGraphic]
    pgwide: Optional[PgwideEnum]
    verbatim: Optional[MultiLanguageVerbatim]
    def __init__(self) -> None:
        """Initialize MlFigure."""
        super().__init__()
        self.figure_caption: Optional[Caption] = None
        self.frame: Optional[FrameEnum] = None
        self.help_entry: Optional[String] = None
        self.l_graphics: list[LGraphic] = []
        self.pgwide: Optional[PgwideEnum] = None
        self.verbatim: Optional[MultiLanguageVerbatim] = None
    def serialize(self) -> ET.Element:
        """Serialize MlFigure to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(MlFigure, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize figure_caption
        if self.figure_caption is not None:
            serialized = ARObject._serialize_item(self.figure_caption, "Caption")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FIGURE-CAPTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize frame
        if self.frame is not None:
            serialized = ARObject._serialize_item(self.frame, "FrameEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FRAME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize help_entry
        if self.help_entry is not None:
            serialized = ARObject._serialize_item(self.help_entry, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HELP-ENTRY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize l_graphics (list to container "L-GRAPHICS")
        if self.l_graphics:
            wrapper = ET.Element("L-GRAPHICS")
            for item in self.l_graphics:
                serialized = ARObject._serialize_item(item, "LGraphic")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize pgwide
        if self.pgwide is not None:
            serialized = ARObject._serialize_item(self.pgwide, "PgwideEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PGWIDE")
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
    def deserialize(cls, element: ET.Element) -> "MlFigure":
        """Deserialize XML element to MlFigure object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MlFigure object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(MlFigure, cls).deserialize(element)

        # Parse figure_caption
        child = ARObject._find_child_element(element, "FIGURE-CAPTION")
        if child is not None:
            figure_caption_value = ARObject._deserialize_by_tag(child, "Caption")
            obj.figure_caption = figure_caption_value

        # Parse frame
        child = ARObject._find_child_element(element, "FRAME")
        if child is not None:
            frame_value = FrameEnum.deserialize(child)
            obj.frame = frame_value

        # Parse help_entry
        child = ARObject._find_child_element(element, "HELP-ENTRY")
        if child is not None:
            help_entry_value = child.text
            obj.help_entry = help_entry_value

        # Parse l_graphics (list from container "L-GRAPHICS")
        obj.l_graphics = []
        container = ARObject._find_child_element(element, "L-GRAPHICS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.l_graphics.append(child_value)

        # Parse pgwide
        child = ARObject._find_child_element(element, "PGWIDE")
        if child is not None:
            pgwide_value = PgwideEnum.deserialize(child)
            obj.pgwide = pgwide_value

        # Parse verbatim
        child = ARObject._find_child_element(element, "VERBATIM")
        if child is not None:
            verbatim_value = ARObject._deserialize_by_tag(child, "MultiLanguageVerbatim")
            obj.verbatim = verbatim_value

        return obj



class MlFigureBuilder:
    """Builder for MlFigure."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MlFigure = MlFigure()

    def build(self) -> MlFigure:
        """Build and return MlFigure object.

        Returns:
            MlFigure instance
        """
        # TODO: Add validation
        return self._obj
