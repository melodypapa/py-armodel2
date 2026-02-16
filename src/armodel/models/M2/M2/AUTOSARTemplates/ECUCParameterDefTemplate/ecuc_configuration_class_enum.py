"""EcucConfigurationClassEnum enumeration."""

from enum import Enum


class EcucConfigurationClassEnum(Enum):
    """AUTOSAR EcucConfigurationClassEnum enumeration."""

    LINK = "Link"
    POSTBUILD = "PostBuild"
    PRECOMPILE = "PreCompile"
    PUBLISHEDINFORMATION = "PublishedInformation"
