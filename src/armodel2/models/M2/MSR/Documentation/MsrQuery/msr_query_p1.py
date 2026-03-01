"""MsrQueryP1 AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 343)

JSON Source: docs/json/packages/M2_MSR_Documentation_MsrQuery.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import PaginateableBuilder
from armodel2.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)
from armodel2.models.M2.MSR.Documentation.MsrQuery.msr_query_props import (
    MsrQueryProps,
)
from armodel2.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable.table import (
    Table,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class MsrQueryP1(Paginateable):
    """AUTOSAR MsrQueryP1."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "MSR-QUERY-P1"


    msr_query_props: MsrQueryProps
    block_level: DocumentationBlock
    table: Optional[Table]
    traceable_table: Any
    _DESERIALIZE_DISPATCH = {
        "MSR-QUERY-PROPS": lambda obj, elem: setattr(obj, "msr_query_props", SerializationHelper.deserialize_by_tag(elem, "MsrQueryProps")),
        "BLOCK-LEVEL": lambda obj, elem: setattr(obj, "block_level", SerializationHelper.deserialize_by_tag(elem, "DocumentationBlock")),
        "TABLE": lambda obj, elem: setattr(obj, "table", SerializationHelper.deserialize_by_tag(elem, "Table")),
        "TRACEABLE-TABLE": lambda obj, elem: setattr(obj, "traceable_table", SerializationHelper.deserialize_by_tag(elem, "any (TraceableTable)")),
    }


    def __init__(self) -> None:
        """Initialize MsrQueryP1."""
        super().__init__()
        self.msr_query_props: MsrQueryProps = None
        self.block_level: DocumentationBlock = None
        self.table: Optional[Table] = None
        self.traceable_table: Any = None

    def serialize(self) -> ET.Element:
        """Serialize MsrQueryP1 to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(MsrQueryP1, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize msr_query_props
        if self.msr_query_props is not None:
            serialized = SerializationHelper.serialize_item(self.msr_query_props, "MsrQueryProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MSR-QUERY-PROPS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize block_level
        if self.block_level is not None:
            serialized = SerializationHelper.serialize_item(self.block_level, "DocumentationBlock")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BLOCK-LEVEL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize table
        if self.table is not None:
            serialized = SerializationHelper.serialize_item(self.table, "Table")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TABLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize traceable_table
        if self.traceable_table is not None:
            serialized = SerializationHelper.serialize_item(self.traceable_table, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TRACEABLE-TABLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MsrQueryP1":
        """Deserialize XML element to MsrQueryP1 object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MsrQueryP1 object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(MsrQueryP1, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "MSR-QUERY-PROPS":
                setattr(obj, "msr_query_props", SerializationHelper.deserialize_by_tag(child, "MsrQueryProps"))
            elif tag == "BLOCK-LEVEL":
                setattr(obj, "block_level", SerializationHelper.deserialize_by_tag(child, "DocumentationBlock"))
            elif tag == "TABLE":
                setattr(obj, "table", SerializationHelper.deserialize_by_tag(child, "Table"))
            elif tag == "TRACEABLE-TABLE":
                setattr(obj, "traceable_table", SerializationHelper.deserialize_by_tag(child, "any (TraceableTable)"))

        return obj



class MsrQueryP1Builder(PaginateableBuilder):
    """Builder for MsrQueryP1 with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: MsrQueryP1 = MsrQueryP1()


    def with_msr_query_props(self, value: MsrQueryProps) -> "MsrQueryP1Builder":
        """Set msr_query_props attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.msr_query_props = value
        return self

    def with_block_level(self, value: DocumentationBlock) -> "MsrQueryP1Builder":
        """Set block_level attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.block_level = value
        return self

    def with_table(self, value: Optional[Table]) -> "MsrQueryP1Builder":
        """Set table attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.table = value
        return self

    def with_traceable_table(self, value: any (TraceableTable)) -> "MsrQueryP1Builder":
        """Set traceable_table attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.traceable_table = value
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


    def build(self) -> MsrQueryP1:
        """Build and return the MsrQueryP1 instance with validation."""
        self._validate_instance()
        pass
        return self._obj