"""AUTOSAR EcucConfigurationVariantEnum enumeration.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 52)

JSON Source: packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.enums.json"""

from enum import Enum


class EcucConfigurationVariantEnum(Enum):
    """AUTOSAR EcucConfigurationVariantEnum enumeration."""

    PRECONFIGUREDCONFIGURATION = "PreconfiguredConfiguration"
    AUTOSAR = "AUTOSAR"
    RECOMMENDEDCONFIGURATION = "RecommendedConfiguration"
    VARIANTLINKTIME = "VariantLinkTime"
    VARIANTPOSTBUILD = "VariantPostBuild"
    VARIANTPRECOMPILE = "VariantPreCompile"
