"""AUTOSAR AutoCollectEnum enumeration.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 399)

JSON Source: packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_ElementCollection.enums.json"""

from enum import Enum


class AutoCollectEnum(Enum):
    """AUTOSAR AutoCollectEnum enumeration."""

    REFALL = "refAll"
    REFNONE = "refNone"
    REFNONSTANDARD = "refNonStandard"
