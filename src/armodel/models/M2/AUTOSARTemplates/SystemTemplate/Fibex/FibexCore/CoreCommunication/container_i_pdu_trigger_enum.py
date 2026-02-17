"""AUTOSAR ContainerIPduTriggerEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 354)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.enums.json"""

from enum import Enum


class ContainerIPduTriggerEnum(Enum):
    """AUTOSAR ContainerIPduTriggerEnum enumeration."""

    DEFAULTTRIGGERFIRSTCONTAINED = "defaultTriggerfirstContained"
    TRIGGER = "Trigger"
