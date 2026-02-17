"""AUTOSAR SupportBufferLockingEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 595)

JSON Source: packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_PortAPIOptions.enums.json"""

from enum import Enum


class SupportBufferLockingEnum(Enum):
    """AUTOSAR SupportBufferLockingEnum enumeration."""

    DOESNOTSUPPORTBUFFERLOCKING = "doesNotSupportBufferLocking"
    SUPPORTSBUFFERLOCKING = "supportsBufferLocking"
