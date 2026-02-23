"""Colspec AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 433)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_OasisExchangeTable.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable import (
    AlignEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable import (
    TableSeparatorString,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class Colspec(ARObject):
    """AUTOSAR Colspec."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    align: Optional[AlignEnum]
    colname: Optional[String]
    colnum: Optional[String]
    colsep: Optional[TableSeparatorString]
    colwidth: Optional[String]
    rowsep: Optional[TableSeparatorString]
    def __init__(self) -> None:
        """Initialize Colspec."""
        super().__init__()
        self.align: Optional[AlignEnum] = None
        self.colname: Optional[String] = None
        self.colnum: Optional[String] = None
        self.colsep: Optional[TableSeparatorString] = None
        self.colwidth: Optional[String] = None
        self.rowsep: Optional[TableSeparatorString] = None

    def serialize(self) -> ET.Element:
        """Serialize Colspec to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Colspec, self).serialize()

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

        # Serialize colnum
        if self.colnum is not None:
            serialized = SerializationHelper.serialize_item(self.colnum, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COLNUM")
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

        # Serialize colwidth
        if self.colwidth is not None:
            serialized = SerializationHelper.serialize_item(self.colwidth, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COLWIDTH")
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

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Colspec":
        """Deserialize XML element to Colspec object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Colspec object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Colspec, cls).deserialize(element)

        # Parse align
        child = SerializationHelper.find_child_element(element, "ALIGN")
        if child is not None:
            align_value = AlignEnum.deserialize(child)
            obj.align = align_value

        # Parse colname
        child = SerializationHelper.find_child_element(element, "COLNAME")
        if child is not None:
            colname_value = child.text
            obj.colname = colname_value

        # Parse colnum
        child = SerializationHelper.find_child_element(element, "COLNUM")
        if child is not None:
            colnum_value = child.text
            obj.colnum = colnum_value

        # Parse colsep
        child = SerializationHelper.find_child_element(element, "COLSEP")
        if child is not None:
            colsep_value = child.text
            obj.colsep = colsep_value

        # Parse colwidth
        child = SerializationHelper.find_child_element(element, "COLWIDTH")
        if child is not None:
            colwidth_value = child.text
            obj.colwidth = colwidth_value

        # Parse rowsep
        child = SerializationHelper.find_child_element(element, "ROWSEP")
        if child is not None:
            rowsep_value = child.text
            obj.rowsep = rowsep_value

        return obj



class ColspecBuilder(BuilderBase):
    """Builder for Colspec with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: Colspec = Colspec()


    def with_align(self, value: Optional[AlignEnum]) -> "ColspecBuilder":
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

    def with_colname(self, value: Optional[String]) -> "ColspecBuilder":
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

    def with_colnum(self, value: Optional[String]) -> "ColspecBuilder":
        """Set colnum attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.colnum = value
        return self

    def with_colsep(self, value: Optional[TableSeparatorString]) -> "ColspecBuilder":
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

    def with_colwidth(self, value: Optional[String]) -> "ColspecBuilder":
        """Set colwidth attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.colwidth = value
        return self

    def with_rowsep(self, value: Optional[TableSeparatorString]) -> "ColspecBuilder":
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


    def build(self) -> Colspec:
        """Build and return the Colspec instance with validation."""
        self._validate_instance()
        pass
        return self._obj