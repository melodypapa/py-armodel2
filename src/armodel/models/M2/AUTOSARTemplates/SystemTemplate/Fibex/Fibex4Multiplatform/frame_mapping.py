"""FrameMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 838)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Multiplatform.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.frame_triggering import (
    FrameTriggering,
)


class FrameMapping(ARObject):
    """AUTOSAR FrameMapping."""

    introduction: Optional[DocumentationBlock]
    source_frame: Optional[FrameTriggering]
    target_frame: Optional[FrameTriggering]
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
