"""AbstractEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 541)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 204)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_InternalBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.executable_entity import (
    ExecutableEntity,
)


class AbstractEvent(Identifiable):
    """AUTOSAR AbstractEvent."""
    """Abstract base class - do not instantiate directly."""

    activation: Optional[ExecutableEntity]
    def __init__(self) -> None:
        """Initialize AbstractEvent."""
        super().__init__()
        self.activation: Optional[ExecutableEntity] = None


class AbstractEventBuilder:
    """Builder for AbstractEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AbstractEvent = AbstractEvent()

    def build(self) -> AbstractEvent:
        """Build and return AbstractEvent object.

        Returns:
            AbstractEvent instance
        """
        # TODO: Add validation
        return self._obj
