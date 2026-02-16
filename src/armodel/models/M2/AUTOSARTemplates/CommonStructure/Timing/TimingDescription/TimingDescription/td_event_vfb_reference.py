"""TDEventVfbReference AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_vfb import (
    TDEventVfb,
)


class TDEventVfbReference(TDEventVfb):
    """AUTOSAR TDEventVfbReference."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("referenced_td_event_vfb", None, False, False, TDEventVfb),  # referencedTDEventVfb
    ]

    def __init__(self) -> None:
        """Initialize TDEventVfbReference."""
        super().__init__()
        self.referenced_td_event_vfb: Optional[TDEventVfb] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TDEventVfbReference to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventVfbReference":
        """Create TDEventVfbReference from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TDEventVfbReference instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TDEventVfbReference since parent returns ARObject
        return cast("TDEventVfbReference", obj)


class TDEventVfbReferenceBuilder:
    """Builder for TDEventVfbReference."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventVfbReference = TDEventVfbReference()

    def build(self) -> TDEventVfbReference:
        """Build and return TDEventVfbReference object.

        Returns:
            TDEventVfbReference instance
        """
        # TODO: Add validation
        return self._obj
