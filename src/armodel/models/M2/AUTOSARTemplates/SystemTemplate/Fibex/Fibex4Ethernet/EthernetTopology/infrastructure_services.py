"""InfrastructureServices AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.do_ip_entity import (
    DoIpEntity,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.time_synchronization import (
    TimeSynchronization,
)


class InfrastructureServices(ARObject):
    """AUTOSAR InfrastructureServices."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("do_ip_entity", None, False, False, DoIpEntity),  # doIpEntity
        ("time", None, False, False, TimeSynchronization),  # time
    ]

    def __init__(self) -> None:
        """Initialize InfrastructureServices."""
        super().__init__()
        self.do_ip_entity: Optional[DoIpEntity] = None
        self.time: Optional[TimeSynchronization] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert InfrastructureServices to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "InfrastructureServices":
        """Create InfrastructureServices from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            InfrastructureServices instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to InfrastructureServices since parent returns ARObject
        return cast("InfrastructureServices", obj)


class InfrastructureServicesBuilder:
    """Builder for InfrastructureServices."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: InfrastructureServices = InfrastructureServices()

    def build(self) -> InfrastructureServices:
        """Build and return InfrastructureServices object.

        Returns:
            InfrastructureServices instance
        """
        # TODO: Add validation
        return self._obj
