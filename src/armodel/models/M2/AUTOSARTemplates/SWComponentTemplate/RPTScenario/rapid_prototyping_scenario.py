"""RapidPrototypingScenario AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 327)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 846)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_RPTScenario.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario.rpt_container import (
    RptContainer,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario.rpt_profile import (
    RptProfile,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.system import (
    System,
)


class RapidPrototypingScenario(ARElement):
    """AUTOSAR RapidPrototypingScenario."""

    def __init__(self) -> None:
        """Initialize RapidPrototypingScenario."""
        super().__init__()
        self.host_system: Optional[System] = None
        self.rpt_containers: list[RptContainer] = []
        self.rpt_profiles: list[RptProfile] = []
        self.rpt_system: Optional[System] = None


class RapidPrototypingScenarioBuilder:
    """Builder for RapidPrototypingScenario."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RapidPrototypingScenario = RapidPrototypingScenario()

    def build(self) -> RapidPrototypingScenario:
        """Build and return RapidPrototypingScenario object.

        Returns:
            RapidPrototypingScenario instance
        """
        # TODO: Add validation
        return self._obj
