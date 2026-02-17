"""BuildActionEnvironment AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 370)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 173)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_BuildActionManifest.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.MSR.AsamHdo.SpecialData.sdg import (
    Sdg,
)


class BuildActionEnvironment(Identifiable):
    """AUTOSAR BuildActionEnvironment."""

    sdgs: list[Sdg]
    def __init__(self) -> None:
        """Initialize BuildActionEnvironment."""
        super().__init__()
        self.sdgs: list[Sdg] = []


class BuildActionEnvironmentBuilder:
    """Builder for BuildActionEnvironment."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BuildActionEnvironment = BuildActionEnvironment()

    def build(self) -> BuildActionEnvironment:
        """Build and return BuildActionEnvironment object.

        Returns:
            BuildActionEnvironment instance
        """
        # TODO: Add validation
        return self._obj
