"""AUTOSAR SignalServiceTranslationControlEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 744)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_SignalServiceTranslation.enums.json"""

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class SignalServiceTranslationControlEnum(AREnum):
    """AUTOSAR SignalServiceTranslationControlEnum enumeration.

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

    ALL_PARTIAL_NETWORKS_ACTIVE = "ALL-PARTIAL-NETWORKS-ACTIVE"
    ANY_PARTIAL_NETWORK_ACTIVE = "ANY-PARTIAL-NETWORK-ACTIVE"
    PARTIAL_NETWORK = "PARTIAL-NETWORK"
    SERVICE_DISCOVERY = "SERVICE-DISCOVERY"
    TRANSLATION_START = "TRANSLATION-START"
