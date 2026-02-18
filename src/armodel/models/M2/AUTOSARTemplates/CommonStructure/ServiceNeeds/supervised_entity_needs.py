"""SupervisedEntityNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 234)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 707)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_needs import (
    ServiceNeeds,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    TimeValue,
)


class SupervisedEntityNeeds(ServiceNeeds):
    """AUTOSAR SupervisedEntityNeeds."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    activate_at_start: Optional[Boolean]
    checkpointses: list[Any]
    enable: Optional[Boolean]
    expected_alive: Optional[TimeValue]
    max_alive_cycle: Optional[TimeValue]
    min_alive_cycle: Optional[TimeValue]
    tolerated_failed: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize SupervisedEntityNeeds."""
        super().__init__()
        self.activate_at_start: Optional[Boolean] = None
        self.checkpointses: list[Any] = []
        self.enable: Optional[Boolean] = None
        self.expected_alive: Optional[TimeValue] = None
        self.max_alive_cycle: Optional[TimeValue] = None
        self.min_alive_cycle: Optional[TimeValue] = None
        self.tolerated_failed: Optional[PositiveInteger] = None


class SupervisedEntityNeedsBuilder:
    """Builder for SupervisedEntityNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SupervisedEntityNeeds = SupervisedEntityNeeds()

    def build(self) -> SupervisedEntityNeeds:
        """Build and return SupervisedEntityNeeds object.

        Returns:
            SupervisedEntityNeeds instance
        """
        # TODO: Add validation
        return self._obj
