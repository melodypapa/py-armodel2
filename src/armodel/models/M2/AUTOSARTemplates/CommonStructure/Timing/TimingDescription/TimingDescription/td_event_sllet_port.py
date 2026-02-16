"""TDEventSLLETPort AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_sllet import (
    TDEventSLLET,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)


class TDEventSLLETPort(TDEventSLLET):
    """AUTOSAR TDEventSLLETPort."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("port", None, False, False, PortPrototype),  # port
    ]

    def __init__(self) -> None:
        """Initialize TDEventSLLETPort."""
        super().__init__()
        self.port: Optional[PortPrototype] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TDEventSLLETPort to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventSLLETPort":
        """Create TDEventSLLETPort from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TDEventSLLETPort instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TDEventSLLETPort since parent returns ARObject
        return cast("TDEventSLLETPort", obj)


class TDEventSLLETPortBuilder:
    """Builder for TDEventSLLETPort."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventSLLETPort = TDEventSLLETPort()

    def build(self) -> TDEventSLLETPort:
        """Build and return TDEventSLLETPort object.

        Returns:
            TDEventSLLETPort instance
        """
        # TODO: Add validation
        return self._obj
