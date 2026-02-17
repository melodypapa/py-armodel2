"""AUTOSAR ShowResourceCategoryEnum enumeration.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 323)

JSON Source: packages/M2_MSR_Documentation_TextModel_InlineAttributeEnums.enums.json"""

from enum import Enum


class ShowResourceCategoryEnum(Enum):
    """AUTOSAR ShowResourceCategoryEnum enumeration."""

    NOSHOWCATEGORY = "noShowCategory"
    SHOWCATEGORY = "showCategory"
