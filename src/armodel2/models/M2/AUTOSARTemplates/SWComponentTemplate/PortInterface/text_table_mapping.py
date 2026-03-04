"""TextTableMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 145)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 230)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import (
    MappingDirectionEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.text_table_value_pair import (
    TextTableValuePair,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class TextTableMapping(ARObject):
    """AUTOSAR TextTableMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "TEXT-TABLE-MAPPING"


    bitfield_text_table: Optional[PositiveInteger]
    identical: Optional[Boolean]
    mapping_ref: Optional[MappingDirectionEnum]
    value_pairs: list[TextTableValuePair]
    _DESERIALIZE_DISPATCH = {
        "BITFIELD-TEXT-TABLE": lambda obj, elem: setattr(obj, "bitfield_text_table", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "IDENTICAL": lambda obj, elem: setattr(obj, "identical", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "MAPPING-REF": lambda obj, elem: setattr(obj, "mapping_ref", MappingDirectionEnum.deserialize(elem)),
        "VALUE-PAIRS": lambda obj, elem: obj.value_pairs.append(SerializationHelper.deserialize_by_tag(elem, "TextTableValuePair")),
    }


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
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "BITFIELD-TEXT-TABLE":
                setattr(obj, "bitfield_text_table", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "IDENTICAL":
                setattr(obj, "identical", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "MAPPING-REF":
                setattr(obj, "mapping_ref", MappingDirectionEnum.deserialize(child))
            elif tag == "VALUE-PAIRS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.value_pairs.append(SerializationHelper.deserialize_by_tag(item_elem, "TextTableValuePair"))

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


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "bitfieldTextTable",
        "identical",
        "mapping",
        "valuePair",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> TextTableMapping:
        """Build and return the TextTableMapping instance with validation."""
        self._validate_instance()
        return self._obj