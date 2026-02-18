"""ServiceNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 227)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 329)
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 306)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 603)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2055)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from abc import ABC, abstractmethod


class ServiceNeeds(Identifiable, ABC):
    """AUTOSAR ServiceNeeds."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    def __init__(self) -> None:
        """Initialize ServiceNeeds."""
        super().__init__()


class ServiceNeedsBuilder:
    """Builder for ServiceNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ServiceNeeds = ServiceNeeds()

    def build(self) -> ServiceNeeds:
        """Build and return ServiceNeeds object.

        Returns:
            ServiceNeeds instance
        """
        # TODO: Add validation
        return self._obj
