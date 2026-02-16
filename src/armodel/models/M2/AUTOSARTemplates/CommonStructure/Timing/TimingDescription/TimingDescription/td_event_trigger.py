"""TDEventTrigger AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_vfb_port import (
    TDEventVfbPort,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger import (
    Trigger,
)


class TDEventTrigger(TDEventVfbPort):
    """AUTOSAR TDEventTrigger."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("td_event_trigger", None, False, False, TDEventTriggerTypeEnum),  # tdEventTrigger
        ("trigger", None, False, False, Trigger),  # trigger
    ]

    def __init__(self) -> None:
        """Initialize TDEventTrigger."""
        super().__init__()
        self.td_event_trigger: Optional[TDEventTriggerTypeEnum] = None
        self.trigger: Optional[Trigger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TDEventTrigger to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventTrigger":
        """Create TDEventTrigger from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TDEventTrigger instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TDEventTrigger since parent returns ARObject
        return cast("TDEventTrigger", obj)


class TDEventTriggerBuilder:
    """Builder for TDEventTrigger."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventTrigger = TDEventTrigger()

    def build(self) -> TDEventTrigger:
        """Build and return TDEventTrigger object.

        Returns:
            TDEventTrigger instance
        """
        # TODO: Add validation
        return self._obj
