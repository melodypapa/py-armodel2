"""AUTOSAR SupportBufferLockingEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 595)

JSON Source: packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_PortAPIOptions.enums.json"""

from __future__ import annotations

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class SupportBufferLockingEnum(AREnum):
    """AUTOSAR SupportBufferLockingEnum enumeration.

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

    DOES_NOT_SUPPORT_BUFFER_LOCKING = "DOES-NOT-SUPPORT-BUFFER-LOCKING"
    SUPPORTS_BUFFER_LOCKING = "SUPPORTS-BUFFER-LOCKING"
