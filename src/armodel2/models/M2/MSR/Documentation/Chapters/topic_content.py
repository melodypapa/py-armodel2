"""TopicContent AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 478)

JSON Source: docs/json/packages/M2_MSR_Documentation_Chapters.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET
from armodel2.serialization.decorators import atp_mixed

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)
from armodel2.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable.table import (
    Table,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


@atp_mixed()

class TopicContent(ARObject):
    """AUTOSAR TopicContent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "TOPIC-CONTENT"


    block_level: DocumentationBlock
    table: Optional[Table]
    traceable_table: Any
    _DESERIALIZE_DISPATCH = {
        "BLOCK-LEVEL": lambda obj, elem: setattr(obj, "block_level", SerializationHelper.deserialize_by_tag(elem, "DocumentationBlock")),
        "TABLE": lambda obj, elem: setattr(obj, "table", SerializationHelper.deserialize_by_tag(elem, "Table")),
        "TRACEABLE-TABLE": lambda obj, elem: setattr(obj, "traceable_table", SerializationHelper.deserialize_by_tag(elem, "any (TraceableTable)")),
    }


    def __init__(self) -> None:
        """Initialize TopicContent."""
        super().__init__()
        self.block_level: DocumentationBlock = None
        self.table: Optional[Table] = None
        self.traceable_table: Any = None

    def serialize(self) -> ET.Element:
        """Serialize TopicContent to XML element (atp_mixed - no wrapping).

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TopicContent, self).serialize()

        # Copy all attributes from parent element to current element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element to current element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element to current element
        for child in parent_elem:
            elem.append(child)

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
    def deserialize(cls, element: ET.Element) -> "TopicContent":
        """Deserialize XML element to TopicContent object (atp_mixed - no unwrapping).

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TopicContent object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TopicContent, cls).deserialize(element)

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



class TopicContentBuilder(BuilderBase):
    """Builder for TopicContent with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TopicContent = TopicContent()


    def with_block_level(self, value: DocumentationBlock) -> "TopicContentBuilder":
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

    def with_table(self, value: Optional[Table]) -> "TopicContentBuilder":
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

    def with_traceable_table(self, value: any (TraceableTable)) -> "TopicContentBuilder":
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



    # Pre-computed validation constants (generated from JSON schema)
    _REQUIRED_ATTRIBUTES = {
        "blockLevel",
        "traceableTable",
    }
    _OPTIONAL_ATTRIBUTES = {
        "table",
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
        if getattr(self._obj, "blockLevel", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError("Required attribute 'blockLevel' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn("Required attribute 'blockLevel' is None", UserWarning)
        if getattr(self._obj, "traceableTable", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError("Required attribute 'traceableTable' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn("Required attribute 'traceableTable' is None", UserWarning)


    def build(self) -> TopicContent:
        """Build and return the TopicContent instance with validation."""
        self._validate_instance()
        return self._obj