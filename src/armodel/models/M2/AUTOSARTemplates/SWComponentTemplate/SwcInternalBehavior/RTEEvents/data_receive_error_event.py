"""DataReceiveErrorEvent AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.rte_event import (
    RTEEvent,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class DataReceiveErrorEvent(RTEEvent):
    """AUTOSAR DataReceiveErrorEvent."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("data", None, False, False, VariableDataPrototype),  # data
    ]

    def __init__(self) -> None:
        """Initialize DataReceiveErrorEvent."""
        super().__init__()
        self.data: Optional[VariableDataPrototype] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DataReceiveErrorEvent to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataReceiveErrorEvent":
        """Create DataReceiveErrorEvent from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DataReceiveErrorEvent instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DataReceiveErrorEvent since parent returns ARObject
        return cast("DataReceiveErrorEvent", obj)


class DataReceiveErrorEventBuilder:
    """Builder for DataReceiveErrorEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataReceiveErrorEvent = DataReceiveErrorEvent()

    def build(self) -> DataReceiveErrorEvent:
        """Build and return DataReceiveErrorEvent object.

        Returns:
            DataReceiveErrorEvent instance
        """
        # TODO: Add validation
        return self._obj
