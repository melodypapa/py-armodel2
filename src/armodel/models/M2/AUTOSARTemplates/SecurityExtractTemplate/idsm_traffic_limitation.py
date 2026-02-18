"""IdsmTrafficLimitation AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 28)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SecurityExtractTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Float,
    PositiveInteger,
)


class IdsmTrafficLimitation(Identifiable):
    """AUTOSAR IdsmTrafficLimitation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    max_bytes_in: Optional[PositiveInteger]
    time_interval: Optional[Float]
    def __init__(self) -> None:
        """Initialize IdsmTrafficLimitation."""
        super().__init__()
        self.max_bytes_in: Optional[PositiveInteger] = None
        self.time_interval: Optional[Float] = None


class IdsmTrafficLimitationBuilder:
    """Builder for IdsmTrafficLimitation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IdsmTrafficLimitation = IdsmTrafficLimitation()

    def build(self) -> IdsmTrafficLimitation:
        """Build and return IdsmTrafficLimitation object.

        Returns:
            IdsmTrafficLimitation instance
        """
        # TODO: Add validation
        return self._obj
