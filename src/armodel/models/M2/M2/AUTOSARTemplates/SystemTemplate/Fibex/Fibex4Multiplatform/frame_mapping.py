"""FrameMapping AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.frame_triggering import (
    FrameTriggering,
)


class FrameMapping(ARObject):
    """AUTOSAR FrameMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "introduction": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DocumentationBlock,
        ),  # introduction
        "source_frame": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=FrameTriggering,
        ),  # sourceFrame
        "target_frame": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=FrameTriggering,
        ),  # targetFrame
    }

    def __init__(self) -> None:
        """Initialize FrameMapping."""
        super().__init__()
        self.introduction: Optional[DocumentationBlock] = None
        self.source_frame: Optional[FrameTriggering] = None
        self.target_frame: Optional[FrameTriggering] = None


class FrameMappingBuilder:
    """Builder for FrameMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FrameMapping = FrameMapping()

    def build(self) -> FrameMapping:
        """Build and return FrameMapping object.

        Returns:
            FrameMapping instance
        """
        # TODO: Add validation
        return self._obj
