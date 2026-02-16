"""SystemSignalToCommunicationResourceMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster import (
    CpSoftwareCluster,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.system_signal import (
    SystemSignal,
)


class SystemSignalToCommunicationResourceMapping(Identifiable):
    """AUTOSAR SystemSignalToCommunicationResourceMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("software_cluster", None, False, False, CpSoftwareCluster),  # softwareCluster
        ("system_signal", None, False, False, SystemSignal),  # systemSignal
    ]

    def __init__(self) -> None:
        """Initialize SystemSignalToCommunicationResourceMapping."""
        super().__init__()
        self.software_cluster: Optional[CpSoftwareCluster] = None
        self.system_signal: Optional[SystemSignal] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SystemSignalToCommunicationResourceMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SystemSignalToCommunicationResourceMapping":
        """Create SystemSignalToCommunicationResourceMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SystemSignalToCommunicationResourceMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SystemSignalToCommunicationResourceMapping since parent returns ARObject
        return cast("SystemSignalToCommunicationResourceMapping", obj)


class SystemSignalToCommunicationResourceMappingBuilder:
    """Builder for SystemSignalToCommunicationResourceMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SystemSignalToCommunicationResourceMapping = SystemSignalToCommunicationResourceMapping()

    def build(self) -> SystemSignalToCommunicationResourceMapping:
        """Build and return SystemSignalToCommunicationResourceMapping object.

        Returns:
            SystemSignalToCommunicationResourceMapping instance
        """
        # TODO: Add validation
        return self._obj
