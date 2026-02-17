"""AUTOSAR EthernetCouplingPortSchedulerEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 123)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.enums.json"""

from enum import Enum


class EthernetCouplingPortSchedulerEnum(Enum):
    """AUTOSAR EthernetCouplingPortSchedulerEnum enumeration."""

    DEFICITROUNDROBIN = "deficitRoundRobin"
    STRICTPRIORITY = "strictPriority"
    WEIGHTEDROUNDROBIN = "weightedRoundRobin"
