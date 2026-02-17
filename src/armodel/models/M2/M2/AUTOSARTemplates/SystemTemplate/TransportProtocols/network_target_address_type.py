"""AUTOSAR NetworkTargetAddressType enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 611)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.enums.json"""

from enum import Enum


class NetworkTargetAddressType(Enum):
    """AUTOSAR NetworkTargetAddressType enumeration."""

    FUNCTIONAL = "functional"
    PHYSICAL = "physical"
