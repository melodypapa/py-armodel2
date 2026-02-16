"""TDEventCom AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description_event import (
    TimingDescriptionEvent,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.ecu_instance import (
    EcuInstance,
)


class TDEventCom(TimingDescriptionEvent):
    """AUTOSAR TDEventCom."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("ecu_instance", None, False, False, EcuInstance),  # ecuInstance
    ]

    def __init__(self) -> None:
        """Initialize TDEventCom."""
        super().__init__()
        self.ecu_instance: Optional[EcuInstance] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TDEventCom to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventCom":
        """Create TDEventCom from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TDEventCom instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TDEventCom since parent returns ARObject
        return cast("TDEventCom", obj)


class TDEventComBuilder:
    """Builder for TDEventCom."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventCom = TDEventCom()

    def build(self) -> TDEventCom:
        """Build and return TDEventCom object.

        Returns:
            TDEventCom instance
        """
        # TODO: Add validation
        return self._obj
