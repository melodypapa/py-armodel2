"""AssignFrameIdRange AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_configuration_entry import (
    LinConfigurationEntry,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.frame_pid import (
    FramePid,
)


class AssignFrameIdRange(LinConfigurationEntry):
    """AUTOSAR AssignFrameIdRange."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "frame_pid": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=FramePid,
        ),  # framePid
        "start_index": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # startIndex
    }

    def __init__(self) -> None:
        """Initialize AssignFrameIdRange."""
        super().__init__()
        self.frame_pid: FramePid = None
        self.start_index: Optional[Integer] = None


class AssignFrameIdRangeBuilder:
    """Builder for AssignFrameIdRange."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AssignFrameIdRange = AssignFrameIdRange()

    def build(self) -> AssignFrameIdRange:
        """Build and return AssignFrameIdRange object.

        Returns:
            AssignFrameIdRange instance
        """
        # TODO: Add validation
        return self._obj
