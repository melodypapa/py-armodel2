"""AUTOSAR MemorySectionType enumeration.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 146)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 417)

JSON Source: packages/M2_MSR_DataDictionary_AuxillaryObjects.enums.json"""

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class MemorySectionType(AREnum):
    """AUTOSAR MemorySectionType enumeration.

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

    CALIBRATION_VARIABLES = "calibrationVariables"
    CALPRM = "calprm"
    CODE = "code"
    CONFIG_DATA = "configData"
    CONST = "const"
    EXCLUDE_FROM_FLASHTIMEIN = "excludeFromFlashtimein"
    VAR = "var"
