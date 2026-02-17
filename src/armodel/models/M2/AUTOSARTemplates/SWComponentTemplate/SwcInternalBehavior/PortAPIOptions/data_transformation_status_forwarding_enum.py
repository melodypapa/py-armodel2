"""AUTOSAR DataTransformationStatusForwardingEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 591)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2015)

JSON Source: packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_PortAPIOptions.enums.json"""

from enum import Enum


class DataTransformationStatusForwardingEnum(Enum):
    """AUTOSAR DataTransformationStatusForwardingEnum enumeration."""

    NOTRANSFORMERSTATUSFORWARDING = "noTransformerStatusForwarding"
    TRANSFORMERSTATUSFORWARDING = "transformerStatusForwarding"
