"""AUTOSAR MaximumMessageLengthType enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 604)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.enums.json"""

from enum import Enum


class MaximumMessageLengthType(Enum):
    """AUTOSAR MaximumMessageLengthType enumeration."""

    I4GLENGTH = "I4glength"
    ISO = "iso"
    ISO6 = "iso6"
    ROUTE = "route"
