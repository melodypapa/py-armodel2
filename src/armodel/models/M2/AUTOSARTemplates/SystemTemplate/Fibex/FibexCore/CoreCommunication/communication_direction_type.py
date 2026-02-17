"""AUTOSAR CommunicationDirectionType enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 351)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.enums.json"""

from enum import Enum


class CommunicationDirectionType(Enum):
    """AUTOSAR CommunicationDirectionType enumeration."""

    INOUT = "inout"
