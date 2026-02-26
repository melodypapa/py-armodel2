"""ImplementationDataTypeElement AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 321)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 269)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2032)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 452)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ImplementationDataTypes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes.abstract_implementation_data_type_element import (
    AbstractImplementationDataTypeElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes.abstract_implementation_data_type_element import AbstractImplementationDataTypeElementBuilder
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes import (
    ArrayImplPolicyEnum,
    ArraySizeSemanticsEnum,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes import (
    ArraySizeHandlingEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)

if TYPE_CHECKING:
    from armodel2.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
        SwDataDefProps,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class ImplementationDataTypeElement(AbstractImplementationDataTypeElement):
    """AUTOSAR ImplementationDataTypeElement."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    array_impl_policy_enum: Optional[ArrayImplPolicyEnum]
    array_size: Optional[ArraySizeSemanticsEnum]
    array_size_handling: Optional[ArraySizeHandlingEnum]
    is_optional: Optional[Boolean]
    sub_elements: list[Any]
    sw_data_def: Optional[SwDataDefProps]
    def __init__(self) -> None:
        """Initialize ImplementationDataTypeElement."""
        super().__init__()
        self.array_impl_policy_enum: Optional[ArrayImplPolicyEnum] = None
        self.array_size: Optional[ArraySizeSemanticsEnum] = None
        self.array_size_handling: Optional[ArraySizeHandlingEnum] = None
        self.is_optional: Optional[Boolean] = None
        self.sub_elements: list[Any] = []
        self.sw_data_def: Optional[SwDataDefProps] = None

    def serialize(self) -> ET.Element:
        """Serialize ImplementationDataTypeElement to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ImplementationDataTypeElement, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize array_impl_policy_enum
        if self.array_impl_policy_enum is not None:
            serialized = SerializationHelper.serialize_item(self.array_impl_policy_enum, "ArrayImplPolicyEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ARRAY-IMPL-POLICY-ENUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize array_size
        if self.array_size is not None:
            serialized = SerializationHelper.serialize_item(self.array_size, "ArraySizeSemanticsEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ARRAY-SIZE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize array_size_handling
        if self.array_size_handling is not None:
            serialized = SerializationHelper.serialize_item(self.array_size_handling, "ArraySizeHandlingEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ARRAY-SIZE-HANDLING")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize is_optional
        if self.is_optional is not None:
            serialized = SerializationHelper.serialize_item(self.is_optional, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IS-OPTIONAL")
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
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize sw_data_def
        if self.sw_data_def is not None:
            serialized = SerializationHelper.serialize_item(self.sw_data_def, "SwDataDefProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-DATA-DEF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ImplementationDataTypeElement":
        """Deserialize XML element to ImplementationDataTypeElement object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ImplementationDataTypeElement object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ImplementationDataTypeElement, cls).deserialize(element)

        # Parse array_impl_policy_enum
        child = SerializationHelper.find_child_element(element, "ARRAY-IMPL-POLICY-ENUM")
        if child is not None:
            array_impl_policy_enum_value = ArrayImplPolicyEnum.deserialize(child)
            obj.array_impl_policy_enum = array_impl_policy_enum_value

        # Parse array_size
        child = SerializationHelper.find_child_element(element, "ARRAY-SIZE")
        if child is not None:
            array_size_value = ArraySizeSemanticsEnum.deserialize(child)
            obj.array_size = array_size_value

        # Parse array_size_handling
        child = SerializationHelper.find_child_element(element, "ARRAY-SIZE-HANDLING")
        if child is not None:
            array_size_handling_value = ArraySizeHandlingEnum.deserialize(child)
            obj.array_size_handling = array_size_handling_value

        # Parse is_optional
        child = SerializationHelper.find_child_element(element, "IS-OPTIONAL")
        if child is not None:
            is_optional_value = child.text
            obj.is_optional = is_optional_value

        # Parse sub_elements (list from container "SUB-ELEMENTS")
        obj.sub_elements = []
        container = SerializationHelper.find_child_element(element, "SUB-ELEMENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.sub_elements.append(child_value)

        # Parse sw_data_def
        child = SerializationHelper.find_child_element(element, "SW-DATA-DEF")
        if child is not None:
            sw_data_def_value = SerializationHelper.deserialize_by_tag(child, "SwDataDefProps")
            obj.sw_data_def = sw_data_def_value

        return obj



class ImplementationDataTypeElementBuilder(AbstractImplementationDataTypeElementBuilder):
    """Builder for ImplementationDataTypeElement with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ImplementationDataTypeElement = ImplementationDataTypeElement()


    def with_array_impl_policy_enum(self, value: Optional[ArrayImplPolicyEnum]) -> "ImplementationDataTypeElementBuilder":
        """Set array_impl_policy_enum attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.array_impl_policy_enum = value
        return self

    def with_array_size(self, value: Optional[ArraySizeSemanticsEnum]) -> "ImplementationDataTypeElementBuilder":
        """Set array_size attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.array_size = value
        return self

    def with_array_size_handling(self, value: Optional[ArraySizeHandlingEnum]) -> "ImplementationDataTypeElementBuilder":
        """Set array_size_handling attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.array_size_handling = value
        return self

    def with_is_optional(self, value: Optional[Boolean]) -> "ImplementationDataTypeElementBuilder":
        """Set is_optional attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.is_optional = value
        return self

    def with_sub_elements(self, items: list[any (ImplementationData)]) -> "ImplementationDataTypeElementBuilder":
        """Set sub_elements list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.sub_elements = list(items) if items else []
        return self

    def with_sw_data_def(self, value: Optional[SwDataDefProps]) -> "ImplementationDataTypeElementBuilder":
        """Set sw_data_def attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_data_def = value
        return self


    def add_sub_element(self, item: any (ImplementationData)) -> "ImplementationDataTypeElementBuilder":
        """Add a single item to sub_elements list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.sub_elements.append(item)
        return self

    def clear_sub_elements(self) -> "ImplementationDataTypeElementBuilder":
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


    def build(self) -> ImplementationDataTypeElement:
        """Build and return the ImplementationDataTypeElement instance with validation."""
        self._validate_instance()
        pass
        return self._obj