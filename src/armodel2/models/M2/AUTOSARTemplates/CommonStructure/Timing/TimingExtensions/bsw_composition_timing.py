"""BswCompositionTiming AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 28)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingExtensions.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions.timing_extension import (
    TimingExtension,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions.timing_extension import TimingExtensionBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswImplementation.bsw_implementation import (
    BswImplementation,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class BswCompositionTiming(TimingExtension):
    """AUTOSAR BswCompositionTiming."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "BSW-COMPOSITION-TIMING"


    implementation_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "IMPLEMENTATIONS": lambda obj, elem: obj.implementation_refs.append(ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize BswCompositionTiming."""
        super().__init__()
        self.implementation_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize BswCompositionTiming to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BswCompositionTiming, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize implementation_refs (list to container "IMPLEMENTATION-REFS")
        if self.implementation_refs:
            wrapper = ET.Element("IMPLEMENTATION-REFS")
            for item in self.implementation_refs:
                serialized = SerializationHelper.serialize_item(item, "BswImplementation")
                if serialized is not None:
                    child_elem = ET.Element("IMPLEMENTATION-REF")
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
    def deserialize(cls, element: ET.Element) -> "BswCompositionTiming":
        """Deserialize XML element to BswCompositionTiming object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswCompositionTiming object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BswCompositionTiming, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "IMPLEMENTATIONS":
                # Iterate through wrapper children
                for item_elem in child:
                    item_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    obj.implementation_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "BswImplementation"))

        return obj



class BswCompositionTimingBuilder(TimingExtensionBuilder):
    """Builder for BswCompositionTiming with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: BswCompositionTiming = BswCompositionTiming()


    def with_implementations(self, items: list[BswImplementation]) -> "BswCompositionTimingBuilder":
        """Set implementations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.implementations = list(items) if items else []
        return self


    def add_implementation(self, item: BswImplementation) -> "BswCompositionTimingBuilder":
        """Add a single item to implementations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.implementations.append(item)
        return self

    def clear_implementations(self) -> "BswCompositionTimingBuilder":
        """Clear all items from implementations list.

        Returns:
            self for method chaining
        """
        self._obj.implementations = []
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


    def build(self) -> BswCompositionTiming:
        """Build and return the BswCompositionTiming instance with validation."""
        self._validate_instance()
        pass
        return self._obj