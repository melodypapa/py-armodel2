"""AUTOSAR ContainedIPduCollectionSemanticsEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 357)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.enums.json"""

from enum import Enum


class ContainedIPduCollectionSemanticsEnum(Enum):
    """AUTOSAR ContainedIPduCollectionSemanticsEnum enumeration."""

    LASTISBEST = "lastIsBest"
    QUEUED = "queued"
