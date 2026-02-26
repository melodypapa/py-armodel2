"""ImplementationDataType AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 320)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 230)
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 299)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 268)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2031)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 47)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 451)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 193)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ImplementationDataTypes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes.abstract_implementation_data_type import (
    AbstractImplementationDataType,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes.abstract_implementation_data_type import AbstractImplementationDataTypeBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    NameToken,
    String,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes.implementation_data_type_element import (
    ImplementationDataTypeElement,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.symbol_props import (
    SymbolProps,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ImplementationDataType(AbstractImplementationDataType):
    """AUTOSAR ImplementationDataType."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    dynamic_array_size_profile: Optional[String]
    is_struct_with_optional_element: Optional[Boolean]
    sub_elements: list[ImplementationDataTypeElement]
    symbol_props: Optional[SymbolProps]
    type_emitter: Optional[NameToken]
    def __init__(self) -> None:
        """Initialize ImplementationDataType."""
        super().__init__()
        self.dynamic_array_size_profile: Optional[String] = None
        self.is_struct_with_optional_element: Optional[Boolean] = None
        self.sub_elements: list[ImplementationDataTypeElement] = []
        self.symbol_props: Optional[SymbolProps] = None
        self.type_emitter: Optional[NameToken] = None

    def serialize(self) -> ET.Element:
        """Serialize ImplementationDataType to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ImplementationDataType, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize dynamic_array_size_profile
        if self.dynamic_array_size_profile is not None:
            serialized = SerializationHelper.serialize_item(self.dynamic_array_size_profile, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DYNAMIC-ARRAY-SIZE-PROFILE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize is_struct_with_optional_element
        if self.is_struct_with_optional_element is not None:
            serialized = SerializationHelper.serialize_item(self.is_struct_with_optional_element, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IS-STRUCT-WITH-OPTIONAL-ELEMENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sub_elements (list to container "SUB-ELEMENTS")
        if self.sub_elements:
            wrapper = ET.Element("SUB-ELEMENTS")
            for item in self.sub_elements:
                serialized = SerializationHelper.serialize_item(item, "ImplementationDataTypeElement")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize symbol_props
        if self.symbol_props is not None:
            serialized = SerializationHelper.serialize_item(self.symbol_props, "SymbolProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SYMBOL-PROPS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize type_emitter
        if self.type_emitter is not None:
            serialized = SerializationHelper.serialize_item(self.type_emitter, "NameToken")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TYPE-EMITTER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ImplementationDataType":
        """Deserialize XML element to ImplementationDataType object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ImplementationDataType object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ImplementationDataType, cls).deserialize(element)

        # Parse dynamic_array_size_profile
        child = SerializationHelper.find_child_element(element, "DYNAMIC-ARRAY-SIZE-PROFILE")
        if child is not None:
            dynamic_array_size_profile_value = child.text
            obj.dynamic_array_size_profile = dynamic_array_size_profile_value

        # Parse is_struct_with_optional_element
        child = SerializationHelper.find_child_element(element, "IS-STRUCT-WITH-OPTIONAL-ELEMENT")
        if child is not None:
            is_struct_with_optional_element_value = child.text
            obj.is_struct_with_optional_element = is_struct_with_optional_element_value

        # Parse sub_elements (list from container "SUB-ELEMENTS")
        obj.sub_elements = []
        container = SerializationHelper.find_child_element(element, "SUB-ELEMENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.sub_elements.append(child_value)

        # Parse symbol_props
        child = SerializationHelper.find_child_element(element, "SYMBOL-PROPS")
        if child is not None:
            symbol_props_value = SerializationHelper.deserialize_by_tag(child, "SymbolProps")
            obj.symbol_props = symbol_props_value

        # Parse type_emitter
        child = SerializationHelper.find_child_element(element, "TYPE-EMITTER")
        if child is not None:
            type_emitter_value = child.text
            obj.type_emitter = type_emitter_value

        return obj



class ImplementationDataTypeBuilder(AbstractImplementationDataTypeBuilder):
    """Builder for ImplementationDataType with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ImplementationDataType = ImplementationDataType()


    def with_dynamic_array_size_profile(self, value: Optional[String]) -> "ImplementationDataTypeBuilder":
        """Set dynamic_array_size_profile attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.dynamic_array_size_profile = value
        return self

    def with_is_struct_with_optional_element(self, value: Optional[Boolean]) -> "ImplementationDataTypeBuilder":
        """Set is_struct_with_optional_element attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.is_struct_with_optional_element = value
        return self

    def with_sub_elements(self, items: list[ImplementationDataTypeElement]) -> "ImplementationDataTypeBuilder":
        """Set sub_elements list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.sub_elements = list(items) if items else []
        return self

    def with_symbol_props(self, value: Optional[SymbolProps]) -> "ImplementationDataTypeBuilder":
        """Set symbol_props attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.symbol_props = value
        return self

    def with_type_emitter(self, value: Optional[NameToken]) -> "ImplementationDataTypeBuilder":
        """Set type_emitter attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.type_emitter = value
        return self


    def add_sub_element(self, item: ImplementationDataTypeElement) -> "ImplementationDataTypeBuilder":
        """Add a single item to sub_elements list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.sub_elements.append(item)
        return self

    def clear_sub_elements(self) -> "ImplementationDataTypeBuilder":
        """Clear all items from sub_elements list.

        Returns:
            self for method chaining
        """
        self._obj.sub_elements = []
        return self



    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

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


    def build(self) -> ImplementationDataType:
        """Build and return the ImplementationDataType instance with validation."""
        self._validate_instance()
        pass
        return self._obj