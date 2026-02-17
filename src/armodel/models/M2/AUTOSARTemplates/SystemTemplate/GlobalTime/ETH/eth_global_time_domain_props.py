"""EthGlobalTimeDomainProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 867)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_GlobalTime_ETH.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.abstract_global_time_domain_props import (
    AbstractGlobalTimeDomainProps,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.ETH import (
    EthGlobalTimeMessageFormatEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    MacAddressString,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.ETH.eth_t_syn_crc_flags import (
    EthTSynCrcFlags,
)


class EthGlobalTimeDomainProps(AbstractGlobalTimeDomainProps):
    """AUTOSAR EthGlobalTimeDomainProps."""

    def __init__(self) -> None:
        """Initialize EthGlobalTimeDomainProps."""
        super().__init__()
        self.crc_flags: Optional[EthTSynCrcFlags] = None
        self.destination: Optional[MacAddressString] = None
        self.fup_data_id_list: PositiveInteger = None
        self.manageds: list[Any] = []
        self.message: Optional[EthGlobalTimeMessageFormatEnum] = None
        self.vlan_priority: Optional[PositiveInteger] = None


class EthGlobalTimeDomainPropsBuilder:
    """Builder for EthGlobalTimeDomainProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EthGlobalTimeDomainProps = EthGlobalTimeDomainProps()

    def build(self) -> EthGlobalTimeDomainProps:
        """Build and return EthGlobalTimeDomainProps object.

        Returns:
            EthGlobalTimeDomainProps instance
        """
        # TODO: Add validation
        return self._obj
