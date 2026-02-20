"""AUTOSAR EcucScopeEnum enumeration.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 46)

JSON Source: packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.enums.json"""

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class EcucScopeEnum(AREnum):
    """AUTOSAR EcucScopeEnum enumeration.

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

    ECU = "E-C-U"
    LOCAL = "LOCAL"
