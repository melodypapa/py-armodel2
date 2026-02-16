"""ClientServerOperationComProps AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster_communication_resource_props import (
    CpSoftwareClusterCommunicationResourceProps,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class ClientServerOperationComProps(CpSoftwareClusterCommunicationResourceProps):
    """AUTOSAR ClientServerOperationComProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("queue_length", None, True, False, None),  # queueLength
    ]

    def __init__(self) -> None:
        """Initialize ClientServerOperationComProps."""
        super().__init__()
        self.queue_length: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ClientServerOperationComProps to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ClientServerOperationComProps":
        """Create ClientServerOperationComProps from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ClientServerOperationComProps instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ClientServerOperationComProps since parent returns ARObject
        return cast("ClientServerOperationComProps", obj)


class ClientServerOperationComPropsBuilder:
    """Builder for ClientServerOperationComProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ClientServerOperationComProps = ClientServerOperationComProps()

    def build(self) -> ClientServerOperationComProps:
        """Build and return ClientServerOperationComProps object.

        Returns:
            ClientServerOperationComProps instance
        """
        # TODO: Add validation
        return self._obj
