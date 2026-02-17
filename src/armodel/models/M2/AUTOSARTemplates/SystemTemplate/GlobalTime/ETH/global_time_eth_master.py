"""GlobalTimeEthMaster AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 866)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_GlobalTime_ETH.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.global_time_master import (
    GlobalTimeMaster,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime import (
    GlobalTimeCrcSupportEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.ETH.eth_t_syn_sub_tlv_config import (
    EthTSynSubTlvConfig,
)


class GlobalTimeEthMaster(GlobalTimeMaster):
    """AUTOSAR GlobalTimeEthMaster."""

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
