"""BswModuleEntity AUTOSAR element."""

from typing import Optional, cast
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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("accessed_modes", None, False, True, ModeDeclarationGroup),  # accessedModes
        ("activation_points", None, False, True, BswInternalTriggeringPoint),  # activationPoints
        ("call_points", None, False, True, BswModuleCallPoint),  # callPoints
        ("data_receives", None, False, True, BswVariableAccess),  # dataReceives
        ("data_send_points", None, False, True, BswVariableAccess),  # dataSendPoints
        ("implemented", None, False, False, BswModuleEntry),  # implemented
        ("issued_triggers", None, False, True, Trigger),  # issuedTriggers
        ("managed_modes", None, False, True, ModeDeclarationGroup),  # managedModes
        ("scheduler_name", None, False, False, BswSchedulerNamePrefix),  # schedulerName
    ]

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

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BswModuleEntity to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswModuleEntity":
        """Create BswModuleEntity from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BswModuleEntity instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BswModuleEntity since parent returns ARObject
        return cast("BswModuleEntity", obj)


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
