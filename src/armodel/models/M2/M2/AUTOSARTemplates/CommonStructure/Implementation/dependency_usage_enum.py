"""DependencyUsageEnum enumeration."""

from enum import Enum


class DependencyUsageEnum(Enum):
    """AUTOSAR DependencyUsageEnum enumeration."""

    BUILD = "build"
    CODEGENERATION = "codegeneration"
    COMPILE = "compile"
    EXECUTE = "execute"
    LINK = "link"
