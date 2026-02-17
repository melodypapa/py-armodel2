"""ExclusiveArea AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 82)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 552)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_InternalBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)


class ExclusiveArea(Identifiable):
    """AUTOSAR ExclusiveArea."""

    def __init__(self) -> None:
        """Initialize ExclusiveArea."""
        super().__init__()


class ExclusiveAreaBuilder:
    """Builder for ExclusiveArea."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ExclusiveArea = ExclusiveArea()

    def build(self) -> ExclusiveArea:
        """Build and return ExclusiveArea object.

        Returns:
            ExclusiveArea instance
        """
        # TODO: Add validation
        return self._obj
