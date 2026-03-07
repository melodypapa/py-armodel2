"""AttributeValueVariationPoint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 617)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 209)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 41)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_VariantHandling_AttributeValueVariationPoints.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import (
    BindingTimeEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PrimitiveIdentifier,
    String,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class AttributeValueVariationPoint(ARObject, ABC):
    """AUTOSAR AttributeValueVariationPoint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    binding_time_enum: Optional[BindingTimeEnum]
    blueprint_value: Optional[String]
    sd: Optional[String]
    short_label: Optional[PrimitiveIdentifier]
    _DESERIALIZE_DISPATCH = {
        "BINDING-TIME-ENUM": lambda obj, elem: setattr(obj, "binding_time_enum", BindingTimeEnum.deserialize(elem)),
        "BLUEPRINT-VALUE": lambda obj, elem: setattr(obj, "blueprint_value", SerializationHelper.deserialize_by_tag(elem, "String")),
        "SD": lambda obj, elem: setattr(obj, "sd", SerializationHelper.deserialize_by_tag(elem, "String")),
        "SHORT-LABEL": lambda obj, elem: setattr(obj, "short_label", SerializationHelper.deserialize_by_tag(elem, "PrimitiveIdentifier")),
    }


    def __init__(self) -> None:
        """Initialize AttributeValueVariationPoint."""
        super().__init__()
        self.binding_time_enum: Optional[BindingTimeEnum] = None
        self.blueprint_value: Optional[String] = None
        self.sd: Optional[String] = None
        self.short_label: Optional[PrimitiveIdentifier] = None

    def serialize(self) -> ET.Element:
        """Serialize AttributeValueVariationPoint to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AttributeValueVariationPoint, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize binding_time_enum
        if self.binding_time_enum is not None:
            serialized = SerializationHelper.serialize_item(self.binding_time_enum, "BindingTimeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BINDING-TIME-ENUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize blueprint_value
        if self.blueprint_value is not None:
            serialized = SerializationHelper.serialize_item(self.blueprint_value, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BLUEPRINT-VALUE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sd
        if self.sd is not None:
            serialized = SerializationHelper.serialize_item(self.sd, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SD")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize short_label
        if self.short_label is not None:
            serialized = SerializationHelper.serialize_item(self.short_label, "PrimitiveIdentifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SHORT-LABEL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AttributeValueVariationPoint":
        """Deserialize XML element to AttributeValueVariationPoint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AttributeValueVariationPoint object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AttributeValueVariationPoint, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "BINDING-TIME-ENUM":
                setattr(obj, "binding_time_enum", BindingTimeEnum.deserialize(child))
            elif tag == "BLUEPRINT-VALUE":
                setattr(obj, "blueprint_value", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "SD":
                setattr(obj, "sd", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "SHORT-LABEL":
                setattr(obj, "short_label", SerializationHelper.deserialize_by_tag(child, "PrimitiveIdentifier"))

        return obj



class AttributeValueVariationPointBuilder(BuilderBase, ABC):
    """Builder for AttributeValueVariationPoint with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: AttributeValueVariationPoint = AttributeValueVariationPoint()


    def with_binding_time_enum(self, value: Optional[BindingTimeEnum]) -> "AttributeValueVariationPointBuilder":
        """Set binding_time_enum attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'binding_time_enum' is required and cannot be None")
        self._obj.binding_time_enum = value
        return self

    def with_blueprint_value(self, value: Optional[String]) -> "AttributeValueVariationPointBuilder":
        """Set blueprint_value attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'blueprint_value' is required and cannot be None")
        self._obj.blueprint_value = value
        return self

    def with_sd(self, value: Optional[String]) -> "AttributeValueVariationPointBuilder":
        """Set sd attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'sd' is required and cannot be None")
        self._obj.sd = value
        return self

    def with_short_label(self, value: Optional[PrimitiveIdentifier]) -> "AttributeValueVariationPointBuilder":
        """Set short_label attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'short_label' is required and cannot be None")
        self._obj.short_label = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "bindingTimeEnum",
        "blueprintValue",
        "sd",
        "shortLabel",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    @abstractmethod
    def build(self) -> AttributeValueVariationPoint:
        """Build and return the AttributeValueVariationPoint instance (abstract)."""
        raise NotImplementedError