"""SwcServiceDependency AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_dependency import (
    ServiceDependency,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_group import (
    PortGroup,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServiceMapping.role_based_port_assignment import (
    RoleBasedPortAssignment,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_needs import (
    ServiceNeeds,
)


class SwcServiceDependency(ServiceDependency):
    """AUTOSAR SwcServiceDependency."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("assigned_datas", None, False, True, any (RoleBasedData)),  # assignedDatas
        ("assigned_ports", None, False, True, RoleBasedPortAssignment),  # assignedPorts
        ("represented_port", None, False, False, PortGroup),  # representedPort
        ("service_needs", None, False, False, ServiceNeeds),  # serviceNeeds
    ]

    def __init__(self) -> None:
        """Initialize SwcServiceDependency."""
        super().__init__()
        self.assigned_datas: list[Any] = []
        self.assigned_ports: list[RoleBasedPortAssignment] = []
        self.represented_port: Optional[PortGroup] = None
        self.service_needs: Optional[ServiceNeeds] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SwcServiceDependency to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwcServiceDependency":
        """Create SwcServiceDependency from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SwcServiceDependency instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SwcServiceDependency since parent returns ARObject
        return cast("SwcServiceDependency", obj)


class SwcServiceDependencyBuilder:
    """Builder for SwcServiceDependency."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwcServiceDependency = SwcServiceDependency()

    def build(self) -> SwcServiceDependency:
        """Build and return SwcServiceDependency object.

        Returns:
            SwcServiceDependency instance
        """
        # TODO: Add validation
        return self._obj
