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
        "IMPLEMENTATION-REFS": lambda obj, elem: [obj.implementation_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
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
            if tag == "IMPLEMENTATION-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.implementation_refs.append(ARRef.deserialize(item_elem))

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


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "implementation",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> BswCompositionTiming:
        """Build and return the BswCompositionTiming instance with validation."""
        self._validate_instance()
        return self._obj