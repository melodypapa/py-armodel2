"""AUTOSAR DataConsistencyPolicyEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 903)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster.enums.json"""

from enum import Enum


class DataConsistencyPolicyEnum(Enum):
    """AUTOSAR DataConsistencyPolicyEnum enumeration."""

    CONSISTENCYMECHANISM = "consistencyMechanism"
    NOCONSISTENCY = "noConsistency"
