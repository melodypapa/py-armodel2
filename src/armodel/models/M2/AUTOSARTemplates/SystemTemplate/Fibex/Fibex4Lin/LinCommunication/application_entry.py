"""ApplicationEntry AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.schedule_table_entry import (
    ScheduleTableEntry,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_frame_triggering import (
    LinFrameTriggering,
)


class ApplicationEntry(ScheduleTableEntry):
    """AUTOSAR ApplicationEntry."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("frame_triggering", None, False, False, LinFrameTriggering),  # frameTriggering
    ]

    def __init__(self) -> None:
        """Initialize ApplicationEntry."""
        super().__init__()
        self.frame_triggering: Optional[LinFrameTriggering] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ApplicationEntry to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ApplicationEntry":
        """Create ApplicationEntry from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ApplicationEntry instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ApplicationEntry since parent returns ARObject
        return cast("ApplicationEntry", obj)


class ApplicationEntryBuilder:
    """Builder for ApplicationEntry."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ApplicationEntry = ApplicationEntry()

    def build(self) -> ApplicationEntry:
        """Build and return ApplicationEntry object.

        Returns:
            ApplicationEntry instance
        """
        # TODO: Add validation
        return self._obj
