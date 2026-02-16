"""LinPhysicalChannel AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.physical_channel import (
    PhysicalChannel,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_schedule_table import (
    LinScheduleTable,
)


class LinPhysicalChannel(PhysicalChannel):
    """AUTOSAR LinPhysicalChannel."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("bus_idle_timeout", None, True, False, None),  # busIdleTimeout
        ("schedule_tables", None, False, True, LinScheduleTable),  # scheduleTables
    ]

    def __init__(self) -> None:
        """Initialize LinPhysicalChannel."""
        super().__init__()
        self.bus_idle_timeout: Optional[TimeValue] = None
        self.schedule_tables: list[LinScheduleTable] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert LinPhysicalChannel to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LinPhysicalChannel":
        """Create LinPhysicalChannel from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            LinPhysicalChannel instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to LinPhysicalChannel since parent returns ARObject
        return cast("LinPhysicalChannel", obj)


class LinPhysicalChannelBuilder:
    """Builder for LinPhysicalChannel."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LinPhysicalChannel = LinPhysicalChannel()

    def build(self) -> LinPhysicalChannel:
        """Build and return LinPhysicalChannel object.

        Returns:
            LinPhysicalChannel instance
        """
        # TODO: Add validation
        return self._obj
