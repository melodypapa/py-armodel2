"""DynamicPart AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 410)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.multiplexed_part import (
    MultiplexedPart,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.multiplexed_part import MultiplexedPartBuilder
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.dynamic_part_alternative import (
    DynamicPartAlternative,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DynamicPart(MultiplexedPart):
    """AUTOSAR DynamicPart."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DYNAMIC-PART"


    dynamic_parts: list[DynamicPartAlternative]
    _DESERIALIZE_DISPATCH = {
        "DYNAMIC-PARTS": lambda obj, elem: obj.dynamic_parts.append(SerializationHelper.deserialize_by_tag(elem, "DynamicPartAlternative")),
    }


    def __init__(self) -> None:
        """Initialize DynamicPart."""
        super().__init__()
        self.dynamic_parts: list[DynamicPartAlternative] = []

    def serialize(self) -> ET.Element:
        """Serialize DynamicPart to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DynamicPart, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize dynamic_parts (list to container "DYNAMIC-PARTS")
        if self.dynamic_parts:
            wrapper = ET.Element("DYNAMIC-PARTS")
            for item in self.dynamic_parts:
                serialized = SerializationHelper.serialize_item(item, "DynamicPartAlternative")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DynamicPart":
        """Deserialize XML element to DynamicPart object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DynamicPart object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DynamicPart, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DYNAMIC-PARTS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.dynamic_parts.append(SerializationHelper.deserialize_by_tag(item_elem, "DynamicPartAlternative"))

        return obj



class DynamicPartBuilder(MultiplexedPartBuilder):
    """Builder for DynamicPart with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DynamicPart = DynamicPart()


    def with_dynamic_parts(self, items: list[DynamicPartAlternative]) -> "DynamicPartBuilder":
        """Set dynamic_parts list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.dynamic_parts = list(items) if items else []
        return self


    def add_dynamic_part(self, item: DynamicPartAlternative) -> "DynamicPartBuilder":
        """Add a single item to dynamic_parts list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.dynamic_parts.append(item)
        return self

    def clear_dynamic_parts(self) -> "DynamicPartBuilder":
        """Clear all items from dynamic_parts list.

        Returns:
            self for method chaining
        """
        self._obj.dynamic_parts = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "dynamicPart",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DynamicPart:
        """Build and return the DynamicPart instance with validation."""
        self._validate_instance()
        return self._obj