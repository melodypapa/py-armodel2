"""EndToEndDescription AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 205)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 385)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_EndToEndProtection.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class EndToEndDescription(ARObject):
    """AUTOSAR EndToEndDescription."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "END-TO-END-DESCRIPTION"


    category: Optional[NameToken]
    counter_offset: Optional[PositiveInteger]
    crc_offset: Optional[PositiveInteger]
    data_id_mode: Optional[PositiveInteger]
    data_id_nibble: Optional[PositiveInteger]
    data_length: Optional[PositiveInteger]
    max_delta: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "CATEGORY": lambda obj, elem: setattr(obj, "category", SerializationHelper.deserialize_by_tag(elem, "NameToken")),
        "COUNTER-OFFSET": lambda obj, elem: setattr(obj, "counter_offset", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "CRC-OFFSET": lambda obj, elem: setattr(obj, "crc_offset", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "DATA-ID-MODE": lambda obj, elem: setattr(obj, "data_id_mode", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "DATA-ID-NIBBLE": lambda obj, elem: setattr(obj, "data_id_nibble", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "DATA-LENGTH": lambda obj, elem: setattr(obj, "data_length", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "MAX-DELTA": lambda obj, elem: setattr(obj, "max_delta", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize EndToEndDescription."""
        super().__init__()
        self.category: Optional[NameToken] = None
        self.counter_offset: Optional[PositiveInteger] = None
        self.crc_offset: Optional[PositiveInteger] = None
        self.data_id_mode: Optional[PositiveInteger] = None
        self.data_id_nibble: Optional[PositiveInteger] = None
        self.data_length: Optional[PositiveInteger] = None
        self.max_delta: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize EndToEndDescription to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EndToEndDescription, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize category
        if self.category is not None:
            serialized = SerializationHelper.serialize_item(self.category, "NameToken")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CATEGORY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize counter_offset
        if self.counter_offset is not None:
            serialized = SerializationHelper.serialize_item(self.counter_offset, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COUNTER-OFFSET")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize crc_offset
        if self.crc_offset is not None:
            serialized = SerializationHelper.serialize_item(self.crc_offset, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CRC-OFFSET")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize data_id_mode
        if self.data_id_mode is not None:
            serialized = SerializationHelper.serialize_item(self.data_id_mode, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-ID-MODE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize data_id_nibble
        if self.data_id_nibble is not None:
            serialized = SerializationHelper.serialize_item(self.data_id_nibble, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-ID-NIBBLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize data_length
        if self.data_length is not None:
            serialized = SerializationHelper.serialize_item(self.data_length, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-LENGTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_delta
        if self.max_delta is not None:
            serialized = SerializationHelper.serialize_item(self.max_delta, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-DELTA")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EndToEndDescription":
        """Deserialize XML element to EndToEndDescription object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EndToEndDescription object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EndToEndDescription, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CATEGORY":
                setattr(obj, "category", SerializationHelper.deserialize_by_tag(child, "NameToken"))
            elif tag == "COUNTER-OFFSET":
                setattr(obj, "counter_offset", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "CRC-OFFSET":
                setattr(obj, "crc_offset", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "DATA-ID-MODE":
                setattr(obj, "data_id_mode", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "DATA-ID-NIBBLE":
                setattr(obj, "data_id_nibble", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "DATA-LENGTH":
                setattr(obj, "data_length", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "MAX-DELTA":
                setattr(obj, "max_delta", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class EndToEndDescriptionBuilder(BuilderBase):
    """Builder for EndToEndDescription with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EndToEndDescription = EndToEndDescription()


    def with_category(self, value: Optional[NameToken]) -> "EndToEndDescriptionBuilder":
        """Set category attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'category' is required and cannot be None")
        self._obj.category = value
        return self

    def with_counter_offset(self, value: Optional[PositiveInteger]) -> "EndToEndDescriptionBuilder":
        """Set counter_offset attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'counter_offset' is required and cannot be None")
        self._obj.counter_offset = value
        return self

    def with_crc_offset(self, value: Optional[PositiveInteger]) -> "EndToEndDescriptionBuilder":
        """Set crc_offset attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'crc_offset' is required and cannot be None")
        self._obj.crc_offset = value
        return self

    def with_data_id_mode(self, value: Optional[PositiveInteger]) -> "EndToEndDescriptionBuilder":
        """Set data_id_mode attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'data_id_mode' is required and cannot be None")
        self._obj.data_id_mode = value
        return self

    def with_data_id_nibble(self, value: Optional[PositiveInteger]) -> "EndToEndDescriptionBuilder":
        """Set data_id_nibble attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'data_id_nibble' is required and cannot be None")
        self._obj.data_id_nibble = value
        return self

    def with_data_length(self, value: Optional[PositiveInteger]) -> "EndToEndDescriptionBuilder":
        """Set data_length attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'data_length' is required and cannot be None")
        self._obj.data_length = value
        return self

    def with_max_delta(self, value: Optional[PositiveInteger]) -> "EndToEndDescriptionBuilder":
        """Set max_delta attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'max_delta' is required and cannot be None")
        self._obj.max_delta = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "category",
        "counterOffset",
        "crcOffset",
        "dataIdMode",
        "dataIdNibble",
        "dataLength",
        "maxDelta",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> EndToEndDescription:
        """Build and return the EndToEndDescription instance with validation."""
        self._validate_instance()
        return self._obj