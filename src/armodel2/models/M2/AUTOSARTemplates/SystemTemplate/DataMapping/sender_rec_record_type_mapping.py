"""SenderRecRecordTypeMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 235)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_DataMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.sender_rec_composite_type_mapping import (
    SenderRecCompositeTypeMapping,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.sender_rec_composite_type_mapping import SenderRecCompositeTypeMappingBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SenderRecRecordTypeMapping(SenderRecCompositeTypeMapping):
    """AUTOSAR SenderRecRecordTypeMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SENDER-REC-RECORD-TYPE-MAPPING"


    record_elements: list[Any]
    _DESERIALIZE_DISPATCH = {
        "RECORD-ELEMENTS": lambda obj, elem: obj.record_elements.append(SerializationHelper.deserialize_by_tag(elem, "any (SenderRecRecord)")),
    }


    def __init__(self) -> None:
        """Initialize SenderRecRecordTypeMapping."""
        super().__init__()
        self.record_elements: list[Any] = []

    def serialize(self) -> ET.Element:
        """Serialize SenderRecRecordTypeMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "RECORD-ELEMENTS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.record_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "any (SenderRecRecord)"))

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


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "recordElement",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> SenderRecRecordTypeMapping:
        """Build and return the SenderRecRecordTypeMapping instance with validation."""
        self._validate_instance()
        return self._obj