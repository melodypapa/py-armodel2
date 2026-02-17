"""SupervisedEntityCheckpointNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 254)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 708)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_needs import (
    ServiceNeeds,
)


class SupervisedEntityCheckpointNeeds(ServiceNeeds):
    """AUTOSAR SupervisedEntityCheckpointNeeds."""

    def __init__(self) -> None:
        """Initialize SupervisedEntityCheckpointNeeds."""
        super().__init__()


class SupervisedEntityCheckpointNeedsBuilder:
    """Builder for SupervisedEntityCheckpointNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SupervisedEntityCheckpointNeeds = SupervisedEntityCheckpointNeeds()

    def build(self) -> SupervisedEntityCheckpointNeeds:
        """Build and return SupervisedEntityCheckpointNeeds object.

        Returns:
            SupervisedEntityCheckpointNeeds instance
        """
        # TODO: Add validation
        return self._obj
