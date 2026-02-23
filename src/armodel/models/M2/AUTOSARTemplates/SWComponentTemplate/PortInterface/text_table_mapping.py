"""TextTableMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 145)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 230)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import (
    MappingDirectionEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.text_table_value_pair import (
    TextTableValuePair,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class TextTableMapping(ARObject):
    """AUTOSAR TextTableMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    bitfield_text_table: Optional[PositiveInteger]
    identical: Optional[Boolean]
    mapping_ref: Optional[MappingDirectionEnum]
    value_pairs: list[TextTableValuePair]
    def __init__(self) -> None:
        """Initialize TextTableMapping."""
        super().__init__()
        self.bitfield_text_table: Optional[PositiveInteger] = None
        self.identical: Optional[Boolean] = None
        self.mapping_ref: Optional[MappingDirectionEnum] = None
        self.value_pairs: list[TextTableValuePair] = []

    def serialize(self) -> ET.Element:
        """Serialize TextTableMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TextTableMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize bitfield_text_table
        if self.bitfield_text_table is not None:
            serialized = SerializationHelper.serialize_item(self.bitfield_text_table, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BITFIELD-TEXT-TABLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize identical
        if self.identical is not None:
            serialized = SerializationHelper.serialize_item(self.identical, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IDENTICAL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mapping_ref
        if self.mapping_ref is not None:
            serialized = SerializationHelper.serialize_item(self.mapping_ref, "MappingDirectionEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAPPING-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize value_pairs (list to container "VALUE-PAIRS")
        if self.value_pairs:
            wrapper = ET.Element("VALUE-PAIRS")
            for item in self.value_pairs:
                serialized = SerializationHelper.serialize_item(item, "TextTableValuePair")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TextTableMapping":
        """Deserialize XML element to TextTableMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TextTableMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TextTableMapping, cls).deserialize(element)

        # Parse bitfield_text_table
        child = SerializationHelper.find_child_element(element, "BITFIELD-TEXT-TABLE")
        if child is not None:
            bitfield_text_table_value = child.text
            obj.bitfield_text_table = bitfield_text_table_value

        # Parse identical
        child = SerializationHelper.find_child_element(element, "IDENTICAL")
        if child is not None:
            identical_value = child.text
            obj.identical = identical_value

        # Parse mapping_ref
        child = SerializationHelper.find_child_element(element, "MAPPING-REF")
        if child is not None:
            mapping_ref_value = ARRef.deserialize(child)
            obj.mapping_ref = mapping_ref_value

        # Parse value_pairs (list from container "VALUE-PAIRS")
        obj.value_pairs = []
        container = SerializationHelper.find_child_element(element, "VALUE-PAIRS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.value_pairs.append(child_value)

        return obj



class TextTableMappingBuilder(BuilderBase):
    """Builder for TextTableMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TextTableMapping = TextTableMapping()


    def with_bitfield_text_table(self, value: Optional[PositiveInteger]) -> "TextTableMappingBuilder":
        """Set bitfield_text_table attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.bitfield_text_table = value
        return self

    def with_identical(self, value: Optional[Boolean]) -> "TextTableMappingBuilder":
        """Set identical attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.identical = value
        return self

    def with_mapping(self, value: Optional[MappingDirectionEnum]) -> "TextTableMappingBuilder":
        """Set mapping attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.mapping = value
        return self

    def with_value_pairs(self, items: list[TextTableValuePair]) -> "TextTableMappingBuilder":
        """Set value_pairs list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.value_pairs = list(items) if items else []
        return self


    def add_value_pair(self, item: TextTableValuePair) -> "TextTableMappingBuilder":
        """Add a single item to value_pairs list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.value_pairs.append(item)
        return self

    def clear_value_pairs(self) -> "TextTableMappingBuilder":
        """Clear all items from value_pairs list.

        Returns:
            self for method chaining
        """
        self._obj.value_pairs = []
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


    def build(self) -> TextTableMapping:
        """Build and return the TextTableMapping instance with validation."""
        self._validate_instance()
        pass
        return self._obj