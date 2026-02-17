"""AUTOSAR IPduSignalProcessingEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 305)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.enums.json"""

from enum import Enum


class IPduSignalProcessingEnum(Enum):
    """AUTOSAR IPduSignalProcessingEnum enumeration."""

    DEFERRED = "deferred"
    IMMEDIATE = "immediate"
