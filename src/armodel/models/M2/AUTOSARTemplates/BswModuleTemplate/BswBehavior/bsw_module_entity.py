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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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
from abc import ABC, abstractmethod


class BswModuleEntity(ExecutableEntity, ABC):
    """AUTOSAR BswModuleEntity."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    accessed_mode_refs: list[ARRef]
    activation_point_refs: list[ARRef]
    call_points: list[BswModuleCallPoint]
    data_receives: list[BswVariableAccess]
    data_send_points: list[BswVariableAccess]
    implemented: Optional[BswModuleEntry]
    issued_trigger_refs: list[ARRef]
    managed_mode_refs: list[ARRef]
    scheduler_name: Optional[BswSchedulerNamePrefix]
    def __init__(self) -> None:
        """Initialize BswModuleEntity."""
        super().__init__()
        self.accessed_mode_refs: list[ARRef] = []
        self.activation_point_refs: list[ARRef] = []
        self.call_points: list[BswModuleCallPoint] = []
        self.data_receives: list[BswVariableAccess] = []
        self.data_send_points: list[BswVariableAccess] = []
        self.implemented: Optional[BswModuleEntry] = None
        self.issued_trigger_refs: list[ARRef] = []
        self.managed_mode_refs: list[ARRef] = []
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
