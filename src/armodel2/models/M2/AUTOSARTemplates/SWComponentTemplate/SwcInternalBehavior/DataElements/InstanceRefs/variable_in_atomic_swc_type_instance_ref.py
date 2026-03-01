"""VariableInAtomicSWCTypeInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 953)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_DataElements_InstanceRefs.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.atomic_sw_component_type import (
    AtomicSwComponentType,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class VariableInAtomicSWCTypeInstanceRef(ARObject):
    """AUTOSAR VariableInAtomicSWCTypeInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "VARIABLE-IN-ATOMIC-SWC-TYPE-INSTANCE-REF"


    base_ref: Optional[ARRef]
    context_data_refs: list[Any]
    port_prototype_ref: Optional[ARRef]
    root_variable_data_prototype_ref: Optional[ARRef]
    target_data_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "BASE-REF": ("_POLYMORPHIC", "base_ref", ["ApplicationSwComponentType", "ComplexDeviceDriverSwComponentType", "EcuAbstractionSwComponentType", "NvBlockSwComponentType", "SensorActuatorSwComponentType", "ServiceProxySwComponentType", "ServiceSwComponentType"]),
        "CONTEXT-DATAS": lambda obj, elem: obj.context_data_refs.append(ARRef.deserialize(elem)),
        "PORT-PROTOTYPE-REF": ("_POLYMORPHIC", "port_prototype_ref", ["AbstractProvidedPortPrototype", "AbstractRequiredPortPrototype"]),
        "ROOT-VARIABLE-DATA-PROTOTYPE-REF": lambda obj, elem: setattr(obj, "root_variable_data_prototype_ref", ARRef.deserialize(elem)),
        "TARGET-DATA-REF": ("_POLYMORPHIC", "target_data_ref", ["ApplicationCompositeElementDataPrototype", "AutosarDataPrototype"]),
    }


    def __init__(self) -> None:
        """Initialize VariableInAtomicSWCTypeInstanceRef."""
        super().__init__()
        self.base_ref: Optional[ARRef] = None
        self.context_data_refs: list[Any] = []
        self.port_prototype_ref: Optional[ARRef] = None
        self.root_variable_data_prototype_ref: Optional[ARRef] = None
        self.target_data_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize VariableInAtomicSWCTypeInstanceRef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(VariableInAtomicSWCTypeInstanceRef, self).serialize()

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
            serialized = SerializationHelper.serialize_item(self.base_ref, "AtomicSwComponentType")
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

        # Serialize port_prototype_ref
        if self.port_prototype_ref is not None:
            serialized = SerializationHelper.serialize_item(self.port_prototype_ref, "PortPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PORT-PROTOTYPE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize root_variable_data_prototype_ref
        if self.root_variable_data_prototype_ref is not None:
            serialized = SerializationHelper.serialize_item(self.root_variable_data_prototype_ref, "VariableDataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ROOT-VARIABLE-DATA-PROTOTYPE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize target_data_ref
        if self.target_data_ref is not None:
            serialized = SerializationHelper.serialize_item(self.target_data_ref, "DataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TARGET-DATA-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "VariableInAtomicSWCTypeInstanceRef":
        """Deserialize XML element to VariableInAtomicSWCTypeInstanceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized VariableInAtomicSWCTypeInstanceRef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(VariableInAtomicSWCTypeInstanceRef, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "BASE-REF":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "APPLICATION-SW-COMPONENT-TYPE":
                        setattr(obj, "base_ref", SerializationHelper.deserialize_by_tag(child[0], "ApplicationSwComponentType"))
                    elif concrete_tag == "COMPLEX-DEVICE-DRIVER-SW-COMPONENT-TYPE":
                        setattr(obj, "base_ref", SerializationHelper.deserialize_by_tag(child[0], "ComplexDeviceDriverSwComponentType"))
                    elif concrete_tag == "ECU-ABSTRACTION-SW-COMPONENT-TYPE":
                        setattr(obj, "base_ref", SerializationHelper.deserialize_by_tag(child[0], "EcuAbstractionSwComponentType"))
                    elif concrete_tag == "NV-BLOCK-SW-COMPONENT-TYPE":
                        setattr(obj, "base_ref", SerializationHelper.deserialize_by_tag(child[0], "NvBlockSwComponentType"))
                    elif concrete_tag == "SENSOR-ACTUATOR-SW-COMPONENT-TYPE":
                        setattr(obj, "base_ref", SerializationHelper.deserialize_by_tag(child[0], "SensorActuatorSwComponentType"))
                    elif concrete_tag == "SERVICE-PROXY-SW-COMPONENT-TYPE":
                        setattr(obj, "base_ref", SerializationHelper.deserialize_by_tag(child[0], "ServiceProxySwComponentType"))
                    elif concrete_tag == "SERVICE-SW-COMPONENT-TYPE":
                        setattr(obj, "base_ref", SerializationHelper.deserialize_by_tag(child[0], "ServiceSwComponentType"))
            elif tag == "CONTEXT-DATAS":
                # Iterate through wrapper children
                for item_elem in child:
                    item_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    obj.context_data_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "any (ApplicationComposite)"))
            elif tag == "PORT-PROTOTYPE-REF":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "ABSTRACT-PROVIDED-PORT-PROTOTYPE":
                        setattr(obj, "port_prototype_ref", SerializationHelper.deserialize_by_tag(child[0], "AbstractProvidedPortPrototype"))
                    elif concrete_tag == "ABSTRACT-REQUIRED-PORT-PROTOTYPE":
                        setattr(obj, "port_prototype_ref", SerializationHelper.deserialize_by_tag(child[0], "AbstractRequiredPortPrototype"))
            elif tag == "ROOT-VARIABLE-DATA-PROTOTYPE-REF":
                setattr(obj, "root_variable_data_prototype_ref", ARRef.deserialize(child))
            elif tag == "TARGET-DATA-REF":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "APPLICATION-COMPOSITE-ELEMENT-DATA-PROTOTYPE":
                        setattr(obj, "target_data_ref", SerializationHelper.deserialize_by_tag(child[0], "ApplicationCompositeElementDataPrototype"))
                    elif concrete_tag == "AUTOSAR-DATA-PROTOTYPE":
                        setattr(obj, "target_data_ref", SerializationHelper.deserialize_by_tag(child[0], "AutosarDataPrototype"))

        return obj



class VariableInAtomicSWCTypeInstanceRefBuilder(BuilderBase):
    """Builder for VariableInAtomicSWCTypeInstanceRef with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: VariableInAtomicSWCTypeInstanceRef = VariableInAtomicSWCTypeInstanceRef()


    def with_base(self, value: Optional[AtomicSwComponentType]) -> "VariableInAtomicSWCTypeInstanceRefBuilder":
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

    def with_context_datas(self, items: list[any (ApplicationComposite)]) -> "VariableInAtomicSWCTypeInstanceRefBuilder":
        """Set context_datas list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.context_datas = list(items) if items else []
        return self

    def with_port_prototype(self, value: Optional[PortPrototype]) -> "VariableInAtomicSWCTypeInstanceRefBuilder":
        """Set port_prototype attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.port_prototype = value
        return self

    def with_root_variable_data_prototype(self, value: Optional[VariableDataPrototype]) -> "VariableInAtomicSWCTypeInstanceRefBuilder":
        """Set root_variable_data_prototype attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.root_variable_data_prototype = value
        return self

    def with_target_data(self, value: Optional[DataPrototype]) -> "VariableInAtomicSWCTypeInstanceRefBuilder":
        """Set target_data attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.target_data = value
        return self


    def add_context_data(self, item: any (ApplicationComposite)) -> "VariableInAtomicSWCTypeInstanceRefBuilder":
        """Add a single item to context_datas list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.context_datas.append(item)
        return self

    def clear_context_datas(self) -> "VariableInAtomicSWCTypeInstanceRefBuilder":
        """Clear all items from context_datas list.

        Returns:
            self for method chaining
        """
        self._obj.context_datas = []
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


    def build(self) -> VariableInAtomicSWCTypeInstanceRef:
        """Build and return the VariableInAtomicSWCTypeInstanceRef instance with validation."""
        self._validate_instance()
        pass
        return self._obj