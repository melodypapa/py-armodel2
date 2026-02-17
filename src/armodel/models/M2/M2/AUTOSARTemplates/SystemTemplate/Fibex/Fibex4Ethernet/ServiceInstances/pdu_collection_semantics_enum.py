"""AUTOSAR PduCollectionSemanticsEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 490)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ServiceInstances.enums.json"""

from enum import Enum


class PduCollectionSemanticsEnum(Enum):
    """AUTOSAR PduCollectionSemanticsEnum enumeration."""

    LASTISBEST = "lastIsBest"
    QUEUED = "queued"
