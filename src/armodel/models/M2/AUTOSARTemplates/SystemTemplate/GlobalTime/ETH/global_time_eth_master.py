"""GlobalTimeEthMaster AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.global_time_master import (
    GlobalTimeMaster,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.ETH.eth_t_syn_sub_tlv_config import (
    EthTSynSubTlvConfig,
)


class GlobalTimeEthMaster(GlobalTimeMaster):
    """AUTOSAR GlobalTimeEthMaster."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("crc_secured", None, False, False, GlobalTimeCrcSupportEnum),  # crcSecured
        ("hold_over_time", None, True, False, None),  # holdOverTime
        ("sub_tlv_config", None, False, False, EthTSynSubTlvConfig),  # subTlvConfig
    ]

    def __init__(self) -> None:
        """Initialize GlobalTimeEthMaster."""
        super().__init__()
        self.crc_secured: Optional[GlobalTimeCrcSupportEnum] = None
        self.hold_over_time: Optional[TimeValue] = None
        self.sub_tlv_config: Optional[EthTSynSubTlvConfig] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert GlobalTimeEthMaster to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "GlobalTimeEthMaster":
        """Create GlobalTimeEthMaster from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            GlobalTimeEthMaster instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to GlobalTimeEthMaster since parent returns ARObject
        return cast("GlobalTimeEthMaster", obj)


class GlobalTimeEthMasterBuilder:
    """Builder for GlobalTimeEthMaster."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: GlobalTimeEthMaster = GlobalTimeEthMaster()

    def build(self) -> GlobalTimeEthMaster:
        """Build and return GlobalTimeEthMaster object.

        Returns:
            GlobalTimeEthMaster instance
        """
        # TODO: Add validation
        return self._obj
