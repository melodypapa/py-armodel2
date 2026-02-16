"""GlobalTimeCanSlave AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.global_time_slave import (
    GlobalTimeSlave,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class GlobalTimeCanSlave(GlobalTimeSlave):
    """AUTOSAR GlobalTimeCanSlave."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("crc_validated", None, False, False, any (GlobalTimeCrc)),  # crcValidated
        ("sequence", None, True, False, None),  # sequence
    ]

    def __init__(self) -> None:
        """Initialize GlobalTimeCanSlave."""
        super().__init__()
        self.crc_validated: Optional[Any] = None
        self.sequence: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert GlobalTimeCanSlave to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "GlobalTimeCanSlave":
        """Create GlobalTimeCanSlave from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            GlobalTimeCanSlave instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to GlobalTimeCanSlave since parent returns ARObject
        return cast("GlobalTimeCanSlave", obj)


class GlobalTimeCanSlaveBuilder:
    """Builder for GlobalTimeCanSlave."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: GlobalTimeCanSlave = GlobalTimeCanSlave()

    def build(self) -> GlobalTimeCanSlave:
        """Build and return GlobalTimeCanSlave object.

        Returns:
            GlobalTimeCanSlave instance
        """
        # TODO: Add validation
        return self._obj
