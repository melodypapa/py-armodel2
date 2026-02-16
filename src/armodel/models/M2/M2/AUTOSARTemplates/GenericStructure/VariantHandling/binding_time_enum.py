"""BindingTimeEnum enumeration."""

from enum import Enum


class BindingTimeEnum(Enum):
    """AUTOSAR BindingTimeEnum enumeration."""

    CODEGENERATIONTIME = "codeGenerationTime"
    LINKTIME = "linkTime"
    PRECOMPILETIME = "preCompileTime"
    SYSTEMDESIGNTIME = "systemDesignTime"
