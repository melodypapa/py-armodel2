"""AUTOSAR DataTransformationKindEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 150)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.enums.json"""

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class DataTransformationKindEnum(AREnum):
    """AUTOSAR DataTransformationKindEnum enumeration.

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

    ASYMMETRIC_FROM = "ASYMMETRIC-FROM"
    ASYMMETRIC_TO_BYTE_ARRAY = "ASYMMETRIC-TO-BYTE-ARRAY"
    SYMMETRIC = "SYMMETRIC"
