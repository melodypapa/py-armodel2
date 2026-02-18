"""AUTOSAR DiagnosticWwhObdDtcClassEnum enumeration.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 187)

JSON Source: packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticTroubleCode.enums.json"""

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class DiagnosticWwhObdDtcClassEnum(AREnum):
    """AUTOSAR DiagnosticWwhObdDtcClassEnum enumeration.

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

    DEM_DTC_WWH_OBD_CLASS_A = "demDtcWwhObdClassA"
    DEM_DTC_WWH_OBD_CLASS_B1 = "demDtcWwhObdClassB1"
    DEM_DTC_WWH_OBD_CLASS_B2 = "demDtcWwhObdClassB2"
    DEM_DTC_WWH_OBD_CLASS_C = "demDtcWwhObdClassC"
    DEM_DTC_WWH_OBD = "demDtcWwhObd"
    CLASS_NO_INFORMATION = "ClassNoInformation"
