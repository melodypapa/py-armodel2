"""AUTOSAR RteApiReturnValueProvisionEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 562)

JSON Source: packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_AccessCount.enums.json"""

from enum import Enum


class RteApiReturnValueProvisionEnum(Enum):
    """AUTOSAR RteApiReturnValueProvisionEnum enumeration."""

    NORETURNVALUEPROVIDED = "noReturnValueProvided"
    RETURNVALUEPROVIDED = "returnValueProvided"
