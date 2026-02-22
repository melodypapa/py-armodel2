"""BswServiceDependency AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 225)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 225)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 978)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_dependency import (
    ServiceDependency,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.role_based_bsw_module_entry_assignment import (
    RoleBasedBswModuleEntryAssignment,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_needs import (
    ServiceNeeds,
)


class BswServiceDependency(ServiceDependency):
    """AUTOSAR BswServiceDependency."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    assigned_datas: list[Any]
    assigned_entries: list[RoleBasedBswModuleEntryAssignment]
    ident: Optional[Any]
    service_needs: Optional[ServiceNeeds]
    def __init__(self) -> None:
        """Initialize BswServiceDependency."""
        super().__init__()
        self.assigned_datas: list[Any] = []
        self.assigned_entries: list[RoleBasedBswModuleEntryAssignment] = []
        self.ident: Optional[Any] = None
        self.service_needs: Optional[ServiceNeeds] = None

    def serialize(self) -> ET.Element:
        """Serialize BswServiceDependency to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BswServiceDependency, self).serialize()

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

        # Serialize assigned_entries (list to container "ASSIGNED-ENTRIES")
        if self.assigned_entries:
            wrapper = ET.Element("ASSIGNED-ENTRIES")
            for item in self.assigned_entries:
                serialized = SerializationHelper.serialize_item(item, "RoleBasedBswModuleEntryAssignment")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize ident
        if self.ident is not None:
            serialized = SerializationHelper.serialize_item(self.ident, "Any")
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
    def deserialize(cls, element: ET.Element) -> "BswServiceDependency":
        """Deserialize XML element to BswServiceDependency object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswServiceDependency object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BswServiceDependency, cls).deserialize(element)

        # Parse assigned_datas (list from container "ASSIGNED-DATAS")
        obj.assigned_datas = []
        container = SerializationHelper.find_child_element(element, "ASSIGNED-DATAS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.assigned_datas.append(child_value)

        # Parse assigned_entries (list from container "ASSIGNED-ENTRIES")
        obj.assigned_entries = []
        container = SerializationHelper.find_child_element(element, "ASSIGNED-ENTRIES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.assigned_entries.append(child_value)

        # Parse ident
        child = SerializationHelper.find_child_element(element, "IDENT")
        if child is not None:
            ident_value = child.text
            obj.ident = ident_value

        # Parse service_needs
        child = SerializationHelper.find_child_element(element, "SERVICE-NEEDS")
        if child is not None:
            service_needs_value = SerializationHelper.deserialize_by_tag(child, "ServiceNeeds")
            obj.service_needs = service_needs_value

        return obj



class BswServiceDependencyBuilder:
    """Builder for BswServiceDependency with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: BswServiceDependency = BswServiceDependency()


    def with_assigned_data(self, value: Optional[RoleBasedDataTypeAssignment]) -> "BswServiceDependencyBuilder":
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

    def with_diagnostic(self, value: Optional[ServiceDiagnosticRelevanceEnum]) -> "BswServiceDependencyBuilder":
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

    def with_symbolic_name_props(self, value: Optional[SymbolicNameProps]) -> "BswServiceDependencyBuilder":
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

    def with_assigned_datas(self, items: list[any (RoleBasedData)]) -> "BswServiceDependencyBuilder":
        """Set assigned_datas list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.assigned_datas = list(items) if items else []
        return self

    def with_assigned_entries(self, items: list[RoleBasedBswModuleEntryAssignment]) -> "BswServiceDependencyBuilder":
        """Set assigned_entries list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.assigned_entries = list(items) if items else []
        return self

    def with_ident(self, value: Optional[any (BswService)]) -> "BswServiceDependencyBuilder":
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

    def with_service_needs(self, value: Optional[ServiceNeeds]) -> "BswServiceDependencyBuilder":
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


    def add_assigned_data(self, item: any (RoleBasedData)) -> "BswServiceDependencyBuilder":
        """Add a single item to assigned_datas list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.assigned_datas.append(item)
        return self

    def clear_assigned_datas(self) -> "BswServiceDependencyBuilder":
        """Clear all items from assigned_datas list.

        Returns:
            self for method chaining
        """
        self._obj.assigned_datas = []
        return self

    def add_assigned_entrie(self, item: RoleBasedBswModuleEntryAssignment) -> "BswServiceDependencyBuilder":
        """Add a single item to assigned_entries list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.assigned_entries.append(item)
        return self

    def clear_assigned_entries(self) -> "BswServiceDependencyBuilder":
        """Clear all items from assigned_entries list.

        Returns:
            self for method chaining
        """
        self._obj.assigned_entries = []
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


    def build(self) -> BswServiceDependency:
        """Build and return the BswServiceDependency instance with validation."""
        self._validate_instance()
        pass
        return self._obj