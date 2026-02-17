"""AUTOSAR IEEE1722TpAcfCanMessageTypeEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 661)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols_IEEE1722Tp_IEEE1722TpAcf.enums.json"""

from enum import Enum


class IEEE1722TpAcfCanMessageTypeEnum(Enum):
    """AUTOSAR IEEE1722TpAcfCanMessageTypeEnum enumeration."""

    CAN = "can"
    CANBRIEF = "canBrief"
