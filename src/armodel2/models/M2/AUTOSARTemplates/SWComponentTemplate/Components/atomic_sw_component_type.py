"""AtomicSwComponentType AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 304)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 300)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 70)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2000)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 205)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 43)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 161)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.sw_component_type import (
    SwComponentType,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.sw_component_type import SwComponentTypeBuilder
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.symbol_props import (
    SymbolProps,
)

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.swc_internal_behavior import (
        SwcInternalBehavior,
    )



from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class AtomicSwComponentType(SwComponentType, ABC):
    """AUTOSAR AtomicSwComponentType."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    internal_behaviors: list[SwcInternalBehavior]
    symbol_props: Optional[SymbolProps]
    _DESERIALIZE_DISPATCH = {
        "INTERNAL-BEHAVIORS": lambda obj, elem: obj.internal_behaviors.append(SerializationHelper.deserialize_by_tag(elem, "SwcInternalBehavior")),
        "SYMBOL-PROPS": lambda obj, elem: setattr(obj, "symbol_props", SerializationHelper.deserialize_by_tag(elem, "SymbolProps")),
    }


    def __init__(self) -> None:
        """Initialize AtomicSwComponentType."""
        super().__init__()
        self.internal_behaviors: list[SwcInternalBehavior] = []
        self.symbol_props: Optional[SymbolProps] = None

    def serialize(self) -> ET.Element:
        """Serialize AtomicSwComponentType to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AtomicSwComponentType, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize internal_behaviors (list to container "INTERNAL-BEHAVIORS")
        if self.internal_behaviors:
            wrapper = ET.Element("INTERNAL-BEHAVIORS")
            for item in self.internal_behaviors:
                serialized = SerializationHelper.serialize_item(item, "SwcInternalBehavior")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize symbol_props
        if self.symbol_props is not None:
            serialized = SerializationHelper.serialize_item(self.symbol_props, "SymbolProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SYMBOL-PROPS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AtomicSwComponentType":
        """Deserialize XML element to AtomicSwComponentType object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AtomicSwComponentType object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AtomicSwComponentType, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "INTERNAL-BEHAVIORS":
                # Iterate through wrapper children
                for item_elem in child:
                    item_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    obj.internal_behaviors.append(SerializationHelper.deserialize_by_tag(item_elem, "SwcInternalBehavior"))
            elif tag == "SYMBOL-PROPS":
                setattr(obj, "symbol_props", SerializationHelper.deserialize_by_tag(child, "SymbolProps"))

        return obj



class AtomicSwComponentTypeBuilder(SwComponentTypeBuilder):
    """Builder for AtomicSwComponentType with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: AtomicSwComponentType = AtomicSwComponentType()


    def with_internal_behaviors(self, items: list[SwcInternalBehavior]) -> "AtomicSwComponentTypeBuilder":
        """Set internal_behaviors list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.internal_behaviors = list(items) if items else []
        return self

    def with_symbol_props(self, value: Optional[SymbolProps]) -> "AtomicSwComponentTypeBuilder":
        """Set symbol_props attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.symbol_props = value
        return self


    def add_internal_behavior(self, item: SwcInternalBehavior) -> "AtomicSwComponentTypeBuilder":
        """Add a single item to internal_behaviors list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.internal_behaviors.append(item)
        return self

    def clear_internal_behaviors(self) -> "AtomicSwComponentTypeBuilder":
        """Clear all items from internal_behaviors list.

        Returns:
            self for method chaining
        """
        self._obj.internal_behaviors = []
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


    @abstractmethod
    def build(self) -> AtomicSwComponentType:
        """Build and return the AtomicSwComponentType instance (abstract)."""
        raise NotImplementedError