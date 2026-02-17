"""AUTOSAR StorageConditionStatusEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 762)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.enums.json"""

from enum import Enum


class StorageConditionStatusEnum(Enum):
    """AUTOSAR StorageConditionStatusEnum enumeration."""

    DISABLED = "Disabled"
    EVENTSTORAGEENABLED = "eventStorageEnabled"
