"""Trigger AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 45)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 109)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2076)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 255)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_TriggerDeclaration.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import (
    SwImplPolicyEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)


class Trigger(Identifiable):
    """AUTOSAR Trigger."""

    sw_impl_policy_enum: Optional[SwImplPolicyEnum]
    trigger_period: Optional[MultidimensionalTime]
    def __init__(self) -> None:
        """Initialize Trigger."""
        super().__init__()
        self.sw_impl_policy_enum: Optional[SwImplPolicyEnum] = None
        self.trigger_period: Optional[MultidimensionalTime] = None


class TriggerBuilder:
    """Builder for Trigger."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Trigger = Trigger()

    def build(self) -> Trigger:
        """Build and return Trigger object.

        Returns:
            Trigger instance
        """
        # TODO: Add validation
        return self._obj
