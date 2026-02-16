"""ArrayImplPolicyEnum enumeration."""

from enum import Enum


class ArrayImplPolicyEnum(Enum):
    """AUTOSAR ArrayImplPolicyEnum enumeration."""

    PAYLOADASARRAY = "payloadAsArray"
    PAYLOADASPOINTERTOARRAY = "payloadAsPointerToArray"
