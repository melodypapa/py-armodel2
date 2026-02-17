"""SwcBswMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 110)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 656)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 217)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_SwcBswMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_internal_behavior import (
    BswInternalBehavior,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.SwcBswMapping.swc_bsw_runnable_mapping import (
    SwcBswRunnableMapping,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.swc_internal_behavior import (
    SwcInternalBehavior,
)


class SwcBswMapping(ARElement):
    """AUTOSAR SwcBswMapping."""

    bsw_behavior: Optional[BswInternalBehavior]
    runnable_mappings: list[SwcBswRunnableMapping]
    swc_behavior: Optional[SwcInternalBehavior]
    synchronizeds: list[Any]
    def __init__(self) -> None:
        """Initialize SwcBswMapping."""
        super().__init__()
        self.bsw_behavior: Optional[BswInternalBehavior] = None
        self.runnable_mappings: list[SwcBswRunnableMapping] = []
        self.swc_behavior: Optional[SwcInternalBehavior] = None
        self.synchronizeds: list[Any] = []


class SwcBswMappingBuilder:
    """Builder for SwcBswMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwcBswMapping = SwcBswMapping()

    def build(self) -> SwcBswMapping:
        """Build and return SwcBswMapping object.

        Returns:
            SwcBswMapping instance
        """
        # TODO: Add validation
        return self._obj
