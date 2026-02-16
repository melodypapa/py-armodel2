"""TDEventSwcInternalBehaviorReference AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_swc import (
    TDEventSwc,
)


class TDEventSwcInternalBehaviorReference(TDEventSwc):
    """AUTOSAR TDEventSwcInternalBehaviorReference."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("referenced_td_event_swc", None, False, False, TDEventSwc),  # referencedTDEventSwc
    ]

    def __init__(self) -> None:
        """Initialize TDEventSwcInternalBehaviorReference."""
        super().__init__()
        self.referenced_td_event_swc: Optional[TDEventSwc] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TDEventSwcInternalBehaviorReference to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventSwcInternalBehaviorReference":
        """Create TDEventSwcInternalBehaviorReference from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TDEventSwcInternalBehaviorReference instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TDEventSwcInternalBehaviorReference since parent returns ARObject
        return cast("TDEventSwcInternalBehaviorReference", obj)


class TDEventSwcInternalBehaviorReferenceBuilder:
    """Builder for TDEventSwcInternalBehaviorReference."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventSwcInternalBehaviorReference = TDEventSwcInternalBehaviorReference()

    def build(self) -> TDEventSwcInternalBehaviorReference:
        """Build and return TDEventSwcInternalBehaviorReference object.

        Returns:
            TDEventSwcInternalBehaviorReference instance
        """
        # TODO: Add validation
        return self._obj
