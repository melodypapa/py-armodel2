"""EthernetWakeupSleepOnDatalineConfig AUTOSAR element."""

from typing import Optional, cast
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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("sleep_mode", None, True, False, None),  # sleepMode
        ("sleep_repetition", None, True, False, None),  # sleepRepetition
        ("sleep", None, True, False, None),  # sleep
        ("wakeup_forward", None, True, False, None),  # wakeupForward
        ("wakeup_local", None, True, False, None),  # wakeupLocal
        ("wakeup_remote", None, True, False, None),  # wakeupRemote
        ("wakeup", None, True, False, None),  # wakeup
    ]

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

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EthernetWakeupSleepOnDatalineConfig to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EthernetWakeupSleepOnDatalineConfig":
        """Create EthernetWakeupSleepOnDatalineConfig from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EthernetWakeupSleepOnDatalineConfig instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EthernetWakeupSleepOnDatalineConfig since parent returns ARObject
        return cast("EthernetWakeupSleepOnDatalineConfig", obj)


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
