"""AUTOSAR EthernetSwitchVlanEgressTaggingEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 130)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.enums.json"""

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class EthernetSwitchVlanEgressTaggingEnum(AREnum):
    """AUTOSAR EthernetSwitchVlanEgressTaggingEnum enumeration.

    This enum inherits from AREnum, which provides:
    - serialize(): XML serialization
    - deserialize(): XML deserialization with automatic member matching
    - Transparent equality comparison with string values
    """

    def __init__(self, value: str) -> None:
        """Initialize enum member.

        Args:
            value: The enum value as a string
        """
        self._value_ = value

    NOT_SENT = "notSent"
