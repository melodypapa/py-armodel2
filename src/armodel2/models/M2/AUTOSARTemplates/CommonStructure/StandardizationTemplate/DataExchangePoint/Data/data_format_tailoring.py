"""DataFormatTailoring AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 180)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint_Data.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.class_tailoring import (
    ClassTailoring,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.constraint_tailoring import (
    ConstraintTailoring,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DataFormatTailoring(ARObject):
    """AUTOSAR DataFormatTailoring."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DATA-FORMAT-TAILORING"


    class_tailorings: list[ClassTailoring]
    constraints: list[ConstraintTailoring]
    _DESERIALIZE_DISPATCH = {
        "CLASS-TAILORINGS": ("_POLYMORPHIC_LIST", "class_tailorings", ["AbstractClassTailoring", "ConcreteClassTailoring"]),
        "CONSTRAINTS": lambda obj, elem: obj.constraints.append(SerializationHelper.deserialize_by_tag(elem, "ConstraintTailoring")),
    }


    def __init__(self) -> None:
        """Initialize DataFormatTailoring."""
        super().__init__()
        self.class_tailorings: list[ClassTailoring] = []
        self.constraints: list[ConstraintTailoring] = []

    def serialize(self) -> ET.Element:
        """Serialize DataFormatTailoring to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DataFormatTailoring, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize class_tailorings (list to container "CLASS-TAILORINGS")
        if self.class_tailorings:
            wrapper = ET.Element("CLASS-TAILORINGS")
            for item in self.class_tailorings:
                serialized = SerializationHelper.serialize_item(item, "ClassTailoring")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize constraints (list to container "CONSTRAINTS")
        if self.constraints:
            wrapper = ET.Element("CONSTRAINTS")
            for item in self.constraints:
                serialized = SerializationHelper.serialize_item(item, "ConstraintTailoring")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataFormatTailoring":
        """Deserialize XML element to DataFormatTailoring object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DataFormatTailoring object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DataFormatTailoring, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "CLASS-TAILORINGS":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "ABSTRACT-CLASS-TAILORING":
                        obj.class_tailorings.append(SerializationHelper.deserialize_by_tag(child[0], "AbstractClassTailoring"))
                    elif concrete_tag == "CONCRETE-CLASS-TAILORING":
                        obj.class_tailorings.append(SerializationHelper.deserialize_by_tag(child[0], "ConcreteClassTailoring"))
            elif tag == "CONSTRAINTS":
                # Iterate through wrapper children
                for item_elem in child:
                    item_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    obj.constraints.append(SerializationHelper.deserialize_by_tag(item_elem, "ConstraintTailoring"))

        return obj



class DataFormatTailoringBuilder(BuilderBase):
    """Builder for DataFormatTailoring with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DataFormatTailoring = DataFormatTailoring()


    def with_class_tailorings(self, items: list[ClassTailoring]) -> "DataFormatTailoringBuilder":
        """Set class_tailorings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.class_tailorings = list(items) if items else []
        return self

    def with_constraints(self, items: list[ConstraintTailoring]) -> "DataFormatTailoringBuilder":
        """Set constraints list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.constraints = list(items) if items else []
        return self


    def add_class_tailoring(self, item: ClassTailoring) -> "DataFormatTailoringBuilder":
        """Add a single item to class_tailorings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.class_tailorings.append(item)
        return self

    def clear_class_tailorings(self) -> "DataFormatTailoringBuilder":
        """Clear all items from class_tailorings list.

        Returns:
            self for method chaining
        """
        self._obj.class_tailorings = []
        return self

    def add_constraint(self, item: ConstraintTailoring) -> "DataFormatTailoringBuilder":
        """Add a single item to constraints list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.constraints.append(item)
        return self

    def clear_constraints(self) -> "DataFormatTailoringBuilder":
        """Clear all items from constraints list.

        Returns:
            self for method chaining
        """
        self._obj.constraints = []
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


    def build(self) -> DataFormatTailoring:
        """Build and return the DataFormatTailoring instance with validation."""
        self._validate_instance()
        pass
        return self._obj