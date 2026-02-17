"""AUTOSAR RxAcceptContainedIPduEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 355)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.enums.json"""

from enum import Enum


class RxAcceptContainedIPduEnum(Enum):
    """AUTOSAR RxAcceptContainedIPduEnum enumeration."""

    ACCEPTALL = "acceptAll"
    ACCEPTCONFIGURED = "acceptConfigured"
