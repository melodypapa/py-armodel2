"""AUTOSAR SwImplPolicyEnum enumeration.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 342)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 336)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2065)

JSON Source: packages/M2_MSR_DataDictionary_DataDefProperties.enums.json"""

from __future__ import annotations

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class SwImplPolicyEnum(AREnum):
    """AUTOSAR SwImplPolicyEnum enumeration.

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

    CONST = "CONST"
    BASIC = "BASIC"
    AUTOSAR = "A-U-T-O-S-A-R"
    FIXED = "FIXED"
    MEASUREMENT_POINT = "MEASUREMENT-POINT"
    QUEUED = "QUEUED"
    STANDARD = "STANDARD"
