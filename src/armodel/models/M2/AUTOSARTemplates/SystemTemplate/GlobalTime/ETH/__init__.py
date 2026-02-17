"""ETH module."""
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.ETH.global_time_eth_master import (
    GlobalTimeEthMaster,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.ETH.eth_t_syn_sub_tlv_config import (
    EthTSynSubTlvConfig,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.ETH.global_time_eth_slave import (
    GlobalTimeEthSlave,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.ETH.eth_global_time_domain_props import (
    EthGlobalTimeDomainProps,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.ETH.eth_t_syn_crc_flags import (
    EthTSynCrcFlags,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.ETH.eth_global_time_managed_coupling_port import (
    EthGlobalTimeManagedCouplingPort,
)

__all__ = [
    "EthGlobalTimeDomainProps",
    "EthGlobalTimeManagedCouplingPort",
    "EthTSynCrcFlags",
    "EthTSynSubTlvConfig",
    "GlobalTimeEthMaster",
    "GlobalTimeEthSlave",
]
