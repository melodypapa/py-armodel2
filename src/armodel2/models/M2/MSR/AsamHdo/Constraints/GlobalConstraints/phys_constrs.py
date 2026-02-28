"""PhysConstrs AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 406)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2043)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_Constraints_GlobalConstraints.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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
from armodel2.models.M2.MSR.AsamHdo.Units.unit import (
    Unit,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class PhysConstrs(ARObject):
    """AUTOSAR PhysConstrs."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "PHYS-CONSTRS"


    lower_limit: Optional[Limit]
    max_diff: Optional[Numerical]
    max_gradient: Optional[Numerical]
    monotony: Optional[MonotonyEnum]
    scale_constrs: list[ScaleConstr]
    upper_limit: Optional[Limit]
    unit_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "LOWER-LIMIT": lambda obj, elem: setattr(obj, "lower_limit", elem.text),
        "MAX-DIFF": lambda obj, elem: setattr(obj, "max_diff", elem.text),
        "MAX-GRADIENT": lambda obj, elem: setattr(obj, "max_gradient", elem.text),
        "MONOTONY": lambda obj, elem: setattr(obj, "monotony", MonotonyEnum.deserialize(elem)),
        "SCALE-CONSTRS": lambda obj, elem: obj.scale_constrs.append(ScaleConstr.deserialize(elem)),
        "UPPER-LIMIT": lambda obj, elem: setattr(obj, "upper_limit", elem.text),
        "UNIT-REF": lambda obj, elem: setattr(obj, "unit_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize PhysConstrs."""
        super().__init__()
        self.lower_limit: Optional[Limit] = None
        self.max_diff: Optional[Numerical] = None
        self.max_gradient: Optional[Numerical] = None
        self.monotony: Optional[MonotonyEnum] = None
        self.scale_constrs: list[ScaleConstr] = []
        self.upper_limit: Optional[Limit] = None
        self.unit_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize PhysConstrs to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(PhysConstrs, self).serialize()

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

        # Serialize unit_ref
        if self.unit_ref is not None:
            serialized = SerializationHelper.serialize_item(self.unit_ref, "Unit")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("UNIT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PhysConstrs":
        """Deserialize XML element to PhysConstrs object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PhysConstrs object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PhysConstrs, cls).deserialize(element)

        # Parse lower_limit
        child = SerializationHelper.find_child_element(element, "LOWER-LIMIT")
        if child is not None:
            lower_limit_value = SerializationHelper.deserialize_by_tag(child, "Limit")
            obj.lower_limit = lower_limit_value

        # Parse max_diff
        child = SerializationHelper.find_child_element(element, "MAX-DIFF")
        if child is not None:
            max_diff_value = child.text
            obj.max_diff = max_diff_value

        # Parse max_gradient
        child = SerializationHelper.find_child_element(element, "MAX-GRADIENT")
        if child is not None:
            max_gradient_value = child.text
            obj.max_gradient = max_gradient_value

        # Parse monotony
        child = SerializationHelper.find_child_element(element, "MONOTONY")
        if child is not None:
            monotony_value = MonotonyEnum.deserialize(child)
            obj.monotony = monotony_value

        # Parse scale_constrs (list from container "SCALE-CONSTRS")
        obj.scale_constrs = []
        container = SerializationHelper.find_child_element(element, "SCALE-CONSTRS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.scale_constrs.append(child_value)

        # Parse upper_limit
        child = SerializationHelper.find_child_element(element, "UPPER-LIMIT")
        if child is not None:
            upper_limit_value = SerializationHelper.deserialize_by_tag(child, "Limit")
            obj.upper_limit = upper_limit_value

        # Parse unit_ref
        child = SerializationHelper.find_child_element(element, "UNIT-REF")
        if child is not None:
            unit_ref_value = ARRef.deserialize(child)
            obj.unit_ref = unit_ref_value

        return obj



class PhysConstrsBuilder(BuilderBase):
    """Builder for PhysConstrs with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: PhysConstrs = PhysConstrs()


    def with_lower_limit(self, value: Optional[Limit]) -> "PhysConstrsBuilder":
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

    def with_max_diff(self, value: Optional[Numerical]) -> "PhysConstrsBuilder":
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

    def with_max_gradient(self, value: Optional[Numerical]) -> "PhysConstrsBuilder":
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

    def with_monotony(self, value: Optional[MonotonyEnum]) -> "PhysConstrsBuilder":
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

    def with_scale_constrs(self, items: list[ScaleConstr]) -> "PhysConstrsBuilder":
        """Set scale_constrs list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.scale_constrs = list(items) if items else []
        return self

    def with_upper_limit(self, value: Optional[Limit]) -> "PhysConstrsBuilder":
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

    def with_unit(self, value: Optional[Unit]) -> "PhysConstrsBuilder":
        """Set unit attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.unit = value
        return self


    def add_scale_constr(self, item: ScaleConstr) -> "PhysConstrsBuilder":
        """Add a single item to scale_constrs list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.scale_constrs.append(item)
        return self

    def clear_scale_constrs(self) -> "PhysConstrsBuilder":
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


    def build(self) -> PhysConstrs:
        """Build and return the PhysConstrs instance with validation."""
        self._validate_instance()
        pass
        return self._obj