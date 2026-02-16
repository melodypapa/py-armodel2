"""DiagnosticStorageConditionNeeds AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import (
    DiagnosticCapabilityElement,
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
