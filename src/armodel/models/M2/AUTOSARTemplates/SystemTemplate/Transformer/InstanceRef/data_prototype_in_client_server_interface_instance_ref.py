"""DataPrototypeInClientServerInterfaceInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 788)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer_InstanceRef.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.InstanceRef.data_prototype_in_port_interface_instance_ref import (
    DataPrototypeInPortInterfaceInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.autosar_data_prototype import (
    AutosarDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_interface import (
    ClientServerInterface,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)


class DataPrototypeInClientServerInterfaceInstanceRef(DataPrototypeInPortInterfaceInstanceRef):
    """AUTOSAR DataPrototypeInClientServerInterfaceInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    base_ref: Optional[ARRef]
    context_data_refs: list[Any]
    root_data_prototype_in_cs_ref: Optional[ARRef]
    target_data_prototype_in_cs_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize DataPrototypeInClientServerInterfaceInstanceRef."""
        super().__init__()
        self.base_ref: Optional[ARRef] = None
        self.context_data_refs: list[Any] = []
        self.root_data_prototype_in_cs_ref: Optional[ARRef] = None
        self.target_data_prototype_in_cs_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize DataPrototypeInClientServerInterfaceInstanceRef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DataPrototypeInClientServerInterfaceInstanceRef, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize base_ref
        if self.base_ref is not None:
            serialized = SerializationHelper.serialize_item(self.base_ref, "ClientServerInterface")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BASE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize context_data_refs (list to container "CONTEXT-DATA-REFS")
        if self.context_data_refs:
            wrapper = ET.Element("CONTEXT-DATA-REFS")
            for item in self.context_data_refs:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    child_elem = ET.Element("CONTEXT-DATA-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize root_data_prototype_in_cs_ref
        if self.root_data_prototype_in_cs_ref is not None:
            serialized = SerializationHelper.serialize_item(self.root_data_prototype_in_cs_ref, "AutosarDataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ROOT-DATA-PROTOTYPE-IN-CS-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize target_data_prototype_in_cs_ref
        if self.target_data_prototype_in_cs_ref is not None:
            serialized = SerializationHelper.serialize_item(self.target_data_prototype_in_cs_ref, "DataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TARGET-DATA-PROTOTYPE-IN-CS-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataPrototypeInClientServerInterfaceInstanceRef":
        """Deserialize XML element to DataPrototypeInClientServerInterfaceInstanceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DataPrototypeInClientServerInterfaceInstanceRef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DataPrototypeInClientServerInterfaceInstanceRef, cls).deserialize(element)

        # Parse base_ref
        child = SerializationHelper.find_child_element(element, "BASE-REF")
        if child is not None:
            base_ref_value = ARRef.deserialize(child)
            obj.base_ref = base_ref_value

        # Parse context_data_refs (list from container "CONTEXT-DATA-REFS")
        obj.context_data_refs = []
        container = SerializationHelper.find_child_element(element, "CONTEXT-DATA-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.context_data_refs.append(child_value)

        # Parse root_data_prototype_in_cs_ref
        child = SerializationHelper.find_child_element(element, "ROOT-DATA-PROTOTYPE-IN-CS-REF")
        if child is not None:
            root_data_prototype_in_cs_ref_value = ARRef.deserialize(child)
            obj.root_data_prototype_in_cs_ref = root_data_prototype_in_cs_ref_value

        # Parse target_data_prototype_in_cs_ref
        child = SerializationHelper.find_child_element(element, "TARGET-DATA-PROTOTYPE-IN-CS-REF")
        if child is not None:
            target_data_prototype_in_cs_ref_value = ARRef.deserialize(child)
            obj.target_data_prototype_in_cs_ref = target_data_prototype_in_cs_ref_value

        return obj



class DataPrototypeInClientServerInterfaceInstanceRefBuilder:
    """Builder for DataPrototypeInClientServerInterfaceInstanceRef with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: DataPrototypeInClientServerInterfaceInstanceRef = DataPrototypeInClientServerInterfaceInstanceRef()


    def with_abstract_base(self, value: Optional[PortInterface]) -> "DataPrototypeInClientServerInterfaceInstanceRefBuilder":
        """Set abstract_base attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.abstract_base = value
        return self

    def with_context_datas(self, items: list[any (ApplicationComposite)]) -> "DataPrototypeInClientServerInterfaceInstanceRefBuilder":
        """Set context_datas list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.context_datas = list(items) if items else []
        return self

    def with_root_data(self, value: Optional[AutosarDataPrototype]) -> "DataPrototypeInClientServerInterfaceInstanceRefBuilder":
        """Set root_data attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.root_data = value
        return self

    def with_target_data(self, value: DataPrototype) -> "DataPrototypeInClientServerInterfaceInstanceRefBuilder":
        """Set target_data attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.target_data = value
        return self

    def with_base(self, value: Optional[ClientServerInterface]) -> "DataPrototypeInClientServerInterfaceInstanceRefBuilder":
        """Set base attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.base = value
        return self

    def with_root_data_prototype_in_cs(self, value: Optional[AutosarDataPrototype]) -> "DataPrototypeInClientServerInterfaceInstanceRefBuilder":
        """Set root_data_prototype_in_cs attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.root_data_prototype_in_cs = value
        return self

    def with_target_data_prototype_in_cs(self, value: Optional[DataPrototype]) -> "DataPrototypeInClientServerInterfaceInstanceRefBuilder":
        """Set target_data_prototype_in_cs attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.target_data_prototype_in_cs = value
        return self


    def add_context_data(self, item: any (ApplicationComposite)) -> "DataPrototypeInClientServerInterfaceInstanceRefBuilder":
        """Add a single item to context_datas list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.context_datas.append(item)
        return self

    def clear_context_datas(self) -> "DataPrototypeInClientServerInterfaceInstanceRefBuilder":
        """Clear all items from context_datas list.

        Returns:
            self for method chaining
        """
        self._obj.context_datas = []
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


    def build(self) -> DataPrototypeInClientServerInterfaceInstanceRef:
        """Build and return the DataPrototypeInClientServerInterfaceInstanceRef instance with validation."""
        self._validate_instance()
        pass
        return self._obj