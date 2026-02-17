"""AUTOSAR TransformerClassEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 200)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 765)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.enums.json"""

from enum import Enum


class TransformerClassEnum(Enum):
    """AUTOSAR TransformerClassEnum enumeration."""

    CUSTOM = "custom"
    SAFETY = "safety"
    SECURITY = "security"
    SERIALIZER = "serializer"
