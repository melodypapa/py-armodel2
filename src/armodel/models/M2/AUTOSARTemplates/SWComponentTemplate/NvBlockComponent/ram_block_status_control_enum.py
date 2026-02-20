"""AUTOSAR RamBlockStatusControlEnum enumeration.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 233)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 701)

JSON Source: packages/M2_AUTOSARTemplates_SWComponentTemplate_NvBlockComponent.enums.json"""

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class RamBlockStatusControlEnum(AREnum):
    """AUTOSAR RamBlockStatusControlEnum enumeration.

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

    API = "API"
    NV_RAM_MANAGER = "NV-RAM-MANAGER"
