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
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "bsw_modules": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class="BswModuleDependency",
        ),  # bswModules
        "bsw_module_documentation": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SwComponentDocumentation,
        ),  # bswModuleDocumentation
        "expected_entries": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=BswModuleEntry,
        ),  # expectedEntries
        "implementeds": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=BswModuleEntry,
        ),  # implementeds
        "internal_behaviors": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=BswInternalBehavior,
        ),  # internalBehaviors
        "module_id": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # moduleId
        "provided_clients": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=BswModuleClientServerEntry,
        ),  # providedClients
        "provided_datas": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=VariableDataPrototype,
        ),  # providedDatas
        "provided_modes": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=ModeDeclarationGroup,
        ),  # providedModes
        "released_triggers": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=Trigger,
        ),  # releasedTriggers
        "required_clients": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=BswModuleClientServerEntry,
        ),  # requiredClients
        "required_datas": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=VariableDataPrototype,
        ),  # requiredDatas
        "required_modes": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=ModeDeclarationGroup,
        ),  # requiredModes
        "required_triggers": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=Trigger,
        ),  # requiredTriggers
    }

    def __init__(self) -> None:
        """Initialize BswModuleDescription."""
        super().__init__()
        self.bsw_modules: list[BswModuleDependency] = []
        self.bsw_module_documentation: Optional[SwComponentDocumentation] = None
        self.expected_entries: list[BswModuleEntry] = []
        self.implementeds: list[BswModuleEntry] = []
        self.internal_behaviors: list[BswInternalBehavior] = []
        self.module_id: Optional[PositiveInteger] = None
        self.provided_clients: list[BswModuleClientServerEntry] = []
        self.provided_datas: list[VariableDataPrototype] = []
        self.provided_modes: list[ModeDeclarationGroup] = []
        self.released_triggers: list[Trigger] = []
        self.required_clients: list[BswModuleClientServerEntry] = []
        self.required_datas: list[VariableDataPrototype] = []
        self.required_modes: list[ModeDeclarationGroup] = []
        self.required_triggers: list[Trigger] = []


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
