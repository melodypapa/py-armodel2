"""ClientServerToSignalMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 242)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_DataMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.data_mapping import (
    DataMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.system_signal import (
    SystemSignal,
)


class ClientServerToSignalMapping(DataMapping):
    """AUTOSAR ClientServerToSignalMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    call_signal: Optional[SystemSignal]
    client_server: Optional[ClientServerOperation]
    return_signal: Optional[SystemSignal]
    def __init__(self) -> None:
        """Initialize ClientServerToSignalMapping."""
        super().__init__()
        self.call_signal: Optional[SystemSignal] = None
        self.client_server: Optional[ClientServerOperation] = None
        self.return_signal: Optional[SystemSignal] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ClientServerToSignalMapping":
        """Deserialize XML element to ClientServerToSignalMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ClientServerToSignalMapping object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse call_signal
        child = ARObject._find_child_element(element, "CALL-SIGNAL")
        if child is not None:
            call_signal_value = ARObject._deserialize_by_tag(child, "SystemSignal")
            obj.call_signal = call_signal_value

        # Parse client_server
        child = ARObject._find_child_element(element, "CLIENT-SERVER")
        if child is not None:
            client_server_value = ARObject._deserialize_by_tag(child, "ClientServerOperation")
            obj.client_server = client_server_value

        # Parse return_signal
        child = ARObject._find_child_element(element, "RETURN-SIGNAL")
        if child is not None:
            return_signal_value = ARObject._deserialize_by_tag(child, "SystemSignal")
            obj.return_signal = return_signal_value

        return obj



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
