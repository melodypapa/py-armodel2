"""Table AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 332)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_OasisExchangeTable.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import PaginateableBuilder
from armodel2.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable import (
    FloatEnum,
    FrameEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    String,
)
from armodel2.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable import (
    TableSeparatorString,
)
from armodel2.models.M2.MSR.Documentation.BlockElements.caption import (
    Caption,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class Table(Paginateable):
    """AUTOSAR Table."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "TABLE"


    colsep: Optional[TableSeparatorString]
    float: FloatEnum
    frame: Optional[FrameEnum]
    help_entry: Optional[String]
    orient: Optional[Any]
    pgwide: Optional[NameToken]
    rowsep: Optional[TableSeparatorString]
    table_caption: Optional[Caption]
    tabstyle: Optional[NameToken]
    _DESERIALIZE_DISPATCH = {
        "COLSEP": lambda obj, elem: setattr(obj, "colsep", SerializationHelper.deserialize_by_tag(elem, "TableSeparatorString")),
        "FLOAT": lambda obj, elem: setattr(obj, "float", FloatEnum.deserialize(elem)),
        "FRAME": lambda obj, elem: setattr(obj, "frame", FrameEnum.deserialize(elem)),
        "HELP-ENTRY": lambda obj, elem: setattr(obj, "help_entry", SerializationHelper.deserialize_by_tag(elem, "String")),
        "ORIENT": lambda obj, elem: setattr(obj, "orient", SerializationHelper.deserialize_by_tag(elem, "any (OrientEnum)")),
        "PGWIDE": lambda obj, elem: setattr(obj, "pgwide", SerializationHelper.deserialize_by_tag(elem, "NameToken")),
        "ROWSEP": lambda obj, elem: setattr(obj, "rowsep", SerializationHelper.deserialize_by_tag(elem, "TableSeparatorString")),
        "TABLE-CAPTION": lambda obj, elem: setattr(obj, "table_caption", SerializationHelper.deserialize_by_tag(elem, "Caption")),
        "TABSTYLE": lambda obj, elem: setattr(obj, "tabstyle", SerializationHelper.deserialize_by_tag(elem, "NameToken")),
    }


    def __init__(self) -> None:
        """Initialize Table."""
        super().__init__()
        self.colsep: Optional[TableSeparatorString] = None
        self.float: FloatEnum = None
        self.frame: Optional[FrameEnum] = None
        self.help_entry: Optional[String] = None
        self.orient: Optional[Any] = None
        self.pgwide: Optional[NameToken] = None
        self.rowsep: Optional[TableSeparatorString] = None
        self.table_caption: Optional[Caption] = None
        self.tabstyle: Optional[NameToken] = None

    def serialize(self) -> ET.Element:
        """Serialize Table to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Table, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize colsep
        if self.colsep is not None:
            serialized = SerializationHelper.serialize_item(self.colsep, "TableSeparatorString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COLSEP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize float
        if self.float is not None:
            serialized = SerializationHelper.serialize_item(self.float, "FloatEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FLOAT")
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

        # Serialize orient
        if self.orient is not None:
            serialized = SerializationHelper.serialize_item(self.orient, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ORIENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize pgwide
        if self.pgwide is not None:
            serialized = SerializationHelper.serialize_item(self.pgwide, "NameToken")
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

        # Serialize rowsep
        if self.rowsep is not None:
            serialized = SerializationHelper.serialize_item(self.rowsep, "TableSeparatorString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ROWSEP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize table_caption
        if self.table_caption is not None:
            serialized = SerializationHelper.serialize_item(self.table_caption, "Caption")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TABLE-CAPTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tabstyle
        if self.tabstyle is not None:
            serialized = SerializationHelper.serialize_item(self.tabstyle, "NameToken")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TABSTYLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Table":
        """Deserialize XML element to Table object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Table object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Table, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "COLSEP":
                setattr(obj, "colsep", SerializationHelper.deserialize_by_tag(child, "TableSeparatorString"))
            elif tag == "FLOAT":
                setattr(obj, "float", FloatEnum.deserialize(child))
            elif tag == "FRAME":
                setattr(obj, "frame", FrameEnum.deserialize(child))
            elif tag == "HELP-ENTRY":
                setattr(obj, "help_entry", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "ORIENT":
                setattr(obj, "orient", SerializationHelper.deserialize_by_tag(child, "any (OrientEnum)"))
            elif tag == "PGWIDE":
                setattr(obj, "pgwide", SerializationHelper.deserialize_by_tag(child, "NameToken"))
            elif tag == "ROWSEP":
                setattr(obj, "rowsep", SerializationHelper.deserialize_by_tag(child, "TableSeparatorString"))
            elif tag == "TABLE-CAPTION":
                setattr(obj, "table_caption", SerializationHelper.deserialize_by_tag(child, "Caption"))
            elif tag == "TABSTYLE":
                setattr(obj, "tabstyle", SerializationHelper.deserialize_by_tag(child, "NameToken"))

        return obj



class TableBuilder(PaginateableBuilder):
    """Builder for Table with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: Table = Table()


    def with_colsep(self, value: Optional[TableSeparatorString]) -> "TableBuilder":
        """Set colsep attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'colsep' is required and cannot be None")
        self._obj.colsep = value
        return self

    def with_float(self, value: FloatEnum) -> "TableBuilder":
        """Set float attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute 'float' is required and cannot be None")
        self._obj.float = value
        return self

    def with_frame(self, value: Optional[FrameEnum]) -> "TableBuilder":
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

    def with_help_entry(self, value: Optional[String]) -> "TableBuilder":
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

    def with_orient(self, value: Optional[Any]) -> "TableBuilder":
        """Set orient attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'orient' is required and cannot be None")
        self._obj.orient = value
        return self

    def with_pgwide(self, value: Optional[NameToken]) -> "TableBuilder":
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

    def with_rowsep(self, value: Optional[TableSeparatorString]) -> "TableBuilder":
        """Set rowsep attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'rowsep' is required and cannot be None")
        self._obj.rowsep = value
        return self

    def with_table_caption(self, value: Optional[Caption]) -> "TableBuilder":
        """Set table_caption attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'table_caption' is required and cannot be None")
        self._obj.table_caption = value
        return self

    def with_tabstyle(self, value: Optional[NameToken]) -> "TableBuilder":
        """Set tabstyle attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'tabstyle' is required and cannot be None")
        self._obj.tabstyle = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _REQUIRED_ATTRIBUTES = {
        "float",
    }
    _OPTIONAL_ATTRIBUTES = {
        "colsep",
        "frame",
        "helpEntry",
        "orient",
        "pgwide",
        "rowsep",
        "tableCaption",
        "tabstyle",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Validate required attributes using pre-computed constants (O(1) lookup)
        # This is much faster than calling get_type_hints() at runtime
        if getattr(self._obj, "float", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError("Required attribute 'float' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn("Required attribute 'float' is None", UserWarning)


    def build(self) -> Table:
        """Build and return the Table instance with validation."""
        self._validate_instance()
        return self._obj