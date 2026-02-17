"""AUTOSAR IntervalTypeEnum enumeration.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 300)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 409)

JSON Source: packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_PrimitiveTypes.enums.json"""

from enum import Enum


class IntervalTypeEnum(Enum):
    """AUTOSAR IntervalTypeEnum enumeration."""

    CLOSED = "closed"
    OPEN = "open"
