"""EcucConditionSpecification AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 100)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_condition_formula import (
    EcucConditionFormula,
)
from armodel2.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_query import (
    EcucQuery,
)
from armodel2.models.M2.MSR.Documentation.BlockElements.Formula.ml_formula import (
    MlFormula,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class EcucConditionSpecification(ARObject):
    """AUTOSAR EcucConditionSpecification."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "ECUC-CONDITION-SPECIFICATION"


    condition: Optional[EcucConditionFormula]
    ecuc_queries: list[EcucQuery]
    informal_formula: Optional[MlFormula]
    _DESERIALIZE_DISPATCH = {
        "CONDITION": lambda obj, elem: setattr(obj, "condition", EcucConditionFormula.deserialize(elem)),
        "ECUC-QUERIES": lambda obj, elem: obj.ecuc_queries.append(EcucQuery.deserialize(elem)),
        "INFORMAL-FORMULA": lambda obj, elem: setattr(obj, "informal_formula", MlFormula.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize EcucConditionSpecification."""
        super().__init__()
        self.condition: Optional[EcucConditionFormula] = None
        self.ecuc_queries: list[EcucQuery] = []
        self.informal_formula: Optional[MlFormula] = None

    def serialize(self) -> ET.Element:
        """Serialize EcucConditionSpecification to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcucConditionSpecification, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize condition
        if self.condition is not None:
            serialized = SerializationHelper.serialize_item(self.condition, "EcucConditionFormula")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONDITION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ecuc_queries (list to container "ECUC-QUERIES")
        if self.ecuc_queries:
            wrapper = ET.Element("ECUC-QUERIES")
            for item in self.ecuc_queries:
                serialized = SerializationHelper.serialize_item(item, "EcucQuery")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize informal_formula
        if self.informal_formula is not None:
            serialized = SerializationHelper.serialize_item(self.informal_formula, "MlFormula")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INFORMAL-FORMULA")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucConditionSpecification":
        """Deserialize XML element to EcucConditionSpecification object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucConditionSpecification object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcucConditionSpecification, cls).deserialize(element)

        # Parse condition
        child = SerializationHelper.find_child_element(element, "CONDITION")
        if child is not None:
            condition_value = SerializationHelper.deserialize_by_tag(child, "EcucConditionFormula")
            obj.condition = condition_value

        # Parse ecuc_queries (list from container "ECUC-QUERIES")
        obj.ecuc_queries = []
        container = SerializationHelper.find_child_element(element, "ECUC-QUERIES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.ecuc_queries.append(child_value)

        # Parse informal_formula
        child = SerializationHelper.find_child_element(element, "INFORMAL-FORMULA")
        if child is not None:
            informal_formula_value = SerializationHelper.deserialize_by_tag(child, "MlFormula")
            obj.informal_formula = informal_formula_value

        return obj



class EcucConditionSpecificationBuilder(BuilderBase):
    """Builder for EcucConditionSpecification with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EcucConditionSpecification = EcucConditionSpecification()


    def with_condition(self, value: Optional[EcucConditionFormula]) -> "EcucConditionSpecificationBuilder":
        """Set condition attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.condition = value
        return self

    def with_ecuc_queries(self, items: list[EcucQuery]) -> "EcucConditionSpecificationBuilder":
        """Set ecuc_queries list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.ecuc_queries = list(items) if items else []
        return self

    def with_informal_formula(self, value: Optional[MlFormula]) -> "EcucConditionSpecificationBuilder":
        """Set informal_formula attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.informal_formula = value
        return self


    def add_ecuc_query(self, item: EcucQuery) -> "EcucConditionSpecificationBuilder":
        """Add a single item to ecuc_queries list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.ecuc_queries.append(item)
        return self

    def clear_ecuc_queries(self) -> "EcucConditionSpecificationBuilder":
        """Clear all items from ecuc_queries list.

        Returns:
            self for method chaining
        """
        self._obj.ecuc_queries = []
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


    def build(self) -> EcucConditionSpecification:
        """Build and return the EcucConditionSpecification instance with validation."""
        self._validate_instance()
        pass
        return self._obj