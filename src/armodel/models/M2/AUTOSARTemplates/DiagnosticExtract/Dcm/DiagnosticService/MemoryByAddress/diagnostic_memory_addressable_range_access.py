"""DiagnosticMemoryAddressableRangeAccess AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 140)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_MemoryByAddress.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.MemoryByAddress.diagnostic_memory_by_address import (
    DiagnosticMemoryByAddress,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from abc import ABC, abstractmethod


class DiagnosticMemoryAddressableRangeAccess(DiagnosticMemoryByAddress, ABC):
    """AUTOSAR DiagnosticMemoryAddressableRangeAccess."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    memory_ranges: list[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticMemoryAddressableRangeAccess."""
        super().__init__()
        self.memory_ranges: list[Any] = []
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

        # Parse memory_ranges (list from container "MEMORY-RANGES")
        obj.memory_ranges = []
        container = ARObject._find_child_element(element, "MEMORY-RANGES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.memory_ranges.append(child_value)

        return obj



class DiagnosticMemoryAddressableRangeAccessBuilder:
    """Builder for DiagnosticMemoryAddressableRangeAccess."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticMemoryAddressableRangeAccess = DiagnosticMemoryAddressableRangeAccess()

    def build(self) -> DiagnosticMemoryAddressableRangeAccess:
        """Build and return DiagnosticMemoryAddressableRangeAccess object.

        Returns:
            DiagnosticMemoryAddressableRangeAccess instance
        """
        # TODO: Add validation
        return self._obj
