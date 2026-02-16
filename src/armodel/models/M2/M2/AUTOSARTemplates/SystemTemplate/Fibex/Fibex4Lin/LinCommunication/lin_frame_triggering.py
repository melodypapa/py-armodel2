"""LinFrameTriggering AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.frame_triggering import (
    FrameTriggering,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)


class LinFrameTriggering(FrameTriggering):
    """AUTOSAR LinFrameTriggering."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "identifier": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # identifier
        "lin_checksum": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=LinChecksumType,
        ),  # linChecksum
    }

    def __init__(self) -> None:
        """Initialize LinFrameTriggering."""
        super().__init__()
        self.identifier: Optional[Integer] = None
        self.lin_checksum: Optional[LinChecksumType] = None


class LinFrameTriggeringBuilder:
    """Builder for LinFrameTriggering."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LinFrameTriggering = LinFrameTriggering()

    def build(self) -> LinFrameTriggering:
        """Build and return LinFrameTriggering object.

        Returns:
            LinFrameTriggering instance
        """
        # TODO: Add validation
        return self._obj
