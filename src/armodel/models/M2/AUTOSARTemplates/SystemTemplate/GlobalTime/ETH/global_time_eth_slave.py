"""GlobalTimeEthSlave AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.global_time_slave import (
    GlobalTimeSlave,
)


class GlobalTimeEthSlave(GlobalTimeSlave):
    """AUTOSAR GlobalTimeEthSlave."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("crc_validated", None, False, False, any (GlobalTimeCrc)),  # crcValidated
    ]

    def __init__(self) -> None:
        """Initialize GlobalTimeEthSlave."""
        super().__init__()
        self.crc_validated: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert GlobalTimeEthSlave to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "GlobalTimeEthSlave":
        """Create GlobalTimeEthSlave from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            GlobalTimeEthSlave instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to GlobalTimeEthSlave since parent returns ARObject
        return cast("GlobalTimeEthSlave", obj)


class GlobalTimeEthSlaveBuilder:
    """Builder for GlobalTimeEthSlave."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: GlobalTimeEthSlave = GlobalTimeEthSlave()

    def build(self) -> GlobalTimeEthSlave:
        """Build and return GlobalTimeEthSlave object.

        Returns:
            GlobalTimeEthSlave instance
        """
        # TODO: Add validation
        return self._obj
