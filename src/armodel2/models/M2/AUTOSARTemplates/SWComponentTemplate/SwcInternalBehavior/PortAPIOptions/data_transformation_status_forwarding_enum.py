"""AUTOSAR DataTransformationStatusForwardingEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 591)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2015)

JSON Source: packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_PortAPIOptions.enums.json"""

from __future__ import annotations

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class DataTransformationStatusForwardingEnum(AREnum):
    """AUTOSAR DataTransformationStatusForwardingEnum enumeration.

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

    NO_TRANSFORMER_STATUS_FORWARDING = "NO-TRANSFORMER-STATUS-FORWARDING"
    TRANSFORMER_STATUS_FORWARDING = "TRANSFORMER-STATUS-FORWARDING"
