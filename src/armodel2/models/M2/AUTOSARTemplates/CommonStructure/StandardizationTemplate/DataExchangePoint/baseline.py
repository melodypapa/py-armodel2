"""Baseline AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 79)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.DocumentationOnM1.documentation import (
    Documentation,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_def import (
    SdgDef,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class Baseline(ARObject):
    """AUTOSAR Baseline."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "BASELINE"


    custom_sdg_def_refs: list[ARRef]
    custom_refs: list[ARRef]
    standards: list[String]
    _DESERIALIZE_DISPATCH = {
        "CUSTOM-SDG-DEFS": lambda obj, elem: obj.custom_sdg_def_refs.append(ARRef.deserialize(elem)),
        "CUSTOMS": lambda obj, elem: obj.custom_refs.append(ARRef.deserialize(elem)),
        "STANDARDS": lambda obj, elem: obj.standards.append(SerializationHelper.deserialize_by_tag(elem, "String")),
    }


    def __init__(self) -> None:
        """Initialize Baseline."""
        super().__init__()
        self.custom_sdg_def_refs: list[ARRef] = []
        self.custom_refs: list[ARRef] = []
        self.standards: list[String] = []

    def serialize(self) -> ET.Element:
        """Serialize Baseline to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Baseline, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize custom_sdg_def_refs (list to container "CUSTOM-SDG-DEF-REFS")
        if self.custom_sdg_def_refs:
            wrapper = ET.Element("CUSTOM-SDG-DEF-REFS")
            for item in self.custom_sdg_def_refs:
                serialized = SerializationHelper.serialize_item(item, "SdgDef")
                if serialized is not None:
                    child_elem = ET.Element("CUSTOM-SDG-DEF-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize custom_refs (list to container "CUSTOM-REFS")
        if self.custom_refs:
            wrapper = ET.Element("CUSTOM-REFS")
            for item in self.custom_refs:
                serialized = SerializationHelper.serialize_item(item, "Documentation")
                if serialized is not None:
                    child_elem = ET.Element("CUSTOM-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize standards (list to container "STANDARDS")
        if self.standards:
            wrapper = ET.Element("STANDARDS")
            for item in self.standards:
                serialized = SerializationHelper.serialize_item(item, "String")
                if serialized is not None:
                    child_elem = ET.Element("STANDARD")
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
    def deserialize(cls, element: ET.Element) -> "Baseline":
        """Deserialize XML element to Baseline object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Baseline object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Baseline, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "CUSTOM-SDG-DEFS":
                # Iterate through wrapper children
                for item_elem in child:
                    item_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    obj.custom_sdg_def_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "SdgDef"))
            elif tag == "CUSTOMS":
                # Iterate through wrapper children
                for item_elem in child:
                    item_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    obj.custom_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "Documentation"))
            elif tag == "STANDARDS":
                # Iterate through wrapper children
                for item_elem in child:
                    item_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    obj.standards.append(SerializationHelper.deserialize_by_tag(item_elem, "String"))

        return obj



class BaselineBuilder(BuilderBase):
    """Builder for Baseline with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: Baseline = Baseline()


    def with_custom_sdg_defs(self, items: list[SdgDef]) -> "BaselineBuilder":
        """Set custom_sdg_defs list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.custom_sdg_defs = list(items) if items else []
        return self

    def with_customs(self, items: list[Documentation]) -> "BaselineBuilder":
        """Set customs list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.customs = list(items) if items else []
        return self

    def with_standards(self, items: list[String]) -> "BaselineBuilder":
        """Set standards list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.standards = list(items) if items else []
        return self


    def add_custom_sdg_def(self, item: SdgDef) -> "BaselineBuilder":
        """Add a single item to custom_sdg_defs list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.custom_sdg_defs.append(item)
        return self

    def clear_custom_sdg_defs(self) -> "BaselineBuilder":
        """Clear all items from custom_sdg_defs list.

        Returns:
            self for method chaining
        """
        self._obj.custom_sdg_defs = []
        return self

    def add_custom(self, item: Documentation) -> "BaselineBuilder":
        """Add a single item to customs list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.customs.append(item)
        return self

    def clear_customs(self) -> "BaselineBuilder":
        """Clear all items from customs list.

        Returns:
            self for method chaining
        """
        self._obj.customs = []
        return self

    def add_standard(self, item: String) -> "BaselineBuilder":
        """Add a single item to standards list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.standards.append(item)
        return self

    def clear_standards(self) -> "BaselineBuilder":
        """Clear all items from standards list.

        Returns:
            self for method chaining
        """
        self._obj.standards = []
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


    def build(self) -> Baseline:
        """Build and return the Baseline instance with validation."""
        self._validate_instance()
        pass
        return self._obj