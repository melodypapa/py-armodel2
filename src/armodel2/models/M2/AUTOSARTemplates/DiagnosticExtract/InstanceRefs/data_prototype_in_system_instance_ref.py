"""DataPrototypeInSystemInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 368)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_InstanceRefs.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.autosar_data_prototype import (
    AutosarDataPrototype,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.root_sw_composition_prototype import (
    RootSwCompositionPrototype,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.system import (
    System,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DataPrototypeInSystemInstanceRef(ARObject):
    """AUTOSAR DataPrototypeInSystemInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DATA-PROTOTYPE-IN-SYSTEM-INSTANCE-REF"


    base_ref: Optional[ARRef]
    context_refs: list[Any]
    context_data_refs: list[Any]
    context_port_ref: Optional[ARRef]
    context_root_ref: Optional[ARRef]
    root_data_prototype_ref: Optional[ARRef]
    target_data_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "BASE-REF": lambda obj, elem: setattr(obj, "base_ref", ARRef.deserialize(elem)),
        "CONTEXT-REFS": lambda obj, elem: [obj.context_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
        "CONTEXT-DATA-REFS": lambda obj, elem: [obj.context_data_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
        "CONTEXT-PORT-REF": ("_POLYMORPHIC", "context_port_ref", ["PPortPrototype", "RPortPrototype", "PRPortPrototype"]),
        "CONTEXT-ROOT-REF": lambda obj, elem: setattr(obj, "context_root_ref", ARRef.deserialize(elem)),
        "ROOT-DATA-PROTOTYPE-REF": ("_POLYMORPHIC", "root_data_prototype_ref", ["ArgumentDataPrototype", "ParameterDataPrototype", "VariableDataPrototype"]),
        "TARGET-DATA-REF": ("_POLYMORPHIC", "target_data_ref", ["ApplicationCompositeElementDataPrototype", "AutosarDataPrototype"]),
    }


    def __init__(self) -> None:
        """Initialize DataPrototypeInSystemInstanceRef."""
        super().__init__()
        self.base_ref: Optional[ARRef] = None
        self.context_refs: list[Any] = []
        self.context_data_refs: list[Any] = []
        self.context_port_ref: Optional[ARRef] = None
        self.context_root_ref: Optional[ARRef] = None
        self.root_data_prototype_ref: Optional[ARRef] = None
        self.target_data_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize DataPrototypeInSystemInstanceRef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DataPrototypeInSystemInstanceRef, self).serialize()

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
            serialized = SerializationHelper.serialize_item(self.base_ref, "System")
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

        # Serialize context_refs (list to container "CONTEXT-REFS")
        if self.context_refs:
            wrapper = ET.Element("CONTEXT-REFS")
            for item in self.context_refs:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    child_elem = ET.Element("CONTEXT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

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

        # Serialize context_port_ref
        if self.context_port_ref is not None:
            serialized = SerializationHelper.serialize_item(self.context_port_ref, "PortPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONTEXT-PORT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize context_root_ref
        if self.context_root_ref is not None:
            serialized = SerializationHelper.serialize_item(self.context_root_ref, "RootSwCompositionPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONTEXT-ROOT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize root_data_prototype_ref
        if self.root_data_prototype_ref is not None:
            serialized = SerializationHelper.serialize_item(self.root_data_prototype_ref, "AutosarDataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ROOT-DATA-PROTOTYPE-REF")
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
    def deserialize(cls, element: ET.Element) -> "DataPrototypeInSystemInstanceRef":
        """Deserialize XML element to DataPrototypeInSystemInstanceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DataPrototypeInSystemInstanceRef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DataPrototypeInSystemInstanceRef, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "BASE-REF":
                setattr(obj, "base_ref", ARRef.deserialize(child))
            elif tag == "CONTEXT-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.context_refs.append(ARRef.deserialize(item_elem))
            elif tag == "CONTEXT-DATA-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.context_data_refs.append(ARRef.deserialize(item_elem))
            elif tag == "CONTEXT-PORT-REF":
                setattr(obj, "context_port_ref", ARRef.deserialize(child))
            elif tag == "CONTEXT-ROOT-REF":
                setattr(obj, "context_root_ref", ARRef.deserialize(child))
            elif tag == "ROOT-DATA-PROTOTYPE-REF":
                setattr(obj, "root_data_prototype_ref", ARRef.deserialize(child))
            elif tag == "TARGET-DATA-REF":
                setattr(obj, "target_data_ref", ARRef.deserialize(child))

        return obj



class DataPrototypeInSystemInstanceRefBuilder(BuilderBase):
    """Builder for DataPrototypeInSystemInstanceRef with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DataPrototypeInSystemInstanceRef = DataPrototypeInSystemInstanceRef()


    def with_base(self, value: Optional[System]) -> "DataPrototypeInSystemInstanceRefBuilder":
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

    def with_contexts(self, items: list[any (SwComponent)]) -> "DataPrototypeInSystemInstanceRefBuilder":
        """Set contexts list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.contexts = list(items) if items else []
        return self

    def with_context_datas(self, items: list[any (ApplicationComposite)]) -> "DataPrototypeInSystemInstanceRefBuilder":
        """Set context_datas list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.context_datas = list(items) if items else []
        return self

    def with_context_port(self, value: Optional[PortPrototype]) -> "DataPrototypeInSystemInstanceRefBuilder":
        """Set context_port attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.context_port = value
        return self

    def with_context_root(self, value: Optional[RootSwCompositionPrototype]) -> "DataPrototypeInSystemInstanceRefBuilder":
        """Set context_root attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.context_root = value
        return self

    def with_root_data_prototype(self, value: Optional[AutosarDataPrototype]) -> "DataPrototypeInSystemInstanceRefBuilder":
        """Set root_data_prototype attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.root_data_prototype = value
        return self

    def with_target_data(self, value: Optional[DataPrototype]) -> "DataPrototypeInSystemInstanceRefBuilder":
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


    def add_context(self, item: any (SwComponent)) -> "DataPrototypeInSystemInstanceRefBuilder":
        """Add a single item to contexts list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.contexts.append(item)
        return self

    def clear_contexts(self) -> "DataPrototypeInSystemInstanceRefBuilder":
        """Clear all items from contexts list.

        Returns:
            self for method chaining
        """
        self._obj.contexts = []
        return self

    def add_context_data(self, item: any (ApplicationComposite)) -> "DataPrototypeInSystemInstanceRefBuilder":
        """Add a single item to context_datas list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.context_datas.append(item)
        return self

    def clear_context_datas(self) -> "DataPrototypeInSystemInstanceRefBuilder":
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


    def build(self) -> DataPrototypeInSystemInstanceRef:
        """Build and return the DataPrototypeInSystemInstanceRef instance with validation."""
        self._validate_instance()
        pass
        return self._obj