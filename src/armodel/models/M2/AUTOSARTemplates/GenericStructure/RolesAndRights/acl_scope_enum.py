"""AUTOSAR AclScopeEnum enumeration.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 384)

JSON Source: packages/M2_AUTOSARTemplates_GenericStructure_RolesAndRights.enums.json"""

from enum import Enum


class AclScopeEnum(Enum):
    """AUTOSAR AclScopeEnum enumeration."""

    DEPENDANT = "dependant"
    DESCENDANT = "descendant"
    EXPLICIT = "explicit"
