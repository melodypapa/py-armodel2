"""AUTOSAR DataTransformationErrorHandlingEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 590)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2014)

JSON Source: packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_PortAPIOptions.enums.json"""

from enum import Enum


class DataTransformationErrorHandlingEnum(Enum):
    """AUTOSAR DataTransformationErrorHandlingEnum enumeration."""

    NOTRANSFORMERERRORHANDLING = "noTransformerErrorHandling"
    TRANSFORMERERRORHANDLING = "transformerErrorHandling"
