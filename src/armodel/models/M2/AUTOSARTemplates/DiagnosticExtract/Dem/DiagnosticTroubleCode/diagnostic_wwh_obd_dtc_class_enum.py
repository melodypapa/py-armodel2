"""AUTOSAR DiagnosticWwhObdDtcClassEnum enumeration.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 187)

JSON Source: packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticTroubleCode.enums.json"""

from enum import Enum


class DiagnosticWwhObdDtcClassEnum(Enum):
    """AUTOSAR DiagnosticWwhObdDtcClassEnum enumeration."""

    DEMDTCWWHOBDCLASSA = "demDtcWwhObdClassA"
    DEMDTCWWHOBDCLASSB1 = "demDtcWwhObdClassB1"
    DEMDTCWWHOBDCLASSB2 = "demDtcWwhObdClassB2"
    DEMDTCWWHOBDCLASSC = "demDtcWwhObdClassC"
    DEMDTCWWHOBD = "demDtcWwhObd"
    CLASSNOINFORMATION = "ClassNoInformation"
