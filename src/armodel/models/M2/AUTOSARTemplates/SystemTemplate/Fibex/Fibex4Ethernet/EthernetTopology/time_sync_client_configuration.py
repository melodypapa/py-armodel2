"""TimeSyncClientConfiguration AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ordered_master import (
    OrderedMaster,
)


class TimeSyncClientConfiguration(ARObject):
    """AUTOSAR TimeSyncClientConfiguration."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("ordered_masters", None, False, True, OrderedMaster),  # orderedMasters
        ("time_sync", None, False, False, TimeSyncTechnologyEnum),  # timeSync
    ]

    def __init__(self) -> None:
        """Initialize TimeSyncClientConfiguration."""
        super().__init__()
        self.ordered_masters: list[OrderedMaster] = []
        self.time_sync: Optional[TimeSyncTechnologyEnum] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TimeSyncClientConfiguration to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TimeSyncClientConfiguration":
        """Create TimeSyncClientConfiguration from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TimeSyncClientConfiguration instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TimeSyncClientConfiguration since parent returns ARObject
        return cast("TimeSyncClientConfiguration", obj)


class TimeSyncClientConfigurationBuilder:
    """Builder for TimeSyncClientConfiguration."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TimeSyncClientConfiguration = TimeSyncClientConfiguration()

    def build(self) -> TimeSyncClientConfiguration:
        """Build and return TimeSyncClientConfiguration object.

        Returns:
            TimeSyncClientConfiguration instance
        """
        # TODO: Add validation
        return self._obj
