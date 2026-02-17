"""BswInternalTriggeringPoint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 91)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import (
    SwImplPolicyEnum,
)


class BswInternalTriggeringPoint(Identifiable):
    """AUTOSAR BswInternalTriggeringPoint."""

    sw_impl_policy_enum: Optional[SwImplPolicyEnum]
    def __init__(self) -> None:
        """Initialize BswInternalTriggeringPoint."""
        super().__init__()
        self.sw_impl_policy_enum: Optional[SwImplPolicyEnum] = None


class BswInternalTriggeringPointBuilder:
    """Builder for BswInternalTriggeringPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswInternalTriggeringPoint = BswInternalTriggeringPoint()

    def build(self) -> BswInternalTriggeringPoint:
        """Build and return BswInternalTriggeringPoint object.

        Returns:
            BswInternalTriggeringPoint instance
        """
        # TODO: Add validation
        return self._obj
