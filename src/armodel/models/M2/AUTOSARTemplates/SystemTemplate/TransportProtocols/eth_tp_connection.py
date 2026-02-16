"""EthTpConnection AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection.tp_connection import (
    TpConnection,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)


class EthTpConnection(TpConnection):
    """AUTOSAR EthTpConnection."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("tp_sdus", None, False, True, PduTriggering),  # tpSdus
    ]

    def __init__(self) -> None:
        """Initialize EthTpConnection."""
        super().__init__()
        self.tp_sdus: list[PduTriggering] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EthTpConnection to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EthTpConnection":
        """Create EthTpConnection from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EthTpConnection instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EthTpConnection since parent returns ARObject
        return cast("EthTpConnection", obj)


class EthTpConnectionBuilder:
    """Builder for EthTpConnection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EthTpConnection = EthTpConnection()

    def build(self) -> EthTpConnection:
        """Build and return EthTpConnection object.

        Returns:
            EthTpConnection instance
        """
        # TODO: Add validation
        return self._obj
