"""EthernetCouplingPortSchedulerEnum enumeration."""

from enum import Enum


class EthernetCouplingPortSchedulerEnum(Enum):
    """AUTOSAR EthernetCouplingPortSchedulerEnum enumeration."""

    DEFICITROUNDROBIN = "deficitRoundRobin"
    STRICTPRIORITY = "strictPriority"
    WEIGHTEDROUNDROBIN = "weightedRoundRobin"
