"""AssignFrameId AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_configuration_entry import (
    LinConfigurationEntry,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_frame_triggering import (
    LinFrameTriggering,
)


class AssignFrameId(LinConfigurationEntry):
    """AUTOSAR AssignFrameId."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "assigned_frame": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=LinFrameTriggering,
        ),  # assignedFrame
    }

    def __init__(self) -> None:
        """Initialize AssignFrameId."""
        super().__init__()
        self.assigned_frame: Optional[LinFrameTriggering] = None


class AssignFrameIdBuilder:
    """Builder for AssignFrameId."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AssignFrameId = AssignFrameId()

    def build(self) -> AssignFrameId:
        """Build and return AssignFrameId object.

        Returns:
            AssignFrameId instance
        """
        # TODO: Add validation
        return self._obj
