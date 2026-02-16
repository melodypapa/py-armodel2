"""Frame AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_to_frame_mapping import (
    PduToFrameMapping,
)


class Frame(FibexElement):
    """AUTOSAR Frame."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "frame_length": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # frameLength
        "pdu_to_frames": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=PduToFrameMapping,
        ),  # pduToFrames
    }

    def __init__(self) -> None:
        """Initialize Frame."""
        super().__init__()
        self.frame_length: Optional[Integer] = None
        self.pdu_to_frames: list[PduToFrameMapping] = []


class FrameBuilder:
    """Builder for Frame."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Frame = Frame()

    def build(self) -> Frame:
        """Build and return Frame object.

        Returns:
            Frame instance
        """
        # TODO: Add validation
        return self._obj
