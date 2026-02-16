"""FlexrayFrameTriggering AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.frame_triggering import (
    FrameTriggering,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayCommunication.flexray_absolutely_scheduled_timing import (
    FlexrayAbsolutelyScheduledTiming,
)


class FlexrayFrameTriggering(FrameTriggering):
    """AUTOSAR FlexrayFrameTriggering."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("absolutelies", None, False, True, FlexrayAbsolutelyScheduledTiming),  # absolutelies
        ("allow_dynamic", None, True, False, None),  # allowDynamic
        ("message_id", None, True, False, None),  # messageId
        ("payload_preamble", None, False, False, any (BooleanIndicator)),  # payloadPreamble
    ]

    def __init__(self) -> None:
        """Initialize FlexrayFrameTriggering."""
        super().__init__()
        self.absolutelies: list[FlexrayAbsolutelyScheduledTiming] = []
        self.allow_dynamic: Optional[Boolean] = None
        self.message_id: Optional[PositiveInteger] = None
        self.payload_preamble: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert FlexrayFrameTriggering to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlexrayFrameTriggering":
        """Create FlexrayFrameTriggering from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            FlexrayFrameTriggering instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to FlexrayFrameTriggering since parent returns ARObject
        return cast("FlexrayFrameTriggering", obj)


class FlexrayFrameTriggeringBuilder:
    """Builder for FlexrayFrameTriggering."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FlexrayFrameTriggering = FlexrayFrameTriggering()

    def build(self) -> FlexrayFrameTriggering:
        """Build and return FlexrayFrameTriggering object.

        Returns:
            FlexrayFrameTriggering instance
        """
        # TODO: Add validation
        return self._obj
