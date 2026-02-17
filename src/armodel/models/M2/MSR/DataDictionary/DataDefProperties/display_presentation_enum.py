"""AUTOSAR DisplayPresentationEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 432)

JSON Source: packages/M2_MSR_DataDictionary_DataDefProperties.enums.json"""

from enum import Enum


class DisplayPresentationEnum(Enum):
    """AUTOSAR DisplayPresentationEnum enumeration."""

    PRESENTATIONCONTINUOUS = "presentationContinuous"
    PRESENTATIONDISCRETE = "presentationDiscrete"
