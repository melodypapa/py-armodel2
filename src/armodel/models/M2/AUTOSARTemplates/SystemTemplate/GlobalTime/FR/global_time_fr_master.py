"""GlobalTimeFrMaster AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.global_time_master import (
    GlobalTimeMaster,
)


class GlobalTimeFrMaster(GlobalTimeMaster):
    """AUTOSAR GlobalTimeFrMaster."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("crc_secured", None, False, False, GlobalTimeCrcSupportEnum),  # crcSecured
    ]

    def __init__(self) -> None:
        """Initialize GlobalTimeFrMaster."""
        super().__init__()
        self.crc_secured: Optional[GlobalTimeCrcSupportEnum] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert GlobalTimeFrMaster to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "GlobalTimeFrMaster":
        """Create GlobalTimeFrMaster from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            GlobalTimeFrMaster instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to GlobalTimeFrMaster since parent returns ARObject
        return cast("GlobalTimeFrMaster", obj)


class GlobalTimeFrMasterBuilder:
    """Builder for GlobalTimeFrMaster."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: GlobalTimeFrMaster = GlobalTimeFrMaster()

    def build(self) -> GlobalTimeFrMaster:
        """Build and return GlobalTimeFrMaster object.

        Returns:
            GlobalTimeFrMaster instance
        """
        # TODO: Add validation
        return self._obj
