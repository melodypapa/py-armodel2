"""GlobalTimeCanMaster AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.global_time_master import (
    GlobalTimeMaster,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class GlobalTimeCanMaster(GlobalTimeMaster):
    """AUTOSAR GlobalTimeCanMaster."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("crc_secured", None, False, False, GlobalTimeCrcSupportEnum),  # crcSecured
        ("sync", None, True, False, None),  # sync
    ]

    def __init__(self) -> None:
        """Initialize GlobalTimeCanMaster."""
        super().__init__()
        self.crc_secured: Optional[GlobalTimeCrcSupportEnum] = None
        self.sync: Optional[TimeValue] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert GlobalTimeCanMaster to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "GlobalTimeCanMaster":
        """Create GlobalTimeCanMaster from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            GlobalTimeCanMaster instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to GlobalTimeCanMaster since parent returns ARObject
        return cast("GlobalTimeCanMaster", obj)


class GlobalTimeCanMasterBuilder:
    """Builder for GlobalTimeCanMaster."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: GlobalTimeCanMaster = GlobalTimeCanMaster()

    def build(self) -> GlobalTimeCanMaster:
        """Build and return GlobalTimeCanMaster object.

        Returns:
            GlobalTimeCanMaster instance
        """
        # TODO: Add validation
        return self._obj
