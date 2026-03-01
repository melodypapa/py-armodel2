"""ClientIdDefinitionSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 44)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.client_id_definition import (
    ClientIdDefinition,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ClientIdDefinitionSet(ARElement):
    """AUTOSAR ClientIdDefinitionSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "CLIENT-ID-DEFINITION-SET"


    client_ids: list[ClientIdDefinition]
    _DESERIALIZE_DISPATCH = {
        "CLIENT-IDS": lambda obj, elem: obj.client_ids.append(SerializationHelper.deserialize_by_tag(elem, "ClientIdDefinition")),
    }


    def __init__(self) -> None:
        """Initialize ClientIdDefinitionSet."""
        super().__init__()
        self.client_ids: list[ClientIdDefinition] = []

    def serialize(self) -> ET.Element:
        """Serialize ClientIdDefinitionSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ClientIdDefinitionSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize client_ids (list to container "CLIENT-IDS")
        if self.client_ids:
            wrapper = ET.Element("CLIENT-IDS")
            for item in self.client_ids:
                serialized = SerializationHelper.serialize_item(item, "ClientIdDefinition")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ClientIdDefinitionSet":
        """Deserialize XML element to ClientIdDefinitionSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ClientIdDefinitionSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ClientIdDefinitionSet, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CLIENT-IDS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.client_ids.append(SerializationHelper.deserialize_by_tag(item_elem, "ClientIdDefinition"))

        return obj



class ClientIdDefinitionSetBuilder(ARElementBuilder):
    """Builder for ClientIdDefinitionSet with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ClientIdDefinitionSet = ClientIdDefinitionSet()


    def with_client_ids(self, items: list[ClientIdDefinition]) -> "ClientIdDefinitionSetBuilder":
        """Set client_ids list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.client_ids = list(items) if items else []
        return self


    def add_client_id(self, item: ClientIdDefinition) -> "ClientIdDefinitionSetBuilder":
        """Add a single item to client_ids list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.client_ids.append(item)
        return self

    def clear_client_ids(self) -> "ClientIdDefinitionSetBuilder":
        """Clear all items from client_ids list.

        Returns:
            self for method chaining
        """
        self._obj.client_ids = []
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


    def build(self) -> ClientIdDefinitionSet:
        """Build and return the ClientIdDefinitionSet instance with validation."""
        self._validate_instance()
        pass
        return self._obj