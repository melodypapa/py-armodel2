"""LinSlaveConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 94)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
    PositiveInteger,
    String,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology.lin_configurable_frame import (
    LinConfigurableFrame,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_error_response import (
    LinErrorResponse,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology.lin_ordered_configurable_frame import (
    LinOrderedConfigurableFrame,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology.lin_slave_config_ident import (
    LinSlaveConfigIdent,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class LinSlaveConfig(ARObject):
    """AUTOSAR LinSlaveConfig."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    configured_nad: Optional[Integer]
    function_id: Optional[PositiveInteger]
    ident: Optional[LinSlaveConfigIdent]
    initial_nad: Optional[Integer]
    lin_configurable_frames: list[LinConfigurableFrame]
    lin_error_response: Optional[LinErrorResponse]
    lin_ordereds: list[LinOrderedConfigurableFrame]
    protocol_version: Optional[String]
    supplier_id: Optional[PositiveInteger]
    variant_id: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize LinSlaveConfig."""
        super().__init__()
        self.configured_nad: Optional[Integer] = None
        self.function_id: Optional[PositiveInteger] = None
        self.ident: Optional[LinSlaveConfigIdent] = None
        self.initial_nad: Optional[Integer] = None
        self.lin_configurable_frames: list[LinConfigurableFrame] = []
        self.lin_error_response: Optional[LinErrorResponse] = None
        self.lin_ordereds: list[LinOrderedConfigurableFrame] = []
        self.protocol_version: Optional[String] = None
        self.supplier_id: Optional[PositiveInteger] = None
        self.variant_id: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize LinSlaveConfig to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(LinSlaveConfig, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize configured_nad
        if self.configured_nad is not None:
            serialized = SerializationHelper.serialize_item(self.configured_nad, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONFIGURED-NAD")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize function_id
        if self.function_id is not None:
            serialized = SerializationHelper.serialize_item(self.function_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FUNCTION-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ident
        if self.ident is not None:
            serialized = SerializationHelper.serialize_item(self.ident, "LinSlaveConfigIdent")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IDENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize initial_nad
        if self.initial_nad is not None:
            serialized = SerializationHelper.serialize_item(self.initial_nad, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INITIAL-NAD")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize lin_configurable_frames (list to container "LIN-CONFIGURABLE-FRAMES")
        if self.lin_configurable_frames:
            wrapper = ET.Element("LIN-CONFIGURABLE-FRAMES")
            for item in self.lin_configurable_frames:
                serialized = SerializationHelper.serialize_item(item, "LinConfigurableFrame")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize lin_error_response
        if self.lin_error_response is not None:
            serialized = SerializationHelper.serialize_item(self.lin_error_response, "LinErrorResponse")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LIN-ERROR-RESPONSE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize lin_ordereds (list to container "LIN-ORDEREDS")
        if self.lin_ordereds:
            wrapper = ET.Element("LIN-ORDEREDS")
            for item in self.lin_ordereds:
                serialized = SerializationHelper.serialize_item(item, "LinOrderedConfigurableFrame")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize protocol_version
        if self.protocol_version is not None:
            serialized = SerializationHelper.serialize_item(self.protocol_version, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PROTOCOL-VERSION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize supplier_id
        if self.supplier_id is not None:
            serialized = SerializationHelper.serialize_item(self.supplier_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SUPPLIER-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize variant_id
        if self.variant_id is not None:
            serialized = SerializationHelper.serialize_item(self.variant_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VARIANT-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LinSlaveConfig":
        """Deserialize XML element to LinSlaveConfig object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LinSlaveConfig object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(LinSlaveConfig, cls).deserialize(element)

        # Parse configured_nad
        child = SerializationHelper.find_child_element(element, "CONFIGURED-NAD")
        if child is not None:
            configured_nad_value = child.text
            obj.configured_nad = configured_nad_value

        # Parse function_id
        child = SerializationHelper.find_child_element(element, "FUNCTION-ID")
        if child is not None:
            function_id_value = child.text
            obj.function_id = function_id_value

        # Parse ident
        child = SerializationHelper.find_child_element(element, "IDENT")
        if child is not None:
            ident_value = SerializationHelper.deserialize_by_tag(child, "LinSlaveConfigIdent")
            obj.ident = ident_value

        # Parse initial_nad
        child = SerializationHelper.find_child_element(element, "INITIAL-NAD")
        if child is not None:
            initial_nad_value = child.text
            obj.initial_nad = initial_nad_value

        # Parse lin_configurable_frames (list from container "LIN-CONFIGURABLE-FRAMES")
        obj.lin_configurable_frames = []
        container = SerializationHelper.find_child_element(element, "LIN-CONFIGURABLE-FRAMES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.lin_configurable_frames.append(child_value)

        # Parse lin_error_response
        child = SerializationHelper.find_child_element(element, "LIN-ERROR-RESPONSE")
        if child is not None:
            lin_error_response_value = SerializationHelper.deserialize_by_tag(child, "LinErrorResponse")
            obj.lin_error_response = lin_error_response_value

        # Parse lin_ordereds (list from container "LIN-ORDEREDS")
        obj.lin_ordereds = []
        container = SerializationHelper.find_child_element(element, "LIN-ORDEREDS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.lin_ordereds.append(child_value)

        # Parse protocol_version
        child = SerializationHelper.find_child_element(element, "PROTOCOL-VERSION")
        if child is not None:
            protocol_version_value = child.text
            obj.protocol_version = protocol_version_value

        # Parse supplier_id
        child = SerializationHelper.find_child_element(element, "SUPPLIER-ID")
        if child is not None:
            supplier_id_value = child.text
            obj.supplier_id = supplier_id_value

        # Parse variant_id
        child = SerializationHelper.find_child_element(element, "VARIANT-ID")
        if child is not None:
            variant_id_value = child.text
            obj.variant_id = variant_id_value

        return obj



class LinSlaveConfigBuilder(BuilderBase):
    """Builder for LinSlaveConfig with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: LinSlaveConfig = LinSlaveConfig()


    def with_configured_nad(self, value: Optional[Integer]) -> "LinSlaveConfigBuilder":
        """Set configured_nad attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.configured_nad = value
        return self

    def with_function_id(self, value: Optional[PositiveInteger]) -> "LinSlaveConfigBuilder":
        """Set function_id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.function_id = value
        return self

    def with_ident(self, value: Optional[LinSlaveConfigIdent]) -> "LinSlaveConfigBuilder":
        """Set ident attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ident = value
        return self

    def with_initial_nad(self, value: Optional[Integer]) -> "LinSlaveConfigBuilder":
        """Set initial_nad attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.initial_nad = value
        return self

    def with_lin_configurable_frames(self, items: list[LinConfigurableFrame]) -> "LinSlaveConfigBuilder":
        """Set lin_configurable_frames list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.lin_configurable_frames = list(items) if items else []
        return self

    def with_lin_error_response(self, value: Optional[LinErrorResponse]) -> "LinSlaveConfigBuilder":
        """Set lin_error_response attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.lin_error_response = value
        return self

    def with_lin_ordereds(self, items: list[LinOrderedConfigurableFrame]) -> "LinSlaveConfigBuilder":
        """Set lin_ordereds list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.lin_ordereds = list(items) if items else []
        return self

    def with_protocol_version(self, value: Optional[String]) -> "LinSlaveConfigBuilder":
        """Set protocol_version attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.protocol_version = value
        return self

    def with_supplier_id(self, value: Optional[PositiveInteger]) -> "LinSlaveConfigBuilder":
        """Set supplier_id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.supplier_id = value
        return self

    def with_variant_id(self, value: Optional[PositiveInteger]) -> "LinSlaveConfigBuilder":
        """Set variant_id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.variant_id = value
        return self


    def add_lin_configurable_frame(self, item: LinConfigurableFrame) -> "LinSlaveConfigBuilder":
        """Add a single item to lin_configurable_frames list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.lin_configurable_frames.append(item)
        return self

    def clear_lin_configurable_frames(self) -> "LinSlaveConfigBuilder":
        """Clear all items from lin_configurable_frames list.

        Returns:
            self for method chaining
        """
        self._obj.lin_configurable_frames = []
        return self

    def add_lin_ordered(self, item: LinOrderedConfigurableFrame) -> "LinSlaveConfigBuilder":
        """Add a single item to lin_ordereds list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.lin_ordereds.append(item)
        return self

    def clear_lin_ordereds(self) -> "LinSlaveConfigBuilder":
        """Clear all items from lin_ordereds list.

        Returns:
            self for method chaining
        """
        self._obj.lin_ordereds = []
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


    def build(self) -> LinSlaveConfig:
        """Build and return the LinSlaveConfig instance with validation."""
        self._validate_instance()
        pass
        return self._obj