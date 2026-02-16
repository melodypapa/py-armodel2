"""EcucConfigurationVariantEnum enumeration."""

from enum import Enum


class EcucConfigurationVariantEnum(Enum):
    """AUTOSAR EcucConfigurationVariantEnum enumeration."""

    PRECONFIGUREDCONFIGURATION = "PreconfiguredConfiguration"
    AUTOSAR = "AUTOSAR"
    RECOMMENDEDCONFIGURATION = "RecommendedConfiguration"
    VARIANTLINKTIME = "VariantLinkTime"
    VARIANTPOSTBUILD = "VariantPostBuild"
    VARIANTPRECOMPILE = "VariantPreCompile"
