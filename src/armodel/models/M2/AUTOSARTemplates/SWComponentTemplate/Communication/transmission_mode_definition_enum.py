"""AUTOSAR TransmissionModeDefinitionEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 181)

JSON Source: packages/M2_AUTOSARTemplates_SWComponentTemplate_Communication.enums.json"""

from enum import Enum


class TransmissionModeDefinitionEnum(Enum):
    """AUTOSAR TransmissionModeDefinitionEnum enumeration."""

    CYCLIC = "cyclic"
    CYCLICANDON = "cyclicAndOn"
    TRIGGERED = "triggered"
