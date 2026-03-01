"""InternalConstrs AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 407)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_Constraints_GlobalConstraints.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    MonotonyEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Limit,
    Numerical,
)
from armodel2.models.M2.MSR.AsamHdo.Constraints.GlobalConstraints.scale_constr import (
    ScaleConstr,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class InternalConstrs(ARObject):
    """AUTOSAR InternalConstrs."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "INTERNAL-CONSTRS"


    lower_limit: Optional[Limit]
    max_diff: Optional[Numerical]
    max_gradient: Optional[Numerical]
    monotony: Optional[MonotonyEnum]
    scale_constrs: list[ScaleConstr]
    upper_limit: Optional[Limit]
    _DESERIALIZE_DISPATCH = {
        "LOWER-LIMIT": lambda obj, elem: setattr(obj, "lower_limit", SerializationHelper.deserialize_by_tag(elem, "Limit")),
        "MAX-DIFF": lambda obj, elem: setattr(obj, "max_diff", SerializationHelper.deserialize_by_tag(elem, "Numerical")),
        "MAX-GRADIENT": lambda obj, elem: setattr(obj, "max_gradient", SerializationHelper.deserialize_by_tag(elem, "Numerical")),
        "MONOTONY": lambda obj, elem: setattr(obj, "monotony", MonotonyEnum.deserialize(elem)),
        "SCALE-CONSTRS": lambda obj, elem: obj.scale_constrs.append(SerializationHelper.deserialize_by_tag(elem, "ScaleConstr")),
        "UPPER-LIMIT": lambda obj, elem: setattr(obj, "upper_limit", SerializationHelper.deserialize_by_tag(elem, "Limit")),
    }


    def __init__(self) -> None:
        """Initialize InternalConstrs."""
        super().__init__()
        self.lower_limit: Optional[Limit] = None
        self.max_diff: Optional[Numerical] = None
        self.max_gradient: Optional[Numerical] = None
        self.monotony: Optional[MonotonyEnum] = None
        self.scale_constrs: list[ScaleConstr] = []
        self.upper_limit: Optional[Limit] = None

    def serialize(self) -> ET.Element:
        """Serialize InternalConstrs to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(InternalConstrs, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize lower_limit
        if self.lower_limit is not None:
            serialized = SerializationHelper.serialize_item(self.lower_limit, "Limit")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LOWER-LIMIT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_diff
        if self.max_diff is not None:
            serialized = SerializationHelper.serialize_item(self.max_diff, "Numerical")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-DIFF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_gradient
        if self.max_gradient is not None:
            serialized = SerializationHelper.serialize_item(self.max_gradient, "Numerical")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-GRADIENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize monotony
        if self.monotony is not None:
            serialized = SerializationHelper.serialize_item(self.monotony, "MonotonyEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MONOTONY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize scale_constrs (list to container "SCALE-CONSTRS")
        if self.scale_constrs:
            wrapper = ET.Element("SCALE-CONSTRS")
            for item in self.scale_constrs:
                serialized = SerializationHelper.serialize_item(item, "ScaleConstr")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize upper_limit
        if self.upper_limit is not None:
            serialized = SerializationHelper.serialize_item(self.upper_limit, "Limit")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("UPPER-LIMIT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "InternalConstrs":
        """Deserialize XML element to InternalConstrs object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized InternalConstrs object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(InternalConstrs, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "LOWER-LIMIT":
                setattr(obj, "lower_limit", SerializationHelper.deserialize_by_tag(child, "Limit"))
            elif tag == "MAX-DIFF":
                setattr(obj, "max_diff", SerializationHelper.deserialize_by_tag(child, "Numerical"))
            elif tag == "MAX-GRADIENT":
                setattr(obj, "max_gradient", SerializationHelper.deserialize_by_tag(child, "Numerical"))
            elif tag == "MONOTONY":
                setattr(obj, "monotony", MonotonyEnum.deserialize(child))
            elif tag == "SCALE-CONSTRS":
                # Iterate through wrapper children
                for item_elem in child:
                    item_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    obj.scale_constrs.append(SerializationHelper.deserialize_by_tag(item_elem, "ScaleConstr"))
            elif tag == "UPPER-LIMIT":
                setattr(obj, "upper_limit", SerializationHelper.deserialize_by_tag(child, "Limit"))

        return obj



class InternalConstrsBuilder(BuilderBase):
    """Builder for InternalConstrs with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: InternalConstrs = InternalConstrs()


    def with_lower_limit(self, value: Optional[Limit]) -> "InternalConstrsBuilder":
        """Set lower_limit attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.lower_limit = value
        return self

    def with_max_diff(self, value: Optional[Numerical]) -> "InternalConstrsBuilder":
        """Set max_diff attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.max_diff = value
        return self

    def with_max_gradient(self, value: Optional[Numerical]) -> "InternalConstrsBuilder":
        """Set max_gradient attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.max_gradient = value
        return self

    def with_monotony(self, value: Optional[MonotonyEnum]) -> "InternalConstrsBuilder":
        """Set monotony attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.monotony = value
        return self

    def with_scale_constrs(self, items: list[ScaleConstr]) -> "InternalConstrsBuilder":
        """Set scale_constrs list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.scale_constrs = list(items) if items else []
        return self

    def with_upper_limit(self, value: Optional[Limit]) -> "InternalConstrsBuilder":
        """Set upper_limit attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.upper_limit = value
        return self


    def add_scale_constr(self, item: ScaleConstr) -> "InternalConstrsBuilder":
        """Add a single item to scale_constrs list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.scale_constrs.append(item)
        return self

    def clear_scale_constrs(self) -> "InternalConstrsBuilder":
        """Clear all items from scale_constrs list.

        Returns:
            self for method chaining
        """
        self._obj.scale_constrs = []
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


    def build(self) -> InternalConstrs:
        """Build and return the InternalConstrs instance with validation."""
        self._validate_instance()
        pass
        return self._obj