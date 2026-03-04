"""HwPin AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (page 20)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_EcuResourceTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
    String,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class HwPin(Identifiable):
    """AUTOSAR HwPin."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "HW-PIN"


    function_names: list[String]
    packaging_pin: Optional[String]
    pin_number: Optional[Integer]
    _DESERIALIZE_DISPATCH = {
        "FUNCTION-NAMES": lambda obj, elem: obj.function_names.append(SerializationHelper.deserialize_by_tag(elem, "String")),
        "PACKAGING-PIN": lambda obj, elem: setattr(obj, "packaging_pin", SerializationHelper.deserialize_by_tag(elem, "String")),
        "PIN-NUMBER": lambda obj, elem: setattr(obj, "pin_number", SerializationHelper.deserialize_by_tag(elem, "Integer")),
    }


    def __init__(self) -> None:
        """Initialize HwPin."""
        super().__init__()
        self.function_names: list[String] = []
        self.packaging_pin: Optional[String] = None
        self.pin_number: Optional[Integer] = None

    def serialize(self) -> ET.Element:
        """Serialize HwPin to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(HwPin, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize function_names (list to container "FUNCTION-NAMES")
        if self.function_names:
            wrapper = ET.Element("FUNCTION-NAMES")
            for item in self.function_names:
                serialized = SerializationHelper.serialize_item(item, "String")
                if serialized is not None:
                    child_elem = ET.Element("FUNCTION-NAME")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize packaging_pin
        if self.packaging_pin is not None:
            serialized = SerializationHelper.serialize_item(self.packaging_pin, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PACKAGING-PIN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize pin_number
        if self.pin_number is not None:
            serialized = SerializationHelper.serialize_item(self.pin_number, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PIN-NUMBER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "HwPin":
        """Deserialize XML element to HwPin object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized HwPin object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(HwPin, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "FUNCTION-NAMES":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.function_names.append(SerializationHelper.deserialize_by_tag(item_elem, "String"))
            elif tag == "PACKAGING-PIN":
                setattr(obj, "packaging_pin", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "PIN-NUMBER":
                setattr(obj, "pin_number", SerializationHelper.deserialize_by_tag(child, "Integer"))

        return obj



class HwPinBuilder(IdentifiableBuilder):
    """Builder for HwPin with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: HwPin = HwPin()


    def with_function_names(self, items: list[String]) -> "HwPinBuilder":
        """Set function_names list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.function_names = list(items) if items else []
        return self

    def with_packaging_pin(self, value: Optional[String]) -> "HwPinBuilder":
        """Set packaging_pin attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.packaging_pin = value
        return self

    def with_pin_number(self, value: Optional[Integer]) -> "HwPinBuilder":
        """Set pin_number attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.pin_number = value
        return self


    def add_function_name(self, item: String) -> "HwPinBuilder":
        """Add a single item to function_names list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.function_names.append(item)
        return self

    def clear_function_names(self) -> "HwPinBuilder":
        """Clear all items from function_names list.

        Returns:
            self for method chaining
        """
        self._obj.function_names = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "functionName",
        "packagingPin",
        "pinNumber",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> HwPin:
        """Build and return the HwPin instance with validation."""
        self._validate_instance()
        return self._obj