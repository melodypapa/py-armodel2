"""AUTOSAR SendIndicationEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 903)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster.enums.json"""

from enum import Enum


class SendIndicationEnum(Enum):
    """AUTOSAR SendIndicationEnum enumeration."""

    ANYSENDOPERATION = "anySendOperation"
    NONE = "none"
