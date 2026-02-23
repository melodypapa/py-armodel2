"""ClassContentConditional AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 103)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint_Data.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.abstract_condition import (
    AbstractCondition,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.attribute_tailoring import (
    AttributeTailoring,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.constraint_tailoring import (
    ConstraintTailoring,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.sdg_tailoring import (
    SdgTailoring,
)


class ClassContentConditional(Identifiable):
    """AUTOSAR ClassContentConditional."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    attributes: list[AttributeTailoring]
    condition: Optional[AbstractCondition]
    constraints: list[ConstraintTailoring]
    sdg_tailorings: list[SdgTailoring]
    def __init__(self) -> None:
        """Initialize ClassContentConditional."""
        super().__init__()
        self.attributes: list[AttributeTailoring] = []
        self.condition: Optional[AbstractCondition] = None
        self.constraints: list[ConstraintTailoring] = []
        self.sdg_tailorings: list[SdgTailoring] = []

    def serialize(self) -> ET.Element:
        """Serialize ClassContentConditional to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ClassContentConditional, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize attributes (list to container "ATTRIBUTES")
        if self.attributes:
            wrapper = ET.Element("ATTRIBUTES")
            for item in self.attributes:
                serialized = SerializationHelper.serialize_item(item, "AttributeTailoring")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize condition
        if self.condition is not None:
            serialized = SerializationHelper.serialize_item(self.condition, "AbstractCondition")
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

        # Serialize constraints (list to container "CONSTRAINTS")
        if self.constraints:
            wrapper = ET.Element("CONSTRAINTS")
            for item in self.constraints:
                serialized = SerializationHelper.serialize_item(item, "ConstraintTailoring")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize sdg_tailorings (list to container "SDG-TAILORINGS")
        if self.sdg_tailorings:
            wrapper = ET.Element("SDG-TAILORINGS")
            for item in self.sdg_tailorings:
                serialized = SerializationHelper.serialize_item(item, "SdgTailoring")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ClassContentConditional":
        """Deserialize XML element to ClassContentConditional object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ClassContentConditional object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ClassContentConditional, cls).deserialize(element)

        # Parse attributes (list from container "ATTRIBUTES")
        obj.attributes = []
        container = SerializationHelper.find_child_element(element, "ATTRIBUTES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.attributes.append(child_value)

        # Parse condition
        child = SerializationHelper.find_child_element(element, "CONDITION")
        if child is not None:
            condition_value = SerializationHelper.deserialize_by_tag(child, "AbstractCondition")
            obj.condition = condition_value

        # Parse constraints (list from container "CONSTRAINTS")
        obj.constraints = []
        container = SerializationHelper.find_child_element(element, "CONSTRAINTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.constraints.append(child_value)

        # Parse sdg_tailorings (list from container "SDG-TAILORINGS")
        obj.sdg_tailorings = []
        container = SerializationHelper.find_child_element(element, "SDG-TAILORINGS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.sdg_tailorings.append(child_value)

        return obj



class ClassContentConditionalBuilder(IdentifiableBuilder):
    """Builder for ClassContentConditional with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ClassContentConditional = ClassContentConditional()


    def with_attributes(self, items: list[AttributeTailoring]) -> "ClassContentConditionalBuilder":
        """Set attributes list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.attributes = list(items) if items else []
        return self

    def with_condition(self, value: Optional[AbstractCondition]) -> "ClassContentConditionalBuilder":
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

    def with_constraints(self, items: list[ConstraintTailoring]) -> "ClassContentConditionalBuilder":
        """Set constraints list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.constraints = list(items) if items else []
        return self

    def with_sdg_tailorings(self, items: list[SdgTailoring]) -> "ClassContentConditionalBuilder":
        """Set sdg_tailorings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.sdg_tailorings = list(items) if items else []
        return self


    def add_attribute(self, item: AttributeTailoring) -> "ClassContentConditionalBuilder":
        """Add a single item to attributes list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.attributes.append(item)
        return self

    def clear_attributes(self) -> "ClassContentConditionalBuilder":
        """Clear all items from attributes list.

        Returns:
            self for method chaining
        """
        self._obj.attributes = []
        return self

    def add_constraint(self, item: ConstraintTailoring) -> "ClassContentConditionalBuilder":
        """Add a single item to constraints list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.constraints.append(item)
        return self

    def clear_constraints(self) -> "ClassContentConditionalBuilder":
        """Clear all items from constraints list.

        Returns:
            self for method chaining
        """
        self._obj.constraints = []
        return self

    def add_sdg_tailoring(self, item: SdgTailoring) -> "ClassContentConditionalBuilder":
        """Add a single item to sdg_tailorings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.sdg_tailorings.append(item)
        return self

    def clear_sdg_tailorings(self) -> "ClassContentConditionalBuilder":
        """Clear all items from sdg_tailorings list.

        Returns:
            self for method chaining
        """
        self._obj.sdg_tailorings = []
        return self



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


    def build(self) -> ClassContentConditional:
        """Build and return the ClassContentConditional instance with validation."""
        self._validate_instance()
        pass
        return self._obj