"""ClientServerToSignalMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.data_mapping import (
    DataMapping,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.system_signal import (
    SystemSignal,
)


class ClientServerToSignalMapping(DataMapping):
    """AUTOSAR ClientServerToSignalMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("call_signal", None, False, False, SystemSignal),  # callSignal
        ("client_server", None, False, False, ClientServerOperation),  # clientServer
        ("return_signal", None, False, False, SystemSignal),  # returnSignal
    ]

    def __init__(self) -> None:
        """Initialize ClientServerToSignalMapping."""
        super().__init__()
        self.call_signal: Optional[SystemSignal] = None
        self.client_server: Optional[ClientServerOperation] = None
        self.return_signal: Optional[SystemSignal] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ClientServerToSignalMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ClientServerToSignalMapping":
        """Create ClientServerToSignalMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ClientServerToSignalMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ClientServerToSignalMapping since parent returns ARObject
        return cast("ClientServerToSignalMapping", obj)


class ClientServerToSignalMappingBuilder:
    """Builder for ClientServerToSignalMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ClientServerToSignalMapping = ClientServerToSignalMapping()

    def build(self) -> ClientServerToSignalMapping:
        """Build and return ClientServerToSignalMapping object.

        Returns:
            ClientServerToSignalMapping instance
        """
        # TODO: Add validation
        return self._obj
