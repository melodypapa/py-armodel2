"""FullBindingTimeEnum enumeration."""

from enum import Enum


class FullBindingTimeEnum(Enum):
    """AUTOSAR FullBindingTimeEnum enumeration."""

    BLUEPRINTDERIVATIONTIME = "blueprintDerivationTime"
    CODEGENERATIONTIME = "codeGenerationTime"
    LINKTIME = "linkTime"
    POSTBUILD = "postBuild"
    PRECOMPILETIME = "preCompileTime"
    SYSTEMDESIGNTIME = "systemDesignTime"
