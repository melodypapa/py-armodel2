"""Linker AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 134)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 622)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Implementation.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class Linker(Identifiable):
    """AUTOSAR Linker."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    name: Optional[String]
    options: Optional[String]
    vendor: Optional[String]
    version: Optional[String]
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
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

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

        # Parse name
        child = SerializationHelper.find_child_element(element, "NAME")
        if child is not None:
            name_value = child.text
            obj.name = name_value

        # Parse options
        child = SerializationHelper.find_child_element(element, "OPTIONS")
        if child is not None:
            options_value = child.text
            obj.options = options_value

        # Parse vendor
        child = SerializationHelper.find_child_element(element, "VENDOR")
        if child is not None:
            vendor_value = child.text
            obj.vendor = vendor_value

        # Parse version
        child = SerializationHelper.find_child_element(element, "VERSION")
        if child is not None:
            version_value = child.text
            obj.version = version_value

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


    def build(self) -> Linker:
        """Build and return the Linker instance with validation."""
        self._validate_instance()
        pass
        return self._obj