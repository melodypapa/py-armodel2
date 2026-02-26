"""AUTOSAR ApiPrincipleEnum enumeration.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 83)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 556)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_InternalBehavior.enums.json"""

from __future__ import annotations

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class ApiPrincipleEnum(AREnum):
    """AUTOSAR ApiPrincipleEnum enumeration.

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

    COMMON = "COMMON"
    PER_EXECUTABLE_MODULE = "PER-EXECUTABLE-MODULE"
