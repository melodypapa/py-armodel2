"""ConditionalChangeNad AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 438)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_configuration_entry import (
    LinConfigurationEntry,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_configuration_entry import LinConfigurationEntryBuilder
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
    PositiveInteger,
)


class ConditionalChangeNad(LinConfigurationEntry):
    """AUTOSAR ConditionalChangeNad."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    byte: Optional[Integer]
    id: Optional[PositiveInteger]
    invert: Optional[Integer]
    mask: Optional[Integer]
    new_nad: Optional[Integer]
    def __init__(self) -> None:
        """Initialize ConditionalChangeNad."""
        super().__init__()
        self.byte: Optional[Integer] = None
        self.id: Optional[PositiveInteger] = None
        self.invert: Optional[Integer] = None
        self.mask: Optional[Integer] = None
        self.new_nad: Optional[Integer] = None

    def serialize(self) -> ET.Element:
        """Serialize ConditionalChangeNad to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ConditionalChangeNad, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize byte
        if self.byte is not None:
            serialized = SerializationHelper.serialize_item(self.byte, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BYTE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize id
        if self.id is not None:
            serialized = SerializationHelper.serialize_item(self.id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize invert
        if self.invert is not None:
            serialized = SerializationHelper.serialize_item(self.invert, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INVERT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mask
        if self.mask is not None:
            serialized = SerializationHelper.serialize_item(self.mask, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MASK")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize new_nad
        if self.new_nad is not None:
            serialized = SerializationHelper.serialize_item(self.new_nad, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NEW-NAD")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ConditionalChangeNad":
        """Deserialize XML element to ConditionalChangeNad object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ConditionalChangeNad object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ConditionalChangeNad, cls).deserialize(element)

        # Parse byte
        child = SerializationHelper.find_child_element(element, "BYTE")
        if child is not None:
            byte_value = child.text
            obj.byte = byte_value

        # Parse id
        child = SerializationHelper.find_child_element(element, "ID")
        if child is not None:
            id_value = child.text
            obj.id = id_value

        # Parse invert
        child = SerializationHelper.find_child_element(element, "INVERT")
        if child is not None:
            invert_value = child.text
            obj.invert = invert_value

        # Parse mask
        child = SerializationHelper.find_child_element(element, "MASK")
        if child is not None:
            mask_value = child.text
            obj.mask = mask_value

        # Parse new_nad
        child = SerializationHelper.find_child_element(element, "NEW-NAD")
        if child is not None:
            new_nad_value = child.text
            obj.new_nad = new_nad_value

        return obj



class ConditionalChangeNadBuilder(LinConfigurationEntryBuilder):
    """Builder for ConditionalChangeNad with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ConditionalChangeNad = ConditionalChangeNad()


    def with_byte(self, value: Optional[Integer]) -> "ConditionalChangeNadBuilder":
        """Set byte attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.byte = value
        return self

    def with_id(self, value: Optional[PositiveInteger]) -> "ConditionalChangeNadBuilder":
        """Set id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.id = value
        return self

    def with_invert(self, value: Optional[Integer]) -> "ConditionalChangeNadBuilder":
        """Set invert attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.invert = value
        return self

    def with_mask(self, value: Optional[Integer]) -> "ConditionalChangeNadBuilder":
        """Set mask attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.mask = value
        return self

    def with_new_nad(self, value: Optional[Integer]) -> "ConditionalChangeNadBuilder":
        """Set new_nad attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.new_nad = value
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


    def build(self) -> ConditionalChangeNad:
        """Build and return the ConditionalChangeNad instance with validation."""
        self._validate_instance()
        pass
        return self._obj