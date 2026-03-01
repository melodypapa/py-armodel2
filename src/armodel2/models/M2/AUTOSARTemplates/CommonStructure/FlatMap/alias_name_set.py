"""AliasNameSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 174)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 968)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 160)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_FlatMap.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.FlatMap.alias_name_assignment import (
    AliasNameAssignment,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class AliasNameSet(ARElement):
    """AUTOSAR AliasNameSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "ALIAS-NAME-SET"


    alias_names: list[AliasNameAssignment]
    _DESERIALIZE_DISPATCH = {
        "ALIAS-NAMES": lambda obj, elem: obj.alias_names.append(SerializationHelper.deserialize_by_tag(elem, "AliasNameAssignment")),
    }


    def __init__(self) -> None:
        """Initialize AliasNameSet."""
        super().__init__()
        self.alias_names: list[AliasNameAssignment] = []

    def serialize(self) -> ET.Element:
        """Serialize AliasNameSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AliasNameSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize alias_names (list to container "ALIAS-NAMES")
        if self.alias_names:
            wrapper = ET.Element("ALIAS-NAMES")
            for item in self.alias_names:
                serialized = SerializationHelper.serialize_item(item, "AliasNameAssignment")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AliasNameSet":
        """Deserialize XML element to AliasNameSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AliasNameSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AliasNameSet, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ALIAS-NAMES":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.alias_names.append(SerializationHelper.deserialize_by_tag(item_elem, "AliasNameAssignment"))

        return obj



class AliasNameSetBuilder(ARElementBuilder):
    """Builder for AliasNameSet with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: AliasNameSet = AliasNameSet()


    def with_alias_names(self, items: list[AliasNameAssignment]) -> "AliasNameSetBuilder":
        """Set alias_names list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.alias_names = list(items) if items else []
        return self


    def add_alias_name(self, item: AliasNameAssignment) -> "AliasNameSetBuilder":
        """Add a single item to alias_names list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.alias_names.append(item)
        return self

    def clear_alias_names(self) -> "AliasNameSetBuilder":
        """Clear all items from alias_names list.

        Returns:
            self for method chaining
        """
        self._obj.alias_names = []
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


    def build(self) -> AliasNameSet:
        """Build and return the AliasNameSet instance with validation."""
        self._validate_instance()
        pass
        return self._obj