"""PRPortPrototype AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 325)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 68)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2042)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 199)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_required_port_prototype import (
    AbstractRequiredPortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface import (
    PortInterface,
)


class PRPortPrototype(AbstractRequiredPortPrototype):
    """AUTOSAR PRPortPrototype."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    provided: Optional[PortInterface]
    def __init__(self) -> None:
        """Initialize PRPortPrototype."""
        super().__init__()
        self.provided: Optional[PortInterface] = None

    def serialize(self) -> ET.Element:
        """Serialize PRPortPrototype to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(PRPortPrototype, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize provided
        if self.provided is not None:
            serialized = SerializationHelper.serialize_item(self.provided, "PortInterface")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PROVIDED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PRPortPrototype":
        """Deserialize XML element to PRPortPrototype object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PRPortPrototype object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PRPortPrototype, cls).deserialize(element)

        # Parse provided
        child = SerializationHelper.find_child_element(element, "PROVIDED")
        if child is not None:
            provided_value = SerializationHelper.deserialize_by_tag(child, "PortInterface")
            obj.provided = provided_value

        return obj



class PRPortPrototypeBuilder:
    """Builder for PRPortPrototype with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: PRPortPrototype = PRPortPrototype()


    def with_short_name(self, value: Identifier) -> "PRPortPrototypeBuilder":
        """Set short_name attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.short_name = value
        return self

    def with_short_name_fragments(self, items: list[ShortNameFragment]) -> "PRPortPrototypeBuilder":
        """Set short_name_fragments list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = list(items) if items else []
        return self

    def with_long_name(self, value: Optional[MultilanguageLongName]) -> "PRPortPrototypeBuilder":
        """Set long_name attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.long_name = value
        return self

    def with_admin_data(self, value: Optional[AdminData]) -> "PRPortPrototypeBuilder":
        """Set admin_data attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.admin_data = value
        return self

    def with_annotations(self, items: list[Annotation]) -> "PRPortPrototypeBuilder":
        """Set annotations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.annotations = list(items) if items else []
        return self

    def with_desc(self, value: Optional[MultiLanguageOverviewParagraph]) -> "PRPortPrototypeBuilder":
        """Set desc attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.desc = value
        return self

    def with_category(self, value: Optional[CategoryString]) -> "PRPortPrototypeBuilder":
        """Set category attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.category = value
        return self

    def with_introduction(self, value: Optional[DocumentationBlock]) -> "PRPortPrototypeBuilder":
        """Set introduction attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.introduction = value
        return self

    def with_uuid(self, value: Optional[String]) -> "PRPortPrototypeBuilder":
        """Set uuid attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.uuid = value
        return self

    def with_client_servers(self, items: list[ClientServerAnnotation]) -> "PRPortPrototypeBuilder":
        """Set client_servers list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.client_servers = list(items) if items else []
        return self

    def with_delegated_port(self, value: Optional[DelegatedPortAnnotation]) -> "PRPortPrototypeBuilder":
        """Set delegated_port attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.delegated_port = value
        return self

    def with_io_hw_abstraction_server_annotations(self, items: list[IoHwAbstractionServerAnnotation]) -> "PRPortPrototypeBuilder":
        """Set io_hw_abstraction_server_annotations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.io_hw_abstraction_server_annotations = list(items) if items else []
        return self

    def with_mode_port_annotations(self, items: list[ModePortAnnotation]) -> "PRPortPrototypeBuilder":
        """Set mode_port_annotations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.mode_port_annotations = list(items) if items else []
        return self

    def with_nv_data_port_annotations(self, items: list[NvDataPortAnnotation]) -> "PRPortPrototypeBuilder":
        """Set nv_data_port_annotations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.nv_data_port_annotations = list(items) if items else []
        return self

    def with_parameter_ports(self, items: list[ParameterPortAnnotation]) -> "PRPortPrototypeBuilder":
        """Set parameter_ports list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.parameter_ports = list(items) if items else []
        return self

    def with_sender_receivers(self, items: list[any (SenderReceiver)]) -> "PRPortPrototypeBuilder":
        """Set sender_receivers list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.sender_receivers = list(items) if items else []
        return self

    def with_trigger_port_annotations(self, items: list[TriggerPortAnnotation]) -> "PRPortPrototypeBuilder":
        """Set trigger_port_annotations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.trigger_port_annotations = list(items) if items else []
        return self

    def with_required_coms(self, items: list[RPortComSpec]) -> "PRPortPrototypeBuilder":
        """Set required_coms list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.required_coms = list(items) if items else []
        return self

    def with_provided(self, value: Optional[PortInterface]) -> "PRPortPrototypeBuilder":
        """Set provided attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.provided = value
        return self


    def add_short_name_fragment(self, item: ShortNameFragment) -> "PRPortPrototypeBuilder":
        """Add a single item to short_name_fragments list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments.append(item)
        return self

    def clear_short_name_fragments(self) -> "PRPortPrototypeBuilder":
        """Clear all items from short_name_fragments list.

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = []
        return self

    def add_annotation(self, item: Annotation) -> "PRPortPrototypeBuilder":
        """Add a single item to annotations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.annotations.append(item)
        return self

    def clear_annotations(self) -> "PRPortPrototypeBuilder":
        """Clear all items from annotations list.

        Returns:
            self for method chaining
        """
        self._obj.annotations = []
        return self

    def add_client_server(self, item: ClientServerAnnotation) -> "PRPortPrototypeBuilder":
        """Add a single item to client_servers list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.client_servers.append(item)
        return self

    def clear_client_servers(self) -> "PRPortPrototypeBuilder":
        """Clear all items from client_servers list.

        Returns:
            self for method chaining
        """
        self._obj.client_servers = []
        return self

    def add_io_hw_abstraction_server_annotation(self, item: IoHwAbstractionServerAnnotation) -> "PRPortPrototypeBuilder":
        """Add a single item to io_hw_abstraction_server_annotations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.io_hw_abstraction_server_annotations.append(item)
        return self

    def clear_io_hw_abstraction_server_annotations(self) -> "PRPortPrototypeBuilder":
        """Clear all items from io_hw_abstraction_server_annotations list.

        Returns:
            self for method chaining
        """
        self._obj.io_hw_abstraction_server_annotations = []
        return self

    def add_mode_port_annotation(self, item: ModePortAnnotation) -> "PRPortPrototypeBuilder":
        """Add a single item to mode_port_annotations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.mode_port_annotations.append(item)
        return self

    def clear_mode_port_annotations(self) -> "PRPortPrototypeBuilder":
        """Clear all items from mode_port_annotations list.

        Returns:
            self for method chaining
        """
        self._obj.mode_port_annotations = []
        return self

    def add_nv_data_port_annotation(self, item: NvDataPortAnnotation) -> "PRPortPrototypeBuilder":
        """Add a single item to nv_data_port_annotations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.nv_data_port_annotations.append(item)
        return self

    def clear_nv_data_port_annotations(self) -> "PRPortPrototypeBuilder":
        """Clear all items from nv_data_port_annotations list.

        Returns:
            self for method chaining
        """
        self._obj.nv_data_port_annotations = []
        return self

    def add_parameter_port(self, item: ParameterPortAnnotation) -> "PRPortPrototypeBuilder":
        """Add a single item to parameter_ports list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.parameter_ports.append(item)
        return self

    def clear_parameter_ports(self) -> "PRPortPrototypeBuilder":
        """Clear all items from parameter_ports list.

        Returns:
            self for method chaining
        """
        self._obj.parameter_ports = []
        return self

    def add_sender_receiver(self, item: any (SenderReceiver)) -> "PRPortPrototypeBuilder":
        """Add a single item to sender_receivers list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.sender_receivers.append(item)
        return self

    def clear_sender_receivers(self) -> "PRPortPrototypeBuilder":
        """Clear all items from sender_receivers list.

        Returns:
            self for method chaining
        """
        self._obj.sender_receivers = []
        return self

    def add_trigger_port_annotation(self, item: TriggerPortAnnotation) -> "PRPortPrototypeBuilder":
        """Add a single item to trigger_port_annotations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.trigger_port_annotations.append(item)
        return self

    def clear_trigger_port_annotations(self) -> "PRPortPrototypeBuilder":
        """Clear all items from trigger_port_annotations list.

        Returns:
            self for method chaining
        """
        self._obj.trigger_port_annotations = []
        return self

    def add_required_com(self, item: RPortComSpec) -> "PRPortPrototypeBuilder":
        """Add a single item to required_coms list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.required_coms.append(item)
        return self

    def clear_required_coms(self) -> "PRPortPrototypeBuilder":
        """Clear all items from required_coms list.

        Returns:
            self for method chaining
        """
        self._obj.required_coms = []
        return self


    @staticmethod
    def _coerce_to_int(value: Any) -> int:
        """Coerce value to int.

        Args:
            value: Value to coerce

        Returns:
            Integer value

        Raises:
            ValueError: If value cannot be coerced to int
        """
        if isinstance(value, int):
            return value
        if isinstance(value, str) and value.isdigit():
            return int(value)
        if isinstance(value, float):
            return int(value)
        if isinstance(value, bool):
            return int(value)
        raise ValueError(f"Cannot coerce {type(value).__name__} to int: {value}")

    @staticmethod
    def _coerce_to_float(value: Any) -> float:
        """Coerce value to float.

        Args:
            value: Value to coerce

        Returns:
            Float value

        Raises:
            ValueError: If value cannot be coerced to float
        """
        if isinstance(value, float):
            return value
        if isinstance(value, int):
            return float(value)
        if isinstance(value, str):
            try:
                return float(value)
            except ValueError:
                pass
        raise ValueError(f"Cannot coerce {type(value).__name__} to float: {value}")

    @staticmethod
    def _coerce_to_bool(value: Any) -> bool:
        """Coerce value to bool.

        Args:
            value: Value to coerce

        Returns:
            Boolean value

        Raises:
            ValueError: If value cannot be coerced to bool
        """
        if isinstance(value, bool):
            return value
        if isinstance(value, int):
            return bool(value)
        if isinstance(value, str):
            if value.lower() in ("true", "1", "yes"):
                return True
            if value.lower() in ("false", "0", "no"):
                return False
        raise ValueError(f"Cannot coerce {type(value).__name__} to bool: {value}")

    @staticmethod
    def _coerce_to_str(value: Any) -> str:
        """Coerce value to str.

        Args:
            value: Value to coerce

        Returns:
            String value
        """
        return str(value)


    @staticmethod
    def _coerce_to_list(value: Any, item_type: str) -> list:
        """Coerce value to list.

        Args:
            value: Value to coerce
            item_type: Expected item type (for error messages)

        Returns:
            List value

        Raises:
            ValueError: If value cannot be coerced to list
        """
        if isinstance(value, list):
            return value
        if isinstance(value, tuple):
            return list(value)
        raise ValueError(f"Cannot coerce {type(value).__name__} to list[{item_type}]: {value}")


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


    def build(self) -> PRPortPrototype:
        """Build and return the PRPortPrototype instance with validation."""
        self._validate_instance()
        pass
        return self._obj