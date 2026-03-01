"""EcucDefinitionCollection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 25)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 185)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_module_def import (
    EcucModuleDef,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class EcucDefinitionCollection(ARElement):
    """AUTOSAR EcucDefinitionCollection."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "ECUC-DEFINITION-COLLECTION"


    module_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "MODULE-REFS": lambda obj, elem: [obj.module_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
    }


    def __init__(self) -> None:
        """Initialize EcucDefinitionCollection."""
        super().__init__()
        self.module_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize EcucDefinitionCollection to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcucDefinitionCollection, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize module_refs (list to container "MODULE-REFS")
        if self.module_refs:
            wrapper = ET.Element("MODULE-REFS")
            for item in self.module_refs:
                serialized = SerializationHelper.serialize_item(item, "EcucModuleDef")
                if serialized is not None:
                    child_elem = ET.Element("MODULE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucDefinitionCollection":
        """Deserialize XML element to EcucDefinitionCollection object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucDefinitionCollection object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcucDefinitionCollection, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "MODULE-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.module_refs.append(ARRef.deserialize(item_elem))

        return obj



class EcucDefinitionCollectionBuilder(ARElementBuilder):
    """Builder for EcucDefinitionCollection with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EcucDefinitionCollection = EcucDefinitionCollection()


    def with_modules(self, items: list[EcucModuleDef]) -> "EcucDefinitionCollectionBuilder":
        """Set modules list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.modules = list(items) if items else []
        return self


    def add_module(self, item: EcucModuleDef) -> "EcucDefinitionCollectionBuilder":
        """Add a single item to modules list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.modules.append(item)
        return self

    def clear_modules(self) -> "EcucDefinitionCollectionBuilder":
        """Clear all items from modules list.

        Returns:
            self for method chaining
        """
        self._obj.modules = []
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


    def build(self) -> EcucDefinitionCollection:
        """Build and return the EcucDefinitionCollection instance with validation."""
        self._validate_instance()
        pass
        return self._obj