"""TDEventOccurrenceExpression AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 84)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.autosar_operation_argument_instance import (
    AutosarOperationArgumentInstance,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition.timing_mode_instance import (
    TimingModeInstance,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class TDEventOccurrenceExpression(ARObject):
    """AUTOSAR TDEventOccurrenceExpression."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "T-D-EVENT-OCCURRENCE-EXPRESSION"


    arguments: list[AutosarOperationArgumentInstance]
    formula: Optional[Any]
    modes: list[TimingModeInstance]
    variables: list[Any]
    _DESERIALIZE_DISPATCH = {
        "ARGUMENTS": lambda obj, elem: obj.arguments.append(SerializationHelper.deserialize_by_tag(elem, "AutosarOperationArgumentInstance")),
        "FORMULA": lambda obj, elem: setattr(obj, "formula", SerializationHelper.deserialize_by_tag(elem, "any (TDEventOccurrence)")),
        "MODES": lambda obj, elem: obj.modes.append(SerializationHelper.deserialize_by_tag(elem, "TimingModeInstance")),
        "VARIABLES": lambda obj, elem: obj.variables.append(SerializationHelper.deserialize_by_tag(elem, "any (AutosarVariable)")),
    }


    def __init__(self) -> None:
        """Initialize TDEventOccurrenceExpression."""
        super().__init__()
        self.arguments: list[AutosarOperationArgumentInstance] = []
        self.formula: Optional[Any] = None
        self.modes: list[TimingModeInstance] = []
        self.variables: list[Any] = []

    def serialize(self) -> ET.Element:
        """Serialize TDEventOccurrenceExpression to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TDEventOccurrenceExpression, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize arguments (list to container "ARGUMENTS")
        if self.arguments:
            wrapper = ET.Element("ARGUMENTS")
            for item in self.arguments:
                serialized = SerializationHelper.serialize_item(item, "AutosarOperationArgumentInstance")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize formula
        if self.formula is not None:
            serialized = SerializationHelper.serialize_item(self.formula, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FORMULA")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize modes (list to container "MODES")
        if self.modes:
            wrapper = ET.Element("MODES")
            for item in self.modes:
                serialized = SerializationHelper.serialize_item(item, "TimingModeInstance")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize variables (list to container "VARIABLES")
        if self.variables:
            wrapper = ET.Element("VARIABLES")
            for item in self.variables:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventOccurrenceExpression":
        """Deserialize XML element to TDEventOccurrenceExpression object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TDEventOccurrenceExpression object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TDEventOccurrenceExpression, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ARGUMENTS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.arguments.append(SerializationHelper.deserialize_by_tag(item_elem, "AutosarOperationArgumentInstance"))
            elif tag == "FORMULA":
                setattr(obj, "formula", SerializationHelper.deserialize_by_tag(child, "any (TDEventOccurrence)"))
            elif tag == "MODES":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.modes.append(SerializationHelper.deserialize_by_tag(item_elem, "TimingModeInstance"))
            elif tag == "VARIABLES":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.variables.append(SerializationHelper.deserialize_by_tag(item_elem, "any (AutosarVariable)"))

        return obj



class TDEventOccurrenceExpressionBuilder(BuilderBase):
    """Builder for TDEventOccurrenceExpression with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TDEventOccurrenceExpression = TDEventOccurrenceExpression()


    def with_arguments(self, items: list[AutosarOperationArgumentInstance]) -> "TDEventOccurrenceExpressionBuilder":
        """Set arguments list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.arguments = list(items) if items else []
        return self

    def with_formula(self, value: Optional[any (TDEventOccurrence)]) -> "TDEventOccurrenceExpressionBuilder":
        """Set formula attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.formula = value
        return self

    def with_modes(self, items: list[TimingModeInstance]) -> "TDEventOccurrenceExpressionBuilder":
        """Set modes list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.modes = list(items) if items else []
        return self

    def with_variables(self, items: list[any (AutosarVariable)]) -> "TDEventOccurrenceExpressionBuilder":
        """Set variables list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.variables = list(items) if items else []
        return self


    def add_argument(self, item: AutosarOperationArgumentInstance) -> "TDEventOccurrenceExpressionBuilder":
        """Add a single item to arguments list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.arguments.append(item)
        return self

    def clear_arguments(self) -> "TDEventOccurrenceExpressionBuilder":
        """Clear all items from arguments list.

        Returns:
            self for method chaining
        """
        self._obj.arguments = []
        return self

    def add_mode(self, item: TimingModeInstance) -> "TDEventOccurrenceExpressionBuilder":
        """Add a single item to modes list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.modes.append(item)
        return self

    def clear_modes(self) -> "TDEventOccurrenceExpressionBuilder":
        """Clear all items from modes list.

        Returns:
            self for method chaining
        """
        self._obj.modes = []
        return self

    def add_variable(self, item: any (AutosarVariable)) -> "TDEventOccurrenceExpressionBuilder":
        """Add a single item to variables list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.variables.append(item)
        return self

    def clear_variables(self) -> "TDEventOccurrenceExpressionBuilder":
        """Clear all items from variables list.

        Returns:
            self for method chaining
        """
        self._obj.variables = []
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


    def build(self) -> TDEventOccurrenceExpression:
        """Build and return the TDEventOccurrenceExpression instance with validation."""
        self._validate_instance()
        pass
        return self._obj