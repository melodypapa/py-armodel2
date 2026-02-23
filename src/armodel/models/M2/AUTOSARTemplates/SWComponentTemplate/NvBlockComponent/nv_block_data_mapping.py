"""NvBlockDataMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 688)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_NvBlockComponent.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.autosar_variable_ref import (
    AutosarVariableRef,
)


class NvBlockDataMapping(ARObject):
    """AUTOSAR NvBlockDataMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    bitfield_text_table: Optional[PositiveInteger]
    nv_ram_block_ref: Optional[ARRef]
    read_nv_data_ref: Optional[ARRef]
    written_nv_data_ref: Optional[ARRef]
    written_read_nv_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize NvBlockDataMapping."""
        super().__init__()
        self.bitfield_text_table: Optional[PositiveInteger] = None
        self.nv_ram_block_ref: Optional[ARRef] = None
        self.read_nv_data_ref: Optional[ARRef] = None
        self.written_nv_data_ref: Optional[ARRef] = None
        self.written_read_nv_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize NvBlockDataMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(NvBlockDataMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize bitfield_text_table
        if self.bitfield_text_table is not None:
            serialized = SerializationHelper.serialize_item(self.bitfield_text_table, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BITFIELD-TEXT-TABLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nv_ram_block_ref
        if self.nv_ram_block_ref is not None:
            serialized = SerializationHelper.serialize_item(self.nv_ram_block_ref, "AutosarVariableRef")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NV-RAM-BLOCK-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize read_nv_data_ref
        if self.read_nv_data_ref is not None:
            serialized = SerializationHelper.serialize_item(self.read_nv_data_ref, "AutosarVariableRef")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("READ-NV-DATA-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize written_nv_data_ref
        if self.written_nv_data_ref is not None:
            serialized = SerializationHelper.serialize_item(self.written_nv_data_ref, "AutosarVariableRef")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("WRITTEN-NV-DATA-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize written_read_nv_ref
        if self.written_read_nv_ref is not None:
            serialized = SerializationHelper.serialize_item(self.written_read_nv_ref, "AutosarVariableRef")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("WRITTEN-READ-NV-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "NvBlockDataMapping":
        """Deserialize XML element to NvBlockDataMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized NvBlockDataMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(NvBlockDataMapping, cls).deserialize(element)

        # Parse bitfield_text_table
        child = SerializationHelper.find_child_element(element, "BITFIELD-TEXT-TABLE")
        if child is not None:
            bitfield_text_table_value = child.text
            obj.bitfield_text_table = bitfield_text_table_value

        # Parse nv_ram_block_ref
        child = SerializationHelper.find_child_element(element, "NV-RAM-BLOCK-REF")
        if child is not None:
            nv_ram_block_ref_value = ARRef.deserialize(child)
            obj.nv_ram_block_ref = nv_ram_block_ref_value

        # Parse read_nv_data_ref
        child = SerializationHelper.find_child_element(element, "READ-NV-DATA-REF")
        if child is not None:
            read_nv_data_ref_value = ARRef.deserialize(child)
            obj.read_nv_data_ref = read_nv_data_ref_value

        # Parse written_nv_data_ref
        child = SerializationHelper.find_child_element(element, "WRITTEN-NV-DATA-REF")
        if child is not None:
            written_nv_data_ref_value = ARRef.deserialize(child)
            obj.written_nv_data_ref = written_nv_data_ref_value

        # Parse written_read_nv_ref
        child = SerializationHelper.find_child_element(element, "WRITTEN-READ-NV-REF")
        if child is not None:
            written_read_nv_ref_value = ARRef.deserialize(child)
            obj.written_read_nv_ref = written_read_nv_ref_value

        return obj



class NvBlockDataMappingBuilder(BuilderBase):
    """Builder for NvBlockDataMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: NvBlockDataMapping = NvBlockDataMapping()


    def with_bitfield_text_table(self, value: Optional[PositiveInteger]) -> "NvBlockDataMappingBuilder":
        """Set bitfield_text_table attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.bitfield_text_table = value
        return self

    def with_nv_ram_block(self, value: Optional[AutosarVariableRef]) -> "NvBlockDataMappingBuilder":
        """Set nv_ram_block attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.nv_ram_block = value
        return self

    def with_read_nv_data(self, value: Optional[AutosarVariableRef]) -> "NvBlockDataMappingBuilder":
        """Set read_nv_data attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.read_nv_data = value
        return self

    def with_written_nv_data(self, value: Optional[AutosarVariableRef]) -> "NvBlockDataMappingBuilder":
        """Set written_nv_data attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.written_nv_data = value
        return self

    def with_written_read_nv(self, value: Optional[AutosarVariableRef]) -> "NvBlockDataMappingBuilder":
        """Set written_read_nv attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.written_read_nv = value
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


    def build(self) -> NvBlockDataMapping:
        """Build and return the NvBlockDataMapping instance with validation."""
        self._validate_instance()
        pass
        return self._obj