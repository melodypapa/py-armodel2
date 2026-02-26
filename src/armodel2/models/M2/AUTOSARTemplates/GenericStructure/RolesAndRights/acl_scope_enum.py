"""AUTOSAR AclScopeEnum enumeration.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 384)

JSON Source: packages/M2_AUTOSARTemplates_GenericStructure_RolesAndRights.enums.json"""

from __future__ import annotations

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class AclScopeEnum(AREnum):
    """AUTOSAR AclScopeEnum enumeration.

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

    DEPENDANT = "DEPENDANT"
    DESCENDANT = "DESCENDANT"
    EXPLICIT = "EXPLICIT"
