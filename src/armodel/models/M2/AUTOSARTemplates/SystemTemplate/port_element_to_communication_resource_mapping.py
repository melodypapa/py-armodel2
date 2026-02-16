"""PortElementToCommunicationResourceMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("client_server_instance_ref", None, False, False, ClientServerOperation),  # clientServerInstanceRef
        ("communication", None, False, False, CpSoftwareCluster),  # communication
        ("mode", None, False, False, ModeDeclarationGroup),  # mode
        ("parameter_data_in_system_instance_ref", None, False, False, ParameterDataPrototype),  # parameterDataInSystemInstanceRef
        ("trigger", None, False, False, Trigger),  # trigger
        ("variable_data_system_instance_ref", None, False, False, VariableDataPrototype),  # variableDataSystemInstanceRef
    ]

    def __init__(self) -> None:
        """Initialize PortElementToCommunicationResourceMapping."""
        super().__init__()
        self.client_server_instance_ref: Optional[ClientServerOperation] = None
        self.communication: Optional[CpSoftwareCluster] = None
        self.mode: Optional[ModeDeclarationGroup] = None
        self.parameter_data_in_system_instance_ref: Optional[ParameterDataPrototype] = None
        self.trigger: Optional[Trigger] = None
        self.variable_data_system_instance_ref: Optional[VariableDataPrototype] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert PortElementToCommunicationResourceMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PortElementToCommunicationResourceMapping":
        """Create PortElementToCommunicationResourceMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            PortElementToCommunicationResourceMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to PortElementToCommunicationResourceMapping since parent returns ARObject
        return cast("PortElementToCommunicationResourceMapping", obj)


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
