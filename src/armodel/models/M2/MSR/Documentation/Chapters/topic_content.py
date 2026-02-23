"""TopicContent AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 478)

JSON Source: docs/json/packages/M2_MSR_Documentation_Chapters.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)
from armodel.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable.table import (
    Table,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class TopicContent(ARObject):
    """AUTOSAR TopicContent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    block_level: DocumentationBlock
    table: Optional[Table]
    traceable_table: Any
    def __init__(self) -> None:
        """Initialize TopicContent."""
        super().__init__()
        self.block_level: DocumentationBlock = None
        self.table: Optional[Table] = None
        self.traceable_table: Any = None

    def serialize(self) -> ET.Element:
        """Serialize TopicContent to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TopicContent, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

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
    def deserialize(cls, element: ET.Element) -> "TopicContent":
        """Deserialize XML element to TopicContent object.

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
            traceable_table_value = child.text
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


    def build(self) -> TopicContent:
        """Build and return the TopicContent instance with validation."""
        self._validate_instance()
        pass
        return self._obj