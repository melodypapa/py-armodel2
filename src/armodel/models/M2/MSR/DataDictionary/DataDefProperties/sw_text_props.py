"""SwTextProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 343)
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 313)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 249)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 216)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_DataDefProperties.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes import (
    ArraySizeSemanticsEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel.models.M2.MSR.AsamHdo.BaseTypes.sw_base_type import (
    SwBaseType,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class SwTextProps(ARObject):
    """AUTOSAR SwTextProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    array_size: Optional[ArraySizeSemanticsEnum]
    base_type_ref: Optional[ARRef]
    sw_fill_character: Optional[Integer]
    sw_max_text_size: Optional[Integer]
    def __init__(self) -> None:
        """Initialize SwTextProps."""
        super().__init__()
        self.array_size: Optional[ArraySizeSemanticsEnum] = None
        self.base_type_ref: Optional[ARRef] = None
        self.sw_fill_character: Optional[Integer] = None
        self.sw_max_text_size: Optional[Integer] = None

    def serialize(self) -> ET.Element:
        """Serialize SwTextProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwTextProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

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

        # Serialize base_type_ref
        if self.base_type_ref is not None:
            serialized = SerializationHelper.serialize_item(self.base_type_ref, "SwBaseType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BASE-TYPE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_fill_character
        if self.sw_fill_character is not None:
            serialized = SerializationHelper.serialize_item(self.sw_fill_character, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-FILL-CHARACTER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_max_text_size
        if self.sw_max_text_size is not None:
            serialized = SerializationHelper.serialize_item(self.sw_max_text_size, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-MAX-TEXT-SIZE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwTextProps":
        """Deserialize XML element to SwTextProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwTextProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwTextProps, cls).deserialize(element)

        # Parse array_size
        child = SerializationHelper.find_child_element(element, "ARRAY-SIZE")
        if child is not None:
            array_size_value = ArraySizeSemanticsEnum.deserialize(child)
            obj.array_size = array_size_value

        # Parse base_type_ref
        child = SerializationHelper.find_child_element(element, "BASE-TYPE-REF")
        if child is not None:
            base_type_ref_value = ARRef.deserialize(child)
            obj.base_type_ref = base_type_ref_value

        # Parse sw_fill_character
        child = SerializationHelper.find_child_element(element, "SW-FILL-CHARACTER")
        if child is not None:
            sw_fill_character_value = child.text
            obj.sw_fill_character = sw_fill_character_value

        # Parse sw_max_text_size
        child = SerializationHelper.find_child_element(element, "SW-MAX-TEXT-SIZE")
        if child is not None:
            sw_max_text_size_value = child.text
            obj.sw_max_text_size = sw_max_text_size_value

        return obj



class SwTextPropsBuilder(BuilderBase):
    """Builder for SwTextProps with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SwTextProps = SwTextProps()


    def with_array_size(self, value: Optional[ArraySizeSemanticsEnum]) -> "SwTextPropsBuilder":
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

    def with_base_type(self, value: Optional[SwBaseType]) -> "SwTextPropsBuilder":
        """Set base_type attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.base_type = value
        return self

    def with_sw_fill_character(self, value: Optional[Integer]) -> "SwTextPropsBuilder":
        """Set sw_fill_character attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_fill_character = value
        return self

    def with_sw_max_text_size(self, value: Optional[Integer]) -> "SwTextPropsBuilder":
        """Set sw_max_text_size attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_max_text_size = value
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


    def build(self) -> SwTextProps:
        """Build and return the SwTextProps instance with validation."""
        self._validate_instance()
        pass
        return self._obj