"""AclScopeEnum enumeration."""

from enum import Enum


class AclScopeEnum(Enum):
    """AUTOSAR AclScopeEnum enumeration."""

    DEPENDANT = "dependant"
    DESCENDANT = "descendant"
    EXPLICIT = "explicit"
