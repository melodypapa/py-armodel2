"""DltMessage AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2018)
  - AUTOSAR_FO_TPS_LogAndTraceExtract.pdf (page 12)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_LogAndTraceExtract.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    String,
)
from armodel2.models.M2.AUTOSARTemplates.LogAndTraceExtract.dlt_argument import (
    DltArgument,
)
from armodel2.models.M2.AUTOSARTemplates.LogAndTraceExtract.privacy_level import (
    PrivacyLevel,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DltMessage(Identifiable):
    """AUTOSAR DltMessage."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DLT-MESSAGE"


    dlt_arguments: list[DltArgument]
    message_id: Optional[PositiveInteger]
    message_line: Optional[PositiveInteger]
    message_source: Optional[String]
    message_type_info: Optional[String]
    privacy_level: Optional[PrivacyLevel]
    _DESERIALIZE_DISPATCH = {
        "DLT-ARGUMENTS": lambda obj, elem: obj.dlt_arguments.append(SerializationHelper.deserialize_by_tag(elem, "DltArgument")),
        "MESSAGE-ID": lambda obj, elem: setattr(obj, "message_id", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "MESSAGE-LINE": lambda obj, elem: setattr(obj, "message_line", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "MESSAGE-SOURCE": lambda obj, elem: setattr(obj, "message_source", SerializationHelper.deserialize_by_tag(elem, "String")),
        "MESSAGE-TYPE-INFO": lambda obj, elem: setattr(obj, "message_type_info", SerializationHelper.deserialize_by_tag(elem, "String")),
        "PRIVACY-LEVEL": lambda obj, elem: setattr(obj, "privacy_level", SerializationHelper.deserialize_by_tag(elem, "PrivacyLevel")),
    }


    def __init__(self) -> None:
        """Initialize DltMessage."""
        super().__init__()
        self.dlt_arguments: list[DltArgument] = []
        self.message_id: Optional[PositiveInteger] = None
        self.message_line: Optional[PositiveInteger] = None
        self.message_source: Optional[String] = None
        self.message_type_info: Optional[String] = None
        self.privacy_level: Optional[PrivacyLevel] = None

    def serialize(self) -> ET.Element:
        """Serialize DltMessage to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DltMessage, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize dlt_arguments (list to container "DLT-ARGUMENTS")
        if self.dlt_arguments:
            wrapper = ET.Element("DLT-ARGUMENTS")
            for item in self.dlt_arguments:
                serialized = SerializationHelper.serialize_item(item, "DltArgument")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize message_id
        if self.message_id is not None:
            serialized = SerializationHelper.serialize_item(self.message_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MESSAGE-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize message_line
        if self.message_line is not None:
            serialized = SerializationHelper.serialize_item(self.message_line, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MESSAGE-LINE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize message_source
        if self.message_source is not None:
            serialized = SerializationHelper.serialize_item(self.message_source, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MESSAGE-SOURCE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize message_type_info
        if self.message_type_info is not None:
            serialized = SerializationHelper.serialize_item(self.message_type_info, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MESSAGE-TYPE-INFO")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize privacy_level
        if self.privacy_level is not None:
            serialized = SerializationHelper.serialize_item(self.privacy_level, "PrivacyLevel")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PRIVACY-LEVEL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DltMessage":
        """Deserialize XML element to DltMessage object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DltMessage object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DltMessage, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DLT-ARGUMENTS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.dlt_arguments.append(SerializationHelper.deserialize_by_tag(item_elem, "DltArgument"))
            elif tag == "MESSAGE-ID":
                setattr(obj, "message_id", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "MESSAGE-LINE":
                setattr(obj, "message_line", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "MESSAGE-SOURCE":
                setattr(obj, "message_source", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "MESSAGE-TYPE-INFO":
                setattr(obj, "message_type_info", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "PRIVACY-LEVEL":
                setattr(obj, "privacy_level", SerializationHelper.deserialize_by_tag(child, "PrivacyLevel"))

        return obj



class DltMessageBuilder(IdentifiableBuilder):
    """Builder for DltMessage with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DltMessage = DltMessage()


    def with_dlt_arguments(self, items: list[DltArgument]) -> "DltMessageBuilder":
        """Set dlt_arguments list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.dlt_arguments = list(items) if items else []
        return self

    def with_message_id(self, value: Optional[PositiveInteger]) -> "DltMessageBuilder":
        """Set message_id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'message_id' is required and cannot be None")
        self._obj.message_id = value
        return self

    def with_message_line(self, value: Optional[PositiveInteger]) -> "DltMessageBuilder":
        """Set message_line attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'message_line' is required and cannot be None")
        self._obj.message_line = value
        return self

    def with_message_source(self, value: Optional[String]) -> "DltMessageBuilder":
        """Set message_source attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'message_source' is required and cannot be None")
        self._obj.message_source = value
        return self

    def with_message_type_info(self, value: Optional[String]) -> "DltMessageBuilder":
        """Set message_type_info attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'message_type_info' is required and cannot be None")
        self._obj.message_type_info = value
        return self

    def with_privacy_level(self, value: Optional[PrivacyLevel]) -> "DltMessageBuilder":
        """Set privacy_level attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'privacy_level' is required and cannot be None")
        self._obj.privacy_level = value
        return self


    def add_dlt_argument(self, item: DltArgument) -> "DltMessageBuilder":
        """Add a single item to dlt_arguments list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.dlt_arguments.append(item)
        return self

    def clear_dlt_arguments(self) -> "DltMessageBuilder":
        """Clear all items from dlt_arguments list.

        Returns:
            self for method chaining
        """
        self._obj.dlt_arguments = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "dltArgument",
        "messageId",
        "messageLine",
        "messageSource",
        "messageTypeInfo",
        "privacyLevel",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DltMessage:
        """Build and return the DltMessage instance with validation."""
        self._validate_instance()
        return self._obj