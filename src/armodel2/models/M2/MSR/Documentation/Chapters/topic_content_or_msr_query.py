"""TopicContentOrMsrQuery AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 342)

JSON Source: docs/json/packages/M2_MSR_Documentation_Chapters.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET
from armodel2.serialization.decorators import atp_mixed

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)
from armodel2.models.M2.MSR.Documentation.MsrQuery.msr_query_p1 import (
    MsrQueryP1,
)
from armodel2.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable.table import (
    Table,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


@atp_mixed()

class TopicContentOrMsrQuery(ARObject):
    """AUTOSAR TopicContentOrMsrQuery."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "TOPIC-CONTENT-OR-MSR-QUERY"


    msr_query_p1: MsrQueryP1
    block_level: DocumentationBlock
    table: Optional[Table]
    traceable_table: Any
    _DESERIALIZE_DISPATCH = {
        "MSR-QUERY-P1": lambda obj, elem: setattr(obj, "msr_query_p1", SerializationHelper.deserialize_by_tag(elem, "MsrQueryP1")),
        "BLOCK-LEVEL": lambda obj, elem: setattr(obj, "block_level", SerializationHelper.deserialize_by_tag(elem, "DocumentationBlock")),
        "TABLE": lambda obj, elem: setattr(obj, "table", SerializationHelper.deserialize_by_tag(elem, "Table")),
        "TRACEABLE-TABLE": lambda obj, elem: setattr(obj, "traceable_table", SerializationHelper.deserialize_by_tag(elem, "any (TraceableTable)")),
    }


    def __init__(self) -> None:
        """Initialize TopicContentOrMsrQuery."""
        super().__init__()
        self.msr_query_p1: MsrQueryP1 = None
        self.block_level: DocumentationBlock = None
        self.table: Optional[Table] = None
        self.traceable_table: Any = None

    def serialize(self) -> ET.Element:
        """Serialize TopicContentOrMsrQuery to XML element (atp_mixed - no wrapping).

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TopicContentOrMsrQuery, self).serialize()

        # Copy all attributes from parent element to current element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element to current element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element to current element
        for child in parent_elem:
            elem.append(child)

        # Serialize msr_query_p1 (complex type)
        if self.msr_query_p1 is not None:
            serialized = SerializationHelper.serialize_item(self.msr_query_p1, "MsrQueryP1")
            if serialized is not None:
                wrapped = ET.Element("MSR-QUERY-P1")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize block_level (complex type)
        if self.block_level is not None:
            serialized = SerializationHelper.serialize_item(self.block_level, "DocumentationBlock")
            if serialized is not None:
                wrapped = ET.Element("BLOCK-LEVEL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize table (complex type)
        if self.table is not None:
            serialized = SerializationHelper.serialize_item(self.table, "Table")
            if serialized is not None:
                wrapped = ET.Element("TABLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize traceable_table (complex type)
        if self.traceable_table is not None:
            serialized = SerializationHelper.serialize_item(self.traceable_table, "Any")
            if serialized is not None:
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
    def deserialize(cls, element: ET.Element) -> "TopicContentOrMsrQuery":
        """Deserialize XML element to TopicContentOrMsrQuery object (atp_mixed - no unwrapping).

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TopicContentOrMsrQuery object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TopicContentOrMsrQuery, cls).deserialize(element)

        # Parse msr_query_p1
        child = SerializationHelper.find_child_element(element, "MSR-QUERY-P1")
        if child is not None:
            msr_query_p1_value = SerializationHelper.deserialize_by_tag(child, "MsrQueryP1")
            obj.msr_query_p1 = msr_query_p1_value

        # Parse block_level
        child = SerializationHelper.find_child_element(element, "BLOCK-LEVEL")
        if child is not None:
            block_level_value = SerializationHelper.deserialize_by_tag(child, "DocumentationBlock")
            obj.block_level = block_level_value

        # Parse table
        child = SerializationHelper.find_child_element(element, "TABLE")
        if child is not None:
            table_value = SerializationHelper.deserialize_by_tag(child, "Table")
            obj.table = table_value

        # Parse traceable_table
        child = SerializationHelper.find_child_element(element, "TRACEABLE-TABLE")
        if child is not None:
            traceable_table_value = SerializationHelper.deserialize_by_tag(child, "Any")
            obj.traceable_table = traceable_table_value

        return obj



class TopicContentOrMsrQueryBuilder(BuilderBase):
    """Builder for TopicContentOrMsrQuery with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TopicContentOrMsrQuery = TopicContentOrMsrQuery()


    def with_msr_query_p1(self, value: MsrQueryP1) -> "TopicContentOrMsrQueryBuilder":
        """Set msr_query_p1 attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.msr_query_p1 = value
        return self

    def with_block_level(self, value: DocumentationBlock) -> "TopicContentOrMsrQueryBuilder":
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

    def with_table(self, value: Optional[Table]) -> "TopicContentOrMsrQueryBuilder":
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

    def with_traceable_table(self, value: any (TraceableTable)) -> "TopicContentOrMsrQueryBuilder":
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


    def build(self) -> TopicContentOrMsrQuery:
        """Build and return the TopicContentOrMsrQuery instance with validation."""
        self._validate_instance()
        pass
        return self._obj