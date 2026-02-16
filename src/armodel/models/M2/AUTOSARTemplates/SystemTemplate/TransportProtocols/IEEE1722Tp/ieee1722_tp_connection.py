"""IEEE1722TpConnection AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    MacAddressString,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)


class IEEE1722TpConnection(ARElement):
    """AUTOSAR IEEE1722TpConnection."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("destination_mac", None, True, False, None),  # destinationMac
        ("mac_address_string", None, True, False, None),  # macAddressString
        ("pdu", None, False, False, PduTriggering),  # pdu
        ("unique_stream_id", None, True, False, None),  # uniqueStreamId
        ("version", None, True, False, None),  # version
        ("vlan_priority", None, True, False, None),  # vlanPriority
    ]

    def __init__(self) -> None:
        """Initialize IEEE1722TpConnection."""
        super().__init__()
        self.destination_mac: Optional[MacAddressString] = None
        self.mac_address_string: Optional[MacAddressString] = None
        self.pdu: Optional[PduTriggering] = None
        self.unique_stream_id: Optional[PositiveInteger] = None
        self.version: Optional[PositiveInteger] = None
        self.vlan_priority: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert IEEE1722TpConnection to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IEEE1722TpConnection":
        """Create IEEE1722TpConnection from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            IEEE1722TpConnection instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to IEEE1722TpConnection since parent returns ARObject
        return cast("IEEE1722TpConnection", obj)


class IEEE1722TpConnectionBuilder:
    """Builder for IEEE1722TpConnection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IEEE1722TpConnection = IEEE1722TpConnection()

    def build(self) -> IEEE1722TpConnection:
        """Build and return IEEE1722TpConnection object.

        Returns:
            IEEE1722TpConnection instance
        """
        # TODO: Add validation
        return self._obj
