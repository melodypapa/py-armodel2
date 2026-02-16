"""FlexrayFrameTriggering AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "absolutelies": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=FlexrayAbsolutelyScheduledTiming,
        ),  # absolutelies
        "allow_dynamic": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # allowDynamic
        "message_id": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # messageId
        "payload_preamble": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (BooleanIndicator),
        ),  # payloadPreamble
    }

    def __init__(self) -> None:
        """Initialize FlexrayFrameTriggering."""
        super().__init__()
        self.absolutelies: list[FlexrayAbsolutelyScheduledTiming] = []
        self.allow_dynamic: Optional[Boolean] = None
        self.message_id: Optional[PositiveInteger] = None
        self.payload_preamble: Optional[Any] = None


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
