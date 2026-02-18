"""AUTOSAR EcucConfigurationVariantEnum enumeration.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 52)

JSON Source: packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.enums.json"""

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class EcucConfigurationVariantEnum(AREnum):
    """AUTOSAR EcucConfigurationVariantEnum enumeration.

    This enum inherits from AREnum, which provides:
    - serialize(): XML serialization
    - deserialize(): XML deserialization with automatic member matching
    - Transparent equality comparison with string values
    """

    def __init__(self, value: str) -> None:
        """Initialize enum member.

        Args:
            value: The enum value as a string
        """
        self._value_ = value

    PRECONFIGURED_CONFIGURATION = "PreconfiguredConfiguration"
    AUTOSAR = "AUTOSAR"
    RECOMMENDED_CONFIGURATION = "RecommendedConfiguration"
    VARIANT_LINK_TIME = "VariantLinkTime"
    VARIANT_POST_BUILD = "VariantPostBuild"
    VARIANT_PRE_COMPILE = "VariantPreCompile"
