"""AUTOSAR VerificationStatusIndicationModeEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 824)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.enums.json"""

from enum import Enum


class VerificationStatusIndicationModeEnum(Enum):
    """AUTOSAR VerificationStatusIndicationModeEnum enumeration."""

    FAILUREANDSUCCESS = "failureAndSuccess"
    FAILUREONLY = "failureOnly"
