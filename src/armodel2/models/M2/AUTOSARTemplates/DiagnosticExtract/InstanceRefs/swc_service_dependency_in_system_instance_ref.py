"""SwcServiceDependencyInSystemInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 369)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_InstanceRefs.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.root_sw_composition_prototype import (
    RootSwCompositionPrototype,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SwcServiceDependencyInSystemInstanceRef(ARObject):
    """AUTOSAR SwcServiceDependencyInSystemInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SWC-SERVICE-DEPENDENCY-IN-SYSTEM-INSTANCE-REF"


    context_root_sw_ref: Optional[ARRef]
    context_sw_prototype_refs: list[Any]
    target_swc_ref: Optional[Any]
    _DESERIALIZE_DISPATCH = {
        "CONTEXT-ROOT-SW-REF": lambda obj, elem: setattr(obj, "context_root_sw_ref", ARRef.deserialize(elem)),
        "CONTEXT-SW-PROTOTYPES": lambda obj, elem: obj.context_sw_prototype_refs.append(ARRef.deserialize(elem)),
        "TARGET-SWC-REF": lambda obj, elem: setattr(obj, "target_swc_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize SwcServiceDependencyInSystemInstanceRef."""
        super().__init__()
        self.context_root_sw_ref: Optional[ARRef] = None
        self.context_sw_prototype_refs: list[Any] = []
        self.target_swc_ref: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize SwcServiceDependencyInSystemInstanceRef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwcServiceDependencyInSystemInstanceRef, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize context_root_sw_ref
        if self.context_root_sw_ref is not None:
            serialized = SerializationHelper.serialize_item(self.context_root_sw_ref, "RootSwCompositionPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONTEXT-ROOT-SW-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize context_sw_prototype_refs (list to container "CONTEXT-SW-PROTOTYPE-REFS")
        if self.context_sw_prototype_refs:
            wrapper = ET.Element("CONTEXT-SW-PROTOTYPE-REFS")
            for item in self.context_sw_prototype_refs:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    child_elem = ET.Element("CONTEXT-SW-PROTOTYPE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize target_swc_ref
        if self.target_swc_ref is not None:
            serialized = SerializationHelper.serialize_item(self.target_swc_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TARGET-SWC-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwcServiceDependencyInSystemInstanceRef":
        """Deserialize XML element to SwcServiceDependencyInSystemInstanceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwcServiceDependencyInSystemInstanceRef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwcServiceDependencyInSystemInstanceRef, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CONTEXT-ROOT-SW-REF":
                setattr(obj, "context_root_sw_ref", ARRef.deserialize(child))
            elif tag == "CONTEXT-SW-PROTOTYPES":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.context_sw_prototype_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "any (SwComponent)"))
            elif tag == "TARGET-SWC-REF":
                setattr(obj, "target_swc_ref", ARRef.deserialize(child))

        return obj



class SwcServiceDependencyInSystemInstanceRefBuilder(BuilderBase):
    """Builder for SwcServiceDependencyInSystemInstanceRef with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SwcServiceDependencyInSystemInstanceRef = SwcServiceDependencyInSystemInstanceRef()


    def with_context_root_sw(self, value: Optional[RootSwCompositionPrototype]) -> "SwcServiceDependencyInSystemInstanceRefBuilder":
        """Set context_root_sw attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.context_root_sw = value
        return self

    def with_context_sw_prototypes(self, items: list[any (SwComponent)]) -> "SwcServiceDependencyInSystemInstanceRefBuilder":
        """Set context_sw_prototypes list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.context_sw_prototypes = list(items) if items else []
        return self

    def with_target_swc(self, value: Optional[any (SwcService)]) -> "SwcServiceDependencyInSystemInstanceRefBuilder":
        """Set target_swc attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.target_swc = value
        return self


    def add_context_sw_prototype(self, item: any (SwComponent)) -> "SwcServiceDependencyInSystemInstanceRefBuilder":
        """Add a single item to context_sw_prototypes list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.context_sw_prototypes.append(item)
        return self

    def clear_context_sw_prototypes(self) -> "SwcServiceDependencyInSystemInstanceRefBuilder":
        """Clear all items from context_sw_prototypes list.

        Returns:
            self for method chaining
        """
        self._obj.context_sw_prototypes = []
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


    def build(self) -> SwcServiceDependencyInSystemInstanceRef:
        """Build and return the SwcServiceDependencyInSystemInstanceRef instance with validation."""
        self._validate_instance()
        pass
        return self._obj