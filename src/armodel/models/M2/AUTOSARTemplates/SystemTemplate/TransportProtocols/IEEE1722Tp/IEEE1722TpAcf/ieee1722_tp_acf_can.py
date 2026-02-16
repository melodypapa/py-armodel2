"""IEEE1722TpAcfCan AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAcf.ieee1722_tp_acf_bus import (
    IEEE1722TpAcfBus,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAcf.ieee1722_tp_acf_can import (
    IEEE1722TpAcfCan,
)


class IEEE1722TpAcfCan(IEEE1722TpAcfBus):
    """AUTOSAR IEEE1722TpAcfCan."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("message_type_message_type_enum", None, False, False, IEEE1722TpAcfCan),  # messageTypeMessageTypeEnum
    ]

    def __init__(self) -> None:
        """Initialize IEEE1722TpAcfCan."""
        super().__init__()
        self.message_type_message_type_enum: Optional[IEEE1722TpAcfCan] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert IEEE1722TpAcfCan to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IEEE1722TpAcfCan":
        """Create IEEE1722TpAcfCan from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            IEEE1722TpAcfCan instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to IEEE1722TpAcfCan since parent returns ARObject
        return cast("IEEE1722TpAcfCan", obj)


class IEEE1722TpAcfCanBuilder:
    """Builder for IEEE1722TpAcfCan."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IEEE1722TpAcfCan = IEEE1722TpAcfCan()

    def build(self) -> IEEE1722TpAcfCan:
        """Build and return IEEE1722TpAcfCan object.

        Returns:
            IEEE1722TpAcfCan instance
        """
        # TODO: Add validation
        return self._obj
