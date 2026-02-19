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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswModuleDescription":
        """Deserialize XML element to BswModuleDescription object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswModuleDescription object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse bsw_module_refs (list)
        obj.bsw_module_refs = []
        for child in ARObject._find_all_child_elements(element, "BSW-MODULES"):
            bsw_module_refs_value = ARObject._deserialize_by_tag(child, "BswModuleDependency")
            obj.bsw_module_refs.append(bsw_module_refs_value)

        # Parse bsw_module_documentation
        child = ARObject._find_child_element(element, "BSW-MODULE-DOCUMENTATION")
        if child is not None:
            bsw_module_documentation_value = ARObject._deserialize_by_tag(child, "SwComponentDocumentation")
            obj.bsw_module_documentation = bsw_module_documentation_value

        # Parse expected_entries (list)
        obj.expected_entries = []
        for child in ARObject._find_all_child_elements(element, "EXPECTED-ENTRIES"):
            expected_entries_value = ARObject._deserialize_by_tag(child, "BswModuleEntry")
            obj.expected_entries.append(expected_entries_value)

        # Parse implementeds (list)
        obj.implementeds = []
        for child in ARObject._find_all_child_elements(element, "IMPLEMENTEDS"):
            implementeds_value = ARObject._deserialize_by_tag(child, "BswModuleEntry")
            obj.implementeds.append(implementeds_value)

        # Parse internal_behaviors (list)
        obj.internal_behaviors = []
        for child in ARObject._find_all_child_elements(element, "INTERNAL-BEHAVIORS"):
            internal_behaviors_value = ARObject._deserialize_by_tag(child, "BswInternalBehavior")
            obj.internal_behaviors.append(internal_behaviors_value)

        # Parse module_id
        child = ARObject._find_child_element(element, "MODULE-ID")
        if child is not None:
            module_id_value = child.text
            obj.module_id = module_id_value

        # Parse provided_clients (list)
        obj.provided_clients = []
        for child in ARObject._find_all_child_elements(element, "PROVIDED-CLIENTS"):
            provided_clients_value = ARObject._deserialize_by_tag(child, "BswModuleClientServerEntry")
            obj.provided_clients.append(provided_clients_value)

        # Parse provided_data_refs (list)
        obj.provided_data_refs = []
        for child in ARObject._find_all_child_elements(element, "PROVIDED-DATAS"):
            provided_data_refs_value = ARObject._deserialize_by_tag(child, "VariableDataPrototype")
            obj.provided_data_refs.append(provided_data_refs_value)

        # Parse provided_mode_refs (list)
        obj.provided_mode_refs = []
        for child in ARObject._find_all_child_elements(element, "PROVIDED-MODES"):
            provided_mode_refs_value = ARObject._deserialize_by_tag(child, "ModeDeclarationGroup")
            obj.provided_mode_refs.append(provided_mode_refs_value)

        # Parse released_trigger_refs (list)
        obj.released_trigger_refs = []
        for child in ARObject._find_all_child_elements(element, "RELEASED-TRIGGERS"):
            released_trigger_refs_value = ARObject._deserialize_by_tag(child, "Trigger")
            obj.released_trigger_refs.append(released_trigger_refs_value)

        # Parse required_clients (list)
        obj.required_clients = []
        for child in ARObject._find_all_child_elements(element, "REQUIRED-CLIENTS"):
            required_clients_value = ARObject._deserialize_by_tag(child, "BswModuleClientServerEntry")
            obj.required_clients.append(required_clients_value)

        # Parse required_data_refs (list)
        obj.required_data_refs = []
        for child in ARObject._find_all_child_elements(element, "REQUIRED-DATAS"):
            required_data_refs_value = ARObject._deserialize_by_tag(child, "VariableDataPrototype")
            obj.required_data_refs.append(required_data_refs_value)

        # Parse required_mode_refs (list)
        obj.required_mode_refs = []
        for child in ARObject._find_all_child_elements(element, "REQUIRED-MODES"):
            required_mode_refs_value = ARObject._deserialize_by_tag(child, "ModeDeclarationGroup")
            obj.required_mode_refs.append(required_mode_refs_value)

        # Parse required_trigger_refs (list)
        obj.required_trigger_refs = []
        for child in ARObject._find_all_child_elements(element, "REQUIRED-TRIGGERS"):
            required_trigger_refs_value = ARObject._deserialize_by_tag(child, "Trigger")
            obj.required_trigger_refs.append(required_trigger_refs_value)

        return obj



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
