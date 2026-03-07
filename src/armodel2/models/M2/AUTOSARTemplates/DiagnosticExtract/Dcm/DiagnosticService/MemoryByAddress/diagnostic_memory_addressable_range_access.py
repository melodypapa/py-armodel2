"""DiagnosticMemoryAddressableRangeAccess AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 140)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_MemoryByAddress.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.MemoryByAddress.diagnostic_memory_by_address import (
    DiagnosticMemoryByAddress,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.MemoryByAddress.diagnostic_memory_by_address import DiagnosticMemoryByAddressBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticMemoryAddressableRangeAccess(DiagnosticMemoryByAddress, ABC):
    """AUTOSAR DiagnosticMemoryAddressableRangeAccess."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    memory_range_refs: list[Any]
    _DESERIALIZE_DISPATCH = {
        "MEMORY-RANGE-REFS": lambda obj, elem: [obj.memory_range_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
    }


    def __init__(self) -> None:
        """Initialize DiagnosticMemoryAddressableRangeAccess."""
        super().__init__()
        self.memory_range_refs: list[Any] = []

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticMemoryAddressableRangeAccess to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticMemoryAddressableRangeAccess, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize memory_range_refs (list to container "MEMORY-RANGE-REFS")
        if self.memory_range_refs:
            wrapper = ET.Element("MEMORY-RANGE-REFS")
            for item in self.memory_range_refs:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    child_elem = ET.Element("MEMORY-RANGE-REF")
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
    def deserialize(cls, element: ET.Element) -> "DiagnosticMemoryAddressableRangeAccess":
        """Deserialize XML element to DiagnosticMemoryAddressableRangeAccess object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticMemoryAddressableRangeAccess object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticMemoryAddressableRangeAccess, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "MEMORY-RANGE-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.memory_range_refs.append(ARRef.deserialize(item_elem))

        return obj



class DiagnosticMemoryAddressableRangeAccessBuilder(DiagnosticMemoryByAddressBuilder):
    """Builder for DiagnosticMemoryAddressableRangeAccess with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticMemoryAddressableRangeAccess = DiagnosticMemoryAddressableRangeAccess()


    def with_memory_ranges(self, items: list[Any]) -> "DiagnosticMemoryAddressableRangeAccessBuilder":
        """Set memory_ranges list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.memory_ranges = list(items) if items else []
        return self


    def add_memory_range(self, item: Any) -> "DiagnosticMemoryAddressableRangeAccessBuilder":
        """Add a single item to memory_ranges list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.memory_ranges.append(item)
        return self

    def clear_memory_ranges(self) -> "DiagnosticMemoryAddressableRangeAccessBuilder":
        """Clear all items from memory_ranges list.

        Returns:
            self for method chaining
        """
        self._obj.memory_ranges = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "memoryRange",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    @abstractmethod
    def build(self) -> DiagnosticMemoryAddressableRangeAccess:
        """Build and return the DiagnosticMemoryAddressableRangeAccess instance (abstract)."""
        raise NotImplementedError