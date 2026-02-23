"""BaseTypeDirectDefinition AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 302)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 290)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2002)
  - AUTOSAR_FO_TPS_LogAndTraceExtract.pdf (page 29)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_BaseTypes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.AsamHdo.BaseTypes.base_type_definition import (
    BaseTypeDefinition,
)
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.MSR.AsamHdo.BaseTypes.base_type_definition import BaseTypeDefinitionBuilder
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ByteOrderEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NativeDeclarationString,
    PositiveInteger,
)
from armodel.models.M2.MSR.AsamHdo.BaseTypes import (
    BaseTypeEncodingString,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class BaseTypeDirectDefinition(BaseTypeDefinition):
    """AUTOSAR BaseTypeDirectDefinition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    base_type_encoding: Optional[BaseTypeEncodingString]
    base_type_size: Optional[PositiveInteger]
    byte_order: Optional[ByteOrderEnum]
    mem_alignment: Optional[PositiveInteger]
    native: Optional[NativeDeclarationString]
    def __init__(self) -> None:
        """Initialize BaseTypeDirectDefinition."""
        super().__init__()
        self.base_type_encoding: Optional[BaseTypeEncodingString] = None
        self.base_type_size: Optional[PositiveInteger] = None
        self.byte_order: Optional[ByteOrderEnum] = None
        self.mem_alignment: Optional[PositiveInteger] = None
        self.native: Optional[NativeDeclarationString] = None

    def serialize(self) -> ET.Element:
        """Serialize BaseTypeDirectDefinition to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BaseTypeDirectDefinition, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize base_type_encoding
        if self.base_type_encoding is not None:
            serialized = SerializationHelper.serialize_item(self.base_type_encoding, "BaseTypeEncodingString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BASE-TYPE-ENCODING")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize base_type_size
        if self.base_type_size is not None:
            serialized = SerializationHelper.serialize_item(self.base_type_size, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BASE-TYPE-SIZE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize byte_order
        if self.byte_order is not None:
            serialized = SerializationHelper.serialize_item(self.byte_order, "ByteOrderEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BYTE-ORDER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mem_alignment
        if self.mem_alignment is not None:
            serialized = SerializationHelper.serialize_item(self.mem_alignment, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MEM-ALIGNMENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize native
        if self.native is not None:
            serialized = SerializationHelper.serialize_item(self.native, "NativeDeclarationString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NATIVE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BaseTypeDirectDefinition":
        """Deserialize XML element to BaseTypeDirectDefinition object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BaseTypeDirectDefinition object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BaseTypeDirectDefinition, cls).deserialize(element)

        # Parse base_type_encoding
        child = SerializationHelper.find_child_element(element, "BASE-TYPE-ENCODING")
        if child is not None:
            base_type_encoding_value = child.text
            obj.base_type_encoding = base_type_encoding_value

        # Parse base_type_size
        child = SerializationHelper.find_child_element(element, "BASE-TYPE-SIZE")
        if child is not None:
            base_type_size_value = child.text
            obj.base_type_size = base_type_size_value

        # Parse byte_order
        child = SerializationHelper.find_child_element(element, "BYTE-ORDER")
        if child is not None:
            byte_order_value = ByteOrderEnum.deserialize(child)
            obj.byte_order = byte_order_value

        # Parse mem_alignment
        child = SerializationHelper.find_child_element(element, "MEM-ALIGNMENT")
        if child is not None:
            mem_alignment_value = child.text
            obj.mem_alignment = mem_alignment_value

        # Parse native
        child = SerializationHelper.find_child_element(element, "NATIVE")
        if child is not None:
            native_value = child.text
            obj.native = native_value

        return obj



class BaseTypeDirectDefinitionBuilder(BaseTypeDefinitionBuilder):
    """Builder for BaseTypeDirectDefinition with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: BaseTypeDirectDefinition = BaseTypeDirectDefinition()


    def with_base_type_encoding(self, value: Optional[BaseTypeEncodingString]) -> "BaseTypeDirectDefinitionBuilder":
        """Set base_type_encoding attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.base_type_encoding = value
        return self

    def with_base_type_size(self, value: Optional[PositiveInteger]) -> "BaseTypeDirectDefinitionBuilder":
        """Set base_type_size attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.base_type_size = value
        return self

    def with_byte_order(self, value: Optional[ByteOrderEnum]) -> "BaseTypeDirectDefinitionBuilder":
        """Set byte_order attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.byte_order = value
        return self

    def with_mem_alignment(self, value: Optional[PositiveInteger]) -> "BaseTypeDirectDefinitionBuilder":
        """Set mem_alignment attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.mem_alignment = value
        return self

    def with_native(self, value: Optional[NativeDeclarationString]) -> "BaseTypeDirectDefinitionBuilder":
        """Set native attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.native = value
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


    def build(self) -> BaseTypeDirectDefinition:
        """Build and return the BaseTypeDirectDefinition instance with validation."""
        self._validate_instance()
        pass
        return self._obj