"""Linker AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 134)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 622)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Implementation.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class Linker(Identifiable):
    """AUTOSAR Linker."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "LINKER"


    name: Optional[String]
    options: Optional[String]
    vendor: Optional[String]
    version: Optional[String]
    _DESERIALIZE_DISPATCH = {
        "NAME": lambda obj, elem: setattr(obj, "name", SerializationHelper.deserialize_by_tag(elem, "String")),
        "OPTIONS": lambda obj, elem: setattr(obj, "options", SerializationHelper.deserialize_by_tag(elem, "String")),
        "VENDOR": lambda obj, elem: setattr(obj, "vendor", SerializationHelper.deserialize_by_tag(elem, "String")),
        "VERSION": lambda obj, elem: setattr(obj, "version", SerializationHelper.deserialize_by_tag(elem, "String")),
    }


    def __init__(self) -> None:
        """Initialize Linker."""
        super().__init__()
        self.name: Optional[String] = None
        self.options: Optional[String] = None
        self.vendor: Optional[String] = None
        self.version: Optional[String] = None

    def serialize(self) -> ET.Element:
        """Serialize Linker to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Linker, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize name
        if self.name is not None:
            serialized = SerializationHelper.serialize_item(self.name, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NAME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize options
        if self.options is not None:
            serialized = SerializationHelper.serialize_item(self.options, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("OPTIONS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize vendor
        if self.vendor is not None:
            serialized = SerializationHelper.serialize_item(self.vendor, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VENDOR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize version
        if self.version is not None:
            serialized = SerializationHelper.serialize_item(self.version, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VERSION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Linker":
        """Deserialize XML element to Linker object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Linker object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Linker, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "NAME":
                setattr(obj, "name", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "OPTIONS":
                setattr(obj, "options", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "VENDOR":
                setattr(obj, "vendor", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "VERSION":
                setattr(obj, "version", SerializationHelper.deserialize_by_tag(child, "String"))

        return obj



class LinkerBuilder(IdentifiableBuilder):
    """Builder for Linker with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: Linker = Linker()


    def with_name(self, value: Optional[String]) -> "LinkerBuilder":
        """Set name attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.name = value
        return self

    def with_options(self, value: Optional[String]) -> "LinkerBuilder":
        """Set options attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.options = value
        return self

    def with_vendor(self, value: Optional[String]) -> "LinkerBuilder":
        """Set vendor attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.vendor = value
        return self

    def with_version(self, value: Optional[String]) -> "LinkerBuilder":
        """Set version attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.version = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "name",
        "options",
        "vendor",
        "version",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> Linker:
        """Build and return the Linker instance with validation."""
        self._validate_instance()
        return self._obj