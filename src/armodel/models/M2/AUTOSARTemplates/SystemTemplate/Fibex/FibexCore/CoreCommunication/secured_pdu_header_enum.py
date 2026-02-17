"""AUTOSAR SecuredPduHeaderEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 368)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.enums.json"""

from enum import Enum


class SecuredPduHeaderEnum(Enum):
    """AUTOSAR SecuredPduHeaderEnum enumeration."""

    NOHEADER = "noHeader"
    SYSTEM = "System"
    AUTOSARSECUREDPDUHEADER08BIT = "AUTOSARsecuredPduHeader08Bit"
    SECUREDPDUHEADER16BIT = "securedPduHeader16Bit"
    SECUREDPDUHEADER32BIT = "securedPduHeader32Bit"
