"""PortAPIOption AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 589)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2045)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_PortAPIOptions.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PortAPIOptions import (
    DataTransformationErrorHandlingEnum,
    DataTransformationStatusForwardingEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PortAPIOptions.port_defined_argument_value import (
    PortDefinedArgumentValue,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PortAPIOptions.swc_supported_feature import (
    SwcSupportedFeature,
)

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
        PortPrototype,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class PortAPIOption(ARObject):
    """AUTOSAR PortAPIOption."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "PORT-API-OPTION"


    enable_take_address: Optional[Boolean]
    error_handling: Optional[DataTransformationErrorHandlingEnum]
    indirect_api: Optional[Boolean]
    port_ref: Optional[ARRef]
    port_arg_values: list[PortDefinedArgumentValue]
    supported_features: list[SwcSupportedFeature]
    transformer_status_forwarding: Optional[DataTransformationStatusForwardingEnum]
    _DESERIALIZE_DISPATCH = {
        "ENABLE-TAKE-ADDRESS": lambda obj, elem: setattr(obj, "enable_take_address", elem.text),
        "ERROR-HANDLING": lambda obj, elem: setattr(obj, "error_handling", DataTransformationErrorHandlingEnum.deserialize(elem)),
        "INDIRECT-API": lambda obj, elem: setattr(obj, "indirect_api", elem.text),
        "PORT-REF": lambda obj, elem: setattr(obj, "port_ref", ARRef.deserialize(elem)),
        "PORT-ARG-VALUES": lambda obj, elem: obj.port_arg_values.append(PortDefinedArgumentValue.deserialize(elem)),
        "SUPPORTED-FEATURES": lambda obj, elem: obj.supported_features.append(SwcSupportedFeature.deserialize(elem)),
        "TRANSFORMER-STATUS-FORWARDING": lambda obj, elem: setattr(obj, "transformer_status_forwarding", DataTransformationStatusForwardingEnum.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize PortAPIOption."""
        super().__init__()
        self.enable_take_address: Optional[Boolean] = None
        self.error_handling: Optional[DataTransformationErrorHandlingEnum] = None
        self.indirect_api: Optional[Boolean] = None
        self.port_ref: Optional[ARRef] = None
        self.port_arg_values: list[PortDefinedArgumentValue] = []
        self.supported_features: list[SwcSupportedFeature] = []
        self.transformer_status_forwarding: Optional[DataTransformationStatusForwardingEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize PortAPIOption to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

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

        # Serialize enable_take_address
        if self.enable_take_address is not None:
            serialized = SerializationHelper.serialize_item(self.enable_take_address, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ENABLE-TAKE-ADDRESS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize error_handling
        if self.error_handling is not None:
            serialized = SerializationHelper.serialize_item(self.error_handling, "DataTransformationErrorHandlingEnum")
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

        # Serialize supported_features (list to container "SUPPORTED-FEATURES")
        if self.supported_features:
            wrapper = ET.Element("SUPPORTED-FEATURES")
            for item in self.supported_features:
                serialized = SerializationHelper.serialize_item(item, "SwcSupportedFeature")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize transformer_status_forwarding
        if self.transformer_status_forwarding is not None:
            serialized = SerializationHelper.serialize_item(self.transformer_status_forwarding, "DataTransformationStatusForwardingEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TRANSFORMER-STATUS-FORWARDING")
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

        # Parse enable_take_address
        child = SerializationHelper.find_child_element(element, "ENABLE-TAKE-ADDRESS")
        if child is not None:
            enable_take_address_value = child.text
            obj.enable_take_address = enable_take_address_value

        # Parse error_handling
        child = SerializationHelper.find_child_element(element, "ERROR-HANDLING")
        if child is not None:
            error_handling_value = DataTransformationErrorHandlingEnum.deserialize(child)
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

        # Parse supported_features (list from container "SUPPORTED-FEATURES")
        obj.supported_features = []
        container = SerializationHelper.find_child_element(element, "SUPPORTED-FEATURES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.supported_features.append(child_value)

        # Parse transformer_status_forwarding
        child = SerializationHelper.find_child_element(element, "TRANSFORMER-STATUS-FORWARDING")
        if child is not None:
            transformer_status_forwarding_value = DataTransformationStatusForwardingEnum.deserialize(child)
            obj.transformer_status_forwarding = transformer_status_forwarding_value

        return obj



class PortAPIOptionBuilder(BuilderBase):
    """Builder for PortAPIOption with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: PortAPIOption = PortAPIOption()


    def with_enable_take_address(self, value: Optional[Boolean]) -> "PortAPIOptionBuilder":
        """Set enable_take_address attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.enable_take_address = value
        return self

    def with_error_handling(self, value: Optional[DataTransformationErrorHandlingEnum]) -> "PortAPIOptionBuilder":
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

    def with_supported_features(self, items: list[SwcSupportedFeature]) -> "PortAPIOptionBuilder":
        """Set supported_features list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.supported_features = list(items) if items else []
        return self

    def with_transformer_status_forwarding(self, value: Optional[DataTransformationStatusForwardingEnum]) -> "PortAPIOptionBuilder":
        """Set transformer_status_forwarding attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.transformer_status_forwarding = value
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

    def add_supported_feature(self, item: SwcSupportedFeature) -> "PortAPIOptionBuilder":
        """Add a single item to supported_features list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.supported_features.append(item)
        return self

    def clear_supported_features(self) -> "PortAPIOptionBuilder":
        """Clear all items from supported_features list.

        Returns:
            self for method chaining
        """
        self._obj.supported_features = []
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


    def build(self) -> PortAPIOption:
        """Build and return the PortAPIOption instance with validation."""
        self._validate_instance()
        pass
        return self._obj