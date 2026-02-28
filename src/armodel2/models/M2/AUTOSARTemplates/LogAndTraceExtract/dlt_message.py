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
        "DLT-ARGUMENTS": lambda obj, elem: obj.dlt_arguments.append(DltArgument.deserialize(elem)),
        "MESSAGE-ID": lambda obj, elem: setattr(obj, "message_id", elem.text),
        "MESSAGE-LINE": lambda obj, elem: setattr(obj, "message_line", elem.text),
        "MESSAGE-SOURCE": lambda obj, elem: setattr(obj, "message_source", elem.text),
        "MESSAGE-TYPE-INFO": lambda obj, elem: setattr(obj, "message_type_info", elem.text),
        "PRIVACY-LEVEL": lambda obj, elem: setattr(obj, "privacy_level", PrivacyLevel.deserialize(elem)),
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

        # Parse dlt_arguments (list from container "DLT-ARGUMENTS")
        obj.dlt_arguments = []
        container = SerializationHelper.find_child_element(element, "DLT-ARGUMENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.dlt_arguments.append(child_value)

        # Parse message_id
        child = SerializationHelper.find_child_element(element, "MESSAGE-ID")
        if child is not None:
            message_id_value = child.text
            obj.message_id = message_id_value

        # Parse message_line
        child = SerializationHelper.find_child_element(element, "MESSAGE-LINE")
        if child is not None:
            message_line_value = child.text
            obj.message_line = message_line_value

        # Parse message_source
        child = SerializationHelper.find_child_element(element, "MESSAGE-SOURCE")
        if child is not None:
            message_source_value = child.text
            obj.message_source = message_source_value

        # Parse message_type_info
        child = SerializationHelper.find_child_element(element, "MESSAGE-TYPE-INFO")
        if child is not None:
            message_type_info_value = child.text
            obj.message_type_info = message_type_info_value

        # Parse privacy_level
        child = SerializationHelper.find_child_element(element, "PRIVACY-LEVEL")
        if child is not None:
            privacy_level_value = SerializationHelper.deserialize_by_tag(child, "PrivacyLevel")
            obj.privacy_level = privacy_level_value

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
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
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
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
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
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
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
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
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
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
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


    def build(self) -> DltMessage:
        """Build and return the DltMessage instance with validation."""
        self._validate_instance()
        pass
        return self._obj