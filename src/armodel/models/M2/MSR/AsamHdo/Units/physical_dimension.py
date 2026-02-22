"""PhysicalDimension AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 398)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_Units.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Numerical,
)


class PhysicalDimension(ARElement):
    """AUTOSAR PhysicalDimension."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    current_exp: Optional[Numerical]
    length_exp: Optional[Numerical]
    luminous_intensity_exp: Optional[Numerical]
    mass_exp: Optional[Numerical]
    molar_amount_exp: Optional[Numerical]
    temperature_exp: Optional[Numerical]
    time_exp: Optional[Numerical]
    def __init__(self) -> None:
        """Initialize PhysicalDimension."""
        super().__init__()
        self.current_exp: Optional[Numerical] = None
        self.length_exp: Optional[Numerical] = None
        self.luminous_intensity_exp: Optional[Numerical] = None
        self.mass_exp: Optional[Numerical] = None
        self.molar_amount_exp: Optional[Numerical] = None
        self.temperature_exp: Optional[Numerical] = None
        self.time_exp: Optional[Numerical] = None

    def serialize(self) -> ET.Element:
        """Serialize PhysicalDimension to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(PhysicalDimension, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize current_exp
        if self.current_exp is not None:
            serialized = SerializationHelper.serialize_item(self.current_exp, "Numerical")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CURRENT-EXP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize length_exp
        if self.length_exp is not None:
            serialized = SerializationHelper.serialize_item(self.length_exp, "Numerical")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LENGTH-EXP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize luminous_intensity_exp
        if self.luminous_intensity_exp is not None:
            serialized = SerializationHelper.serialize_item(self.luminous_intensity_exp, "Numerical")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LUMINOUS-INTENSITY-EXP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mass_exp
        if self.mass_exp is not None:
            serialized = SerializationHelper.serialize_item(self.mass_exp, "Numerical")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MASS-EXP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize molar_amount_exp
        if self.molar_amount_exp is not None:
            serialized = SerializationHelper.serialize_item(self.molar_amount_exp, "Numerical")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MOLAR-AMOUNT-EXP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize temperature_exp
        if self.temperature_exp is not None:
            serialized = SerializationHelper.serialize_item(self.temperature_exp, "Numerical")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TEMPERATURE-EXP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize time_exp
        if self.time_exp is not None:
            serialized = SerializationHelper.serialize_item(self.time_exp, "Numerical")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIME-EXP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PhysicalDimension":
        """Deserialize XML element to PhysicalDimension object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PhysicalDimension object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PhysicalDimension, cls).deserialize(element)

        # Parse current_exp
        child = SerializationHelper.find_child_element(element, "CURRENT-EXP")
        if child is not None:
            current_exp_value = child.text
            obj.current_exp = current_exp_value

        # Parse length_exp
        child = SerializationHelper.find_child_element(element, "LENGTH-EXP")
        if child is not None:
            length_exp_value = child.text
            obj.length_exp = length_exp_value

        # Parse luminous_intensity_exp
        child = SerializationHelper.find_child_element(element, "LUMINOUS-INTENSITY-EXP")
        if child is not None:
            luminous_intensity_exp_value = child.text
            obj.luminous_intensity_exp = luminous_intensity_exp_value

        # Parse mass_exp
        child = SerializationHelper.find_child_element(element, "MASS-EXP")
        if child is not None:
            mass_exp_value = child.text
            obj.mass_exp = mass_exp_value

        # Parse molar_amount_exp
        child = SerializationHelper.find_child_element(element, "MOLAR-AMOUNT-EXP")
        if child is not None:
            molar_amount_exp_value = child.text
            obj.molar_amount_exp = molar_amount_exp_value

        # Parse temperature_exp
        child = SerializationHelper.find_child_element(element, "TEMPERATURE-EXP")
        if child is not None:
            temperature_exp_value = child.text
            obj.temperature_exp = temperature_exp_value

        # Parse time_exp
        child = SerializationHelper.find_child_element(element, "TIME-EXP")
        if child is not None:
            time_exp_value = child.text
            obj.time_exp = time_exp_value

        return obj



class PhysicalDimensionBuilder:
    """Builder for PhysicalDimension with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: PhysicalDimension = PhysicalDimension()


    def with_short_name(self, value: Identifier) -> "PhysicalDimensionBuilder":
        """Set short_name attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.short_name = value
        return self

    def with_short_name_fragments(self, items: list[ShortNameFragment]) -> "PhysicalDimensionBuilder":
        """Set short_name_fragments list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = list(items) if items else []
        return self

    def with_long_name(self, value: Optional[MultilanguageLongName]) -> "PhysicalDimensionBuilder":
        """Set long_name attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.long_name = value
        return self

    def with_admin_data(self, value: Optional[AdminData]) -> "PhysicalDimensionBuilder":
        """Set admin_data attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.admin_data = value
        return self

    def with_annotations(self, items: list[Annotation]) -> "PhysicalDimensionBuilder":
        """Set annotations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.annotations = list(items) if items else []
        return self

    def with_desc(self, value: Optional[MultiLanguageOverviewParagraph]) -> "PhysicalDimensionBuilder":
        """Set desc attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.desc = value
        return self

    def with_category(self, value: Optional[CategoryString]) -> "PhysicalDimensionBuilder":
        """Set category attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.category = value
        return self

    def with_introduction(self, value: Optional[DocumentationBlock]) -> "PhysicalDimensionBuilder":
        """Set introduction attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.introduction = value
        return self

    def with_uuid(self, value: Optional[String]) -> "PhysicalDimensionBuilder":
        """Set uuid attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.uuid = value
        return self

    def with_current_exp(self, value: Optional[Numerical]) -> "PhysicalDimensionBuilder":
        """Set current_exp attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.current_exp = value
        return self

    def with_length_exp(self, value: Optional[Numerical]) -> "PhysicalDimensionBuilder":
        """Set length_exp attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.length_exp = value
        return self

    def with_luminous_intensity_exp(self, value: Optional[Numerical]) -> "PhysicalDimensionBuilder":
        """Set luminous_intensity_exp attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.luminous_intensity_exp = value
        return self

    def with_mass_exp(self, value: Optional[Numerical]) -> "PhysicalDimensionBuilder":
        """Set mass_exp attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.mass_exp = value
        return self

    def with_molar_amount_exp(self, value: Optional[Numerical]) -> "PhysicalDimensionBuilder":
        """Set molar_amount_exp attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.molar_amount_exp = value
        return self

    def with_temperature_exp(self, value: Optional[Numerical]) -> "PhysicalDimensionBuilder":
        """Set temperature_exp attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.temperature_exp = value
        return self

    def with_time_exp(self, value: Optional[Numerical]) -> "PhysicalDimensionBuilder":
        """Set time_exp attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.time_exp = value
        return self


    def add_short_name_fragment(self, item: ShortNameFragment) -> "PhysicalDimensionBuilder":
        """Add a single item to short_name_fragments list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments.append(item)
        return self

    def clear_short_name_fragments(self) -> "PhysicalDimensionBuilder":
        """Clear all items from short_name_fragments list.

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = []
        return self

    def add_annotation(self, item: Annotation) -> "PhysicalDimensionBuilder":
        """Add a single item to annotations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.annotations.append(item)
        return self

    def clear_annotations(self) -> "PhysicalDimensionBuilder":
        """Clear all items from annotations list.

        Returns:
            self for method chaining
        """
        self._obj.annotations = []
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


    def build(self) -> PhysicalDimension:
        """Build and return the PhysicalDimension instance with validation."""
        self._validate_instance()
        pass
        return self._obj