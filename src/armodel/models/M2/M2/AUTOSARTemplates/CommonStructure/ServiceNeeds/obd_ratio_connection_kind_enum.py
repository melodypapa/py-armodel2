"""AUTOSAR ObdRatioConnectionKindEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 796)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.enums.json"""

from enum import Enum


class ObdRatioConnectionKindEnum(Enum):
    """AUTOSAR ObdRatioConnectionKindEnum enumeration."""

    APIUSE = "apiUse"
    OBSERVER = "observer"
