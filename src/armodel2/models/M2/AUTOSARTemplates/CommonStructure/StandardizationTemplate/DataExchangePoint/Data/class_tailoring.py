"""ClassTailoring AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 102)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint_Data.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.class_content_conditional import (
    ClassContentConditional,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.variation_restriction_with_severity import (
    VariationRestrictionWithSeverity,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ClassTailoring(ARObject, ABC):
    """AUTOSAR ClassTailoring."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    class_contents: list[ClassContentConditional]
    multiplicity: Optional[Any]
    variation: Optional[VariationRestrictionWithSeverity]
    _DESERIALIZE_DISPATCH = {
        "CLASS-CONTENTS": lambda obj, elem: obj.class_contents.append(SerializationHelper.deserialize_by_tag(elem, "ClassContentConditional")),
        "MULTIPLICITY": lambda obj, elem: setattr(obj, "multiplicity", SerializationHelper.deserialize_by_tag(elem, "any (MultiplicityRestriction)")),
        "VARIATION": lambda obj, elem: setattr(obj, "variation", SerializationHelper.deserialize_by_tag(elem, "VariationRestrictionWithSeverity")),
    }


    def __init__(self) -> None:
        """Initialize ClassTailoring."""
        super().__init__()
        self.class_contents: list[ClassContentConditional] = []
        self.multiplicity: Optional[Any] = None
        self.variation: Optional[VariationRestrictionWithSeverity] = None

    def serialize(self) -> ET.Element:
        """Serialize ClassTailoring to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ClassTailoring, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize class_contents (list to container "CLASS-CONTENTS")
        if self.class_contents:
            wrapper = ET.Element("CLASS-CONTENTS")
            for item in self.class_contents:
                serialized = SerializationHelper.serialize_item(item, "ClassContentConditional")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize multiplicity
        if self.multiplicity is not None:
            serialized = SerializationHelper.serialize_item(self.multiplicity, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MULTIPLICITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize variation
        if self.variation is not None:
            serialized = SerializationHelper.serialize_item(self.variation, "VariationRestrictionWithSeverity")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VARIATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ClassTailoring":
        """Deserialize XML element to ClassTailoring object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ClassTailoring object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ClassTailoring, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CLASS-CONTENTS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.class_contents.append(SerializationHelper.deserialize_by_tag(item_elem, "ClassContentConditional"))
            elif tag == "MULTIPLICITY":
                setattr(obj, "multiplicity", SerializationHelper.deserialize_by_tag(child, "any (MultiplicityRestriction)"))
            elif tag == "VARIATION":
                setattr(obj, "variation", SerializationHelper.deserialize_by_tag(child, "VariationRestrictionWithSeverity"))

        return obj



class ClassTailoringBuilder(BuilderBase, ABC):
    """Builder for ClassTailoring with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ClassTailoring = ClassTailoring()


    def with_class_contents(self, items: list[ClassContentConditional]) -> "ClassTailoringBuilder":
        """Set class_contents list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.class_contents = list(items) if items else []
        return self

    def with_multiplicity(self, value: Optional[any (MultiplicityRestriction)]) -> "ClassTailoringBuilder":
        """Set multiplicity attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.multiplicity = value
        return self

    def with_variation(self, value: Optional[VariationRestrictionWithSeverity]) -> "ClassTailoringBuilder":
        """Set variation attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.variation = value
        return self


    def add_class_content(self, item: ClassContentConditional) -> "ClassTailoringBuilder":
        """Add a single item to class_contents list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.class_contents.append(item)
        return self

    def clear_class_contents(self) -> "ClassTailoringBuilder":
        """Clear all items from class_contents list.

        Returns:
            self for method chaining
        """
        self._obj.class_contents = []
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
    def build(self) -> ClassTailoring:
        """Build and return the ClassTailoring instance (abstract)."""
        raise NotImplementedError