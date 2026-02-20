"""AUTOSAR GlobalTimeIcvVerificationEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 881)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_GlobalTime.enums.json"""

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class GlobalTimeIcvVerificationEnum(AREnum):
    """AUTOSAR GlobalTimeIcvVerificationEnum enumeration.

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

    ICV_IGNORED = "ICV-IGNORED"
    ICV_NOT_VERIFIED = "ICV-NOT-VERIFIED"
    ICV_OPTIONAL = "ICV-OPTIONAL"
    ICV_VERIFIED = "ICV-VERIFIED"
