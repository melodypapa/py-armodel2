"""AUTOSAR EcucDestinationUriNestingContractEnum enumeration.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 83)

JSON Source: packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.enums.json"""

from enum import Enum


class EcucDestinationUriNestingContractEnum(Enum):
    """AUTOSAR EcucDestinationUriNestingContractEnum enumeration."""

    LEAFOFTARGET = "leafOfTarget"
    TARGETCONTAINER = "targetContainer"
    VERTEXOFTARGET = "vertexOfTarget"
