"""EthernetWakeupSleepOnDatalineConfigSet AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)


class EthernetWakeupSleepOnDatalineConfigSet(FibexElement):
    """AUTOSAR EthernetWakeupSleepOnDatalineConfigSet."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("ethernets", None, False, True, any (EthernetWakeupSleep)),  # ethernets
    ]

    def __init__(self) -> None:
        """Initialize EthernetWakeupSleepOnDatalineConfigSet."""
        super().__init__()
        self.ethernets: list[Any] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EthernetWakeupSleepOnDatalineConfigSet to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EthernetWakeupSleepOnDatalineConfigSet":
        """Create EthernetWakeupSleepOnDatalineConfigSet from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EthernetWakeupSleepOnDatalineConfigSet instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EthernetWakeupSleepOnDatalineConfigSet since parent returns ARObject
        return cast("EthernetWakeupSleepOnDatalineConfigSet", obj)


class EthernetWakeupSleepOnDatalineConfigSetBuilder:
    """Builder for EthernetWakeupSleepOnDatalineConfigSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EthernetWakeupSleepOnDatalineConfigSet = EthernetWakeupSleepOnDatalineConfigSet()

    def build(self) -> EthernetWakeupSleepOnDatalineConfigSet:
        """Build and return EthernetWakeupSleepOnDatalineConfigSet object.

        Returns:
            EthernetWakeupSleepOnDatalineConfigSet instance
        """
        # TODO: Add validation
        return self._obj
