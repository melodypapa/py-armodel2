"""TtcanAbsolutelyScheduledTiming AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_cycle import (
    CommunicationCycle,
)


class TtcanAbsolutelyScheduledTiming(ARObject):
    """AUTOSAR TtcanAbsolutelyScheduledTiming."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("communication_cycle_cycle", None, False, False, CommunicationCycle),  # communicationCycleCycle
        ("time_mark", None, True, False, None),  # timeMark
        ("trigger", None, False, False, TtcanTriggerType),  # trigger
    ]

    def __init__(self) -> None:
        """Initialize TtcanAbsolutelyScheduledTiming."""
        super().__init__()
        self.communication_cycle_cycle: Optional[CommunicationCycle] = None
        self.time_mark: Optional[Integer] = None
        self.trigger: Optional[TtcanTriggerType] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TtcanAbsolutelyScheduledTiming to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TtcanAbsolutelyScheduledTiming":
        """Create TtcanAbsolutelyScheduledTiming from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TtcanAbsolutelyScheduledTiming instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TtcanAbsolutelyScheduledTiming since parent returns ARObject
        return cast("TtcanAbsolutelyScheduledTiming", obj)


class TtcanAbsolutelyScheduledTimingBuilder:
    """Builder for TtcanAbsolutelyScheduledTiming."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TtcanAbsolutelyScheduledTiming = TtcanAbsolutelyScheduledTiming()

    def build(self) -> TtcanAbsolutelyScheduledTiming:
        """Build and return TtcanAbsolutelyScheduledTiming object.

        Returns:
            TtcanAbsolutelyScheduledTiming instance
        """
        # TODO: Add validation
        return self._obj
