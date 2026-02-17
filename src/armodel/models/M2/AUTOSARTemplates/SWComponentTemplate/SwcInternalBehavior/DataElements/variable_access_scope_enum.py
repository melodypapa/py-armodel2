"""AUTOSAR VariableAccessScopeEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 567)

JSON Source: packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_DataElements.enums.json"""

from enum import Enum


class VariableAccessScopeEnum(Enum):
    """AUTOSAR VariableAccessScopeEnum enumeration."""

    COMMUNICATIONINTER = "communicationInter"
    COMMUNICATIONINTRAINTERPARTITIONINTRA = "communicationIntrainterPartitionIntra"
