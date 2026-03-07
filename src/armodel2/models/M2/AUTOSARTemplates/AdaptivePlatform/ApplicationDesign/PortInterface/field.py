"""Field AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 45)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_AdaptivePlatform_ApplicationDesign_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.autosar_data_prototype import (
    AutosarDataPrototype,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.autosar_data_prototype import AutosarDataPrototypeBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class Field(AutosarDataPrototype):
    """AUTOSAR Field."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "FIELD"


    has_getter: Optional[Boolean]
    has_notifier: Optional[Boolean]
    has_setter: Optional[Boolean]
    _DESERIALIZE_DISPATCH = {
        "HAS-GETTER": lambda obj, elem: setattr(obj, "has_getter", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "HAS-NOTIFIER": lambda obj, elem: setattr(obj, "has_notifier", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "HAS-SETTER": lambda obj, elem: setattr(obj, "has_setter", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
    }


    def __init__(self) -> None:
        """Initialize Field."""
        super().__init__()
        self.has_getter: Optional[Boolean] = None
        self.has_notifier: Optional[Boolean] = None
        self.has_setter: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize Field to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Field, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize has_getter
        if self.has_getter is not None:
            serialized = SerializationHelper.serialize_item(self.has_getter, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HAS-GETTER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize has_notifier
        if self.has_notifier is not None:
            serialized = SerializationHelper.serialize_item(self.has_notifier, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HAS-NOTIFIER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize has_setter
        if self.has_setter is not None:
            serialized = SerializationHelper.serialize_item(self.has_setter, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HAS-SETTER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Field":
        """Deserialize XML element to Field object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Field object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Field, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "HAS-GETTER":
                setattr(obj, "has_getter", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "HAS-NOTIFIER":
                setattr(obj, "has_notifier", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "HAS-SETTER":
                setattr(obj, "has_setter", SerializationHelper.deserialize_by_tag(child, "Boolean"))

        return obj



class FieldBuilder(AutosarDataPrototypeBuilder):
    """Builder for Field with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: Field = Field()


    def with_has_getter(self, value: Optional[Boolean]) -> "FieldBuilder":
        """Set has_getter attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'has_getter' is required and cannot be None")
        self._obj.has_getter = value
        return self

    def with_has_notifier(self, value: Optional[Boolean]) -> "FieldBuilder":
        """Set has_notifier attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'has_notifier' is required and cannot be None")
        self._obj.has_notifier = value
        return self

    def with_has_setter(self, value: Optional[Boolean]) -> "FieldBuilder":
        """Set has_setter attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'has_setter' is required and cannot be None")
        self._obj.has_setter = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "hasGetter",
        "hasNotifier",
        "hasSetter",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> Field:
        """Build and return the Field instance with validation."""
        self._validate_instance()
        return self._obj