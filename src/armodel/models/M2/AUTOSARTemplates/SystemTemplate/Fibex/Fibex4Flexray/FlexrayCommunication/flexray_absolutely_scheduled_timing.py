"""FlexrayAbsolutelyScheduledTiming AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_cycle import (
    CommunicationCycle,
)


class FlexrayAbsolutelyScheduledTiming(ARObject):
    """AUTOSAR FlexrayAbsolutelyScheduledTiming."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("communication_cycle_cycle", None, False, False, CommunicationCycle),  # communicationCycleCycle
        ("slot_id", None, True, False, None),  # slotID
    ]

    def __init__(self) -> None:
        """Initialize FlexrayAbsolutelyScheduledTiming."""
        super().__init__()
        self.communication_cycle_cycle: Optional[CommunicationCycle] = None
        self.slot_id: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert FlexrayAbsolutelyScheduledTiming to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlexrayAbsolutelyScheduledTiming":
        """Create FlexrayAbsolutelyScheduledTiming from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            FlexrayAbsolutelyScheduledTiming instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to FlexrayAbsolutelyScheduledTiming since parent returns ARObject
        return cast("FlexrayAbsolutelyScheduledTiming", obj)


class FlexrayAbsolutelyScheduledTimingBuilder:
    """Builder for FlexrayAbsolutelyScheduledTiming."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FlexrayAbsolutelyScheduledTiming = FlexrayAbsolutelyScheduledTiming()

    def build(self) -> FlexrayAbsolutelyScheduledTiming:
        """Build and return FlexrayAbsolutelyScheduledTiming object.

        Returns:
            FlexrayAbsolutelyScheduledTiming instance
        """
        # TODO: Add validation
        return self._obj
