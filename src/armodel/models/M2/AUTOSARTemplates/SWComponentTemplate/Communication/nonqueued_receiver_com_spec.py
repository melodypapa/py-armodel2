"""NonqueuedReceiverComSpec AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 172)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2039)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 198)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Communication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.receiver_com_spec import (
    ReceiverComSpec,
)
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.receiver_com_spec import ReceiverComSpecBuilder
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import (
    HandleTimeoutEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Filter.data_filter import (
    DataFilter,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
        ValueSpecification,
    )



from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
class NonqueuedReceiverComSpec(ReceiverComSpec):
    """AUTOSAR NonqueuedReceiverComSpec."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    alive_timeout: Optional[TimeValue]
    enable_update: Optional[Boolean]
    filter: Optional[DataFilter]
    handle_data: Optional[Boolean]
    handle_never: Optional[Boolean]
    handle_timeout_enum: Optional[HandleTimeoutEnum]
    init_value: Optional[ValueSpecification]
    timeout: Optional[ValueSpecification]
    def __init__(self) -> None:
        """Initialize NonqueuedReceiverComSpec."""
        super().__init__()
        self.alive_timeout: Optional[TimeValue] = None
        self.enable_update: Optional[Boolean] = None
        self.filter: Optional[DataFilter] = None
        self.handle_data: Optional[Boolean] = None
        self.handle_never: Optional[Boolean] = None
        self.handle_timeout_enum: Optional[HandleTimeoutEnum] = None
        self.init_value: Optional[ValueSpecification] = None
        self.timeout: Optional[ValueSpecification] = None

    def serialize(self) -> ET.Element:
        """Serialize NonqueuedReceiverComSpec to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(NonqueuedReceiverComSpec, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize alive_timeout
        if self.alive_timeout is not None:
            serialized = SerializationHelper.serialize_item(self.alive_timeout, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ALIVE-TIMEOUT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize enable_update
        if self.enable_update is not None:
            serialized = SerializationHelper.serialize_item(self.enable_update, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ENABLE-UPDATE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize filter
        if self.filter is not None:
            serialized = SerializationHelper.serialize_item(self.filter, "DataFilter")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FILTER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize handle_data
        if self.handle_data is not None:
            serialized = SerializationHelper.serialize_item(self.handle_data, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HANDLE-DATA")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize handle_never
        if self.handle_never is not None:
            serialized = SerializationHelper.serialize_item(self.handle_never, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HANDLE-NEVER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize handle_timeout_enum
        if self.handle_timeout_enum is not None:
            serialized = SerializationHelper.serialize_item(self.handle_timeout_enum, "HandleTimeoutEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HANDLE-TIMEOUT-ENUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize init_value
        if self.init_value is not None:
            serialized = SerializationHelper.serialize_item(self.init_value, "ValueSpecification")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INIT-VALUE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize timeout
        if self.timeout is not None:
            serialized = SerializationHelper.serialize_item(self.timeout, "ValueSpecification")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIMEOUT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "NonqueuedReceiverComSpec":
        """Deserialize XML element to NonqueuedReceiverComSpec object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized NonqueuedReceiverComSpec object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(NonqueuedReceiverComSpec, cls).deserialize(element)

        # Parse alive_timeout
        child = SerializationHelper.find_child_element(element, "ALIVE-TIMEOUT")
        if child is not None:
            alive_timeout_value = child.text
            obj.alive_timeout = alive_timeout_value

        # Parse enable_update
        child = SerializationHelper.find_child_element(element, "ENABLE-UPDATE")
        if child is not None:
            enable_update_value = child.text
            obj.enable_update = enable_update_value

        # Parse filter
        child = SerializationHelper.find_child_element(element, "FILTER")
        if child is not None:
            filter_value = SerializationHelper.deserialize_by_tag(child, "DataFilter")
            obj.filter = filter_value

        # Parse handle_data
        child = SerializationHelper.find_child_element(element, "HANDLE-DATA")
        if child is not None:
            handle_data_value = child.text
            obj.handle_data = handle_data_value

        # Parse handle_never
        child = SerializationHelper.find_child_element(element, "HANDLE-NEVER")
        if child is not None:
            handle_never_value = child.text
            obj.handle_never = handle_never_value

        # Parse handle_timeout_enum
        child = SerializationHelper.find_child_element(element, "HANDLE-TIMEOUT-ENUM")
        if child is not None:
            handle_timeout_enum_value = HandleTimeoutEnum.deserialize(child)
            obj.handle_timeout_enum = handle_timeout_enum_value

        # Parse init_value
        child = SerializationHelper.find_child_element(element, "INIT-VALUE")
        if child is not None:
            init_value_value = SerializationHelper.deserialize_by_tag(child, "ValueSpecification")
            obj.init_value = init_value_value

        # Parse timeout
        child = SerializationHelper.find_child_element(element, "TIMEOUT")
        if child is not None:
            timeout_value = SerializationHelper.deserialize_by_tag(child, "ValueSpecification")
            obj.timeout = timeout_value

        return obj



class NonqueuedReceiverComSpecBuilder(ReceiverComSpecBuilder):
    """Builder for NonqueuedReceiverComSpec with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: NonqueuedReceiverComSpec = NonqueuedReceiverComSpec()


    def with_alive_timeout(self, value: Optional[TimeValue]) -> "NonqueuedReceiverComSpecBuilder":
        """Set alive_timeout attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.alive_timeout = value
        return self

    def with_enable_update(self, value: Optional[Boolean]) -> "NonqueuedReceiverComSpecBuilder":
        """Set enable_update attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.enable_update = value
        return self

    def with_filter(self, value: Optional[DataFilter]) -> "NonqueuedReceiverComSpecBuilder":
        """Set filter attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.filter = value
        return self

    def with_handle_data(self, value: Optional[Boolean]) -> "NonqueuedReceiverComSpecBuilder":
        """Set handle_data attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.handle_data = value
        return self

    def with_handle_never(self, value: Optional[Boolean]) -> "NonqueuedReceiverComSpecBuilder":
        """Set handle_never attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.handle_never = value
        return self

    def with_handle_timeout_enum(self, value: Optional[HandleTimeoutEnum]) -> "NonqueuedReceiverComSpecBuilder":
        """Set handle_timeout_enum attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.handle_timeout_enum = value
        return self

    def with_init_value(self, value: Optional[ValueSpecification]) -> "NonqueuedReceiverComSpecBuilder":
        """Set init_value attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.init_value = value
        return self

    def with_timeout(self, value: Optional[ValueSpecification]) -> "NonqueuedReceiverComSpecBuilder":
        """Set timeout attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.timeout = value
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


    def build(self) -> NonqueuedReceiverComSpec:
        """Build and return the NonqueuedReceiverComSpec instance with validation."""
        self._validate_instance()
        pass
        return self._obj