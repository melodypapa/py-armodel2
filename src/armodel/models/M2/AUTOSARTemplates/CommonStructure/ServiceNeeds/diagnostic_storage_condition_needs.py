"""DiagnosticStorageConditionNeeds AUTOSAR element.

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
    StorageConditionStatusEnum,
)


class DiagnosticStorageConditionNeeds(DiagnosticCapabilityElement):
    """AUTOSAR DiagnosticStorageConditionNeeds."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    initial_status: Optional[StorageConditionStatusEnum]
    def __init__(self) -> None:
        """Initialize DiagnosticStorageConditionNeeds."""
        super().__init__()
        self.initial_status: Optional[StorageConditionStatusEnum] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticStorageConditionNeeds":
        """Deserialize XML element to DiagnosticStorageConditionNeeds object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticStorageConditionNeeds object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticStorageConditionNeeds, cls).deserialize(element)

        # Parse initial_status
        child = ARObject._find_child_element(element, "INITIAL-STATUS")
        if child is not None:
            initial_status_value = StorageConditionStatusEnum.deserialize(child)
            obj.initial_status = initial_status_value

        return obj



class DiagnosticStorageConditionNeedsBuilder:
    """Builder for DiagnosticStorageConditionNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticStorageConditionNeeds = DiagnosticStorageConditionNeeds()

    def build(self) -> DiagnosticStorageConditionNeeds:
        """Build and return DiagnosticStorageConditionNeeds object.

        Returns:
            DiagnosticStorageConditionNeeds instance
        """
        # TODO: Add validation
        return self._obj
