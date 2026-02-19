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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "EthernetWakeupSleepOnDatalineConfig":
        """Deserialize XML element to EthernetWakeupSleepOnDatalineConfig object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EthernetWakeupSleepOnDatalineConfig object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EthernetWakeupSleepOnDatalineConfig, cls).deserialize(element)

        # Parse sleep_mode
        child = ARObject._find_child_element(element, "SLEEP-MODE")
        if child is not None:
            sleep_mode_value = child.text
            obj.sleep_mode = sleep_mode_value

        # Parse sleep_repetition
        child = ARObject._find_child_element(element, "SLEEP-REPETITION")
        if child is not None:
            sleep_repetition_value = child.text
            obj.sleep_repetition = sleep_repetition_value

        # Parse sleep
        child = ARObject._find_child_element(element, "SLEEP")
        if child is not None:
            sleep_value = child.text
            obj.sleep = sleep_value

        # Parse wakeup_forward
        child = ARObject._find_child_element(element, "WAKEUP-FORWARD")
        if child is not None:
            wakeup_forward_value = child.text
            obj.wakeup_forward = wakeup_forward_value

        # Parse wakeup_local
        child = ARObject._find_child_element(element, "WAKEUP-LOCAL")
        if child is not None:
            wakeup_local_value = child.text
            obj.wakeup_local = wakeup_local_value

        # Parse wakeup_remote
        child = ARObject._find_child_element(element, "WAKEUP-REMOTE")
        if child is not None:
            wakeup_remote_value = child.text
            obj.wakeup_remote = wakeup_remote_value

        # Parse wakeup
        child = ARObject._find_child_element(element, "WAKEUP")
        if child is not None:
            wakeup_value = child.text
            obj.wakeup = wakeup_value

        return obj



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
