"""AUTOSAR DataTransformationKindEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 150)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.enums.json"""

from enum import Enum


class DataTransformationKindEnum(Enum):
    """AUTOSAR DataTransformationKindEnum enumeration."""

    ASYMMETRICFROM = "asymmetricFrom"
    ASYMMETRICTOBYTEARRAY = "asymmetricToByteArray"
    SYMMETRIC = "symmetric"
