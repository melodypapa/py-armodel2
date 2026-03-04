"""PduMappingDefaultValue AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 841)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Multiplatform.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Multiplatform.default_value_element import (
    DefaultValueElement,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class PduMappingDefaultValue(ARObject):
    """AUTOSAR PduMappingDefaultValue."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "PDU-MAPPING-DEFAULT-VALUE"


    default_values: list[DefaultValueElement]
    _DESERIALIZE_DISPATCH = {
        "DEFAULT-VALUES": lambda obj, elem: obj.default_values.append(SerializationHelper.deserialize_by_tag(elem, "DefaultValueElement")),
    }


    def __init__(self) -> None:
        """Initialize PduMappingDefaultValue."""
        super().__init__()
        self.default_values: list[DefaultValueElement] = []

    def serialize(self) -> ET.Element:
        """Serialize PduMappingDefaultValue to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(PduMappingDefaultValue, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize default_values (list to container "DEFAULT-VALUES")
        if self.default_values:
            wrapper = ET.Element("DEFAULT-VALUES")
            for item in self.default_values:
                serialized = SerializationHelper.serialize_item(item, "DefaultValueElement")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PduMappingDefaultValue":
        """Deserialize XML element to PduMappingDefaultValue object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PduMappingDefaultValue object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PduMappingDefaultValue, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DEFAULT-VALUES":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.default_values.append(SerializationHelper.deserialize_by_tag(item_elem, "DefaultValueElement"))

        return obj



class PduMappingDefaultValueBuilder(BuilderBase):
    """Builder for PduMappingDefaultValue with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: PduMappingDefaultValue = PduMappingDefaultValue()


    def with_default_values(self, items: list[DefaultValueElement]) -> "PduMappingDefaultValueBuilder":
        """Set default_values list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.default_values = list(items) if items else []
        return self


    def add_default_value(self, item: DefaultValueElement) -> "PduMappingDefaultValueBuilder":
        """Add a single item to default_values list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.default_values.append(item)
        return self

    def clear_default_values(self) -> "PduMappingDefaultValueBuilder":
        """Clear all items from default_values list.

        Returns:
            self for method chaining
        """
        self._obj.default_values = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "defaultValue",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> PduMappingDefaultValue:
        """Build and return the PduMappingDefaultValue instance with validation."""
        self._validate_instance()
        return self._obj