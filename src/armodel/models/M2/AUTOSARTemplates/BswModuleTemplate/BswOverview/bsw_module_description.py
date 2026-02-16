"""BswModuleDescription AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
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
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_module_dependency import (
    BswModuleDependency,
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


class BswModuleDescription(ARElement):
    """AUTOSAR BswModuleDescription."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("bsw_modules", None, False, True, BswModuleDependency),  # bswModules
        ("bsw_module_documentation", None, False, False, SwComponentDocumentation),  # bswModuleDocumentation
        ("expected_entries", None, False, True, BswModuleEntry),  # expectedEntries
        ("implementeds", None, False, True, BswModuleEntry),  # implementeds
        ("internal_behaviors", None, False, True, BswInternalBehavior),  # internalBehaviors
        ("module_id", None, True, False, None),  # moduleId
        ("provided_clients", None, False, True, BswModuleClientServerEntry),  # providedClients
        ("provided_datas", None, False, True, VariableDataPrototype),  # providedDatas
        ("provided_modes", None, False, True, ModeDeclarationGroup),  # providedModes
        ("released_triggers", None, False, True, Trigger),  # releasedTriggers
        ("required_clients", None, False, True, BswModuleClientServerEntry),  # requiredClients
        ("required_datas", None, False, True, VariableDataPrototype),  # requiredDatas
        ("required_modes", None, False, True, ModeDeclarationGroup),  # requiredModes
        ("required_triggers", None, False, True, Trigger),  # requiredTriggers
    ]

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

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BswModuleDescription to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswModuleDescription":
        """Create BswModuleDescription from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BswModuleDescription instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BswModuleDescription since parent returns ARObject
        return cast("BswModuleDescription", obj)


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
