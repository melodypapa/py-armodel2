"""BswDataReceivedEvent AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_schedule_event import (
    BswScheduleEvent,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class BswDataReceivedEvent(BswScheduleEvent):
    """AUTOSAR BswDataReceivedEvent."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("data", None, False, False, VariableDataPrototype),  # data
    ]

    def __init__(self) -> None:
        """Initialize BswDataReceivedEvent."""
        super().__init__()
        self.data: Optional[VariableDataPrototype] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BswDataReceivedEvent to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswDataReceivedEvent":
        """Create BswDataReceivedEvent from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BswDataReceivedEvent instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BswDataReceivedEvent since parent returns ARObject
        return cast("BswDataReceivedEvent", obj)


class BswDataReceivedEventBuilder:
    """Builder for BswDataReceivedEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswDataReceivedEvent = BswDataReceivedEvent()

    def build(self) -> BswDataReceivedEvent:
        """Build and return BswDataReceivedEvent object.

        Returns:
            BswDataReceivedEvent instance
        """
        # TODO: Add validation
        return self._obj
