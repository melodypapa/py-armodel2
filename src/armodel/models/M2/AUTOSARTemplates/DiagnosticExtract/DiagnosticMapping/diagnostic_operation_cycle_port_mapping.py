"""DiagnosticOperationCyclePortMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 250)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_sw_mapping import (
    DiagnosticSwMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class DiagnosticOperationCyclePortMapping(DiagnosticSwMapping):
    """AUTOSAR DiagnosticOperationCyclePortMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    operation_cycle: Optional[Any]
    swc_flat_service: Optional[Any]
    swc_service: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticOperationCyclePortMapping."""
        super().__init__()
        self.operation_cycle: Optional[Any] = None
        self.swc_flat_service: Optional[Any] = None
        self.swc_service: Optional[Any] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticOperationCyclePortMapping":
        """Deserialize XML element to DiagnosticOperationCyclePortMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticOperationCyclePortMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticOperationCyclePortMapping, cls).deserialize(element)

        # Parse operation_cycle
        child = ARObject._find_child_element(element, "OPERATION-CYCLE")
        if child is not None:
            operation_cycle_value = child.text
            obj.operation_cycle = operation_cycle_value

        # Parse swc_flat_service
        child = ARObject._find_child_element(element, "SWC-FLAT-SERVICE")
        if child is not None:
            swc_flat_service_value = child.text
            obj.swc_flat_service = swc_flat_service_value

        # Parse swc_service
        child = ARObject._find_child_element(element, "SWC-SERVICE")
        if child is not None:
            swc_service_value = child.text
            obj.swc_service = swc_service_value

        return obj



class DiagnosticOperationCyclePortMappingBuilder:
    """Builder for DiagnosticOperationCyclePortMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticOperationCyclePortMapping = DiagnosticOperationCyclePortMapping()

    def build(self) -> DiagnosticOperationCyclePortMapping:
        """Build and return DiagnosticOperationCyclePortMapping object.

        Returns:
            DiagnosticOperationCyclePortMapping instance
        """
        # TODO: Add validation
        return self._obj
