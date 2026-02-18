"""PortElementToCommunicationResourceMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 905)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster import (
    CpSoftwareCluster,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.parameter_data_prototype import (
    ParameterDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger import (
    Trigger,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class PortElementToCommunicationResourceMapping(Identifiable):
    """AUTOSAR PortElementToCommunicationResourceMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    client_server_instance_ref: Optional[ClientServerOperation]
    communication: Optional[CpSoftwareCluster]
    mode_ref: Optional[ARRef]
    parameter_data_in_system_instance_ref: Optional[ARRef]
    trigger_ref: Optional[ARRef]
    variable_data_system_instance_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize PortElementToCommunicationResourceMapping."""
        super().__init__()
        self.client_server_instance_ref: Optional[ClientServerOperation] = None
        self.communication: Optional[CpSoftwareCluster] = None
        self.mode_ref: Optional[ARRef] = None
        self.parameter_data_in_system_instance_ref: Optional[ARRef] = None
        self.trigger_ref: Optional[ARRef] = None
        self.variable_data_system_instance_ref: Optional[ARRef] = None


class PortElementToCommunicationResourceMappingBuilder:
    """Builder for PortElementToCommunicationResourceMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PortElementToCommunicationResourceMapping = PortElementToCommunicationResourceMapping()

    def build(self) -> PortElementToCommunicationResourceMapping:
        """Build and return PortElementToCommunicationResourceMapping object.

        Returns:
            PortElementToCommunicationResourceMapping instance
        """
        # TODO: Add validation
        return self._obj
