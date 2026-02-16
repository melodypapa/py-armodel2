"""TimeSyncServerConfiguration AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    String,
    TimeValue,
)


class TimeSyncServerConfiguration(Referrable):
    """AUTOSAR TimeSyncServerConfiguration."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("priority", None, True, False, None),  # priority
        ("sync_interval", None, True, False, None),  # syncInterval
        ("time_sync_server_identifier", None, True, False, None),  # timeSyncServerIdentifier
        ("time_sync", None, False, False, TimeSyncTechnologyEnum),  # timeSync
    ]

    def __init__(self) -> None:
        """Initialize TimeSyncServerConfiguration."""
        super().__init__()
        self.priority: Optional[PositiveInteger] = None
        self.sync_interval: Optional[TimeValue] = None
        self.time_sync_server_identifier: Optional[String] = None
        self.time_sync: Optional[TimeSyncTechnologyEnum] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TimeSyncServerConfiguration to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TimeSyncServerConfiguration":
        """Create TimeSyncServerConfiguration from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TimeSyncServerConfiguration instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TimeSyncServerConfiguration since parent returns ARObject
        return cast("TimeSyncServerConfiguration", obj)


class TimeSyncServerConfigurationBuilder:
    """Builder for TimeSyncServerConfiguration."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TimeSyncServerConfiguration = TimeSyncServerConfiguration()

    def build(self) -> TimeSyncServerConfiguration:
        """Build and return TimeSyncServerConfiguration object.

        Returns:
            TimeSyncServerConfiguration instance
        """
        # TODO: Add validation
        return self._obj
