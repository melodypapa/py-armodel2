"""InternalTriggeringPoint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 322)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 561)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_Trigger.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount.abstract_access_point import (
    AbstractAccessPoint,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import (
    SwImplPolicyEnum,
)


class InternalTriggeringPoint(AbstractAccessPoint):
    """AUTOSAR InternalTriggeringPoint."""

    def __init__(self) -> None:
        """Initialize InternalTriggeringPoint."""
        super().__init__()
        self.sw_impl_policy_enum: Optional[SwImplPolicyEnum] = None


class InternalTriggeringPointBuilder:
    """Builder for InternalTriggeringPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: InternalTriggeringPoint = InternalTriggeringPoint()

    def build(self) -> InternalTriggeringPoint:
        """Build and return InternalTriggeringPoint object.

        Returns:
            InternalTriggeringPoint instance
        """
        # TODO: Add validation
        return self._obj
