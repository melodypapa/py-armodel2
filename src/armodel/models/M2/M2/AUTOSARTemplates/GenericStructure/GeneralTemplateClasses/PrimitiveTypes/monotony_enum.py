"""AUTOSAR MonotonyEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 408)

JSON Source: packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_PrimitiveTypes.enums.json"""

from enum import Enum


class MonotonyEnum(Enum):
    """AUTOSAR MonotonyEnum enumeration."""

    DECREASINGINCREASING = "decreasingincreasing"
    MONOTONOUS = "monotonous"
    NOMONOTONY = "noMonotony"
    STRICTLYDECREASING = "strictlyDecreasing"
    STRICTLYINCREASING = "strictlyIncreasing"
    STRICTMONOTONOUS = "strictMonotonous"
