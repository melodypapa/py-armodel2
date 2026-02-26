"""Entry AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 336)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_OasisExchangeTable.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable import (
    AlignEnum,
    ValignEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel2.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable import (
    TableSeparatorString,
)
from armodel2.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class Entry(ARObject):
    """AUTOSAR Entry."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    align: Optional[AlignEnum]
    bgcolor: String
    colname: Optional[String]
    colsep: Optional[TableSeparatorString]
    entry_contents: DocumentationBlock
    morerows: Optional[String]
    nameend: Optional[String]
    namest: Optional[String]
    rotate: Optional[String]
    rowsep: Optional[TableSeparatorString]
    spanname: Optional[String]
    valign: Optional[ValignEnum]
    def __init__(self) -> None:
        """Initialize Entry."""
        super().__init__()
        self.align: Optional[AlignEnum] = None
        self.bgcolor: String = None
        self.colname: Optional[String] = None
        self.colsep: Optional[TableSeparatorString] = None
        self.entry_contents: DocumentationBlock = None
        self.morerows: Optional[String] = None
        self.nameend: Optional[String] = None
        self.namest: Optional[String] = None
        self.rotate: Optional[String] = None
        self.rowsep: Optional[TableSeparatorString] = None
        self.spanname: Optional[String] = None
        self.valign: Optional[ValignEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize Entry to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Entry, self).serialize()

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

        # Serialize bgcolor
        if self.bgcolor is not None:
            serialized = SerializationHelper.serialize_item(self.bgcolor, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BGCOLOR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize colname
        if self.colname is not None:
            serialized = SerializationHelper.serialize_item(self.colname, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COLNAME")
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

        # Serialize entry_contents
        if self.entry_contents is not None:
            serialized = SerializationHelper.serialize_item(self.entry_contents, "DocumentationBlock")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ENTRY-CONTENTS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize morerows
        if self.morerows is not None:
            serialized = SerializationHelper.serialize_item(self.morerows, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MOREROWS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nameend
        if self.nameend is not None:
            serialized = SerializationHelper.serialize_item(self.nameend, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NAMEEND")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize namest
        if self.namest is not None:
            serialized = SerializationHelper.serialize_item(self.namest, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NAMEST")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rotate
        if self.rotate is not None:
            serialized = SerializationHelper.serialize_item(self.rotate, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ROTATE")
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

        # Serialize spanname
        if self.spanname is not None:
            serialized = SerializationHelper.serialize_item(self.spanname, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SPANNAME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize valign
        if self.valign is not None:
            serialized = SerializationHelper.serialize_item(self.valign, "ValignEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VALIGN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Entry":
        """Deserialize XML element to Entry object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Entry object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Entry, cls).deserialize(element)

        # Parse align
        child = SerializationHelper.find_child_element(element, "ALIGN")
        if child is not None:
            align_value = AlignEnum.deserialize(child)
            obj.align = align_value

        # Parse bgcolor
        child = SerializationHelper.find_child_element(element, "BGCOLOR")
        if child is not None:
            bgcolor_value = child.text
            obj.bgcolor = bgcolor_value

        # Parse colname
        child = SerializationHelper.find_child_element(element, "COLNAME")
        if child is not None:
            colname_value = child.text
            obj.colname = colname_value

        # Parse colsep
        child = SerializationHelper.find_child_element(element, "COLSEP")
        if child is not None:
            colsep_value = child.text
            obj.colsep = colsep_value

        # Parse entry_contents
        child = SerializationHelper.find_child_element(element, "ENTRY-CONTENTS")
        if child is not None:
            entry_contents_value = SerializationHelper.deserialize_by_tag(child, "DocumentationBlock")
            obj.entry_contents = entry_contents_value

        # Parse morerows
        child = SerializationHelper.find_child_element(element, "MOREROWS")
        if child is not None:
            morerows_value = child.text
            obj.morerows = morerows_value

        # Parse nameend
        child = SerializationHelper.find_child_element(element, "NAMEEND")
        if child is not None:
            nameend_value = child.text
            obj.nameend = nameend_value

        # Parse namest
        child = SerializationHelper.find_child_element(element, "NAMEST")
        if child is not None:
            namest_value = child.text
            obj.namest = namest_value

        # Parse rotate
        child = SerializationHelper.find_child_element(element, "ROTATE")
        if child is not None:
            rotate_value = child.text
            obj.rotate = rotate_value

        # Parse rowsep
        child = SerializationHelper.find_child_element(element, "ROWSEP")
        if child is not None:
            rowsep_value = child.text
            obj.rowsep = rowsep_value

        # Parse spanname
        child = SerializationHelper.find_child_element(element, "SPANNAME")
        if child is not None:
            spanname_value = child.text
            obj.spanname = spanname_value

        # Parse valign
        child = SerializationHelper.find_child_element(element, "VALIGN")
        if child is not None:
            valign_value = ValignEnum.deserialize(child)
            obj.valign = valign_value

        return obj



class EntryBuilder(BuilderBase):
    """Builder for Entry with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: Entry = Entry()


    def with_align(self, value: Optional[AlignEnum]) -> "EntryBuilder":
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

    def with_bgcolor(self, value: String) -> "EntryBuilder":
        """Set bgcolor attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.bgcolor = value
        return self

    def with_colname(self, value: Optional[String]) -> "EntryBuilder":
        """Set colname attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.colname = value
        return self

    def with_colsep(self, value: Optional[TableSeparatorString]) -> "EntryBuilder":
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

    def with_entry_contents(self, value: DocumentationBlock) -> "EntryBuilder":
        """Set entry_contents attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.entry_contents = value
        return self

    def with_morerows(self, value: Optional[String]) -> "EntryBuilder":
        """Set morerows attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.morerows = value
        return self

    def with_nameend(self, value: Optional[String]) -> "EntryBuilder":
        """Set nameend attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.nameend = value
        return self

    def with_namest(self, value: Optional[String]) -> "EntryBuilder":
        """Set namest attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.namest = value
        return self

    def with_rotate(self, value: Optional[String]) -> "EntryBuilder":
        """Set rotate attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.rotate = value
        return self

    def with_rowsep(self, value: Optional[TableSeparatorString]) -> "EntryBuilder":
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

    def with_spanname(self, value: Optional[String]) -> "EntryBuilder":
        """Set spanname attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.spanname = value
        return self

    def with_valign(self, value: Optional[ValignEnum]) -> "EntryBuilder":
        """Set valign attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.valign = value
        return self




    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

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


    def build(self) -> Entry:
        """Build and return the Entry instance with validation."""
        self._validate_instance()
        pass
        return self._obj