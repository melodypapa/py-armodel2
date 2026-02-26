"""PrimitiveAttributeTailoring AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 111)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint_Data.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.attribute_tailoring import (
    AttributeTailoring,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.attribute_tailoring import AttributeTailoringBuilder
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data import (
    DefaultValueApplicationStrategyEnum,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.value_restriction_with_severity import (
    ValueRestrictionWithSeverity,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class PrimitiveAttributeTailoring(AttributeTailoring):
    """AUTOSAR PrimitiveAttributeTailoring."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    default_value: Optional[DefaultValueApplicationStrategyEnum]
    sub_attributes: list[Any]
    value_restriction_with_severity: Optional[ValueRestrictionWithSeverity]
    def __init__(self) -> None:
        """Initialize PrimitiveAttributeTailoring."""
        super().__init__()
        self.default_value: Optional[DefaultValueApplicationStrategyEnum] = None
        self.sub_attributes: list[Any] = []
        self.value_restriction_with_severity: Optional[ValueRestrictionWithSeverity] = None

    def serialize(self) -> ET.Element:
        """Serialize PrimitiveAttributeTailoring to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(PrimitiveAttributeTailoring, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize default_value
        if self.default_value is not None:
            serialized = SerializationHelper.serialize_item(self.default_value, "DefaultValueApplicationStrategyEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DEFAULT-VALUE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sub_attributes (list to container "SUB-ATTRIBUTES")
        if self.sub_attributes:
            wrapper = ET.Element("SUB-ATTRIBUTES")
            for item in self.sub_attributes:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize value_restriction_with_severity
        if self.value_restriction_with_severity is not None:
            serialized = SerializationHelper.serialize_item(self.value_restriction_with_severity, "ValueRestrictionWithSeverity")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VALUE-RESTRICTION-WITH-SEVERITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PrimitiveAttributeTailoring":
        """Deserialize XML element to PrimitiveAttributeTailoring object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PrimitiveAttributeTailoring object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PrimitiveAttributeTailoring, cls).deserialize(element)

        # Parse default_value
        child = SerializationHelper.find_child_element(element, "DEFAULT-VALUE")
        if child is not None:
            default_value_value = DefaultValueApplicationStrategyEnum.deserialize(child)
            obj.default_value = default_value_value

        # Parse sub_attributes (list from container "SUB-ATTRIBUTES")
        obj.sub_attributes = []
        container = SerializationHelper.find_child_element(element, "SUB-ATTRIBUTES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.sub_attributes.append(child_value)

        # Parse value_restriction_with_severity
        child = SerializationHelper.find_child_element(element, "VALUE-RESTRICTION-WITH-SEVERITY")
        if child is not None:
            value_restriction_with_severity_value = SerializationHelper.deserialize_by_tag(child, "ValueRestrictionWithSeverity")
            obj.value_restriction_with_severity = value_restriction_with_severity_value

        return obj



class PrimitiveAttributeTailoringBuilder(AttributeTailoringBuilder):
    """Builder for PrimitiveAttributeTailoring with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: PrimitiveAttributeTailoring = PrimitiveAttributeTailoring()


    def with_default_value(self, value: Optional[DefaultValueApplicationStrategyEnum]) -> "PrimitiveAttributeTailoringBuilder":
        """Set default_value attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.default_value = value
        return self

    def with_sub_attributes(self, items: list[any (PrimitiveAttribute)]) -> "PrimitiveAttributeTailoringBuilder":
        """Set sub_attributes list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.sub_attributes = list(items) if items else []
        return self

    def with_value_restriction_with_severity(self, value: Optional[ValueRestrictionWithSeverity]) -> "PrimitiveAttributeTailoringBuilder":
        """Set value_restriction_with_severity attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.value_restriction_with_severity = value
        return self


    def add_sub_attribute(self, item: any (PrimitiveAttribute)) -> "PrimitiveAttributeTailoringBuilder":
        """Add a single item to sub_attributes list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.sub_attributes.append(item)
        return self

    def clear_sub_attributes(self) -> "PrimitiveAttributeTailoringBuilder":
        """Clear all items from sub_attributes list.

        Returns:
            self for method chaining
        """
        self._obj.sub_attributes = []
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


    def build(self) -> PrimitiveAttributeTailoring:
        """Build and return the PrimitiveAttributeTailoring instance with validation."""
        self._validate_instance()
        pass
        return self._obj