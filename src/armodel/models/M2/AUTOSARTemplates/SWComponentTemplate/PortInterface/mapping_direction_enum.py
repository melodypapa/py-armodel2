"""AUTOSAR MappingDirectionEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 146)

JSON Source: packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.enums.json"""

from enum import Enum


class MappingDirectionEnum(Enum):
    """AUTOSAR MappingDirectionEnum enumeration."""

    BIDIRECTIONALFIRSTTOSECOND = "bidirectionalfirstToSecond"
    SECONDTOFIRST = "secondToFirst"
