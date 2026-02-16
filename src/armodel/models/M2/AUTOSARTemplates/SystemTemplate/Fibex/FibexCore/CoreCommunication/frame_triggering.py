"""FrameTriggering AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.frame import (
    Frame,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.frame_port import (
    FramePort,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)


class FrameTriggering(Identifiable):
    """AUTOSAR FrameTriggering."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "frame": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=Frame,
        ),  # frame
        "frame_ports": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=FramePort,
        ),  # framePorts
        "pdu_triggerings": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=PduTriggering,
        ),  # pduTriggerings
    }

    def __init__(self) -> None:
        """Initialize FrameTriggering."""
        super().__init__()
        self.frame: Optional[Frame] = None
        self.frame_ports: list[FramePort] = []
        self.pdu_triggerings: list[PduTriggering] = []


class FrameTriggeringBuilder:
    """Builder for FrameTriggering."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FrameTriggering = FrameTriggering()

    def build(self) -> FrameTriggering:
        """Build and return FrameTriggering object.

        Returns:
            FrameTriggering instance
        """
        # TODO: Add validation
        return self._obj
