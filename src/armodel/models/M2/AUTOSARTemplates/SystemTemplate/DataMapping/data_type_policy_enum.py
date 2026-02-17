"""AUTOSAR DataTypePolicyEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 322)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_DataMapping.enums.json"""

from enum import Enum


class DataTypePolicyEnum(Enum):
    """AUTOSAR DataTypePolicyEnum enumeration."""

    DDSSERVICE = "ddsService"
    DDSSIGNAL = "ddsSignal"
    LEGACY = "legacy"
    NETWORK = "network"
    REPRESENTATION = "Representation"
    FROMCOMSPEC = "FromComSpec"
    OVERRIDE = "override"
    TRANSFORMINGISIGNAL = "transformingISignal"
