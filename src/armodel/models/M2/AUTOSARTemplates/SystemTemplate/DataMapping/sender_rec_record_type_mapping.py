"""SenderRecRecordTypeMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 235)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_DataMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.sender_rec_composite_type_mapping import (
    SenderRecCompositeTypeMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.sender_rec_composite_type_mapping import SenderRecCompositeTypeMappingBuilder


class SenderRecRecordTypeMapping(SenderRecCompositeTypeMapping):
    """AUTOSAR SenderRecRecordTypeMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    record_elements: list[Any]
    def __init__(self) -> None:
        """Initialize SenderRecRecordTypeMapping."""
        super().__init__()
        self.record_elements: list[Any] = []

    def serialize(self) -> ET.Element:
        """Serialize SenderRecRecordTypeMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SenderRecRecordTypeMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize record_elements (list to container "RECORD-ELEMENTS")
        if self.record_elements:
            wrapper = ET.Element("RECORD-ELEMENTS")
            for item in self.record_elements:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SenderRecRecordTypeMapping":
        """Deserialize XML element to SenderRecRecordTypeMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SenderRecRecordTypeMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SenderRecRecordTypeMapping, cls).deserialize(element)

        # Parse record_elements (list from container "RECORD-ELEMENTS")
        obj.record_elements = []
        container = SerializationHelper.find_child_element(element, "RECORD-ELEMENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.record_elements.append(child_value)

        return obj



class SenderRecRecordTypeMappingBuilder(SenderRecCompositeTypeMappingBuilder):
    """Builder for SenderRecRecordTypeMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SenderRecRecordTypeMapping = SenderRecRecordTypeMapping()


    def with_record_elements(self, items: list[any (SenderRecRecord)]) -> "SenderRecRecordTypeMappingBuilder":
        """Set record_elements list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.record_elements = list(items) if items else []
        return self


    def add_record_element(self, item: any (SenderRecRecord)) -> "SenderRecRecordTypeMappingBuilder":
        """Add a single item to record_elements list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.record_elements.append(item)
        return self

    def clear_record_elements(self) -> "SenderRecRecordTypeMappingBuilder":
        """Clear all items from record_elements list.

        Returns:
            self for method chaining
        """
        self._obj.record_elements = []
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


    def build(self) -> SenderRecRecordTypeMapping:
        """Build and return the SenderRecRecordTypeMapping instance with validation."""
        self._validate_instance()
        pass
        return self._obj