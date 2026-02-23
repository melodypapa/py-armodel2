"""PortAPIOption AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 589)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2045)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_PortAPIOptions.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.data_transformation import (
    DataTransformation,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PortAPIOptions.port_defined_argument_value import (
    PortDefinedArgumentValue,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PortAPIOptions.swc_supported_feature import (
    SwcSupportedFeature,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class PortAPIOption(ARObject):
    """AUTOSAR PortAPIOption."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    enable_take: Optional[Boolean]
    error_handling: Optional[DataTransformation]
    indirect_api: Optional[Boolean]
    port_ref: Optional[ARRef]
    port_arg_values: list[PortDefinedArgumentValue]
    supporteds: list[SwcSupportedFeature]
    transformer: Optional[DataTransformation]
    def __init__(self) -> None:
        """Initialize PortAPIOption."""
        super().__init__()
        self.enable_take: Optional[Boolean] = None
        self.error_handling: Optional[DataTransformation] = None
        self.indirect_api: Optional[Boolean] = None
        self.port_ref: Optional[ARRef] = None
        self.port_arg_values: list[PortDefinedArgumentValue] = []
        self.supporteds: list[SwcSupportedFeature] = []
        self.transformer: Optional[DataTransformation] = None

    def serialize(self) -> ET.Element:
        """Serialize PortAPIOption to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(PortAPIOption, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize enable_take
        if self.enable_take is not None:
            serialized = SerializationHelper.serialize_item(self.enable_take, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ENABLE-TAKE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize error_handling
        if self.error_handling is not None:
            serialized = SerializationHelper.serialize_item(self.error_handling, "DataTransformation")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ERROR-HANDLING")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize indirect_api
        if self.indirect_api is not None:
            serialized = SerializationHelper.serialize_item(self.indirect_api, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INDIRECT-API")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize port_ref
        if self.port_ref is not None:
            serialized = SerializationHelper.serialize_item(self.port_ref, "PortPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PORT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize port_arg_values (list to container "PORT-ARG-VALUES")
        if self.port_arg_values:
            wrapper = ET.Element("PORT-ARG-VALUES")
            for item in self.port_arg_values:
                serialized = SerializationHelper.serialize_item(item, "PortDefinedArgumentValue")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize supporteds (list to container "SUPPORTEDS")
        if self.supporteds:
            wrapper = ET.Element("SUPPORTEDS")
            for item in self.supporteds:
                serialized = SerializationHelper.serialize_item(item, "SwcSupportedFeature")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize transformer
        if self.transformer is not None:
            serialized = SerializationHelper.serialize_item(self.transformer, "DataTransformation")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TRANSFORMER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PortAPIOption":
        """Deserialize XML element to PortAPIOption object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PortAPIOption object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PortAPIOption, cls).deserialize(element)

        # Parse enable_take
        child = SerializationHelper.find_child_element(element, "ENABLE-TAKE")
        if child is not None:
            enable_take_value = child.text
            obj.enable_take = enable_take_value

        # Parse error_handling
        child = SerializationHelper.find_child_element(element, "ERROR-HANDLING")
        if child is not None:
            error_handling_value = SerializationHelper.deserialize_by_tag(child, "DataTransformation")
            obj.error_handling = error_handling_value

        # Parse indirect_api
        child = SerializationHelper.find_child_element(element, "INDIRECT-API")
        if child is not None:
            indirect_api_value = child.text
            obj.indirect_api = indirect_api_value

        # Parse port_ref
        child = SerializationHelper.find_child_element(element, "PORT-REF")
        if child is not None:
            port_ref_value = ARRef.deserialize(child)
            obj.port_ref = port_ref_value

        # Parse port_arg_values (list from container "PORT-ARG-VALUES")
        obj.port_arg_values = []
        container = SerializationHelper.find_child_element(element, "PORT-ARG-VALUES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.port_arg_values.append(child_value)

        # Parse supporteds (list from container "SUPPORTEDS")
        obj.supporteds = []
        container = SerializationHelper.find_child_element(element, "SUPPORTEDS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.supporteds.append(child_value)

        # Parse transformer
        child = SerializationHelper.find_child_element(element, "TRANSFORMER")
        if child is not None:
            transformer_value = SerializationHelper.deserialize_by_tag(child, "DataTransformation")
            obj.transformer = transformer_value

        return obj



class PortAPIOptionBuilder(BuilderBase):
    """Builder for PortAPIOption with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: PortAPIOption = PortAPIOption()


    def with_enable_take(self, value: Optional[Boolean]) -> "PortAPIOptionBuilder":
        """Set enable_take attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.enable_take = value
        return self

    def with_error_handling(self, value: Optional[DataTransformation]) -> "PortAPIOptionBuilder":
        """Set error_handling attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.error_handling = value
        return self

    def with_indirect_api(self, value: Optional[Boolean]) -> "PortAPIOptionBuilder":
        """Set indirect_api attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.indirect_api = value
        return self

    def with_port(self, value: Optional[PortPrototype]) -> "PortAPIOptionBuilder":
        """Set port attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.port = value
        return self

    def with_port_arg_values(self, items: list[PortDefinedArgumentValue]) -> "PortAPIOptionBuilder":
        """Set port_arg_values list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.port_arg_values = list(items) if items else []
        return self

    def with_supporteds(self, items: list[SwcSupportedFeature]) -> "PortAPIOptionBuilder":
        """Set supporteds list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.supporteds = list(items) if items else []
        return self

    def with_transformer(self, value: Optional[DataTransformation]) -> "PortAPIOptionBuilder":
        """Set transformer attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.transformer = value
        return self


    def add_port_arg_value(self, item: PortDefinedArgumentValue) -> "PortAPIOptionBuilder":
        """Add a single item to port_arg_values list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.port_arg_values.append(item)
        return self

    def clear_port_arg_values(self) -> "PortAPIOptionBuilder":
        """Clear all items from port_arg_values list.

        Returns:
            self for method chaining
        """
        self._obj.port_arg_values = []
        return self

    def add_supported(self, item: SwcSupportedFeature) -> "PortAPIOptionBuilder":
        """Add a single item to supporteds list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.supporteds.append(item)
        return self

    def clear_supporteds(self) -> "PortAPIOptionBuilder":
        """Clear all items from supporteds list.

        Returns:
            self for method chaining
        """
        self._obj.supporteds = []
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


    def build(self) -> PortAPIOption:
        """Build and return the PortAPIOption instance with validation."""
        self._validate_instance()
        pass
        return self._obj