"""SecuredPduHeaderEnum enumeration."""

from enum import Enum


class SecuredPduHeaderEnum(Enum):
    """AUTOSAR SecuredPduHeaderEnum enumeration."""

    NOHEADER = "noHeader"
    SYSTEM = "System"
    AUTOSARSECUREDPDUHEADER08BIT = "AUTOSARsecuredPduHeader08Bit"
    SECUREDPDUHEADER16BIT = "securedPduHeader16Bit"
    SECUREDPDUHEADER32BIT = "securedPduHeader32Bit"
