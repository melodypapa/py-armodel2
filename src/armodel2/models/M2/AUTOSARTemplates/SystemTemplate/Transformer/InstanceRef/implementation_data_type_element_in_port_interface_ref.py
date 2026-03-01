"""ImplementationDataTypeElementInPortInterfaceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 789)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer_InstanceRef.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.data_prototype_reference import (
    DataPrototypeReference,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.data_prototype_reference import DataPrototypeReferenceBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.autosar_data_prototype import (
    AutosarDataPrototype,
)

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes.abstract_implementation_data_type import (
        AbstractImplementationDataType,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class ImplementationDataTypeElementInPortInterfaceRef(DataPrototypeReference):
    """AUTOSAR ImplementationDataTypeElementInPortInterfaceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "IMPLEMENTATION-DATA-TYPE-ELEMENT-IN-PORT-INTERFACE-REF"


    context_refs: list[Any]
    root_data_ref: Optional[ARRef]
    target_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "CONTEXTS": lambda obj, elem: obj.context_refs.append(ARRef.deserialize(elem)),
        "ROOT-DATA-REF": ("_POLYMORPHIC", "root_data_ref", ["ArgumentDataPrototype", "ParameterDataPrototype", "VariableDataPrototype"]),
        "TARGET-REF": ("_POLYMORPHIC", "target_ref", ["ImplementationDataType"]),
    }


    def __init__(self) -> None:
        """Initialize ImplementationDataTypeElementInPortInterfaceRef."""
        super().__init__()
        self.context_refs: list[Any] = []
        self.root_data_ref: Optional[ARRef] = None
        self.target_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize ImplementationDataTypeElementInPortInterfaceRef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ImplementationDataTypeElementInPortInterfaceRef, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

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

        # Serialize root_data_ref
        if self.root_data_ref is not None:
            serialized = SerializationHelper.serialize_item(self.root_data_ref, "AutosarDataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ROOT-DATA-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize target_ref
        if self.target_ref is not None:
            serialized = SerializationHelper.serialize_item(self.target_ref, "AbstractImplementationDataType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TARGET-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ImplementationDataTypeElementInPortInterfaceRef":
        """Deserialize XML element to ImplementationDataTypeElementInPortInterfaceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ImplementationDataTypeElementInPortInterfaceRef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ImplementationDataTypeElementInPortInterfaceRef, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "CONTEXTS":
                obj.context_refs.append(ARRef.deserialize(child))
            elif tag == "ROOT-DATA-REF":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "ARGUMENT-DATA-PROTOTYPE":
                        setattr(obj, "root_data_ref", SerializationHelper.deserialize_by_tag(child[0], "ArgumentDataPrototype"))
                    elif concrete_tag == "PARAMETER-DATA-PROTOTYPE":
                        setattr(obj, "root_data_ref", SerializationHelper.deserialize_by_tag(child[0], "ParameterDataPrototype"))
                    elif concrete_tag == "VARIABLE-DATA-PROTOTYPE":
                        setattr(obj, "root_data_ref", SerializationHelper.deserialize_by_tag(child[0], "VariableDataPrototype"))
            elif tag == "TARGET-REF":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "IMPLEMENTATION-DATA-TYPE":
                        setattr(obj, "target_ref", SerializationHelper.deserialize_by_tag(child[0], "ImplementationDataType"))

        return obj



class ImplementationDataTypeElementInPortInterfaceRefBuilder(DataPrototypeReferenceBuilder):
    """Builder for ImplementationDataTypeElementInPortInterfaceRef with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ImplementationDataTypeElementInPortInterfaceRef = ImplementationDataTypeElementInPortInterfaceRef()


    def with_contexts(self, items: list[any (AbstractImplementation)]) -> "ImplementationDataTypeElementInPortInterfaceRefBuilder":
        """Set contexts list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.contexts = list(items) if items else []
        return self

    def with_root_data(self, value: Optional[AutosarDataPrototype]) -> "ImplementationDataTypeElementInPortInterfaceRefBuilder":
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

    def with_target(self, value: Optional[AbstractImplementationDataType]) -> "ImplementationDataTypeElementInPortInterfaceRefBuilder":
        """Set target attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.target = value
        return self


    def add_context(self, item: any (AbstractImplementation)) -> "ImplementationDataTypeElementInPortInterfaceRefBuilder":
        """Add a single item to contexts list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.contexts.append(item)
        return self

    def clear_contexts(self) -> "ImplementationDataTypeElementInPortInterfaceRefBuilder":
        """Clear all items from contexts list.

        Returns:
            self for method chaining
        """
        self._obj.contexts = []
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


    def build(self) -> ImplementationDataTypeElementInPortInterfaceRef:
        """Build and return the ImplementationDataTypeElementInPortInterfaceRef instance with validation."""
        self._validate_instance()
        pass
        return self._obj