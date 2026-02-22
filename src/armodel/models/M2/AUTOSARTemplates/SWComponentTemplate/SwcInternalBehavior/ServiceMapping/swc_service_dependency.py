"""SwcServiceDependency AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 224)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 608)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_ServiceMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_dependency import (
    ServiceDependency,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_group import (
    PortGroup,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServiceMapping.role_based_port_assignment import (
    RoleBasedPortAssignment,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_needs import (
    ServiceNeeds,
)


class SwcServiceDependency(ServiceDependency):
    """AUTOSAR SwcServiceDependency."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    assigned_datas: list[Any]
    assigned_ports: list[RoleBasedPortAssignment]
    represented_port_ref: Optional[ARRef]
    service_needs: Optional[ServiceNeeds]
    def __init__(self) -> None:
        """Initialize SwcServiceDependency."""
        super().__init__()
        self.assigned_datas: list[Any] = []
        self.assigned_ports: list[RoleBasedPortAssignment] = []
        self.represented_port_ref: Optional[ARRef] = None
        self.service_needs: Optional[ServiceNeeds] = None

    def serialize(self) -> ET.Element:
        """Serialize SwcServiceDependency to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwcServiceDependency, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize assigned_datas (list to container "ASSIGNED-DATAS")
        if self.assigned_datas:
            wrapper = ET.Element("ASSIGNED-DATAS")
            for item in self.assigned_datas:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize assigned_ports (list to container "ASSIGNED-PORTS")
        if self.assigned_ports:
            wrapper = ET.Element("ASSIGNED-PORTS")
            for item in self.assigned_ports:
                serialized = SerializationHelper.serialize_item(item, "RoleBasedPortAssignment")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize represented_port_ref
        if self.represented_port_ref is not None:
            serialized = SerializationHelper.serialize_item(self.represented_port_ref, "PortGroup")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REPRESENTED-PORT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize service_needs
        if self.service_needs is not None:
            serialized = SerializationHelper.serialize_item(self.service_needs, "ServiceNeeds")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SERVICE-NEEDS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwcServiceDependency":
        """Deserialize XML element to SwcServiceDependency object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwcServiceDependency object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwcServiceDependency, cls).deserialize(element)

        # Parse assigned_datas (list from container "ASSIGNED-DATAS")
        obj.assigned_datas = []
        container = SerializationHelper.find_child_element(element, "ASSIGNED-DATAS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.assigned_datas.append(child_value)

        # Parse assigned_ports (list from container "ASSIGNED-PORTS")
        obj.assigned_ports = []
        container = SerializationHelper.find_child_element(element, "ASSIGNED-PORTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.assigned_ports.append(child_value)

        # Parse represented_port_ref
        child = SerializationHelper.find_child_element(element, "REPRESENTED-PORT-REF")
        if child is not None:
            represented_port_ref_value = ARRef.deserialize(child)
            obj.represented_port_ref = represented_port_ref_value

        # Parse service_needs
        child = SerializationHelper.find_child_element(element, "SERVICE-NEEDS")
        if child is not None:
            service_needs_value = SerializationHelper.deserialize_by_tag(child, "ServiceNeeds")
            obj.service_needs = service_needs_value

        return obj



class SwcServiceDependencyBuilder:
    """Builder for SwcServiceDependency with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: SwcServiceDependency = SwcServiceDependency()


    def with_assigned_data(self, value: Optional[RoleBasedDataTypeAssignment]) -> "SwcServiceDependencyBuilder":
        """Set assigned_data attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.assigned_data = value
        return self

    def with_diagnostic(self, value: Optional[ServiceDiagnosticRelevanceEnum]) -> "SwcServiceDependencyBuilder":
        """Set diagnostic attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.diagnostic = value
        return self

    def with_symbolic_name_props(self, value: Optional[SymbolicNameProps]) -> "SwcServiceDependencyBuilder":
        """Set symbolic_name_props attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.symbolic_name_props = value
        return self

    def with_assigned_datas(self, items: list[any (RoleBasedData)]) -> "SwcServiceDependencyBuilder":
        """Set assigned_datas list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.assigned_datas = list(items) if items else []
        return self

    def with_assigned_ports(self, items: list[RoleBasedPortAssignment]) -> "SwcServiceDependencyBuilder":
        """Set assigned_ports list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.assigned_ports = list(items) if items else []
        return self

    def with_represented_port(self, value: Optional[PortGroup]) -> "SwcServiceDependencyBuilder":
        """Set represented_port attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.represented_port = value
        return self

    def with_service_needs(self, value: Optional[ServiceNeeds]) -> "SwcServiceDependencyBuilder":
        """Set service_needs attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.service_needs = value
        return self


    def add_assigned_data(self, item: any (RoleBasedData)) -> "SwcServiceDependencyBuilder":
        """Add a single item to assigned_datas list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.assigned_datas.append(item)
        return self

    def clear_assigned_datas(self) -> "SwcServiceDependencyBuilder":
        """Clear all items from assigned_datas list.

        Returns:
            self for method chaining
        """
        self._obj.assigned_datas = []
        return self

    def add_assigned_port(self, item: RoleBasedPortAssignment) -> "SwcServiceDependencyBuilder":
        """Add a single item to assigned_ports list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.assigned_ports.append(item)
        return self

    def clear_assigned_ports(self) -> "SwcServiceDependencyBuilder":
        """Clear all items from assigned_ports list.

        Returns:
            self for method chaining
        """
        self._obj.assigned_ports = []
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


    def build(self) -> SwcServiceDependency:
        """Build and return the SwcServiceDependency instance with validation."""
        self._validate_instance()
        pass
        return self._obj