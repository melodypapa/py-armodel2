"""HwAttributeDef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (page 26)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_EcuResourceTemplate_HwElementCategory.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel2.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementCategory.hw_attribute_literal_def import (
    HwAttributeLiteralDef,
)
from armodel2.models.M2.MSR.AsamHdo.Units.unit import (
    Unit,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class HwAttributeDef(Identifiable):
    """AUTOSAR HwAttributeDef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "HW-ATTRIBUTE-DEF"


    hw_attributes: list[HwAttributeLiteralDef]
    is_required: Optional[Boolean]
    unit_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "HW-ATTRIBUTES": lambda obj, elem: obj.hw_attributes.append(SerializationHelper.deserialize_by_tag(elem, "HwAttributeLiteralDef")),
        "IS-REQUIRED": lambda obj, elem: setattr(obj, "is_required", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "UNIT-REF": lambda obj, elem: setattr(obj, "unit_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize HwAttributeDef."""
        super().__init__()
        self.hw_attributes: list[HwAttributeLiteralDef] = []
        self.is_required: Optional[Boolean] = None
        self.unit_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize HwAttributeDef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(HwAttributeDef, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize hw_attributes (list to container "HW-ATTRIBUTES")
        if self.hw_attributes:
            wrapper = ET.Element("HW-ATTRIBUTES")
            for item in self.hw_attributes:
                serialized = SerializationHelper.serialize_item(item, "HwAttributeLiteralDef")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize is_required
        if self.is_required is not None:
            serialized = SerializationHelper.serialize_item(self.is_required, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IS-REQUIRED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize unit_ref
        if self.unit_ref is not None:
            serialized = SerializationHelper.serialize_item(self.unit_ref, "Unit")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("UNIT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "HwAttributeDef":
        """Deserialize XML element to HwAttributeDef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized HwAttributeDef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(HwAttributeDef, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "HW-ATTRIBUTES":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.hw_attributes.append(SerializationHelper.deserialize_by_tag(item_elem, "HwAttributeLiteralDef"))
            elif tag == "IS-REQUIRED":
                setattr(obj, "is_required", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "UNIT-REF":
                setattr(obj, "unit_ref", ARRef.deserialize(child))

        return obj



class HwAttributeDefBuilder(IdentifiableBuilder):
    """Builder for HwAttributeDef with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: HwAttributeDef = HwAttributeDef()


    def with_hw_attributes(self, items: list[HwAttributeLiteralDef]) -> "HwAttributeDefBuilder":
        """Set hw_attributes list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.hw_attributes = list(items) if items else []
        return self

    def with_is_required(self, value: Optional[Boolean]) -> "HwAttributeDefBuilder":
        """Set is_required attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.is_required = value
        return self

    def with_unit(self, value: Optional[Unit]) -> "HwAttributeDefBuilder":
        """Set unit attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.unit = value
        return self


    def add_hw_attribute(self, item: HwAttributeLiteralDef) -> "HwAttributeDefBuilder":
        """Add a single item to hw_attributes list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.hw_attributes.append(item)
        return self

    def clear_hw_attributes(self) -> "HwAttributeDefBuilder":
        """Clear all items from hw_attributes list.

        Returns:
            self for method chaining
        """
        self._obj.hw_attributes = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "hwAttribute",
        "isRequired",
        "unit",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> HwAttributeDef:
        """Build and return the HwAttributeDef instance with validation."""
        self._validate_instance()
        return self._obj