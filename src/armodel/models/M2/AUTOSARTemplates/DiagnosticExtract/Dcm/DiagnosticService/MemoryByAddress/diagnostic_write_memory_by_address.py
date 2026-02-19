"""DiagnosticWriteMemoryByAddress AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 140)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_MemoryByAddress.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.MemoryByAddress.diagnostic_memory_addressable_range_access import (
    DiagnosticMemoryAddressableRangeAccess,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class DiagnosticWriteMemoryByAddress(DiagnosticMemoryAddressableRangeAccess):
    """AUTOSAR DiagnosticWriteMemoryByAddress."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    write_class: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticWriteMemoryByAddress."""
        super().__init__()
        self.write_class: Optional[Any] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticWriteMemoryByAddress":
        """Deserialize XML element to DiagnosticWriteMemoryByAddress object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticWriteMemoryByAddress object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticWriteMemoryByAddress, cls).deserialize(element)

        # Parse write_class
        child = ARObject._find_child_element(element, "WRITE-CLASS")
        if child is not None:
            write_class_value = child.text
            obj.write_class = write_class_value

        return obj



class DiagnosticWriteMemoryByAddressBuilder:
    """Builder for DiagnosticWriteMemoryByAddress."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticWriteMemoryByAddress = DiagnosticWriteMemoryByAddress()

    def build(self) -> DiagnosticWriteMemoryByAddress:
        """Build and return DiagnosticWriteMemoryByAddress object.

        Returns:
            DiagnosticWriteMemoryByAddress instance
        """
        # TODO: Add validation
        return self._obj
