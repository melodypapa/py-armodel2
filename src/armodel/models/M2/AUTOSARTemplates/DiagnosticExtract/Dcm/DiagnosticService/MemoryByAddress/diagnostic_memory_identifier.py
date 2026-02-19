"""DiagnosticMemoryIdentifier AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 140)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_MemoryByAddress.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    String,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.diagnostic_access_permission import (
    DiagnosticAccessPermission,
)


class DiagnosticMemoryIdentifier(DiagnosticCommonElement):
    """AUTOSAR DiagnosticMemoryIdentifier."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    access: Optional[DiagnosticAccessPermission]
    id: Optional[PositiveInteger]
    memory_high: Optional[String]
    memory_low: Optional[String]
    def __init__(self) -> None:
        """Initialize DiagnosticMemoryIdentifier."""
        super().__init__()
        self.access: Optional[DiagnosticAccessPermission] = None
        self.id: Optional[PositiveInteger] = None
        self.memory_high: Optional[String] = None
        self.memory_low: Optional[String] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticMemoryIdentifier":
        """Deserialize XML element to DiagnosticMemoryIdentifier object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticMemoryIdentifier object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse access
        child = ARObject._find_child_element(element, "ACCESS")
        if child is not None:
            access_value = ARObject._deserialize_by_tag(child, "DiagnosticAccessPermission")
            obj.access = access_value

        # Parse id
        child = ARObject._find_child_element(element, "ID")
        if child is not None:
            id_value = child.text
            obj.id = id_value

        # Parse memory_high
        child = ARObject._find_child_element(element, "MEMORY-HIGH")
        if child is not None:
            memory_high_value = child.text
            obj.memory_high = memory_high_value

        # Parse memory_low
        child = ARObject._find_child_element(element, "MEMORY-LOW")
        if child is not None:
            memory_low_value = child.text
            obj.memory_low = memory_low_value

        return obj



class DiagnosticMemoryIdentifierBuilder:
    """Builder for DiagnosticMemoryIdentifier."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticMemoryIdentifier = DiagnosticMemoryIdentifier()

    def build(self) -> DiagnosticMemoryIdentifier:
        """Build and return DiagnosticMemoryIdentifier object.

        Returns:
            DiagnosticMemoryIdentifier instance
        """
        # TODO: Add validation
        return self._obj
