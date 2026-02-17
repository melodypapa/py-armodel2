"""BswModuleEntry AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 32)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 976)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 216)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 431)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 171)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswInterfaces.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces import (
    BswCallType,
    BswEntryKindEnum,
    BswExecutionContext,
)
from armodel.models.M2.MSR.DataDictionary.ServiceProcessTask import (
    SwServiceImplPolicyEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Identifier,
    NameToken,
    PositiveInteger,
)

if TYPE_CHECKING:
    from armodel.models.M2.MSR.DataDictionary.ServiceProcessTask.sw_service_arg import (
        SwServiceArg,
    )



class BswModuleEntry(ARElement):
    """AUTOSAR BswModuleEntry."""

    def __init__(self) -> None:
        """Initialize BswModuleEntry."""
        super().__init__()
        self.arguments: list[SwServiceArg] = []
        self.bsw_entry_kind_enum: Optional[BswEntryKindEnum] = None
        self.call_type: Optional[BswCallType] = None
        self.execution: Optional[BswExecutionContext] = None
        self.function: Optional[NameToken] = None
        self.is_reentrant: Optional[Boolean] = None
        self.is_synchronous: Optional[Boolean] = None
        self.return_type: Optional[SwServiceArg] = None
        self.role: Optional[Identifier] = None
        self.service_id: Optional[PositiveInteger] = None
        self.sw_service_impl_policy: Optional[SwServiceImplPolicyEnum] = None


class BswModuleEntryBuilder:
    """Builder for BswModuleEntry."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswModuleEntry = BswModuleEntry()

    def build(self) -> BswModuleEntry:
        """Build and return BswModuleEntry object.

        Returns:
            BswModuleEntry instance
        """
        # TODO: Add validation
        return self._obj
