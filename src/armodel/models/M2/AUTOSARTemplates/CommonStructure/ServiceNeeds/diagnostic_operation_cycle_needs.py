"""DiagnosticOperationCycleNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 761)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import (
    DiagnosticCapabilityElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class DiagnosticOperationCycleNeeds(DiagnosticCapabilityElement):
    """AUTOSAR DiagnosticOperationCycleNeeds."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    operation_cycle: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticOperationCycleNeeds."""
        super().__init__()
        self.operation_cycle: Optional[Any] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticOperationCycleNeeds":
        """Deserialize XML element to DiagnosticOperationCycleNeeds object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticOperationCycleNeeds object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse operation_cycle
        child = ARObject._find_child_element(element, "OPERATION-CYCLE")
        if child is not None:
            operation_cycle_value = child.text
            obj.operation_cycle = operation_cycle_value

        return obj



class DiagnosticOperationCycleNeedsBuilder:
    """Builder for DiagnosticOperationCycleNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticOperationCycleNeeds = DiagnosticOperationCycleNeeds()

    def build(self) -> DiagnosticOperationCycleNeeds:
        """Build and return DiagnosticOperationCycleNeeds object.

        Returns:
            DiagnosticOperationCycleNeeds instance
        """
        # TODO: Add validation
        return self._obj
