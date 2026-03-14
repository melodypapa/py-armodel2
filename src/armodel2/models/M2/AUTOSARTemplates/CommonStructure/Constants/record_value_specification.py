"""RecordValueSpecification AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 328)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 435)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Constants.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Constants.composite_value_specification import (
    CompositeValueSpecification,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Constants.composite_value_specification import CompositeValueSpecificationBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class RecordValueSpecification(CompositeValueSpecification):
    """AUTOSAR RecordValueSpecification."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "RECORD-VALUE-SPECIFICATION"


    fields: list[ValueSpecification ]
    _DESERIALIZE_DISPATCH = {
        "FIELDS": lambda obj, elem: obj.fields.append(SerializationHelper.deserialize_by_tag(elem, "ValueSpecification ")),
    }


    def __init__(self) -> None:
        """Initialize RecordValueSpecification."""
        super().__init__()
        self.fields: list[ValueSpecification ] = []

    def serialize(self) -> ET.Element:
        """Serialize RecordValueSpecification to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(RecordValueSpecification, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize fields (list to container "FIELDS")
        if self.fields:
            wrapper = ET.Element("FIELDS")
            for item in self.fields:
                serialized = SerializationHelper.serialize_item(item, "ValueSpecification ")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RecordValueSpecification":
        """Deserialize XML element to RecordValueSpecification object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RecordValueSpecification object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(RecordValueSpecification, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "FIELDS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.fields.append(SerializationHelper.deserialize_by_tag(item_elem, "ValueSpecification "))

        return obj



class RecordValueSpecificationBuilder(CompositeValueSpecificationBuilder):
    """Builder for RecordValueSpecification with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: RecordValueSpecification = RecordValueSpecification()


    def with_fields(self, items: list[ValueSpecification]) -> "RecordValueSpecificationBuilder":
        """Set fields list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.fields = list(items) if items else []
        return self


    def add_field(self, item: ValueSpecification) -> "RecordValueSpecificationBuilder":
        """Add a single item to fields list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.fields.append(item)
        return self

    def clear_fields(self) -> "RecordValueSpecificationBuilder":
        """Clear all items from fields list.

        Returns:
            self for method chaining
        """
        self._obj.fields = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "field",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> RecordValueSpecification:
        """Build and return the RecordValueSpecification instance with validation."""
        self._validate_instance()
        return self._obj