"""DiagnosticCapabilityElement AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 236)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 753)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_needs import (
    ServiceNeeds,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    DiagnosticAudienceEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    DiagRequirementIdString,
    PositiveInteger,
)
from abc import ABC, abstractmethod


class DiagnosticCapabilityElement(ServiceNeeds, ABC):
    """AUTOSAR DiagnosticCapabilityElement."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    audiences: list[DiagnosticAudienceEnum]
    diag: Optional[DiagRequirementIdString]
    security_access: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize DiagnosticCapabilityElement."""
        super().__init__()
        self.audiences: list[DiagnosticAudienceEnum] = []
        self.diag: Optional[DiagRequirementIdString] = None
        self.security_access: Optional[PositiveInteger] = None


class DiagnosticCapabilityElementBuilder:
    """Builder for DiagnosticCapabilityElement."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticCapabilityElement = DiagnosticCapabilityElement()

    def build(self) -> DiagnosticCapabilityElement:
        """Build and return DiagnosticCapabilityElement object.

        Returns:
            DiagnosticCapabilityElement instance
        """
        # TODO: Add validation
        return self._obj
