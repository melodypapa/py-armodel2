"""AUTOSAR CSTransformerErrorReactionEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 773)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.enums.json"""

from enum import Enum


class CSTransformerErrorReactionEnum(Enum):
    """AUTOSAR CSTransformerErrorReactionEnum enumeration."""

    APPLICATIONONLY = "applicationOnly"
    AUTONOMOUS = "autonomous"
