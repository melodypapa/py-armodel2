"""AUTOSAR EcucConfigurationClassEnum enumeration.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 52)

JSON Source: packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.enums.json"""

from enum import Enum


class EcucConfigurationClassEnum(Enum):
    """AUTOSAR EcucConfigurationClassEnum enumeration."""

    LINK = "Link"
    POSTBUILD = "PostBuild"
    PRECOMPILE = "PreCompile"
    PUBLISHEDINFORMATION = "PublishedInformation"
