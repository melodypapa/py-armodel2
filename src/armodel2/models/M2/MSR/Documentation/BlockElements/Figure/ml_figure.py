"""MlFigure AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 307)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_Figure.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel2.serialization.decorators import lang_prefix

from armodel2.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import PaginateableBuilder
from armodel2.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable import (
    FrameEnum,
    PgwideEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel2.models.M2.MSR.Documentation.BlockElements.caption import (
    Caption,
)
from armodel2.models.M2.MSR.Documentation.BlockElements.Figure.l_graphic import (
    LGraphic,
)
from armodel2.models.M2.MSR.Documentation.TextModel.MultilanguageData.multi_language_verbatim import (
    MultiLanguageVerbatim,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class MlFigure(Paginateable):
    """AUTOSAR MlFigure."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "ML-FIGURE"


    figure_caption: Optional[Caption]
    frame: Optional[FrameEnum]
    help_entry: Optional[String]
    _l_graphics: list[LGraphic]
    pgwide: Optional[PgwideEnum]
    verbatim: Optional[MultiLanguageVerbatim]
    _DESERIALIZE_DISPATCH = {
        "FIGURE-CAPTION": lambda obj, elem: setattr(obj, "figure_caption", SerializationHelper.deserialize_by_tag(elem, "Caption")),
        "FRAME": lambda obj, elem: setattr(obj, "frame", FrameEnum.deserialize(elem)),
        "HELP-ENTRY": lambda obj, elem: setattr(obj, "help_entry", SerializationHelper.deserialize_by_tag(elem, "String")),
        "L-GRAPHICS": lambda obj, elem: obj._l_graphics.append(SerializationHelper.deserialize_by_tag(elem, "LGraphic")),
        "PGWIDE": lambda obj, elem: setattr(obj, "pgwide", PgwideEnum.deserialize(elem)),
        "VERBATIM": lambda obj, elem: setattr(obj, "verbatim", SerializationHelper.deserialize_by_tag(elem, "MultiLanguageVerbatim")),
    }


    def __init__(self) -> None:
        """Initialize MlFigure."""
        super().__init__()
        self.figure_caption: Optional[Caption] = None
        self.frame: Optional[FrameEnum] = None
        self.help_entry: Optional[String] = None
        self._l_graphics: list[LGraphic] = []
        self.pgwide: Optional[PgwideEnum] = None
        self.verbatim: Optional[MultiLanguageVerbatim] = None
    @property
    @lang_prefix("L-GRAPHIC")
    def l_graphics(self) -> list[LGraphic]:
        """Get l_graphics with language-specific wrapper."""
        return self._l_graphics

    @l_graphics.setter
    def l_graphics(self, value: list[LGraphic]) -> None:
        """Set l_graphics with language-specific wrapper."""
        self._l_graphics = value


    def serialize(self) -> ET.Element:
        """Serialize MlFigure to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(MlFigure, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize figure_caption
        if self.figure_caption is not None:
            serialized = SerializationHelper.serialize_item(self.figure_caption, "Caption")
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
            serialized = SerializationHelper.serialize_item(self.frame, "FrameEnum")
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
            serialized = SerializationHelper.serialize_item(self.help_entry, "String")
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

        # Serialize l_graphics (list of direct "L-GRAPHIC" children, no container)
        if self.l_graphics:
            for item in self.l_graphics:
                serialized = SerializationHelper.serialize_item(item, "LGraphic")
                if serialized is not None:
                    # Wrap with correct tag from @xml_element_name decorator
                    wrapped = ET.Element("L-GRAPHIC")
                    if hasattr(serialized, 'attrib'):
                        wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                    for child in serialized:
                        wrapped.append(child)
                    elem.append(wrapped)
        # Serialize pgwide
        if self.pgwide is not None:
            serialized = SerializationHelper.serialize_item(self.pgwide, "PgwideEnum")
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
            serialized = SerializationHelper.serialize_item(self.verbatim, "MultiLanguageVerbatim")
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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "FIGURE-CAPTION":
                setattr(obj, "figure_caption", SerializationHelper.deserialize_by_tag(child, "Caption"))
            elif tag == "FRAME":
                setattr(obj, "frame", FrameEnum.deserialize(child))
            elif tag == "HELP-ENTRY":
                setattr(obj, "help_entry", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "PGWIDE":
                setattr(obj, "pgwide", PgwideEnum.deserialize(child))
            elif tag == "VERBATIM":
                setattr(obj, "verbatim", SerializationHelper.deserialize_by_tag(child, "MultiLanguageVerbatim"))

        # Parse l_graphics (list with lang_prefix "L-GRAPHIC")
        for child in SerializationHelper.find_all_child_elements(element, "L-GRAPHIC"):
            l_graphics_item = SerializationHelper.deserialize_by_tag(child, "LGraphic")
            obj._l_graphics.append(l_graphics_item)

        return obj



class MlFigureBuilder(PaginateableBuilder):
    """Builder for MlFigure with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: MlFigure = MlFigure()


    def with_figure_caption(self, value: Optional[Caption]) -> "MlFigureBuilder":
        """Set figure_caption attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'figure_caption' is required and cannot be None")
        self._obj.figure_caption = value
        return self

    def with_frame(self, value: Optional[FrameEnum]) -> "MlFigureBuilder":
        """Set frame attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'frame' is required and cannot be None")
        self._obj.frame = value
        return self

    def with_help_entry(self, value: Optional[String]) -> "MlFigureBuilder":
        """Set help_entry attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'help_entry' is required and cannot be None")
        self._obj.help_entry = value
        return self

    def with_l_graphics(self, items: list[LGraphic]) -> "MlFigureBuilder":
        """Set l_graphics list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.l_graphics = list(items) if items else []
        return self

    def with_pgwide(self, value: Optional[PgwideEnum]) -> "MlFigureBuilder":
        """Set pgwide attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'pgwide' is required and cannot be None")
        self._obj.pgwide = value
        return self

    def with_verbatim(self, value: Optional[MultiLanguageVerbatim]) -> "MlFigureBuilder":
        """Set verbatim attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'verbatim' is required and cannot be None")
        self._obj.verbatim = value
        return self


    def add_l_graphic(self, item: LGraphic) -> "MlFigureBuilder":
        """Add a single item to l_graphics list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.l_graphics.append(item)
        return self

    def clear_l_graphics(self) -> "MlFigureBuilder":
        """Clear all items from l_graphics list.

        Returns:
            self for method chaining
        """
        self._obj.l_graphics = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "figureCaption",
        "frame",
        "helpEntry",
        "lGraphic",
        "pgwide",
        "verbatim",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> MlFigure:
        """Build and return the MlFigure instance with validation."""
        self._validate_instance()
        return self._obj