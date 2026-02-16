"""ServerComSpec AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.p_port_com_spec import (
    PPortComSpec,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)


class ServerComSpec(PPortComSpec):
    """AUTOSAR ServerComSpec."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("operation", None, False, False, ClientServerOperation),  # operation
        ("queue_length", None, True, False, None),  # queueLength
        ("transformation_coms", None, False, True, any (TransformationCom)),  # transformationComs
    ]

    def __init__(self) -> None:
        """Initialize ServerComSpec."""
        super().__init__()
        self.operation: Optional[ClientServerOperation] = None
        self.queue_length: Optional[PositiveInteger] = None
        self.transformation_coms: list[Any] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ServerComSpec to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ServerComSpec":
        """Create ServerComSpec from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ServerComSpec instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ServerComSpec since parent returns ARObject
        return cast("ServerComSpec", obj)


class ServerComSpecBuilder:
    """Builder for ServerComSpec."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ServerComSpec = ServerComSpec()

    def build(self) -> ServerComSpec:
        """Build and return ServerComSpec object.

        Returns:
            ServerComSpec instance
        """
        # TODO: Add validation
        return self._obj
