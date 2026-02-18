"""EthernetWakeupSleepOnDatalineConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 158)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    TimeValue,
)


class EthernetWakeupSleepOnDatalineConfig(Identifiable):
    """AUTOSAR EthernetWakeupSleepOnDatalineConfig."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    sleep_mode: Optional[TimeValue]
    sleep_repetition: Optional[TimeValue]
    sleep: Optional[PositiveInteger]
    wakeup_forward: Optional[Boolean]
    wakeup_local: Optional[Boolean]
    wakeup_remote: Optional[Boolean]
    wakeup: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize EthernetWakeupSleepOnDatalineConfig."""
        super().__init__()
        self.sleep_mode: Optional[TimeValue] = None
        self.sleep_repetition: Optional[TimeValue] = None
        self.sleep: Optional[PositiveInteger] = None
        self.wakeup_forward: Optional[Boolean] = None
        self.wakeup_local: Optional[Boolean] = None
        self.wakeup_remote: Optional[Boolean] = None
        self.wakeup: Optional[PositiveInteger] = None


class EthernetWakeupSleepOnDatalineConfigBuilder:
    """Builder for EthernetWakeupSleepOnDatalineConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EthernetWakeupSleepOnDatalineConfig = EthernetWakeupSleepOnDatalineConfig()

    def build(self) -> EthernetWakeupSleepOnDatalineConfig:
        """Build and return EthernetWakeupSleepOnDatalineConfig object.

        Returns:
            EthernetWakeupSleepOnDatalineConfig instance
        """
        # TODO: Add validation
        return self._obj
