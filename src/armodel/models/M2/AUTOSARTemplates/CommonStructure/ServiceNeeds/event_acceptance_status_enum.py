"""AUTOSAR EventAcceptanceStatusEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 762)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.enums.json"""

from enum import Enum


class EventAcceptanceStatusEnum(Enum):
    """AUTOSAR EventAcceptanceStatusEnum enumeration."""

    DISABLED = "Disabled"
    EVENTACCEPTANCEENABLED = "eventAcceptanceEnabled"
