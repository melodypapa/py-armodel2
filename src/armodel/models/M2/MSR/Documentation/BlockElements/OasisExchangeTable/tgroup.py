"""Tgroup AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 334)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_OasisExchangeTable.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable import (
    AlignEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable import (
    TableSeparatorString,
)
from armodel.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable.colspec import (
    Colspec,
)
from armodel.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable.tbody import (
    Tbody,
)


class Tgroup(ARObject):
    """AUTOSAR Tgroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    align: Optional[AlignEnum]
    cols: Integer
    colsep: Optional[TableSeparatorString]
    colspecs: list[Colspec]
    rowsep: Optional[TableSeparatorString]
    tbody: Tbody
    tfoot: Optional[Tbody]
    thead: Optional[Tbody]
    def __init__(self) -> None:
        """Initialize Tgroup."""
        super().__init__()
        self.align: Optional[AlignEnum] = None
        self.cols: Integer = None
        self.colsep: Optional[TableSeparatorString] = None
        self.colspecs: list[Colspec] = []
        self.rowsep: Optional[TableSeparatorString] = None
        self.tbody: Tbody = None
        self.tfoot: Optional[Tbody] = None
        self.thead: Optional[Tbody] = None

    def serialize(self) -> ET.Element:
        """Serialize Tgroup to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Tgroup, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize align
        if self.align is not None:
            serialized = SerializationHelper.serialize_item(self.align, "AlignEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ALIGN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize cols
        if self.cols is not None:
            serialized = SerializationHelper.serialize_item(self.cols, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COLS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

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

        # Serialize colspecs (list to container "COLSPECS")
        if self.colspecs:
            wrapper = ET.Element("COLSPECS")
            for item in self.colspecs:
                serialized = SerializationHelper.serialize_item(item, "Colspec")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

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

        # Serialize tbody
        if self.tbody is not None:
            serialized = SerializationHelper.serialize_item(self.tbody, "Tbody")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TBODY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tfoot
        if self.tfoot is not None:
            serialized = SerializationHelper.serialize_item(self.tfoot, "Tbody")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TFOOT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize thead
        if self.thead is not None:
            serialized = SerializationHelper.serialize_item(self.thead, "Tbody")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("THEAD")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Tgroup":
        """Deserialize XML element to Tgroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Tgroup object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Tgroup, cls).deserialize(element)

        # Parse align
        child = SerializationHelper.find_child_element(element, "ALIGN")
        if child is not None:
            align_value = AlignEnum.deserialize(child)
            obj.align = align_value

        # Parse cols
        child = SerializationHelper.find_child_element(element, "COLS")
        if child is not None:
            cols_value = child.text
            obj.cols = cols_value

        # Parse colsep
        child = SerializationHelper.find_child_element(element, "COLSEP")
        if child is not None:
            colsep_value = child.text
            obj.colsep = colsep_value

        # Parse colspecs (list from container "COLSPECS")
        obj.colspecs = []
        container = SerializationHelper.find_child_element(element, "COLSPECS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.colspecs.append(child_value)

        # Parse rowsep
        child = SerializationHelper.find_child_element(element, "ROWSEP")
        if child is not None:
            rowsep_value = child.text
            obj.rowsep = rowsep_value

        # Parse tbody
        child = SerializationHelper.find_child_element(element, "TBODY")
        if child is not None:
            tbody_value = SerializationHelper.deserialize_by_tag(child, "Tbody")
            obj.tbody = tbody_value

        # Parse tfoot
        child = SerializationHelper.find_child_element(element, "TFOOT")
        if child is not None:
            tfoot_value = SerializationHelper.deserialize_by_tag(child, "Tbody")
            obj.tfoot = tfoot_value

        # Parse thead
        child = SerializationHelper.find_child_element(element, "THEAD")
        if child is not None:
            thead_value = SerializationHelper.deserialize_by_tag(child, "Tbody")
            obj.thead = thead_value

        return obj



class TgroupBuilder(BuilderBase):
    """Builder for Tgroup with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: Tgroup = Tgroup()


    def with_align(self, value: Optional[AlignEnum]) -> "TgroupBuilder":
        """Set align attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.align = value
        return self

    def with_cols(self, value: Integer) -> "TgroupBuilder":
        """Set cols attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.cols = value
        return self

    def with_colsep(self, value: Optional[TableSeparatorString]) -> "TgroupBuilder":
        """Set colsep attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.colsep = value
        return self

    def with_colspecs(self, items: list[Colspec]) -> "TgroupBuilder":
        """Set colspecs list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.colspecs = list(items) if items else []
        return self

    def with_rowsep(self, value: Optional[TableSeparatorString]) -> "TgroupBuilder":
        """Set rowsep attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.rowsep = value
        return self

    def with_tbody(self, value: Tbody) -> "TgroupBuilder":
        """Set tbody attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tbody = value
        return self

    def with_tfoot(self, value: Optional[Tbody]) -> "TgroupBuilder":
        """Set tfoot attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tfoot = value
        return self

    def with_thead(self, value: Optional[Tbody]) -> "TgroupBuilder":
        """Set thead attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.thead = value
        return self


    def add_colspec(self, item: Colspec) -> "TgroupBuilder":
        """Add a single item to colspecs list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.colspecs.append(item)
        return self

    def clear_colspecs(self) -> "TgroupBuilder":
        """Clear all items from colspecs list.

        Returns:
            self for method chaining
        """
        self._obj.colspecs = []
        return self



    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Get type hints for the class
        try:
            type_hints_dict = get_type_hints(type(self._obj))
        except Exception:
            # Cannot resolve type hints (e.g., forward references), skip validation
            return

        for attr_name, attr_type in type_hints_dict.items():
            if attr_name.startswith("_"):
                continue

            value = getattr(self._obj, attr_name)

            # Check required fields (not Optional)
            if value is None and not self._is_optional_type(attr_type):
                if mode == BuilderValidationMode.STRICT:
                    raise ValueError(
                        f"Required attribute '{attr_name}' is None"
                    )
                elif mode == BuilderValidationMode.LENIENT:
                    import warnings
                    warnings.warn(
                        f"Required attribute '{attr_name}' is None",
                        UserWarning
                    )

    @staticmethod
    def _is_optional_type(type_hint: Any) -> bool:
        """Check if a type hint is Optional.

        Args:
            type_hint: Type hint to check

        Returns:
            True if type is Optional, False otherwise
        """
        origin = getattr(type_hint, "__origin__", None)
        return origin is Union

    @staticmethod
    def _get_expected_type(type_hint: Any) -> type:
        """Extract expected type from type hint.

        Args:
            type_hint: Type hint to extract from

        Returns:
            Expected type
        """
        if isinstance(type_hint, str):
            return object
        origin = getattr(type_hint, "__origin__", None)
        if origin is Union:
            args = getattr(type_hint, "__args__", [])
            for arg in args:
                if arg is not type(None):
                    return arg
        elif origin is list:
            args = getattr(type_hint, "__args__", [object])
            return args[0] if args else object
        return type_hint if isinstance(type_hint, type) else object


    def build(self) -> Tgroup:
        """Build and return the Tgroup instance with validation."""
        self._validate_instance()
        pass
        return self._obj