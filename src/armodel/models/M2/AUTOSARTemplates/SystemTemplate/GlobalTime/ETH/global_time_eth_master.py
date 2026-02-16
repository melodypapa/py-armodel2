"""GlobalTimeEthMaster AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "crc_secured": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=GlobalTimeCrcSupportEnum,
        ),  # crcSecured
        "hold_over_time": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # holdOverTime
        "sub_tlv_config": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=EthTSynSubTlvConfig,
        ),  # subTlvConfig
    }

    def __init__(self) -> None:
        """Initialize GlobalTimeEthMaster."""
        super().__init__()
        self.crc_secured: Optional[GlobalTimeCrcSupportEnum] = None
        self.hold_over_time: Optional[TimeValue] = None
        self.sub_tlv_config: Optional[EthTSynSubTlvConfig] = None


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
