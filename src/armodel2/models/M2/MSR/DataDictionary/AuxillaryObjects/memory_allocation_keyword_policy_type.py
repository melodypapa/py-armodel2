"""AUTOSAR MemoryAllocationKeywordPolicyType enumeration.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 145)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 418)

JSON Source: packages/M2_MSR_DataDictionary_AuxillaryObjects.enums.json"""

from __future__ import annotations

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class MemoryAllocationKeywordPolicyType(AREnum):
    """AUTOSAR MemoryAllocationKeywordPolicyType enumeration.

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

    ADDR_METHOD_SHORT_NAME = "ADDR-METHOD-SHORT-NAME"
    ADDR_METHOD_SHORT_NAME_AND_ALIGNMENT = "ADDR-METHOD-SHORT-NAME-AND-ALIGNMENT"
