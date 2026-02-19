"""DiagnosticEnableConditionNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 762)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import (
    DiagnosticCapabilityElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    EventAcceptanceStatusEnum,
)


class DiagnosticEnableConditionNeeds(DiagnosticCapabilityElement):
    """AUTOSAR DiagnosticEnableConditionNeeds."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    initial_status: Optional[EventAcceptanceStatusEnum]
    def __init__(self) -> None:
        """Initialize DiagnosticEnableConditionNeeds."""
        super().__init__()
        self.initial_status: Optional[EventAcceptanceStatusEnum] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticEnableConditionNeeds":
        """Deserialize XML element to DiagnosticEnableConditionNeeds object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticEnableConditionNeeds object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse initial_status
        child = ARObject._find_child_element(element, "INITIAL-STATUS")
        if child is not None:
            initial_status_value = child.text
            obj.initial_status = initial_status_value

        return obj



class DiagnosticEnableConditionNeedsBuilder:
    """Builder for DiagnosticEnableConditionNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEnableConditionNeeds = DiagnosticEnableConditionNeeds()

    def build(self) -> DiagnosticEnableConditionNeeds:
        """Build and return DiagnosticEnableConditionNeeds object.

        Returns:
            DiagnosticEnableConditionNeeds instance
        """
        # TODO: Add validation
        return self._obj
