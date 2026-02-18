"""BswModuleDescription AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 26)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 303)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 973)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 212)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 426)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 168)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswOverview.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_internal_behavior import (
    BswInternalBehavior,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_module_client_server_entry import (
    BswModuleClientServerEntry,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_module_entry import (
    BswModuleEntry,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SoftwareComponentDocumentation.sw_component_documentation import (
    SwComponentDocumentation,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger import (
    Trigger,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_module_dependency import (
        BswModuleDependency,
    )



class BswModuleDescription(ARElement):
    """AUTOSAR BswModuleDescription."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    bsw_module_refs: list[ARRef]
    bsw_module_documentation: Optional[SwComponentDocumentation]
    expected_entries: list[BswModuleEntry]
    implementeds: list[BswModuleEntry]
    internal_behaviors: list[BswInternalBehavior]
    module_id: Optional[PositiveInteger]
    provided_clients: list[BswModuleClientServerEntry]
    provided_data_refs: list[ARRef]
    provided_mode_refs: list[ARRef]
    released_trigger_refs: list[ARRef]
    required_clients: list[BswModuleClientServerEntry]
    required_data_refs: list[ARRef]
    required_mode_refs: list[ARRef]
    required_trigger_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize BswModuleDescription."""
        super().__init__()
        self.bsw_module_refs: list[ARRef] = []
        self.bsw_module_documentation: Optional[SwComponentDocumentation] = None
        self.expected_entries: list[BswModuleEntry] = []
        self.implementeds: list[BswModuleEntry] = []
        self.internal_behaviors: list[BswInternalBehavior] = []
        self.module_id: Optional[PositiveInteger] = None
        self.provided_clients: list[BswModuleClientServerEntry] = []
        self.provided_data_refs: list[ARRef] = []
        self.provided_mode_refs: list[ARRef] = []
        self.released_trigger_refs: list[ARRef] = []
        self.required_clients: list[BswModuleClientServerEntry] = []
        self.required_data_refs: list[ARRef] = []
        self.required_mode_refs: list[ARRef] = []
        self.required_trigger_refs: list[ARRef] = []


class BswModuleDescriptionBuilder:
    """Builder for BswModuleDescription."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswModuleDescription = BswModuleDescription()

    def build(self) -> BswModuleDescription:
        """Build and return BswModuleDescription object.

        Returns:
            BswModuleDescription instance
        """
        # TODO: Add validation
        return self._obj
