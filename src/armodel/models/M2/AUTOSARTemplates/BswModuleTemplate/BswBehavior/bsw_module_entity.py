"""BswModuleEntity AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 70)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 215)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 429)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.executable_entity import (
    ExecutableEntity,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_internal_triggering_point import (
    BswInternalTriggeringPoint,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_module_call_point import (
    BswModuleCallPoint,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_module_entry import (
    BswModuleEntry,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_scheduler_name_prefix import (
    BswSchedulerNamePrefix,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_variable_access import (
    BswVariableAccess,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger import (
    Trigger,
)


class BswModuleEntity(ExecutableEntity):
    """AUTOSAR BswModuleEntity."""
    """Abstract base class - do not instantiate directly."""

    accessed_modes: list[ModeDeclarationGroup]
    activation_points: list[BswInternalTriggeringPoint]
    call_points: list[BswModuleCallPoint]
    data_receives: list[BswVariableAccess]
    data_send_points: list[BswVariableAccess]
    implemented: Optional[BswModuleEntry]
    issued_triggers: list[Trigger]
    managed_modes: list[ModeDeclarationGroup]
    scheduler_name: Optional[BswSchedulerNamePrefix]
    def __init__(self) -> None:
        """Initialize BswModuleEntity."""
        super().__init__()
        self.accessed_modes: list[ModeDeclarationGroup] = []
        self.activation_points: list[BswInternalTriggeringPoint] = []
        self.call_points: list[BswModuleCallPoint] = []
        self.data_receives: list[BswVariableAccess] = []
        self.data_send_points: list[BswVariableAccess] = []
        self.implemented: Optional[BswModuleEntry] = None
        self.issued_triggers: list[Trigger] = []
        self.managed_modes: list[ModeDeclarationGroup] = []
        self.scheduler_name: Optional[BswSchedulerNamePrefix] = None


class BswModuleEntityBuilder:
    """Builder for BswModuleEntity."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswModuleEntity = BswModuleEntity()

    def build(self) -> BswModuleEntity:
        """Build and return BswModuleEntity object.

        Returns:
            BswModuleEntity instance
        """
        # TODO: Add validation
        return self._obj
