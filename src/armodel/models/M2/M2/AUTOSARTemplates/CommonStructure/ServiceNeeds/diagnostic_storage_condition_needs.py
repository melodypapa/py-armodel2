"""DiagnosticStorageConditionNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 762)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import (
    DiagnosticCapabilityElement,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    StorageConditionStatusEnum,
)


class DiagnosticStorageConditionNeeds(DiagnosticCapabilityElement):
    """AUTOSAR DiagnosticStorageConditionNeeds."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "initial_status": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=StorageConditionStatusEnum,
        ),  # initialStatus
    }

    def __init__(self) -> None:
        """Initialize DiagnosticStorageConditionNeeds."""
        super().__init__()
        self.initial_status: Optional[StorageConditionStatusEnum] = None


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
