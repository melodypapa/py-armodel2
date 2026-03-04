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
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PortAPIOptions.swc_supported_feature import (
    SwcSupportedFeature,
)

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PortAPIOptions.port_defined_argument_value import (
        PortDefinedArgumentValue,
    )
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
    port_arg_values: list[PortDefinedArgumentValue]
    port_ref: Optional[ARRef]
    supported_features: list[SwcSupportedFeature]
    transformer_status_forwarding: Optional[DataTransformationStatusForwardingEnum]
    _DESERIALIZE_DISPATCH = {
        "ENABLE-TAKE-ADDRESS": lambda obj, elem: setattr(obj, "enable_take_address", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "ERROR-HANDLING": lambda obj, elem: setattr(obj, "error_handling", DataTransformationErrorHandlingEnum.deserialize(elem)),
        "INDIRECT-API": lambda obj, elem: setattr(obj, "indirect_api", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "PORT-ARG-VALUES": lambda obj, elem: obj.port_arg_values.append(SerializationHelper.deserialize_by_tag(elem, "PortDefinedArgumentValue")),
        "PORT-REF": ("_POLYMORPHIC", "port_ref", ["AbstractProvidedPortPrototype", "AbstractRequiredPortPrototype", "PPortPrototype", "PRPortPrototype", "RPortPrototype"]),
        "SUPPORTED-FEATURES": ("_POLYMORPHIC_LIST", "supported_features", ["CommunicationBufferLocking"]),
        "TRANSFORMER-STATUS-FORWARDING": lambda obj, elem: setattr(obj, "transformer_status_forwarding", DataTransformationStatusForwardingEnum.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize PortAPIOption."""
        super().__init__()
        self.enable_take_address: Optional[Boolean] = None
        self.error_handling: Optional[DataTransformationErrorHandlingEnum] = None
        self.indirect_api: Optional[Boolean] = None
        self.port_arg_values: list[PortDefinedArgumentValue] = []
        self.port_ref: Optional[ARRef] = None
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

        # Serialize port_arg_values (list to container "PORT-ARG-VALUES")
        if self.port_arg_values:
            wrapper = ET.Element("PORT-ARG-VALUES")
            for item in self.port_arg_values:
                serialized = SerializationHelper.serialize_item(item, "PortDefinedArgumentValue")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ENABLE-TAKE-ADDRESS":
                setattr(obj, "enable_take_address", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "ERROR-HANDLING":
                setattr(obj, "error_handling", DataTransformationErrorHandlingEnum.deserialize(child))
            elif tag == "INDIRECT-API":
                setattr(obj, "indirect_api", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "PORT-ARG-VALUES":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.port_arg_values.append(SerializationHelper.deserialize_by_tag(item_elem, "PortDefinedArgumentValue"))
            elif tag == "PORT-REF":
                setattr(obj, "port_ref", ARRef.deserialize(child))
            elif tag == "SUPPORTED-FEATURES":
                # Iterate through all child elements and deserialize each based on its concrete type
                for item_elem in child:
                    concrete_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    if concrete_tag == "COMMUNICATION-BUFFER-LOCKING":
                        obj.supported_features.append(SerializationHelper.deserialize_by_tag(item_elem, "CommunicationBufferLocking"))
            elif tag == "TRANSFORMER-STATUS-FORWARDING":
                setattr(obj, "transformer_status_forwarding", DataTransformationStatusForwardingEnum.deserialize(child))

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

    def with_port_arg_values(self, items: list[PortDefinedArgumentValue]) -> "PortAPIOptionBuilder":
        """Set port_arg_values list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.port_arg_values = list(items) if items else []
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


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "enableTakeAddress",
        "errorHandling",
        "indirectAPI",
        "port",
        "portArgValue",
        "supportedFeature",
        "transformerStatusForwarding",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> PortAPIOption:
        """Build and return the PortAPIOption instance with validation."""
        self._validate_instance()
        return self._obj