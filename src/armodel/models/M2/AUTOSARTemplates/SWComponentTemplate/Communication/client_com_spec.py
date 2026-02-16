"""ClientComSpec AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.r_port_com_spec import (
    RPortComSpec,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)


class ClientComSpec(RPortComSpec):
    """AUTOSAR ClientComSpec."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("end_to_end_call", None, True, False, None),  # endToEndCall
        ("operation", None, False, False, ClientServerOperation),  # operation
        ("transformation_coms", None, False, True, any (TransformationCom)),  # transformationComs
    ]

    def __init__(self) -> None:
        """Initialize ClientComSpec."""
        super().__init__()
        self.end_to_end_call: Optional[TimeValue] = None
        self.operation: Optional[ClientServerOperation] = None
        self.transformation_coms: list[Any] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ClientComSpec to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ClientComSpec":
        """Create ClientComSpec from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ClientComSpec instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ClientComSpec since parent returns ARObject
        return cast("ClientComSpec", obj)


class ClientComSpecBuilder:
    """Builder for ClientComSpec."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ClientComSpec = ClientComSpec()

    def build(self) -> ClientComSpec:
        """Build and return ClientComSpec object.

        Returns:
            ClientComSpec instance
        """
        # TODO: Add validation
        return self._obj
