"""AUTOSAR DataTypePolicyEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 322)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_DataMapping.enums.json"""

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class DataTypePolicyEnum(AREnum):
    """AUTOSAR DataTypePolicyEnum enumeration.

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

    DDS_SERVICE = "DDS-SERVICE"
    DDS_SIGNAL = "DDS-SIGNAL"
    LEGACY = "LEGACY"
    NETWORK = "NETWORK"
    REPRESENTATION = "REPRESENTATION"
    FROM_COM_SPEC = "FROM-COM-SPEC"
    OVERRIDE = "OVERRIDE"
    TRANSFORMING_I_SIGNAL = "TRANSFORMING-I-SIGNAL"
