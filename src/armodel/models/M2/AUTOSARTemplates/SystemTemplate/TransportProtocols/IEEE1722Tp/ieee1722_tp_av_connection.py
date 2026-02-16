"""IEEE1722TpAvConnection AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.ieee1722_tp_connection import (
    IEEE1722TpConnection,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)


class IEEE1722TpAvConnection(IEEE1722TpConnection):
    """AUTOSAR IEEE1722TpAvConnection."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("max_transit_time", None, True, False, None),  # maxTransitTime
        ("sdus", None, False, True, PduTriggering),  # sdus
    ]

    def __init__(self) -> None:
        """Initialize IEEE1722TpAvConnection."""
        super().__init__()
        self.max_transit_time: Optional[TimeValue] = None
        self.sdus: list[PduTriggering] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert IEEE1722TpAvConnection to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IEEE1722TpAvConnection":
        """Create IEEE1722TpAvConnection from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            IEEE1722TpAvConnection instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to IEEE1722TpAvConnection since parent returns ARObject
        return cast("IEEE1722TpAvConnection", obj)


class IEEE1722TpAvConnectionBuilder:
    """Builder for IEEE1722TpAvConnection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IEEE1722TpAvConnection = IEEE1722TpAvConnection()

    def build(self) -> IEEE1722TpAvConnection:
        """Build and return IEEE1722TpAvConnection object.

        Returns:
            IEEE1722TpAvConnection instance
        """
        # TODO: Add validation
        return self._obj
