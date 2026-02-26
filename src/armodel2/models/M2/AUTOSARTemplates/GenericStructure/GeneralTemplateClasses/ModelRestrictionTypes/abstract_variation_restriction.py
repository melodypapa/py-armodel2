"""AbstractVariationRestriction AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 104)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 88)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_ModelRestrictionTypes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ModelRestrictionTypes import (
    FullBindingTimeEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class AbstractVariationRestriction(ARObject, ABC):
    """AUTOSAR AbstractVariationRestriction."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    valid_bindings: list[FullBindingTimeEnum]
    variation: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize AbstractVariationRestriction."""
        super().__init__()
        self.valid_bindings: list[FullBindingTimeEnum] = []
        self.variation: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize AbstractVariationRestriction to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AbstractVariationRestriction, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize valid_bindings (list to container "VALID-BINDINGS")
        if self.valid_bindings:
            wrapper = ET.Element("VALID-BINDINGS")
            for item in self.valid_bindings:
                serialized = SerializationHelper.serialize_item(item, "FullBindingTimeEnum")
                if serialized is not None:
                    child_elem = ET.Element("VALID-BINDING")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize variation
        if self.variation is not None:
            serialized = SerializationHelper.serialize_item(self.variation, "Boolean")
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
    def deserialize(cls, element: ET.Element) -> "AbstractVariationRestriction":
        """Deserialize XML element to AbstractVariationRestriction object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AbstractVariationRestriction object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AbstractVariationRestriction, cls).deserialize(element)

        # Parse valid_bindings (list from container "VALID-BINDINGS")
        obj.valid_bindings = []
        container = SerializationHelper.find_child_element(element, "VALID-BINDINGS")
        if container is not None:
            for child in container:
                # Extract enum value (FullBindingTimeEnum)
                child_value = FullBindingTimeEnum.deserialize(child)
                if child_value is not None:
                    obj.valid_bindings.append(child_value)

        # Parse variation
        child = SerializationHelper.find_child_element(element, "VARIATION")
        if child is not None:
            variation_value = child.text
            obj.variation = variation_value

        return obj



class AbstractVariationRestrictionBuilder(BuilderBase, ABC):
    """Builder for AbstractVariationRestriction with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: AbstractVariationRestriction = AbstractVariationRestriction()


    def with_valid_bindings(self, items: list[FullBindingTimeEnum]) -> "AbstractVariationRestrictionBuilder":
        """Set valid_bindings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.valid_bindings = list(items) if items else []
        return self

    def with_variation(self, value: Optional[Boolean]) -> "AbstractVariationRestrictionBuilder":
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


    def add_valid_binding(self, item: FullBindingTimeEnum) -> "AbstractVariationRestrictionBuilder":
        """Add a single item to valid_bindings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.valid_bindings.append(item)
        return self

    def clear_valid_bindings(self) -> "AbstractVariationRestrictionBuilder":
        """Clear all items from valid_bindings list.

        Returns:
            self for method chaining
        """
        self._obj.valid_bindings = []
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
    def build(self) -> AbstractVariationRestriction:
        """Build and return the AbstractVariationRestriction instance (abstract)."""
        raise NotImplementedError