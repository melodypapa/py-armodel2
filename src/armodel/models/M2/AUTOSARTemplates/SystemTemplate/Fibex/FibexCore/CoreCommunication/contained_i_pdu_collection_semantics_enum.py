"""AUTOSAR ContainedIPduCollectionSemanticsEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 357)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.enums.json"""

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class ContainedIPduCollectionSemanticsEnum(AREnum):
    """AUTOSAR ContainedIPduCollectionSemanticsEnum enumeration.

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

    LAST_IS_BEST = "LAST-IS-BEST"
    QUEUED = "QUEUED"
