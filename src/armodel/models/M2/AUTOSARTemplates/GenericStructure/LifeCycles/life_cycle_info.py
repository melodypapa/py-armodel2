"""LifeCycleInfo AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 392)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 195)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_LifeCycles.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.LifeCycles.life_cycle_period import (
    LifeCyclePeriod,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.LifeCycles.life_cycle_state import (
    LifeCycleState,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)


class LifeCycleInfo(ARObject):
    """AUTOSAR LifeCycleInfo."""

    def __init__(self) -> None:
        """Initialize LifeCycleInfo."""
        super().__init__()
        self.lc_object: Referrable = None
        self.lc_state: Optional[LifeCycleState] = None
        self.period_begin: Optional[LifeCyclePeriod] = None
        self.period_end: Optional[LifeCyclePeriod] = None
        self.remark: Optional[DocumentationBlock] = None
        self.use_insteads: list[Referrable] = []


class LifeCycleInfoBuilder:
    """Builder for LifeCycleInfo."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LifeCycleInfo = LifeCycleInfo()

    def build(self) -> LifeCycleInfo:
        """Build and return LifeCycleInfo object.

        Returns:
            LifeCycleInfo instance
        """
        # TODO: Add validation
        return self._obj
