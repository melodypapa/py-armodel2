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
            raise ValueError("Attribute 'msr_query_props' is required and cannot be None")
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
            raise ValueError("Attribute 'block_level' is required and cannot be None")
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
            raise ValueError("Attribute 'table' is required and cannot be None")
        self._obj.table = value
        return self

    def with_traceable_table(self, value: Any) -> "MsrQueryP1Builder":
        """Set traceable_table attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute 'traceable_table' is required and cannot be None")
        self._obj.traceable_table = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _REQUIRED_ATTRIBUTES = {
        "msrQueryProps",
    }
    _OPTIONAL_ATTRIBUTES = {
        "msrQueryResult",
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
        if getattr(self._obj, "msrQueryProps", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError("Required attribute 'msrQueryProps' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn("Required attribute 'msrQueryProps' is None", UserWarning)


    def build(self) -> MsrQueryP1:
        """Build and return the MsrQueryP1 instance with validation."""
        self._validate_instance()
        return self._obj