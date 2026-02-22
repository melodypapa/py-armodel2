"""RPortPrototype AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 68)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2047)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 237)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 460)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 202)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_required_port_prototype import (
    AbstractRequiredPortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface import (
    PortInterface,
)


class RPortPrototype(AbstractRequiredPortPrototype):
    """AUTOSAR RPortPrototype."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    may_be_unconnected: Optional[Boolean]
    required_interface_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize RPortPrototype."""
        super().__init__()
        self.may_be_unconnected: Optional[Boolean] = None
        self.required_interface_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize RPortPrototype to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(RPortPrototype, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize may_be_unconnected
        if self.may_be_unconnected is not None:
            serialized = SerializationHelper.serialize_item(self.may_be_unconnected, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAY-BE-UNCONNECTED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize required_interface_ref
        if self.required_interface_ref is not None:
            serialized = SerializationHelper.serialize_item(self.required_interface_ref, "PortInterface")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REQUIRED-INTERFACE-TREF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RPortPrototype":
        """Deserialize XML element to RPortPrototype object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RPortPrototype object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(RPortPrototype, cls).deserialize(element)

        # Parse may_be_unconnected
        child = SerializationHelper.find_child_element(element, "MAY-BE-UNCONNECTED")
        if child is not None:
            may_be_unconnected_value = child.text
            obj.may_be_unconnected = may_be_unconnected_value

        # Parse required_interface_ref
        child = SerializationHelper.find_child_element(element, "REQUIRED-INTERFACE-TREF")
        if child is not None:
            required_interface_ref_value = ARRef.deserialize(child)
            obj.required_interface_ref = required_interface_ref_value

        return obj



class RPortPrototypeBuilder:
    """Builder for RPortPrototype with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: RPortPrototype = RPortPrototype()


    def with_short_name(self, value: Identifier) -> "RPortPrototypeBuilder":
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

    def with_short_name_fragments(self, items: list[ShortNameFragment]) -> "RPortPrototypeBuilder":
        """Set short_name_fragments list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = list(items) if items else []
        return self

    def with_long_name(self, value: Optional[MultilanguageLongName]) -> "RPortPrototypeBuilder":
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

    def with_admin_data(self, value: Optional[AdminData]) -> "RPortPrototypeBuilder":
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

    def with_annotations(self, items: list[Annotation]) -> "RPortPrototypeBuilder":
        """Set annotations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.annotations = list(items) if items else []
        return self

    def with_desc(self, value: Optional[MultiLanguageOverviewParagraph]) -> "RPortPrototypeBuilder":
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

    def with_category(self, value: Optional[CategoryString]) -> "RPortPrototypeBuilder":
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

    def with_introduction(self, value: Optional[DocumentationBlock]) -> "RPortPrototypeBuilder":
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

    def with_uuid(self, value: Optional[String]) -> "RPortPrototypeBuilder":
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

    def with_client_servers(self, items: list[ClientServerAnnotation]) -> "RPortPrototypeBuilder":
        """Set client_servers list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.client_servers = list(items) if items else []
        return self

    def with_delegated_port(self, value: Optional[DelegatedPortAnnotation]) -> "RPortPrototypeBuilder":
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

    def with_io_hw_abstraction_server_annotations(self, items: list[IoHwAbstractionServerAnnotation]) -> "RPortPrototypeBuilder":
        """Set io_hw_abstraction_server_annotations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.io_hw_abstraction_server_annotations = list(items) if items else []
        return self

    def with_mode_port_annotations(self, items: list[ModePortAnnotation]) -> "RPortPrototypeBuilder":
        """Set mode_port_annotations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.mode_port_annotations = list(items) if items else []
        return self

    def with_nv_data_port_annotations(self, items: list[NvDataPortAnnotation]) -> "RPortPrototypeBuilder":
        """Set nv_data_port_annotations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.nv_data_port_annotations = list(items) if items else []
        return self

    def with_parameter_ports(self, items: list[ParameterPortAnnotation]) -> "RPortPrototypeBuilder":
        """Set parameter_ports list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.parameter_ports = list(items) if items else []
        return self

    def with_sender_receivers(self, items: list[any (SenderReceiver)]) -> "RPortPrototypeBuilder":
        """Set sender_receivers list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.sender_receivers = list(items) if items else []
        return self

    def with_trigger_port_annotations(self, items: list[TriggerPortAnnotation]) -> "RPortPrototypeBuilder":
        """Set trigger_port_annotations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.trigger_port_annotations = list(items) if items else []
        return self

    def with_required_coms(self, items: list[RPortComSpec]) -> "RPortPrototypeBuilder":
        """Set required_coms list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.required_coms = list(items) if items else []
        return self

    def with_may_be_unconnected(self, value: Optional[Boolean]) -> "RPortPrototypeBuilder":
        """Set may_be_unconnected attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.may_be_unconnected = value
        return self

    def with_required_interface(self, value: Optional[PortInterface]) -> "RPortPrototypeBuilder":
        """Set required_interface attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.required_interface = value
        return self


    def add_short_name_fragment(self, item: ShortNameFragment) -> "RPortPrototypeBuilder":
        """Add a single item to short_name_fragments list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments.append(item)
        return self

    def clear_short_name_fragments(self) -> "RPortPrototypeBuilder":
        """Clear all items from short_name_fragments list.

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = []
        return self

    def add_annotation(self, item: Annotation) -> "RPortPrototypeBuilder":
        """Add a single item to annotations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.annotations.append(item)
        return self

    def clear_annotations(self) -> "RPortPrototypeBuilder":
        """Clear all items from annotations list.

        Returns:
            self for method chaining
        """
        self._obj.annotations = []
        return self

    def add_client_server(self, item: ClientServerAnnotation) -> "RPortPrototypeBuilder":
        """Add a single item to client_servers list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.client_servers.append(item)
        return self

    def clear_client_servers(self) -> "RPortPrototypeBuilder":
        """Clear all items from client_servers list.

        Returns:
            self for method chaining
        """
        self._obj.client_servers = []
        return self

    def add_io_hw_abstraction_server_annotation(self, item: IoHwAbstractionServerAnnotation) -> "RPortPrototypeBuilder":
        """Add a single item to io_hw_abstraction_server_annotations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.io_hw_abstraction_server_annotations.append(item)
        return self

    def clear_io_hw_abstraction_server_annotations(self) -> "RPortPrototypeBuilder":
        """Clear all items from io_hw_abstraction_server_annotations list.

        Returns:
            self for method chaining
        """
        self._obj.io_hw_abstraction_server_annotations = []
        return self

    def add_mode_port_annotation(self, item: ModePortAnnotation) -> "RPortPrototypeBuilder":
        """Add a single item to mode_port_annotations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.mode_port_annotations.append(item)
        return self

    def clear_mode_port_annotations(self) -> "RPortPrototypeBuilder":
        """Clear all items from mode_port_annotations list.

        Returns:
            self for method chaining
        """
        self._obj.mode_port_annotations = []
        return self

    def add_nv_data_port_annotation(self, item: NvDataPortAnnotation) -> "RPortPrototypeBuilder":
        """Add a single item to nv_data_port_annotations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.nv_data_port_annotations.append(item)
        return self

    def clear_nv_data_port_annotations(self) -> "RPortPrototypeBuilder":
        """Clear all items from nv_data_port_annotations list.

        Returns:
            self for method chaining
        """
        self._obj.nv_data_port_annotations = []
        return self

    def add_parameter_port(self, item: ParameterPortAnnotation) -> "RPortPrototypeBuilder":
        """Add a single item to parameter_ports list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.parameter_ports.append(item)
        return self

    def clear_parameter_ports(self) -> "RPortPrototypeBuilder":
        """Clear all items from parameter_ports list.

        Returns:
            self for method chaining
        """
        self._obj.parameter_ports = []
        return self

    def add_sender_receiver(self, item: any (SenderReceiver)) -> "RPortPrototypeBuilder":
        """Add a single item to sender_receivers list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.sender_receivers.append(item)
        return self

    def clear_sender_receivers(self) -> "RPortPrototypeBuilder":
        """Clear all items from sender_receivers list.

        Returns:
            self for method chaining
        """
        self._obj.sender_receivers = []
        return self

    def add_trigger_port_annotation(self, item: TriggerPortAnnotation) -> "RPortPrototypeBuilder":
        """Add a single item to trigger_port_annotations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.trigger_port_annotations.append(item)
        return self

    def clear_trigger_port_annotations(self) -> "RPortPrototypeBuilder":
        """Clear all items from trigger_port_annotations list.

        Returns:
            self for method chaining
        """
        self._obj.trigger_port_annotations = []
        return self

    def add_required_com(self, item: RPortComSpec) -> "RPortPrototypeBuilder":
        """Add a single item to required_coms list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.required_coms.append(item)
        return self

    def clear_required_coms(self) -> "RPortPrototypeBuilder":
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


    def build(self) -> RPortPrototype:
        """Build and return the RPortPrototype instance with validation."""
        self._validate_instance()
        pass
        return self._obj